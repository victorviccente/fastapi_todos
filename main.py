from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool = False

todos: List[Todo] = [
    Todo(id=1, title="Estudar Python", description="Assistir aula de FastAPI", done=False),
    Todo(id=2, title="Gravar vídeo", description="Explicando projeto de ToDo", done=False),
    Todo(id=3, title="Revisar conteúdo", description="Preparar slides para aula", done=True),
]

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    for t in todos:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"detail": "Tarefa deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
