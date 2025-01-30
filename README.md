# Chatbot with MySQL Database Integration

## Overview

This project is a chatbot powered by OpenAI's GPT-3.5-turbo that provides answers to user queries based on a MySQL database. It integrates a Large Language Model (LLM) with structured data retrieval to deliver accurate and context-aware responses.

## Features

- **Natural Language Understanding**: Leverages OpenAI's GPT-3.5-turbo for intelligent responses.
- **MySQL Integration**: Fetches relevant data from a MySQL database to enhance accuracy.
- **Dynamic Query Handling**: Interprets user queries and retrieves appropriate information.
- **Customizable Responses**: Adaptable to different domains and use cases.
- **Efficient Performance**: Optimized query execution and LLM interaction.

## Technologies Used

- **Programming Language**: Python
- **Database**: MySQL
- **LLM Provider**: OpenAI GPT-3.5-turbo
- **Libraries**:
  - `openai` for LLM interaction
  - `mysql-connector-python` for database connectivity
  - `streamlit` for developing the web site

## Installation & Setup

### Prerequisites

- Python (>= 3.8)
- MySQL Server
- OpenAI API Key
- Required Python Libraries

### Steps

create Virtual env

  ```
  python -m venv chatDB
  ```
activate Virtual env

  ```
  cd chatDB\Scripts\activate
  ```
creating .gitignore file , .env file and chatbot.py

  ```
  echo "# Files to ignore" > .gitignore && echo "OPENAI_API_KEY=your_api_key_here" > .env && echo "# Chatbot script" > chatbot.py
  ```
Insatalling Required dependencies

  ```
  pip install -r requirements.txt
  ```

Save OpenAI API Key inside .env file
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

Run Chatbot.py file

  ```
  streamlit run charDB.py
  ```

## Usage

- The chatbot processes user input, extracts relevant keywords, and queries the MySQL database.
- If the answer is available in the database, it fetches and returns the result.
- If additional context is needed, the chatbot leverages GPT-3.5-turbo to generate a response based on structured data.

## Configuration

Modify `config.py` to update:

- Database credentials
- OpenAI API key
- Additional settings such as query optimization

## Potential Enhancements

- Support for multiple databases (e.g., PostgreSQL, MongoDB)
- Caching mechanisms for faster response times
- More advanced natural language processing
- Integration with messaging platforms (e.g., WhatsApp, Telegram, Slack)

## Contact

For any questions or support, reach out via:

- Email: [Personal Email](isuruadg850@gmail.com)
- LinkedIn: [www.linkedin.com/in/isuru-madhushan-096878273](www.linkedin.com/in/isuru-madhushan-096878273)

---

**Happy Coding! 🚀**



