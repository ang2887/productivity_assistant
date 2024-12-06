# tasks.py 2

# add task to the database
def add_task(cursor, conn, description, priority, due_date=None, completed = False):
    # to get rid of lingering erorrs
    conn.rollback()
    # to check for a similar task
    query = """
    select id
    from tasks
    where description = %s 
    and priority = %s 
    and due_date is not distinct from %s -- overcoming null = null issue 
    and completed = %s;
    """
    cursor.execute(query, (description, priority, due_date,completed))
    existing_task = cursor.fetchone()

    if existing_task:
        return existing_task[0] , False  
    try:
        cursor.execute('INSERT INTO tasks(description, priority, due_date, completed) VALUES (%s, %s, %s, %s) RETURNING id;',
                    (description, priority, due_date, completed))
        conn.commit()
        new_task_id = cursor.fetchone()[0]
        return new_task_id, True
        
    except Exception as e:
        conn.rollback()
        print('Error adding task:', e)
        return None, False
# retrieve task from the database
def get_tasks(cursor):
    cursor.execute('select id, description, priority, due_date, completed from tasks order by due_date is Null, due_date, priority;')
    return cursor.fetchall()

def generate_task_list(input_text, model):
    response = model(input_text)
    return response['choices'][0]['text'] 
