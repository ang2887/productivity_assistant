# productivity_assistant

A simple productivity assistant using LLaMA and Streamlit for managing tasks.

## Python Version
- Python 3.11.4

## Environment Variables
- **MODEL_PATH**: Path to the model file. 
  - Example: `models/llama-2-7b-chat.Q4_K_M.gguf`
- **DATABASE_URL**: Connection string for the PostgreSQL database.
  - Example: `postgresql://assistant_user:password@localhost:5432/productivity_db`

## Model Setup
Since the model file (llama-2-7b-chat.Q4_K_M.gguf, 4.08 GB) is large, it’s recommended to download it separately:
- Download the model file from [Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-hf).
- Place the model file in a folder named `models` within the project directory.

## Database Setup
- Set up a postgresql database (e.g., `productivity_db`).
- Run the sql schema file `create_tasks_table.sql` in pgAdmin4 (or any sql editor).

## Starting the streamlit app
To start the streamlit app:
```
streamlit run app_streamlit.py
```
