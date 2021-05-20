import numpy as np 
import csv

def getDataSource(path):
    coffee_in_ml=[]
    sleep_in_hour = []
    with open(path) as file:
        froakie = csv.DictReader(file)
        for row in froakie:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hour.append(float(row["sleep in hours"]))
    
    return {"x":sleep_in_hour,"y":coffee_in_ml}
def findCorrelation(ds):
    delphox = np.corrcoef(ds["x"],ds["y"])
    print(delphox[0,-1])
def setup():
    path="data.csv"
    chestnaught=getDataSource(path)
    findCorrelation(chestnaught)

setup()