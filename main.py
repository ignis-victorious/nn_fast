#  _______________ 
#  Import LIBRARIES
from typing import Any, Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field 
from enum import Enum
#  Import FILES
from todo_db import all_todos
#  _______________
# 

api = FastAPI()


# GET, POST, PUT, DELETE
@api.get('/')
def index() -> dict[str, str]:
    return {"message": "Hello World"}


#  Displays the give id todo - GET
@api.get('/todos/{todo_id}')
def get_todo(todo_id: int) -> dict[str, dict[str, Any]] | None:
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}

#  Prints all_todo if none passed else print the first x - GET
@api.get('/todos')
def get_todos(first_n: int|None = None) -> list[dict[str, Any]]:
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

# CREATE a new Todo - POST
# {
#     "todo_name": "New Todo",
#     "todo_description": "New Todo Description"
# 
@api.post('/todos')
def create_todo(todo: dict) -> dict[str, Any]:
    new_todo_id:int = max([todo['todo_id'] for todo in all_todos]) + 1

    new_todo :  dict[str, Any]= {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)

    return new_todo

# UPDATE a todo = PUT
@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict) -> dict[str, Any] | Literal['Error, not found']:# -> dict[str, Any] | Literal['Error, not found']:
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            return todo
    return "Error, not found"


#  DELETE a todo - DELETE
@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int)-> dict[str, Any] | Literal['Error, not found']:
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo:dict[str,any] = all_todos.pop(index)
            return deleted_todo
    return "Error, not found"


# def main():
#     print("Hello from nn-fast!")


# if __name__ == "__main__":
#     main()
