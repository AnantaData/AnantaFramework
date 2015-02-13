__author__ = 'lakmal'
import shutil
import pandas as pd

def getStatistics(trainingSet, filename_prefix):
    print "Started tracking Statistics and Data"
    stat = trainingSet.data.describe().transpose()
    print stat.shape
    if(stat.shape[1]== 4):
        columns = ["Count","Mean","St.Dev","Min"]
        writeLine = "Field,Count,Mean,St.Dev,Min\n"
    else:
        columns = ["Count","Mean","St.Dev","Min","Q1","Median","Q3","Max"]
        writeLine = "Field,Count,Mean,St.Dev,Min,Q1,Median,Q3,Max\n"
    stat.columns = columns
    stat.to_csv("stat_temp.csv", sep=",", encoding="utf-8")

    from_file = open("stat_temp.csv","r");
    from_file.readline() # and discard
    stat_save = str(filename_prefix)+"stat.csv"
    to_file = open(stat_save,"w");
    to_file.write(writeLine)
    shutil.copyfileobj(from_file, to_file)
    from_file.close()
    to_file.close()
    shutil.copyfile(stat_save,"stat.csv")
    print "Finished tracking Statistics"

    types = pd.DataFrame({'DataType':trainingSet.data.dtypes})
    types.to_csv("types_temp.csv", sep=",", encoding="utf-8")

    from_file = open("types_temp.csv","r");
    from_file.readline() # and discard
    types_save = str(filename_prefix)+"types.csv"
    to_file = open(types_save,"w");
    to_file.write("Field,DataType\n")
    shutil.copyfileobj(from_file, to_file)
    from_file.close()
    to_file.close()
    shutil.copyfile(types_save,"types.csv")
    print "Finished tracking DataTypes"

    data_save = str(filename_prefix)+"data.csv"
    trainingSet.data.to_csv(data_save, sep=",", encoding="utf-8")
    print "Finished tracking Data"