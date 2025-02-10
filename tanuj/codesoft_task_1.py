import sqlite3


conn = sqlite3.connect ("todo_list.db")
cursor = conn.cursor ()


cursor.execute ('''
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'pending' ) ''')

conn.commit ()

def add_task (title):
    """ Add a new task to the database"""
    cursor.execute ("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit ()
    print ("successfully added work!")

def view_tasks ():
    """ Look at all the tasks"""
    cursor.execute ("select * from tasks")
    tasks = cursor.fetchall ()
    if not   tasks:
        print ("No work found!")
    else:
        for task in tasks:
             print(f"[{task[0]}] {task[1]} - {task[2]}")
            

def update_task (task_id, new_title):
    """ Update Task Title"""
    cursor.execute ("UPDATE tasks SET Title =? WHERE ID =?", (new_title, task_id))
    conn.commit ()
    print ("Task was successfully updated!")

def delete_task (task_id):
    """ Remove a task. """ ,
    cursor.execute ("DELETE FROM  tasks WHERE ID =?", (task_id,))
    conn.commit ()
    print ("Task was successfully removed!")

def mark_completed (task_id):
    """ complete Mark Task. """ ,
    cursor.execute ("UPDATE   tasks SET position = 'full'WHERE ID  =?", (task_id,))
    conn.commit ()
    print ("marked as the work being completed!")

def main ():
  while True:
        print ("\nTo-DO list menu:")
        print ("1. Add work")
        print ("2. See work")
        print ("3. Update work")
        print ("4. Remove task")
        print ("5. Mark completed as Task")
        print ("6. Get out")
        choice = input ("Enter your choice:")

        if choice == "1":
            title = input ("Enter the task title:")
            add_task (title)
        
        elif choice == "2":
         view_tasks ()
        
        elif choice == "3":
            title_id = input ("Enter the task id to update: ")
            new_title = input("enter new title:")
        
        elif choice == "4":
           task_id = input ("Enter the task id to delete :")
           delete_task(task_id)
        
        elif choice == "5":
          task_id = input ("Enter the task  id to mark as completed:")
          mark_completed(task_id)
        
        elif choice == "6":
           print("Exiting program.....")
           break
        else:
            print("invalid choice. please try again")


if __name__ == "__main__":
    main()
    conn.close()
