#!/bin/bash

echo "🔁 Limpando ambiente anterior..."
rm -rf clean_env

echo "🧪 Criando novo ambiente virtual clean_env..."
python3.11 -m venv clean_env
source clean_env/bin/activate

echo "⬆️ Atualizando pip..."
pip install --upgrade pip

echo "📦 Instalando dependências com compatibilidade garantida..."
pip install numpy==1.26.4 pandas==2.2.2 scikit-learn==1.4.2 \
    matplotlib==3.8.4 seaborn==0.13.2 networkx==2.8.8 \
    node2vec==0.4.6 tqdm==4.67.1 jupyterlab==4.1.5 umap-learn==0.5.4

echo "✅ Ambiente limpo e funcional criado!"