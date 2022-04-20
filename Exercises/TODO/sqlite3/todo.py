import sqlite3
from argparse import ArgumentParser

parser = ArgumentParser(description='simple todo app with sql')
parser.add_argument(
    '--install', help='Create DB. ATTENTION, will clear the current one.', action='store_true')
parser.add_argument('--add', help='Add new task to database')
parser.add_argument('--list', help='Show tasks', action='store_true')
parser.add_argument('--toogle', help='Change of task status')
args = parser.parse_args()


connection = sqlite3.connect(r'D:\Python\Git\Exercises\TODO\todo.db')
cursor = connection.cursor()


if args.install:
    print('DB Created.')
    cursor.execute('DROP TABLE todos')
    cursor.execute(
        'CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, is_done BOOLEAN)')
    connection.commit()

if args.add is not None:
    print('task added to database')
    title = args.add
    cursor.execute(
        'INSERT INTO todos(title, is_done) VALUES(?, false)', (title,))
    connection.commit()

if args.toogle is not None:
    print("Switching task status...")
    cursor.execute('SELECT is_done FROM todos WHERE id=?', (args.toogle,))
    is_done = cursor.fetchone()

    if is_done is None:
        print("There is no such task")
        quit()
    elif is_done[0] == 1:
        print("Marked as not completed")
        new_is_done = 0
    elif is_done[0] == 0:
        print("Marked as completed")
        new_is_done = 1

    cursor.execute('UPDATE todos SET is_done=? WHERE id=?',
                   (new_is_done, args.toogle))
    connection.commit()

if args.list:
    for todo_id, title, is_done in cursor.execute('SELECT * FROM todos'):
        print(f'{todo_id} \t {title} \t {"[v]" if is_done else "[ ]"}')
