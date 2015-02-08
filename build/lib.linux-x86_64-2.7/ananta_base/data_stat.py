__author__ = 'lakmal'
import shutil



def getStatistics(trainingSet, filename_prefix):
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

    types_save = str(filename_prefix)+"types.csv"
    df = trainingSet.data
    types_list = df.dtypes
    types_list.to_csv(types_save, sep=",", encoding="utf-8")