import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df, x="Temperature", y="Ice-cream Sales( ₹ )")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales=[]
    temperature=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            temperature.append(float(row["Ice-cream Sales( ₹ )"]))
    return{"x":ice_cream_sales, "y":temperature}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"], data_source["y"])
    print("correlation is:", correlation[0,1])

def setup():
    data_path="/Users/Kartik/Downloads/correlation-master/data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()
    


    
    
