# app_streamlit.py 10

import os
from dotenv import load_dotenv
from utils.database_connection import get_db_connection
from utils.model_loader import load_llama_model
from utils.tasks import add_task, get_tasks
import streamlit as st
from datetime import date

# Load environment variables
load_dotenv()

# Determine paths based on environment
if os.getenv('IS_DOCKER', '0') == '1':
    model_path = os.getenv('MODEL_PATH_DOCKER')
    database_url = os.getenv('DATABASE_URL_DOCKER')
else:
    model_path = os.getenv('MODEL_PATH_LOCAL')
    database_url = os.getenv('DATABASE_URL_LOCAL')

if not model_path or not os.path.exists(model_path):
    raise FileNotFoundError(f"Model path does not exist: {model_path}")

# Cached model loader
@st.cache_resource
def cached_model():
    if not model_path or not os.path.exists(model_path):
        raise FileNotFoundError(f"Model path does not exist: {model_path}")
    return load_llama_model(model_path)

# Load the cached model
model = cached_model()

# Streamlit App UI
st.title("Task Management App")

# Add Task Section
st.header("Add a New Task")
description = st.text_input("Task Description")
priority = st.number_input("Priority", min_value=1, max_value=5, value=1)
due_date = st.date_input("Due Date (optional)")
completed = st.checkbox("Completed")

if st.button("Add Task"):
    try:
        conn, cursor = get_db_connection()
        task_id, is_new = add_task(cursor, conn, description, priority, due_date, completed)
        conn.commit()
        conn.close()  # Close the connection
        if task_id is None:
            st.error("Error adding task. Please try again.")
        elif is_new:
            st.success(f"Task added with ID: {task_id}")
        else:
            st.info(f"Task already exists with ID: {task_id}")
    except Exception as e:
        st.error(f"Error adding task: {e}")

# Show All Tasks Section
st.header("All Tasks")
try:
    conn, cursor = get_db_connection()
    tasks = get_tasks(cursor)
    conn.close()  
    if tasks:
        for task in tasks:
            st.write(
                f"ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}, Due Date: {task[3]}, Completed: {task[4]}"
            )
    else:
        st.write("No tasks available.")
except Exception as e:
    st.error(f"Error fetching tasks: {e}")
