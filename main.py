from fastapi import FastAPI
from database import Base, engine
from routers import categorias, produtos, movimentacoes

# Cria tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Estoque")

# Inclui routers
app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(movimentacoes.router)
