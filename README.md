# ✅ Projeto ToDo com FastAPI

Este é um projeto básico de uma API de tarefas (ToDo) feito com **FastAPI**. Ele foi criado para fins educacionais e será utilizado nas aulas.

---

## 🔧 Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 📌 Funcionalidades da API

A API permite realizar operações básicas de um CRUD:

- ✅ `GET /todos` — Lista todas as tarefas
- 🔍 `GET /todos/{id}` — Retorna uma tarefa específica
- ➕ `POST /todos` — Cria uma nova tarefa
- 🔄 `PUT /todos/{id}` — Atualiza uma tarefa existente
- ❌ `DELETE /todos/{id}` — Remove uma tarefa

---

## 📋 Exemplo de tarefa

```json
{
  "id": 1,
  "title": "Estudar Python",
  "description": "Assistir aula de FastAPI",
  "done": false
}
