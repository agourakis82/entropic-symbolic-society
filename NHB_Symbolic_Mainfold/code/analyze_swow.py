import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import pickle

# Caminhos
graph_path = "NHB_Symbolic_Mainfold/data/swow_graph.gpickle"
out_path = pathlib.Path("NHB_Symbolic_Mainfold/figs")
out_path.mkdir(parents=True, exist_ok=True)

# Carrega o grafo
with open(graph_path, "rb") as f:
    G = pickle.load(f)

# Métricas básicas
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
density = nx.density(G)
avg_degree = sum(dict(G.degree()).values()) / num_nodes
largest_scc = max(nx.strongly_connected_components(G), key=len)
scc_size = len(largest_scc)

# Plot da distribuição de grau
degree_sequence = sorted([d for _, d in G.degree()], reverse=True)
plt.figure(figsize=(10, 6))
plt.hist(degree_sequence, bins=100, color="steelblue", edgecolor="black")
plt.title("Degree Distribution in the SWOW Graph")
plt.xlabel("Degree")
plt.ylabel("Frequency (log)")
plt.yscale("log")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(out_path / "swow_degree_distribution.png", dpi=300)
plt.close()

# Relatório no terminal
print(f"✅ Analysis complete!")
print(f"Nodes: {num_nodes}, Edges: {num_edges}")
print(f"Density: {density:.6f}, Average degree: {avg_degree:.2f}")
print(f"Size of the largest strongly connected component: {scc_size}")
print(f"Graph saved to: {out_path / 'swow_degree_distribution.png'}")