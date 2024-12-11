# SQL Llama Chat

This project implements an interactive chat with the Llama model to generate SQL queries based on natural language questions.

## Prerequisites

1. Python 3.8 or higher
2. Ollama installed and running locally

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Via Python Script

You can run the script in two ways:

1. By providing the schema file directly:
```bash
python chat_interface.py --schema path/to/your/schema.sql
```

2. Or by running without arguments and providing the schema path during execution:
```bash
python chat_interface.py
```

## How to use the chat

1. If you haven't provided the schema file as an argument, the chat will ask for the file path
2. After successfully loading the schema, you can ask questions in natural language
3. The model will only respond with SQL SELECT queries or ask for clarification
4. To exit, type 'exit'

## Usage Example

```
# Running with schema file
$ python chat_interface.py --schema my_schema.sql
Model: Schema loaded successfully

You: show me all users
Model: SELECT * FROM users;

You: what are the users' emails
Model: SELECT email FROM users;

# Running without schema file
$ python chat_interface.py
Model: Please provide the path to the database schema file.
You: my_schema.sql
Model: Schema loaded successfully

You: show me all users
Model: SELECT * FROM users;
```

## Tips

1. Prepare your SQL schema file before starting the chat
2. The schema file can be a complete SQL dump or just the CREATE TABLE definitions
3. Make sure the file is in a readable text format
4. The model works better with well-structured and commented schemas
