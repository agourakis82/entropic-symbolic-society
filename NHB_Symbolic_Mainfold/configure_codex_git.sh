#!/bin/bash

# === CONFIGURAÇÃO MANUAL ===
GITHUB_USER="agourakis82"
REPO_NAME="entropic-symbolic-society"
REPO_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Biologia Fractal/$REPO_NAME"
TOKEN="<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>"

# === CONFIGURAÇÕES DE GIT ===
cd "$REPO_DIR" || exit 1

echo "🔐 Configurando autenticação com token..."

# Cria o arquivo .netrc com credenciais seguras
echo -e "machine github.com\nlogin $GITHUB_USER\npassword $TOKEN" > ~/.netrc
chmod 600 ~/.netrc

# Configura URL remota com token embutido (não recomendado expor diretamente)
git remote set-url origin https://$GITHUB_USER:$TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git

# Garante identidade
git config --global user.name "Demetrios Codex Agent"
git config --global user.email "demetrios-codex@users.noreply.github.com"

echo "✅ Configuração finalizada com sucesso."