class Memento:
  
  def __init__(self, state):
    self._state = list(state)
    
  def get_state(self):
    return self._state
  def name(self):
      self.manager.my_name('Dilan')

class TodoList:
    def __init__(self):
        self._tasks = []
        self.momento=Memento().name()

    def add_task(self, task):
        if not isinstance(task, str) or not task:
            print("Error: Task must be a non-empty string.")
            return
        self._tasks.append(task)
        print(f"Task added: '{task}'")

    def remove_task(self, task):
        try:
            Memento(self._tasks)
            self._tasks.remove(task)
            print(f"Task removed: '{task}'")
        except ValueError:
            print(f"Task '{task}' not found in the list.")

    def save(self):
        print("Saving TodoList state...")
        return Memento(self._tasks)

    def restore(self, memento):
        if not isinstance(memento, Memento):
            print("Error: Invalid Memento object provided for restoration.")
            return
        self._tasks = memento.get_state()
        print("TodoList state restored from Memento.")

    def get_tasks(self):
        return list(self._tasks)

class History:
    def __init__(self):
        self._history = []

    def add_memento(self, memento):
        if not isinstance(memento, Memento):
            print("Error: Can only add Memento objects to history.")
            return
        self._history.append(memento)
        print("Memento added to history.")

    def get_memento(self):
        if not self._history:
            print("History is empty. Cannot retrieve memento.")
            return None
        print("Retrieving memento from history.")
        return self._history.pop()

def run_todo_interface():
    todo_list = TodoList()  
    history = History()     

    print("--- To-Do System ---")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Save State")
        print("4. Undo")
        print("5. Delete Task") 
        print("6. Exit")

        choice = input("Enter your choice (1-6): ") 

        if choice == '1':
            task = input("Enter task description: ")
            todo_list.add_task(task)

        elif choice == '2':
            tasks = todo_list.get_tasks()
            print("\n--- Your Tasks ---")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet.")
            print("------------------")

        elif choice == '3':
            memento = todo_list.save()
            history.add_memento(memento)

        elif choice == '4':
            memento = history.get_memento()
            if memento:
                todo_list.restore(memento)
            else:
                print("No history to undo.")

        elif choice == '5': 
            task_to_delete = input("Enter the task description to delete: ")
            todo_list.remove_task(task_to_delete)

        elif choice == '6': 
            print("Exiting To-Do System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.") 

if __name__ == "__main__":
    run_todo_interface()