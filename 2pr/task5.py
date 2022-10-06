from sklearn.datasets import fetch_california_housing
import pandas as pd
data = fetch_california_housing(as_frame=True)


print(data.data, data.target)


Med = pd.concat([data.data, data.target], axis=1)

print(Med)

print(data.data.info())