# 🧠 The Symbolic Manifold Project: Entropic Dynamics in Cognitive Space

![Symbolic Graph](figs/cover_symbolic_graph.png)

## 📘 Overview

This repository contains the full implementation, simulation, and symbolic analysis pipeline for the study entitled:

> **"Symbolic Manifolds and Entropic Dynamics: A Cognitive Topology of Mental States"**

This project is part of the manuscript preparation for submission to **Nature Human Behaviour** and builds upon the foundational fractal-entropic model previously structured under the DOI: [10.5281/zenodo.16533374](https://doi.org/10.5281/zenodo.16533374).

## 🔭 Project Scope

This work integrates large-scale semantic networks (SWOW) with symbolic metrics, graph theory, node embeddings (Node2Vec), and topological clustering (UMAP + HDBSCAN) to construct a dynamic and interpretable manifold of cognition. The project is guided by four core research questions:

1. **Can symbolic distances in associative space model cognitive entropy?**
2. **How do topological centrality and clustering reflect symbolic anchoring and curvature of thought?**
3. **Is it possible to derive measurable symbolic metrics that correlate with mental states?**
4. **Can entropic manifolds reveal hidden cognitive constraints or attractors?**

## 🧪 Architecture

| Notebook | Description |
|---------|-------------|
| `00_Overview_and_Readme.ipynb` | Project scope, goals, and roadmap (this document in notebook form) |
| `01_Load_and_Visualize_SWOW.ipynb` | Loads SWOW dataset, basic structure and stats |
| `01_SWOW_graph_analysis.ipynb` | Graph building and visualization using NetworkX |
| `02_Centrality_and_SymbolicMetrics.ipynb` | Calculates symbolic anchoring, curvature, entropy |
| `03_EntropicEmbeddings_and_CognitiveDistances.ipynb` | Node2Vec embeddings, cognitive space projection |
| `04_Map_Symbolic_Metrics_From_SWOW.ipynb` | Aligns graph metrics and embeddings, builds dataframe |
| `05_Clustering_Symbolic_Manifold.ipynb` | UMAP + HDBSCAN clustering and symbolic topology inference |
| `06_Visualize_UMAP_Embeddings.ipynb` | Advanced visualizations, inter-cluster relationships |

## 🗂 Directory Structure

```
NHB_Symbolic_Mainfold/
├── data/                      # Processed graph and metric files (LFS tracked)
├── figs/                      # All generated figures
├── notebook/                 # Source notebooks (00 to 06)
├── requirements.txt          # Reproducible environment
├── reset_env.sh              # Clean environment setup script
├── clean_and_commit.sh       # Commit-cleanup automation script
└── README.md                 # This document
```

## ⚙️ Setup Instructions

1. Create and activate environment:
```bash
bash reset_env.sh
source clean_env/bin/activate
```

2. Launch JupyterLab:
```bash
jupyter lab
```

3. Run notebooks in order (`00_` to `06_`).

## 🧠 Author and Affiliation

This project is developed by **Demetrios Agourakis**, in the context of a multi-disciplinary exploration of cognition, entropy, symbolic logic and computational neuroscience. 

Part of a broader research series under the title:
> **"The Fractal Nature of an Entropically-Driven Society"**  
> DOI (main): [10.5281/zenodo.16533374](https://doi.org/10.5281/zenodo.16533374)

## 📎 License
MIT License.

---

For additional files, related publications or scripts, see the companion repositories and datasets listed in the main Zenodo registry.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16752238.svg)](https://doi.org/10.5281/zenodo.16752238)

**This repository corresponds to version v1.5 (DOI: 10.5281/zenodo.16752238), building on v1.4 (10.5281/zenodo.16730036).**  
Please cite as follows:

```bibtex
@misc{agourakis2025symbolic_v1_5,
 author = {Demetrios Agourakis},
 title = {Symbolic Manifolds and Entropic Dynamics: A Cognitive Topology of Mental States},
 year = {2025},
 publisher = {Zenodo},
 doi = {10.5281/zenodo.16752238},
 version = {v1.5},
 url = {https://doi.org/10.5281/zenodo.16752238}
}
