__author__ = 'lakmal'
import shutil



def getStatistics(trainingSet, filename_prefix):
    print "Started tracking Statistics and Data"
    stat = trainingSet.data.describe().transpose()
    columns = ["Count","Mean","St.Dev","Min","Q1","Median","Q3","Max"]
    stat.columns = columns
    stat.to_csv("stat_temp.csv", sep=",", encoding="utf-8")

    from_file = open("stat_temp.csv","r");
    from_file.readline() # and discard
    stat_save = str(filename_prefix)+"stat.csv"
    to_file = open(stat_save,"w");
    to_file.write("Field,Count,Mean,St.Dev,Min,Q1,Median,Q3,Max\n")
    shutil.copyfileobj(from_file, to_file)
    print "Finished tracking Statistics"

    types_save = str(filename_prefix)+"types.csv"
    df = trainingSet.data
    types_list = df.dtypes
    types_list.to_csv(types_save, sep=",", encoding="utf-8")
    print "Finished tracking DataTypes"

    data_save = str(filename_prefix)+"data.csv"
    trainingSet.data.to_csv(data_save, sep=",", encoding="utf-8")
    print "Finished tracking Data"