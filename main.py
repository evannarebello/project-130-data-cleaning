import pandas as pd 

df = pd.read_csv("total_stars.csv")
    

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("final.csv")