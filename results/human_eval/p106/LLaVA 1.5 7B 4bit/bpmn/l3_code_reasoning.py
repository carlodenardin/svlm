def run_todo_app():
    """
    Simple to-do list application:
    - Displays current tasks (name and status)
    - Allows adding, removing, and updating tasks
    - Shows updated list after each operation
    - Exits on user command
    """
    tasks = []

    def display_tasks():
        if not tasks:
            print('No tasks.')
        else:
            print('Current tasks:')
            for idx, t in enumerate(tasks, start=1):
                print(f"{idx}. {t['name']} - {t['status']}")
        print()

    def add_task():
        name = input('Enter task name: ').strip()
        if not name:
            print('Task name cannot be empty.')
            return
        status = input('Enter status (e.g., Pending, In Progress, Completed): ').strip()
        if not status:
            status = 'Pending'
        tasks.append({'name': name, 'status': status})
        print('Task added.')

    def remove_task():
        if not tasks:
            print('No tasks to remove.')
            return
        display_tasks()
        try:
            idx = int(input('Enter task number to remove: ').strip())
            if 1 <= idx <= len(tasks):
                removed = tasks.pop(idx - 1)
                print(f"Removed: {removed['name']}")
            else:
                print('Invalid task number.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    def update_task():
        if not tasks:
            print('No tasks to update.')
            return
        display_tasks()
        try:
            idx = int(input('Enter task number to update: ').strip())
            if 1 <= idx <= len(tasks):
                new_status = input('Enter new status: ').strip()
                if new_status:
                    tasks[idx - 1]['status'] = new_status
                    print('Status updated.')
                else:
                    print('No status entered; nothing updated.')
            else:
                print('Invalid task number.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    print('To-Do List Application')
    while True:
        display_tasks()
        print('Commands: add, remove, update, exit')
        command = input('Enter command: ').strip().lower()
        if command == 'add':
            add_task()
        elif command == 'remove':
            remove_task()
        elif command == 'update':
            update_task()
        elif command == 'exit':
            break
        else:
            print('Unknown command.')
        print()
    print('Final task list:')
    display_tasks()
    return tasks