import os
from dotenv import load_dotenv
from utils.database_connection import get_db_connection
from utils.model_loader import load_llama_model
from utils.tasks import add_task, get_tasks, generate_task_list

load_dotenv()

conn, cursor = get_db_connection()
model_path = os.getenv("MODEL_PATH")
model = load_llama_model(model_path)

def main():
    input_text = '''Please create a structured, prioritised task list:
                    1. Complete the project report
                    2. Buy groceries
                    3. Schedule a mechanic appointment.'''
    
    # generate task list
    task_list = generate_task_list(input_text, model)
    print('Generated task list:', task_list)

    # add task to database
    task_id, is_new = add_task(cursor, conn, 'Buy hat', 2)
    if is_new:
        print (f'Task added with task id {task_id}')
    else:
        print(f'Task not added as it already exists with id {task_id}')

        # get and display all tasks
        tasks = get_tasks(cursor)
        print('All tasks: ', tasks)

if __name__ == '__main__':
    main()


        


