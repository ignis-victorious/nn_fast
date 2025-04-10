#  _______________
#  Import LIBRARIES
from typing import Literal
from fastapi import FastAPI

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
    return {"message": "Hello World"}


#  Displays the give id todo - GET
@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo | Literal["Error, not found"]:
    print(f"todo_id: {todo_id}")
    for todo in all_todos:
        if todo.todo_id == todo_id:
            print(todo)
            return todo

    return "Error, not found"


# @api.get('/todos/{todo_id}')
# def get_todo(todo_id: int) -> dict[str, dict[str, Any]] | None:
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             return {'result': todo}


#  Prints all_todo if none passed else print the first x - GET
@api.get("/todos", response_model=list[Todo])
def get_todos(first_n: int | None = None) -> list[Todo]:
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos


# @api.get("/todos")
# def get_todos(first_n: int | None = None) -> list[dict[str, Any]]:
#     if first_n:
#         return all_todos[:first_n]
#     else:
#         return all_todos


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


# # {
# #     "todo_name": "New Todo",
# #     "todo_description": "New Todo Description"
# #
# @api.post("/todos")
# def create_todo(todo: dict) -> dict[str, Any]:
#     new_todo_id: int = max([todo["todo_id"] for todo in all_todos]) + 1

#     new_todo: dict[str, Any] = {
#         "todo_id": new_todo_id,
#         "todo_name": todo["todo_name"],
#         "todo_description": todo["todo_description"],
#     }

#     all_todos.append(new_todo)

#     return new_todo


# # UPDATE a todo = PUT
@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: int, updated_todo: TodoUpdate
) -> Todo | Literal["Error, not found"]:
    print("___________ entered the function ____________")
    for todo in all_todos:
        print(f"_______ todo: {todo}")
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name
            todo.todo_description = updated_todo.todo_description
            todo.priority = updated_todo.priority
            return todo
    return "Error, not found"


# @api.put("/todos/{todo_id}")
# def update_todo(
#     todo_id: int, updated_todo: dict
# ) -> (
#     dict[str, Any] | Literal["Error, not found"]
# ):  # -> dict[str, Any] | Literal['Error, not found']:
#     for todo in all_todos:
#         if todo["todo_id"] == todo_id:
#             todo["todo_name"] = updated_todo["todo_name"]
#             todo["todo_description"] = updated_todo["todo_description"]
#             return todo
#     return "Error, not found"


# #  DELETE a todo - DELETE
@api.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int) -> Todo | Literal["Error, not found"]:
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo: Todo = all_todos.pop(index)
            return deleted_todo
    return "Error, not found"


# @api.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int) -> dict[str, Any] | Literal["Error, not found"]:
#     for index, todo in enumerate(all_todos):
#         if todo["todo_id"] == todo_id:
#             deleted_todo: dict[str, any] = all_todos.pop(index)
#             return deleted_todo
#     return "Error, not found"


# # def main():
# #     print("Hello from nn-fast!")


# # if __name__ == "__main__":
# #     main()
