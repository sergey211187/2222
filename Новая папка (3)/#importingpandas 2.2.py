#importing pandas mobule
import pandas as pd 

#making data frame from csv file
data = pd.read_csv("nbaNew.csv")

for key, value in data.items():
    print(key, value)
    print()