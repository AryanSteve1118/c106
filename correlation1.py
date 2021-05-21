import numpy as np
import csv

def getDataSource(path):
    Marks_In_Percentage=[]
    Days_Present = []
    with open(path) as file:
        ret = csv.DictReader(file)
        for row in ret:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    
    return {"x":Days_Present,"y":Marks_In_Percentage}
def findCorrelation(ds):
    meg = np.corrcoef(ds["x"],ds["y"])
    print(meg[0,1])
def setup():
    path="data1.csv"
    sce=getDataSource(path)
    findCorrelation(sce)

setup()