
# tasks.py 14

from utils.database_connection import get_db_connection


# Add task to the database
def add_task(cursor, conn, description, priority, due_date=None, completed=False):
    if not description.strip():
        raise ValueError("Task description cannot be empty.")

    try:
        query = """
        SELECT id
        FROM tasks
        WHERE lower(description) = lower(%s) 
        AND priority = %s 
        AND due_date IS NOT DISTINCT FROM %s
        AND completed = %s;
        """
        cursor.execute(query, (description, priority, due_date, completed))
        existing_task = cursor.fetchone()

        if existing_task:
            print(f"Task already exists: {description} (ID: {existing_task[0]})")
            return existing_task[0], False  

        cursor.execute(
            'INSERT INTO tasks(description, priority, due_date, completed) '
            'VALUES (%s, %s, %s, %s) RETURNING id;',
            (description, priority, due_date, completed)
        )
        conn.commit()
        new_task_id = cursor.fetchone()[0]
        print(f"Task added successfully: {description} (ID: {new_task_id})")
        return new_task_id, True

    except Exception as e:
        conn.rollback()
        print(f"Error adding task: {e}")
        return None, False

# Retrieve all tasks
def get_tasks(cursor):
    print("DEBUG: Fetching all tasks...")
    query = """
    SELECT id, description, priority, due_date, completed 
    FROM tasks 
    ORDER BY due_date IS NULL, due_date, priority;
    """
    cursor.execute(query)
    all_tasks = cursor.fetchall()  # Renamed for clarity
    print(f"DEBUG: All tasks fetched: {all_tasks}")
    return all_tasks

# Retrieve incomplete tasks
def get_incomplete_tasks(cursor):
    query = """
    SELECT id, description, priority, due_date 
    FROM tasks 
    WHERE completed = FALSE 
    ORDER BY due_date, priority;
    """
    cursor.execute(query)
    incomplete_tasks = cursor.fetchall()  # Renamed for clarity
    return incomplete_tasks


# Generate witty reminders

def generate_witty_reminders(tasks, model):
    
    try:               
        
        # Filter tasks with valid descriptions and due dates
        tasks_with_descriptions = [task for task in tasks if task[1].strip() and task[3] is not None]
        print(f"DEBUG: Tasks with valid descriptions and due dates: {tasks_with_descriptions}")

        if not tasks_with_descriptions:
            return "🎉 All tasks are completed or have no due date! Relax and enjoy!"

        # Create task descriptions
        task_descriptions = "\n".join(task[1] for task in tasks_with_descriptions)

        # Simplified prompt
        input_text = f"""
        Tasks:
        {task_descriptions}

        For each task, write one funny and encouraging comment. Keep responses short and relevant.
        """
        print(f"DEBUG: Input to model:\n{input_text}")

        # Generation arguments
        generation_args = {
            "max_tokens": 150,
            "temperature": 0.9,
            "top_p": 0.95,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0
        }

        # Send input to model
        response = model(input_text, **generation_args)

        # Log model response
        response_text = response['choices'][0]['text'].strip()
        print(f"DEBUG: Model raw response:\n{response_text}")
        response_lines = response_text.split("\n")
        formatted_response = "\n".join(response_lines)                                   
        
        return formatted_response or "Error: The model failed to generate reminders. Please try again later."
        

    except Exception as e:
        print(f"ERROR: {e}")
        return f"Error generating reminders: {e}"
    
# main logic
if __name__ == "__main__":
    from utils.database_connection import get_db_connection
    from model_loader import load_llama_model

    conn, cursor = get_db_connection()
    model = load_llama_model("path_to_model")
    incomplete_tasks = get_incomplete_tasks(cursor)
    reminders = generate_witty_reminders(incomplete_tasks, model)
    print(f"Generated reminders:\n{reminders}")
    conn.close()