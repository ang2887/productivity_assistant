# productivity_assistant

A simple productivity assistant built using LLaMA and Streamlit for managing tasks, with optional Docker support for easy setup and deployment.

## Python Version
- Python 3.11.4

## Environment Variables
- **MODEL_PATH**: Path to the model file. 
  - Example: `models/llama-2-7b-chat.Q4_K_M.gguf`
- **DATABASE_URL**: Connection string for the PostgreSQL database.
  - Example: `postgresql://postgres:password@localhost:5432/productivity_db`

## Model Setup
Since the model file (llama-2-7b-chat.Q4_K_M.gguf, 4.08 GB) is large, it’s recommended to download it separately:
- Download the model file from [Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-hf).
- Place the model file in a folder named `models` within the project directory.

## Database Setup
- Set up a postgresql database (e.g., `productivity_db`).
- Run the sql schema file `create_tasks_table.sql` in pgAdmin4 (or any sql editor).

## Starting the Streamlit app locally (without Docker)
Run the app with:
```
streamlit run app_streamlit.py
```
Note:The app relies on the streamlit-aggrid library for displaying and interacting with task data in a user-friendly grid.

## Using Docker for Setup and Deployment
This project supports Docker for simplified setup and deployment. The `Dockerfile` and `docker-compose.yml` are provided for containerized execution.

### Steps to Use Docker:
1. **Build and Start the Application:**
   ```
   docker-compose up --build
   ```
This command will build the Docker image and start the application along with a PostgreSQL database container.

2.	**Stop the Application:**
```
docker-compose down
```
3.	**Access the Streamlit Application:**
Open your browser and navigate to: http://localhost:8501

4.	**Database Configuration with Docker:**
The PostgreSQL database runs in a Docker container.
Connection string example: postgresql://postgres:password@db:5432/productivity_db






