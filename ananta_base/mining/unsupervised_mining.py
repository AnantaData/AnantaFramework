__author__ = 'gilgamesh'
from clustering.gsom import gsom as gsom
from clustering.kgsom import kgsom as kgsom
from clustering.som import som as som
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.cluster import DBSCAN
def normalize(arr):
    for i in range(arr.shape[1]):

        m = np.array([np.abs(np.min(arr[:,i])) for j in range(arr.shape[0])] )
        arr[:,i]+=m
    return arr

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

    def __init__(self,dimensions,x=10,y=10,alpha=0.99,alpha_min=0.9,decay=0.1):
        self.dims = dimensions
        self.num_x = x
        self.num_y = y
        self.alpha = alpha
        self.alpha_min = alpha_min
        self.decay = decay
        self.mp = som.SOM(self.num_x,self.num_y,self.dims)

    def execute(self,data):

        data=np.array(data)
        try:
            self.mp._train_map(data,self.alpha,self.alpha_min,self.decay)
            points=[]
            for inp in data:
                points.append(self.mp._predict(np.array(inp)))
            return np.array(points)
        except:
            return 'error occured while training / predicting the Self-Organizing Map'


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

            data = normalize((np.array(points).astype(int)))
            df = pd.DataFrame(columns = ['x', 'y', 'c'])
            x =[]
            y = []
            c =[]
            for elem in data :
                x.append(elem[0])
                y.append(elem[1])
                c.append('g')
            df['x']=x
            df['y']=y
            df['c']=c

            df.to_csv('somout.csv')
            return np.array(points)
        except:
            return 'error occured while training / predicting'


class KGSOMStep:

    def __init__(self,dimensions):
        self.dims = dimensions
        self.mp = kgsom.gsomap(SP=0.999999,dims=self.dims,nr_s=10,lr_s=0.01,fd=0.999,lrr=0.95,sig2=100000,prune=0.75)

    def execute(self,data):
        data = np.array(data)
        print "executing on data"
        self.mp.process_batch(data)
        points=[]
        print len(self.mp.map_neurons)
        print "predicting"
        for inp in data:
            points.append(self.mp.predict_point(inp))
        data = normalize(np.array(points).astype(int))

        df = pd.DataFrame(columns = ['x', 'y', 'c'])
        x =[]
        y = []
        c =[]
        for elem in data :
            x.append(elem[0])
            y.append(elem[1])
            c.append('g')
        df['x']=x
        df['y']=y
        df['c']=c

        df.to_csv('somout.csv')        #print "prediction done"
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