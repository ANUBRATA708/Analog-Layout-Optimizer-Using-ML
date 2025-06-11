import pandas as pd

def calculate_complexity(num_nodes, num_edges, avg_degree):
    return round(num_nodes * 0.5 + num_edges * 0.3 + avg_degree * 0.2, 2)

def decide_path(complexity, area):
    if complexity < 8 and area < 200:
        return "Reuse existing layout"
    elif complexity < 12:
        return "Semi-Automated (template-based)"
    else:
        return "Full Custom Required"

def rank_circuits(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    df["complexity_score"] = df.apply(
        lambda row: calculate_complexity(row["num_nodes"], row["num_edges"], row["avg_degree"]), axis=1)
    df["rank_by_complexity"] = df["complexity_score"].rank(ascending=False).astype(int)
    df["rank_by_area"] = df["area"].rank(ascending=False).astype(int)
    df["decision"] = df.apply(lambda row: decide_path(row["complexity_score"], row["area"]), axis=1)

    df.to_csv(output_csv, index=False)
    print(f"Ranked results saved to {output_csv}")

# Optional test run
if __name__ == "__main__":
    rank_circuits("circuit_data/features.csv", "reports/ranked_results.csv")
