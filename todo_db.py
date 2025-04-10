#  _______________
#  Import LIBRARIES
# from typing import Any
#  Import FILES
from schema import Todo, Priority
#  _______________
#


all_todos: list[Todo] = [
    Todo(
        todo_id=1,
        todo_name="Clean house",
        todo_description="Cleaning the house thoroughly",
        priority=Priority.HIGH,
    ),
    Todo(
        todo_id=2,
        todo_name="Sports",
        todo_description="Going to the gym for workout",
        priority=Priority.MEDIUM,
    ),
    Todo(
        todo_id=3,
        todo_name="Read",
        todo_description="Read chapter 5 of the book",
        priority=Priority.LOW,
    ),
    Todo(
        todo_id=4,
        todo_name="Work",
        todo_description="Complete project documentation",
        priority=Priority.MEDIUM,
    ),
    Todo(
        todo_id=5,
        todo_name="Study",
        todo_description="Prepare for upcoming exam",
        priority=Priority.LOW,
    ),
]


# {
#   "todo_name": "test",
#   "todo_description": "test",
#   "priority": 2
# }


# {
#   "todo_name": "Code",
#   "todo_description": "Write python tests",
#   "priority": 1
# }


#  __________________________  OLD:  all_todos  _______________________

# all_todos: list[str, Any] = [
#     {"todo_id": 1, "todo_name": "Sports", "todo_description": "Go to the gym"},
#     {"todo_id": 2, "todo_name": "Read", "todo_description": "Read 10 pages"},
#     {"todo_id": 3, "todo_name": "Shop", "todo_description": "Go shopping"},
#     {"todo_id": 4, "todo_name": "Study", "todo_description": "Study for exam"},
#     {"todo_id": 5, "todo_name": "Meditate", "todo_description": "Meditate 20 minutes"},
# ]


# {
#     "todo_name": "New Todo",
#     "todo_description": "New Todo Description"
# }

# {
#     "todo_name": "Power-walking",
#     "todo_description": "Make 10.000 fast steps"
# }

# {
#     "todo_name": "test",
#     "todo_description": "test"
# }
