# ============================================================
# database.py — Conexão com o banco de dados
# Descrição: Cria a conexão entre a API e o MySQL.
# Como usar: A função conectar() é utilizada pelas rotas.
# ============================================================

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def conectar():
    # Cria e retorna uma conexão com o banco de dados
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )