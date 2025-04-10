#  _______________
#  Import LIBRARIES
from pydantic import BaseModel, Field
from enum import IntEnum
#  Import FILES
#  _______________
#


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    todo_name: str = Field(
        ..., min_length=3, max_length=512, description="Name of the todo"
    )
    todo_description: str = Field(..., description="Description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier of the todo")
    # pass


class TodoUpdate(BaseModel):
    todo_name: str | None = Field(
        None, min_length=3, max_length=512, description="Name of the todo"
    )
    todo_description: str | None = Field(None, description="Description of the todo")
    priority: Priority | None = Field(None, description="Priority of the todo")
