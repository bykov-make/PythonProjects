import FreeSimpleGUI as sg
import streamlit

file = 'todos.txt'
#ToDos Read / Write
def get_todos(filepath=file):
    '''Returns the todo items in a list'''
    with open(filepath,'r') as local_file:
        return local_file.readlines()


def write_todos(todos_arg, filepath=file):

    with open(filepath,'w') as local_file:
        return local_file.writelines(todos_arg)

