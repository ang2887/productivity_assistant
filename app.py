# app.py 9

import os
import threading
import time
import signal
from dotenv import load_dotenv
from utils.database_connection import get_db_connection
from utils.model_loader import load_llama_model
from utils.tasks import add_task, get_tasks, get_incomplete_tasks, generate_witty_reminders

# Global stop event for clean thread shutdown
stop_event = threading.Event()

# Signal handler for graceful shutdown
def stop_running(signum, frame):
    stop_event.set()

# Load environment variables
load_dotenv()

# Determine paths based on environment
if os.getenv('IS_DOCKER', '0') == '1':
    model_path = os.getenv('MODEL_PATH_DOCKER')
else:
    model_path = os.getenv('MODEL_PATH_LOCAL')

if not model_path or not os.path.exists(model_path):
    raise FileNotFoundError(f'Model path does not exist: {model_path}')

# Load the Llama model
model = load_llama_model(model_path)

# Reminder display function
def display_reminders(cursor, model):
    try:
        incomplete_tasks = get_incomplete_tasks(cursor)
        if not incomplete_tasks:
            print("🎉 No pending tasks! Relax and enjoy!")
            return

        reminders = generate_witty_reminders(incomplete_tasks, model)
        print(f"🔥 Reminder: \n{reminders}")
    except Exception as e:
        print(f"Error displaying reminders: {e}")

# Background reminder thread function
def background_reminder_task(interval=3600):
    conn, cursor = get_db_connection()
    print("Background reminder thread started.")
    try:
        while not stop_event.is_set():
            print("Running reminder task...")
            display_reminders(cursor, model)
            time.sleep(interval)
    finally:
        conn.close()
        print("Background reminder thread exited.")

# Main application logic
if __name__ == '__main__':
    try:
        # Register signal handlers
        signal.signal(signal.SIGINT, stop_running)
        signal.signal(signal.SIGTERM, stop_running)

        # Start the background thread for reminders
        reminder_thread = threading.Thread(
            target=background_reminder_task,
            args=(3600,),  # Check every hour
            daemon=True
        )
        reminder_thread.start()

        # Main loop to keep the app running
        while not stop_event.is_set():
            time.sleep(1)
    finally:
        print("Shutting down gracefully...")
        