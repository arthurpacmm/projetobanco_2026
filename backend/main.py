# ============================================================
# main.py — API do Estúdio de Tatuagem
# Descrição: Configura a aplicação e registra as rotas.
# Como rodar: python -m uvicorn main:app --reload
# ============================================================

from fastapi import FastAPI
from rotas import clientes

app = FastAPI()

app.include_router(clientes.router)


@app.get("/")
def inicio():
    # Retorna uma mensagem confirmando que a API está funcionando
    return {"mensagem": "API do estúdio de tatuagem funcionando!"}