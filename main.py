#  _______________
#  Import LIBRARIES
from typing import Literal
from fastapi import FastAPI, HTTPException

# from pydantic import BaseModel, Field
# from enum import Enum
#  Import FILES
from schema import Todo, TodoCreate, TodoUpdate
from todo_db import all_todos
#  _______________
#

api = FastAPI()


# GET, POST, PUT, DELETE
@api.get("/")
def index() -> dict[str, str]:
    return {"message": "This is the root of this web app!"}


#  Displays the give id todo - GET
@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo | Literal["Error, not found"]:
    print(f"todo_id: {todo_id}")
    for todo in all_todos:
        if todo.todo_id == todo_id:
            print(todo)
            return todo

    raise HTTPException(status_code=404, detail="Todo, not found")


#  Prints all_todo if none passed else print the first x - GET
@api.get("/todos", response_model=list[Todo])
def get_todos(first_n: int | None = None) -> list[Todo]:
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


# # CREATE a new Todo - POST
@api.post("/todos", response_model=Todo)
def create_todo(todo_create: TodoCreate) -> Todo:
    new_todo_id: int = (
        len(all_todos) + 1
    )  # max([todo.todo_id for todo in all_todos]) + 1

    new_todo: Todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo_create.todo_name,
        todo_description=todo_create.todo_description,
        priority=todo_create.priority,
    )

    all_todos.append(new_todo)

    return new_todo


# # UPDATE a todo = PUT
@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: int, updated_todo: TodoUpdate
) -> Todo | Literal["Error, not found"]:
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo, not found")


# #  DELETE a todo - DELETE
@api.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int) -> Todo | Literal["Error, not found"]:
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo: Todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo, not found")
