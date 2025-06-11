import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("circuit_data/features.csv")
X = df[["num_nodes", "num_edges", "avg_degree"]]
y = df["area"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "ml_model/model.pkl")
print("✅ Model trained.")
