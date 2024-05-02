#importing pandas as pd 
import pandas as pd 

#dictionary of lists
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'Score': [90, 40, 80, 98]}

#creating a dataframefrom a dictionary
df = pd.DataFrame(dict)

# using iteritams() function to retrieve rows
for key, value in df.iteitems():
    print(key, value)
    print()