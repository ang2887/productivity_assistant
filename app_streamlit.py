# app_streamlit.py 2
import os
from dotenv import load_dotenv
from utils.database_connection import get_db_connection
from utils.model_loader import load_llama_model
from utils.tasks import add_task, get_tasks, generate_task_list
import streamlit as st
from datetime import date

# Load environment variables
load_dotenv()

# Initialize database and model
conn, cursor = get_db_connection()
model = load_llama_model("/Users/alenadocherty/Downloads/PROJECTS/productivity_assistant/llama.cpp/models/llama-2-7b-chat.Q4_K_M.gguf")

# Streamlit App Title
st.title("Task Management App")

# Form to Add a New Task
st.header("Add a New Task")
description = st.text_input("Task Description")
priority = st.number_input("Priority", min_value=1, max_value=10, value=1)
due_date = st.date_input("Due Date (optional)")
completed = st.checkbox("Completed")

# Convert due_date to None if not provided
due_date = due_date if due_date != date.today() else None

if st.button("Add Task"):
    # Add Task and Handle Success/Failure
    task_id, is_new = add_task(cursor, conn, description, priority, due_date, completed)
    if task_id is None:
        st.error("Error adding task. Please try again.")
    elif is_new:
        st.success(f"Task added with ID: {task_id}")
    else:
        st.info(f"Task already exists with ID: {task_id}")

# Display the List of All Tasks
st.header("All Tasks")
try:
    tasks = get_tasks(cursor)
    if tasks:
        for task in tasks:
            st.write(f"ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}, Due Date: {task[3]}, Completed: {task[4]}")
    else:
        st.write("No tasks available.")
except Exception as e:
    st.error(f"Error fetching tasks: {e}")

# Close the Connection when the Session Ends
@st.cache_resource
def close_connection():
    conn.close()