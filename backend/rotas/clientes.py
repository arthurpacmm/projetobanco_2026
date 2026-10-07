# ============================================================
# clientes.py — Rotas de clientes
# Descrição: Contém as rotas CRUD dos clientes.
# Como usar: As rotas são registradas pelo main.py.
# ============================================================

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from database import conectar

router = APIRouter()