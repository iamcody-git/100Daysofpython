todos = []

while True:
    user_task = input("Enter add, edit, show, delete or exit: ")
    user_task = user_task.strip()
    
    match user_task:
        case 'add':
            todo = input("Enter a todo task: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'delete':
            number = int(input("Enter the number you want to delete: "))
            number = number -1
            todos.pop(number)
        case 'edit':
            number = int(input("Enter a index you want to edit: "))
            new_todo = input("Enter a new todo: ")
            todos[number] = (new_todo)
        case 'exit':
            break
            
    
   
    

        
    