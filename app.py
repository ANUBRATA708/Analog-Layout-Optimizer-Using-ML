import streamlit as st
import os
import pandas as pd
import joblib
import altair as alt
from sklearn.linear_model import LinearRegression
from feature_extractor.extract_features import extract_features_from_netlist
from utils.rank_circuits import rank_circuits

st.set_page_config(page_title="Analog Layout Area Predictor", layout="wide")
st.title("📐 Predict Layout Area from Netlist with Ranking Visualization")

def train_model(features_path, model_path):
    df = pd.read_csv(features_path)
    df = df[df["area"] > 0]
    if df.empty:
        return None
    X = df[["num_nodes", "num_edges", "avg_degree"]]
    y = df["area"]
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, model_path)
    return model

uploaded_file = st.file_uploader("📎 Upload a .sp Netlist", type=["sp"])

if uploaded_file is not None:
    upload_dir = os.path.join("circuit_data", "netlists")
    os.makedirs(upload_dir, exist_ok=True)
    netlist_path = os.path.join(upload_dir, uploaded_file.name)
    with open(netlist_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Saved: {uploaded_file.name}")

    num_nodes, num_edges, avg_degree = extract_features_from_netlist(netlist_path)
    st.write("### 🧠 Extracted Features")
    st.json({
        "Nodes": num_nodes,
        "Edges": num_edges,
        "Average Degree": round(avg_degree, 2)
    })

    model_path = "ml_model/model.pkl"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        predicted_area = model.predict([[num_nodes, num_edges, avg_degree]])[0]
        st.success(f"📏 Predicted Layout Area: {predicted_area:.2f} sq. units")
    else:
        st.error("❌ Trained model not found. Please train it first.")

    features_path = "circuit_data/features.csv"
    if os.path.exists(features_path) and st.button("📊 Rank and Visualize Training Data"):
        output_csv = "reports/ranked_results.csv"
        os.makedirs("reports", exist_ok=True)
        rank_circuits(features_path, output_csv)

        df = pd.read_csv(output_csv)
        st.write("### 🧾 Ranked Results Table")
        st.dataframe(df)

        st.write("### 📊 Complexity Score Ranking (Bar Chart)")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('circuit_name:N', sort='-y', title='Circuit'),
            y=alt.Y('complexity_score:Q', title='Complexity Score'),
            color=alt.Color('decision:N', title='Decision'),
            tooltip=['circuit_name', 'complexity_score', 'decision']
        ).properties(width=800, height=400)

        st.altair_chart(chart, use_container_width=True)
        st.download_button("📥 Download Ranked Results CSV", data=open(output_csv).read(), file_name="ranked_results.csv")
