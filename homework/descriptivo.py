# %%

import pandas as pd

df= pd.read_csv("../files/input/house_data.csv")

features = df[
    [
    "bedrooms",
    "bathrooms",
    "sqft_lot",
    "floors",
    "waterfront",
    "condition",
    ]
]

target = df[["price"]]
# %%
