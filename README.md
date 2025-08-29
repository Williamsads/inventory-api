# 📦 Inventory API

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.111.0-brightgreen)
![SQLite](https://img.shields.io/badge/SQLite-3.41.2-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

API RESTful para gerenciamento de inventário, desenvolvida em **Python** com **FastAPI** e **SQLAlchemy**.  
Permite cadastrar, listar, atualizar e remover itens de estoque de forma simples e eficiente. 🚀

---

## 🚀 Tecnologias

- [Python 3.12+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- Banco de dados: **SQLite**

---

## 📂 Estrutura do projeto  

```
INVENTORY-API
│── main.py # Ponto de entrada da aplicação (Controller root)
│── database.py # Configuração da base de dados
│── models.py # Modelos do banco (ORM)
│── schemas.py # Schemas de validação
│── README.md # Documentação
│── estoque.db # Base local SQLite
│
├── repository/ # Camada de acesso a dados (Repository)
│ │── categoria_repo.py
│ │── movimentacao_repo.py
│ │── produto_repo.py
│
├── services/ # Regras de negócio (Service Layer)
│ │── categoria_service.py
│ │── movimentacao_service.py
│ │── produto_service.py
│
├── routers/ # Endpoints da API (Controllers)
│ │── categorias.py
│ │── movimentacoes.py
│ │── produtos.py
│
├── venv/ # Ambiente virtual
└── pycache/ # Cache do Python
```

---

## ⚡ Funcionalidades

### Categorias
- Criar categoria com nome único
- Listar todas as categorias
- Buscar categoria por ID
- Atualizar categoria
- Excluir categoria (somente se não houver produtos vinculados)

### Produtos
- Criar produto com SKU único
- Listar todos os produtos
- Buscar produto por ID
- Atualizar produto
- Excluir produto (com remoção automática do estoque)
- Vincular produto obrigatoriamente a uma categoria

### Movimentações de Estoque
- Criar registro automático de estoque ao criar produto
- Registrar entrada de mercadorias
- Registrar saída de mercadorias
- Listar todos os estoques
- Buscar estoque por produto
- Histórico de movimentações (entrada/saída)

### Regras de Negócio
- Não permitir estoque negativo
- Não permitir exclusão de categoria com produtos vinculados
- SKU e nome de categoria devem ser únicos
- Operações críticas devem ser atômicas

---

## 🛠️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/inventory-api.git
cd inventory-api

python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate
```

---

2. crie o ambiente virtual.
   
```bash

python -m venv venv

# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate

⚠️ No Windows, se der erro de execução de scripts, rode no powershell como adm:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
3. Instale as dependências:
   
```bash
pip install fastapi uvicorn sqlalchemy
```

▶️ Executando a API

```bash
uvicorn main:app --reload
```
Acesse a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs

📝 Exemplos de Requisições:

Criar Categoria
```bash
POST /categorias/
Content-Type: application/json

{
  "nome": "Bebidas"
}
```
Listar Categorias
```bash
GET /categorias/
```
Criar Produto
```bash
POST /produtos/
Content-Type: application/json

{
  "nome": "Coca-Cola 350ml",
  "sku": "COCA350",
  "categoria_id": 1
}
```
Movimentação de Estoque
```bash
POST /movimentacoes/
Content-Type: application/json

{
  "estoque_id": 1,
  "tipo": "entrada",
  "quantidade": 50
}
```
Histórico de Movimentações

```bash
GET /movimentacoes/1
```

🧩 Observações



```bash
Todas as respostas seguem o formato JSON.

Códigos HTTP são adequados para cada tipo de resposta.

Logs são gerados para operações críticas (criação, atualização, remoção).
``` 
