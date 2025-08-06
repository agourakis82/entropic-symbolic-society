#!/bin/bash

echo "⏳ Limpando ambiente anterior..."
rm -rf ../env311
rm -rf clean_env

echo "🔧 Criando novo ambiente clean_env..."
python3.11 -m venv clean_env
source clean_env/bin/activate

echo "⬇️ Atualizando pip e setuptools..."
pip install --upgrade pip setuptools wheel

echo "📦 Instalando dependências..."
pip install pandas==2.2.2 numpy==2.3.2 scikit-learn==1.4.2 \
    matplotlib==3.8.4 seaborn==0.13.2 networkx==3.2.1 \
    node2vec==0.4.6 tqdm==4.67.1 jupyterlab==4.1.5

echo "✅ Ambiente pronto. Ative com:"
echo "source clean_env/bin/activate"