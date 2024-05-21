import pandas as pd

# Read Feather file
df = pd.read_feather('/MS3D/data_temp/argo/val_anno.feather')

# Now you can work with the DataFrame 'df'
print(df.head())
