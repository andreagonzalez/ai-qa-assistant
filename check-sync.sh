#!/bin/bash

# Atualiza informações do remoto
git fetch

echo "=== Verificando branch MAIN ==="
git checkout main >/dev/null 2>&1
git status
echo "Commits no remoto e não no local:"
git log main..origin/main --oneline
echo "Commits no local e não no remoto:"
git log origin/main..main --oneline

echo ""
echo "=== Verificando branch DEVELOP ==="
git checkout develop >/dev/null 2>&1
git status
echo "Commits no remoto e não no local:"
git log develop..origin/develop --oneline
echo "Commits no local e não no remoto:"
git log origin/develop..develop --oneline

