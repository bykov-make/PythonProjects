import os
import FreeSimpleGUI as sg

#Define base directory and file paths
current_dir = os.path.dirname(os.path.abspath(__file__))

files_dir = os.path.join(current_dir, 'files')
images_dir = os.path.join(files_dir, 'images')

file = os.path.join(files_dir, 'todos.txt')
print(file)

print(images_dir)

#ToDos Read / Write
def get_todos(filepath=file):
    '''Returns the todo items in a list'''
    with open(filepath,'r') as local_file:
        return local_file.readlines()


def write_todos(todos_arg, filepath=file):

    with open(filepath,'w') as local_file:
        return local_file.writelines(todos_arg)

#Images
def get_image_path(image_name):
    '''Return the absolute path to an image'''
    return os.path.join(images_dir, image_name)

def create_image_button(image_name, **button_args):
    '''Create a button with an image using the absolute path'''
    image_path = get_image_path(image_name)
    if os.path.exists(image_path):
        return sg.Button(image_source=image_path, **button_args)
    else:
        fallback_text = image_name.replace('.png','').title()
        print(f"Image not found: {image_path}, using text button instead")
        return sg.Button(fallback_text, **button_args)