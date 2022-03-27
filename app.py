import os
import sqlite3

connection = sqlite3.connect("tasks.db")


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()
    cls()
    print("Current tasks:")
    for row in result:
        print(f'{row[0]}. {row[1]}')


def add_task(connection):
    task = input("Type task name: ")
    if task == 0:
        print("powrot do menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        connection.commit()
    cls()
    print(f'Task added: {task}')


def delete_task(connection):
    id_to_be_deleted = input("Type number of task to be deleted: ")
    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid =?""",
                               (id_to_be_deleted,)).rowcount
    cls()
    if rows_deleted == 0:
        print("Incorrect task number :(")
    else:
        print("task deleted")
    connection.commit()


def show_menu():
    print()
    print('1. Show tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Exit')
    global user_choice
    user_choice = int(input("Select number: "))


while True:
    show_menu()
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        add_task()
    if user_choice == 3:
        delete_task()
    if user_choice == 4:
        break
