__author__ = 'lakmal'
import shutil



def getStatistics(trainingSet):
    stat = trainingSet.data.describe().transpose()
    columns = ["Count","Mean","St.Dev","Min","Q1","Median","Q3","Max"]
    stat.columns = columns
    stat.to_csv("stat_1.csv", sep=",", encoding="utf-8")

    from_file = open("stat_1.csv","r");
    from_file.readline() # and discard
    to_file = open("stat.csv","w");
    to_file.write("Field,Count,Mean,St.Dev,Min,Q1,Median,Q3,Max\n")
    shutil.copyfileobj(from_file, to_file)

    df = trainingSet.data
    types_list = df.dtypes
    types_list.to_csv("types.csv", sep=",", encoding="utf-8")