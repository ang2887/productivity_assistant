/* // instructions for pgAdmin: copy and paste the code below 
into the pgAdmin query tool to create the required table */

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    priority INTEGER NOT NULL,
    due_date DATE,
    completed BOOLEAN DEFAULT FALSE
);