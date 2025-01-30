import streamlit as st                          # Create interactive web application
from streamlit_chat import message              # Display the chat messages
from dotenv import load_dotenv                  # Load the open API key from the environment variable
import os                                       # Access the environment variable
from langchain.chat_models import ChatOpenAI 
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser  # Get the Out Put as a String
from langchain_core.runnables import RunnablePassthrough   
from langchain_openai import ChatOpenAI                    # Importing the OpenAI Chat Model
from langchain_core.prompts import ChatPromptTemplate  
from langchain.schema import SystemMessage, HumanMessage, AIMessage # Import the message schema    


def init_DB(User,Host,Port,Database):       # Initialize the Streamlit app
    

    # Define the connection URI
    mysql_uri = f"mysql+mysqlconnector://{User}:@{Host}:{Port}/{Database}"

    # Create an SQLAlchemy engine
    engine = create_engine(mysql_uri)

    # Pass the engine to SQLDatabase
    return SQLDatabase(engine)

 # Initialize message history
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant.Give the answer with simple english"), # Initial system message for the message Schema
        AIMessage(content="Hello I am a SQL assistant. What do you want to know about database") # Initial AI message for the message Schema
    ]

def SQL_chain(db):

    from langchain_core.prompts import ChatPromptTemplate

    template = """
    Based on the schema below wirte Sql queries to answer the following question:
    {schema}   

    Conversation Chat History:{chat_history}

    Write only the sql query and do not use \n when writing the query.
    as an example :
    Question :if want get the all the table from the database you can write the query as:
    Answer : show tables;
    Question: {question}

    Sql Query:
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(temperature=0.5)   

    def get_schema(_):    # For the RunnablePassthrough towork function should be consist with at least one parameter
        return db.get_table_info()
    
    return ( RunnablePassthrough.assign(schema=get_schema) 
    | prompt
    | llm
    | StrOutputParser()
    )

def final_response(user_query,chat_history,db):
    sql_chain = SQL_chain(db)

    template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
    {schema}

    Question: {question}
    SQL Query: {query}
    SQL Response: {response}"""

    prompt_response = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(temperature=0.5,
                     max_tokens=100,
                     model = 'gpt-3.5-turbo')
    
    def get_schema(_):
        return db.get_table_info()
    
    def run_query(query):
        return db.run(query)
    
    return (RunnablePassthrough.assign(query=sql_chain).assign(
        schema = get_schema,
        response = lambda vars: run_query(vars["query"])
    )
    | prompt_response
    | llm
    | StrOutputParser()
    )
    






    
load_dotenv() # Load the OpenAI API key from the environment variable

# Test that the API key exists
if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
    st.error("OPENAI_API_KEY is not set. Please set it in your environment variables.")
    st.stop()  # Safely stop the Streamlit app

# Setup Streamlit page
st.set_page_config(
    page_title="Chat Bot DB With OpenAI",
    page_icon="🤖"
)

st.header("Chat Bot Database Reader 🗄️")

with st.sidebar:

    st.subheader("Settings")
    st.write("This is a chat bot can answer the question from the database")

    st.session_state.Host = st.text_input("Host", key="host", value="localhost")
    st.session_state.Port = st.text_input("Port", key="port", value="3306")
    st.session_state.User = st.text_input("User Name", key="user", value="root")
    st.session_state.Password = st.text_input("Password", key="password", type="password")
    st.session_state.Database = st.text_input("Database", key="database", value="classicmodels")

    if st.button("Connect to the Database"):

        with st.spinner("Connecting to the Database..."):

            st.session_state.db = init_DB(st.session_state.User,st.session_state.Host,st.session_state.Port ,st.session_state.Database)
            st.success("Database connected successfully!")


for message in st.session_state.chat_history:
    
    if isinstance(message, AIMessage):
       with st.chat_message("AI"):
           st.markdown(message.content)

    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
        
user_query= st.chat_input("Enter your question here")  # User input

if user_query is not None: 

    # Add the user's message to the message history
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        full_chain = final_response(user_query,st.session_state.chat_history,st.session_state.db)
        response = full_chain.invoke({"question":user_query,"chat_history":st.session_state.chat_history})
        st.markdown(response) 

    st.session_state.chat_history.append(AIMessage(content=response)) # Add the AI's response to the message history     

    # with st.spinner("Thinking..."):
    #     sql_chain = SQL_chain(st.session_state.db)
    #     response = sql_chain.invoke({"question":user_query,"chat_history":st.session_state.chat_history})
    #     # st.write(f"SQL Query:    {response}")

    # st.session_state.chat_history.append(AIMessage(content=response)) # Add the AI's response to the message history      

        





                








