__author__ = 'gilgamesh'
from clustering.gsom import gsom as gsom
from clustering.kgsom import kgsom as kgsom
from clustering.som import som as som
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.cluster import DBSCAN

#### soem methods to calculate clustering quality measures ####
def _get_prf(res_set):

    res_set=np.array(res_set)
    modes=[]
    precs=[]
    recs=[]
    for res in res_set:
        modes.append(mode(res)[0][0])
        precs.append(mode(res)[0][0]/len(res))

    for m in modes:
        m=0



class SOMStep:


    def __init__(self,dimensions,num_x=10,num_y=10,decay=0.99,alpha=0.9,alpha_min=0.1):
        self.dims = dimensions
        self.x = num_x
        self.y = num_y
        self.decay = decay
        self.alpha = alpha
        self.alpha_min =alpha_min
        self.mp = som.som(self.x,self.y,self.dims)

    def execute(self,data):
        data = np.array(data)
        print "executing on data"
        self.mp._train_map(data,self.alpha,self.alpha_min,self.decay)
        points = []
        print len(self.mp.neurons)
        print 'predicting'
        for inp in data:
            points.append(self.mp._predict(inp))
        data = np.array(points).astype(int)
        return data



class UnsupervisedMiningProfile:

    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def execute(self, dataset):
        data = dataset.data
        for step in self.steps:
            data = step.execute(data)
        dataset.data = data


class GSOMStep:

    def __init__(self,dimensions):
        self.dims = dimensions
        self.mp = gsom.gsomap(SP=0.5,dims=self.dims,nr_s=6,lr_s=0.9,boolean=False, lrr =0.5,fd=0.5, n_jobs = 2)

    def execute(self,data):
        data=np.array(data)
        try:
            self.mp.process_input(data)
            points=[]
            for inp in data:
                points.append(self.mp.predict_point(np.array(inp)))

            return np.array(points)
        except:
            return 'error occured while training / predicting'


class KGSOMStep:

    def __init__(self,dimensions):
        self.dims = dimensions
        self.mp = kgsom.gsomap(SP=0.9999,dims=self.dims,nr_s=10,lr_s=0.01,fd=0.999,lrr=0.95,sig2=1000,prune=0.8)

    def execute(self,data):
        data = np.array(data)
        print "executing on data"
        self.mp.process_batch(data)
        points=[]
        print len(self.mp.map_neurons)
        print "predicting"
        for inp in data:
            points.append(self.mp.predict_point(inp))
        data = np.array(points).astype(int)
        #print "prediction done"
        #print np.array(points)
        return data




class KmeanStep:

    def __init__(self, kv):
        self.model = KMeans(n_clusters=kv)

    def execute(self,data):
        try:
            labels= self.model.fit(data).labels_

            return labels
        except:
            return 'error fitting model'



#####################################

''' Cluster Quality Calculations'''

class KMeanEvalStep:
    def __init__(self):
        self.precs=[]
        self.recs=[]
        self.fs=[]
        self.heteval=None
        self.homeval=None

    def execute(self,data):
        clusters=data
        #print clusters
        clustering=get_clust_dict(clusters,data)
        #print clustering
        het=mean_inter_het(clustering)
        hom=mean_intra_hom(clustering)

        op = pd.DataFrame(columns=['het','hom'])
        op.het = [het]
        op.hom= [hom]
        op.to_csv('stat.csv', sep=',', encoding='utf-8')
        return data

class MapEvalStep:

    def __init__(self):
        self.precs=[]
        self.recs=[]
        self.fs=[]
        self.heteval=None
        self.homeval=None

    def execute(self,data):
        dbsc=DBSCAN(eps=2.828,min_samples=2)
        #print data
        dbsc.fit(data)

        clusters= dbsc.labels_
        #print clusters
        clustering=get_clust_dict(clusters,data)
        #print clustering
        het=mean_inter_het(clustering)
        hom=mean_intra_hom(clustering)

        op = pd.DataFrame(columns=['het','hom'])
        op.het = [het]
        op.hom= [hom]
        op.to_csv('stat.csv', sep=',', encoding='utf-8')
        return data



def get_clust_dict(labels, data):
    clust={}
    for i in (np.unique(labels)):
        clust[i]=[]
    for i in range(len(labels)):
        clust[labels[i]].append(data[i])
    for k in clust.keys():
        clust[k]=np.array(clust[k])
    return clust

def get_centroids(clustering):
    centroids=[]
    for k in clustering.keys():
        cluster=np.array(clustering[k])
        #print cluster
        centroids.append(np.sum(cluster,axis=0)/cluster.shape[0])
    return np.array(centroids)

def mean_intra_hom(clustering):
    cens=get_centroids(clustering)
    sums=0
    for i in range(len(clustering.keys())):
        s=0
        for elem in clustering[clustering.keys()[i]]:
            #print elem
            #print cens[i]
            s+=np.linalg.norm(elem.astype(int)-cens[i]).astype(float)
        s/=np.array(clustering[clustering.keys()[i]]).shape[0]
        sums+=s
    return sums/len(clustering.keys())


def mean_inter_het(clustering):
    cens=get_centroids(clustering)
    dismat=np.ndarray(shape=(cens.shape[0],cens.shape[0]))

    for i in range(cens.shape[0]):
        for j in range(cens.shape[0]):
            dismat[i][j]=np.linalg.norm(cens[i]-cens[j])

    return np.sum(dismat)/(dismat.shape[0]*dismat.shape[0]),dismat