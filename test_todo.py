from todo import add_task, get_tasks, delete_task


def test_add_task():
    add_task("Test Task", "test_tasks.txt")
    tasks = get_tasks("test_tasks.txt")
    assert "Test Task\n" in tasks


def test_get_tasks():
    add_task("Task 1", "test_tasks.txt")
    add_task("Task 2", "test_tasks.txt")
    tasks = get_tasks("test_tasks.txt")
    assert len(tasks) >= 2


def test_delete_task():
    add_task("Delete Me", "test_tasks.txt")
    tasks_before = get_tasks("test_tasks.txt")
    delete_task(0, "test_tasks.txt")
    tasks_after = get_tasks("test_tasks.txt")
    assert len(tasks_after) < len(tasks_before)
