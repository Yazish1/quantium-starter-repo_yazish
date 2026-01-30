import pandas as pd
import glob

path = "quantium-starter-repo_yazish\data"
all_files = glob.glob(path + "\*.csv")

dfs = []
for file in all_files:
    df = pd.read_csv(file)
    
    modified = df[df['product'] == "pink morsel"].copy()
    
    modified["price"] = (modified["price"].str.replace("$","",regex=False)
                        .astype(float))
    
    modified["quantity"] = modified["quantity"].astype(float)
    modified["total"] = modified["price"] * modified["quantity"] 
    
    modified = modified.drop(columns=["price", "quantity"])

    dfs.append(modified)

final_sales = pd.concat(dfs, ignore_index=True)
final_sales.to_csv("quantium-starter-repo_yazish\data\pink_morsel_sales.csv", index=False)