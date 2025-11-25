# 🚀 Py Finances

Backend desenvolvido em **Python** utilizando **FastAPI**, com suporte a migrações via **Alembic** e gerenciamento de ambiente virtual com **UV**.

## 🧰 Tecnologias Utilizadas

- **pyenv** – Gerenciamento de versões do Python  
- **uv** – Gerenciador de ambientes e pacotes ultrarrápido  
- **FastAPI** – Framework web moderno e performático  
- **Uvicorn** – Servidor ASGI para execução da API  
- **Alembic** – Controle de versões/migrações do banco de dados  

---

## ⚙️ Como Inicializar o Projeto

### 1️⃣ Instale o UV  
O projeto utiliza o **UV** como gerenciador de ambiente e dependências.  
Siga a instalação oficial:  
https://docs.astral.sh/uv/getting-started/installation/

---

### 2️⃣ Configure o arquivo `.env`  
Crie um arquivo `.env` na raiz do projeto contendo:

```
DATABASE_HOST=seu_host
DATABASE_PORT=sua_porta
DATABASE_NAME=seu_banco
DATABASE_USERNAME=seu_usuario
DATABASE_PASSWORD=sua_senha
OPENAI_API_KEY=sua_chave_openai
```

> 💡 **Dica:** Recomendo utilizar o **Supabase** para criar seu banco PostgreSQL:  
> https://supabase.com/

### 3️⃣ Prepare o banco de dados (Migrações Alembic)

Gere a migração inicial:

```sh
uv run alembic revision --autogenerate -m "initial migration"
uv run alembic upgrade head
```

---

### 4️⃣ Execute o servidor FastAPI
```sh
uv run taskipy app

uv run task app
```