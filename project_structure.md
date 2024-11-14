# Project structure for `productivity_assistant`

This document provides an overview of the project directory structure and the purpose of each major file.

```
productivity_assistant/
├── app.py                       # Core backend logic of the application
├── app_streamlit.py             # Streamlit-based user interface
├── create_tasks_table.sql       # SQL file for setting up the database schema
├── LICENSE                      # License for the project
├── project_structure.md         # Documentation of the project's directory structure
├── README.md                    # Project documentation
├── requirements.txt             # Lists dependencies for the project
├── setup.py                     # Script for setting up the project environment
├── utils/                       
│   ├── database_connection.py   # Database connection logic
│   ├── model_loader.py          # Code for loading the model
│   └── tasks.py                 # Task-related functions (e.g., add, get tasks)
├── env/                         # Virtual environment (usually ignored by .gitignore)
├── llama.cpp/                   # Model-related files
└── scratchpad.ipynb             # Jupyter notebook for testing and scratch work
```

