#!/bin/bash

# Parar o servidor dentro da screen
screen -S django -X quit

# Atualizar o repositório usando git pull
git pull origin main

# Reiniciar o servidor dentro da screen
screen -rd django
python3 manage.py runserver 0.0.0.0:8000

# Opcional: Aguardar alguns segundos para o servidor iniciar
sleep 10