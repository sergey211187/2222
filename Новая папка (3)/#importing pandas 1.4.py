#importing pandas as pd 
import pandas as pd 

#dictionary of lists
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'Score': [90, 40, 80, 98]}

#creating a dataframe from a dictionary
df = pd.DataFrame(dict)

print(df)

#creating a list of dataframe columns
columns = list(df)

for i in columns:
    #printing the third element of the column
    print(df[i][2])