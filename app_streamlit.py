# app_streamlit.py 27l 

import os
from dotenv import load_dotenv
from utils.database_connection import get_db_connection
from utils.model_loader import load_llama_model
from utils.tasks import add_task, get_tasks, get_incomplete_tasks, generate_witty_reminders
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Load environment variables
load_dotenv()

# Determine paths based on environment
if os.getenv('IS_DOCKER', '0') == '1':
    model_path = os.getenv('MODEL_PATH_DOCKER')
else:
    model_path = os.getenv('MODEL_PATH_LOCAL')

if not model_path or not os.path.exists(model_path):
    raise FileNotFoundError(f"Model path does not exist: {model_path}")

# Load the Llama model
model = load_llama_model(model_path)

# Streamlit App UI
st.title("Task Management App")

# Add Task Section
st.header("Add a New Task")
description = st.text_input("Task Description")
priority = st.number_input("Priority", min_value=1, max_value=3)
include_due_date = st.checkbox("Set Due Date")

if include_due_date:
    due_date = st.date_input("Due Date")
else:
    due_date = None

if st.button("Add Task"):
    conn, cursor = get_db_connection()
    try:
        task_id, is_new = add_task(cursor, conn, description.strip(), priority, due_date, False)
        conn.commit()

        if task_id is None:
            st.error("Error adding task. Please try again.")
        elif is_new:
            st.success(f"Task added with ID: {task_id}")
        else:
            st.info(f"Task already exists with ID: {task_id}")
    except Exception as e:
        st.error(f"Error adding task: {e}")
    finally:
        conn.close()

# Show All Tasks Section
st.header("All Tasks")
conn, cursor = get_db_connection()
try:
    tasks = get_tasks(cursor)

    if tasks:
        df = pd.DataFrame(tasks, columns=["ID", "Description", "Priority", "Due Date", "Completed"])
        df["Due Date"] = pd.to_datetime(df["Due Date"], errors="coerce").dt.strftime("%d-%b-%Y")
        AgGrid(df)
    else:
        st.write("No tasks available.")
except Exception as e:
    st.error(f"Error fetching tasks: {e}")
finally:
    conn.close()

# Reminder Section
st.header("Reminders for Pending Tasks")

conn, cursor = get_db_connection()
try:
    incomplete_tasks = get_incomplete_tasks(cursor)

    if incomplete_tasks:
        reminders = generate_witty_reminders(incomplete_tasks, model)
        for line in reminders.split("\n"):
            st.write(line)
    else:
        st.write("🎉 No pending tasks! Relax and enjoy!")
except Exception as e:
    st.error(f"Error fetching reminders: {e}")
finally:
    conn.close()
