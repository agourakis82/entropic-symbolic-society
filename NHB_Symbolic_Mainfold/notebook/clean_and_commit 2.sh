#!/bin/bash

echo "🔍 Atualizando .gitignore..."
echo -e "\n# Ignorar ambiente virtual, cache e arquivos temporários" >> .gitignore
echo "env311/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "*.DS_Store" >> .gitignore
echo "*.ipynb_checkpoints/" >> .gitignore

echo "📦 Adicionando arquivos relevantes..."
git add NHB_Symbolic_Mainfold/data/*.csv
git add NHB_Symbolic_Mainfold/data/*.gpickle
git add NHB_Symbolic_Mainfold/data/*.npy
git add NHB_Symbolic_Mainfold/notebook/*.ipynb
git add NHB_Symbolic_Mainfold/notebook/*.sh
git add NHB_Symbolic_Mainfold/notebook/requirements.txt
git add .gitignore

echo "📝 Commitando alterações com rastreabilidade editorial..."
git commit -m "🔁 Reorganiza estrutura do projeto NHB: notebooks, dados, .gitignore e padronização de diretórios"

echo "⬆️ Pronto para dar push com:"
echo "git push origin main"