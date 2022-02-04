import numpy as np
import csv
def getDataSource(dataPath):
    marks=[]
    attendance=[]
    with open(dataPath)as f:
        df=csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"]))
    return {"x":marks,"y":attendance}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation is: ",correlation[0,1])
def setup():
    dataPath="C:/Users/dell/Desktop/Python/folderA/txt/Student Marks vs Days Present.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
setup()