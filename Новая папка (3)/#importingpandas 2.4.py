#importingpandas mobule
import pandas as pd 

#making data frame from csv file
data = pd.read_csv("nbaNew.csv")

#for data visualization we filter first 3 datasets
col = data.head(3)
col 

#creating a list of daraframe columns
clmn = list(col)

for i in clmn:
    #priting a third a third element of column 
    print(col[i][2])