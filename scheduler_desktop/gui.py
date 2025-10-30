import FreeSimpleGUI as sg
import time
import functions
import os

'''Make sure txt is created if not exists'''
if not os.path.exists(functions.file):
    os.makedirs(os.path.dirname(functions.file), exist_ok = True)
    with open(functions.file,"w") as file:
        pass

sg.theme("DarkBlue3")

''' Create items for window'''

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do:")
input_box = sg.InputText(tooltip="Enter a To Do", key='todo')
add_button = functions.create_image_button('add.png', size=6,
                                           mouseover_colors="lightBlue2", tooltip='Add A ToDo', key='Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = functions.create_image_button('edit.png', size=6,
                            mouseover_colors='lightBlue2', tooltip='Edit the Task', key='Edit')
complete_button = functions.create_image_button('complete.png', size=6,
                            mouseover_colors='lightBlue2', tooltip='Complete the Task', key='Complete')
exit_button = functions.create_image_button('close.png', size=2, mouseover_colors='lightBlue2',
                                            tooltip='Close the App', key='Exit')

'''Create the window instance'''

window = sg.Window("My scheduler_desktop App",
                   layout= [[clock],[label],
                            [input_box,add_button],
                            [list_box], [edit_button, complete_button, exit_button]],
                   font=(["monospace", 16]))

while True:
    event, values = window.read(timeout=300) #Allows clock to appear running.
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    """Code is executed initially up to the previous line.
    Anything below is executed after user action."""

    if event == sg.WINDOW_CLOSED:
        break

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first",font=("Helvetica", 12))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select an item first", font=("Helvetica", 12))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()

