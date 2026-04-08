# Simple To-Do List Application
# functions to add
def add_task(task, file="tasks.txt"):
    with open(file, "a") as f:
        f.write(task + "\n")


# function to get all tasks
def get_tasks(file="tasks.txt"):
    try:
        with open(file, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []


# function to delete a task by index
def delete_task(index, file="tasks.txt"):
    tasks = get_tasks(file)
    if 0 <= index < len(tasks):
        tasks.pop(index)
        with open(file, "w") as f:
            f.writelines(tasks)
        return True
    return False
