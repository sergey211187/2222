#importingpandas mobule
import pandas as pd 

#making data frame from csv file
data = pd.read_csv("nbaNew.csv")

#for data visualization we filter first 3 datasets
data.head(3)