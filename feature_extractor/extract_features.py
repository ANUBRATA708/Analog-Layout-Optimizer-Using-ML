import os
import csv

def extract_features_from_netlist(netlist_path):
    with open(netlist_path, 'r') as f:
        lines = f.readlines()

    num_nodes = 0
    num_edges = 0
    components = 0
    nodes = set()

    for line in lines:
        if line.strip() == '' or line.strip().startswith('*'):
            continue
        parts = line.strip().split()
        if len(parts) >= 3:
            nodes.update(parts[1:3])
            components += 1
            num_edges += 1

    num_nodes = len(nodes)
    avg_degree = (2 * num_edges) / num_nodes if num_nodes > 0 else 0

    return num_nodes, num_edges, avg_degree

def generate_features_csv():
    base_dir = 'circuit_data'
    netlist_dir = os.path.join(base_dir, 'netlists')
    features_csv_path = os.path.join(base_dir, 'features.csv')

    with open(features_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['circuit_name', 'num_nodes', 'num_edges', 'avg_degree', 'area']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for filename in os.listdir(netlist_dir):
            if filename.endswith('.sp'):
                netlist_path = os.path.join(netlist_dir, filename)
                num_nodes, num_edges, avg_degree = extract_features_from_netlist(netlist_path)

                # Dummy area = weighted sum (until prediction is integrated)
                predicted_area = num_nodes * 10 + avg_degree * 5

                writer.writerow({
                    'circuit_name': filename,
                    'num_nodes': num_nodes,
                    'num_edges': num_edges,
                    'avg_degree': avg_degree,
                    'area': predicted_area
                })

    print(f"✅ Features extracted and saved to {features_csv_path}")

if __name__ == "__main__":
    generate_features_csv()
