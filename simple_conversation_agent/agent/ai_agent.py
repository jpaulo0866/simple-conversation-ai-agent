from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from simple_conversation_agent.configuration.conf_service import ConfigTypes, get_all_config, get_config, set_config
from simple_conversation_agent.history.session_history import generate_session_id, get_history, get_history_file, rewrite_history, set_history

def get_chat_history(session_id: str):
    print("get_chat_history", session_id)
    return FileChatMessageHistory(str(get_history_file(session_id)))

def load_chain():
    config = get_all_config()
    llm = ChatOpenAI(model=config.model, max_tokens=config.max_tokens, temperature=config.temperature)

    prompt = ChatPromptTemplate.from_messages([
        ("system", config.system_role),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | llm

    return RunnableWithMessageHistory(
        chain,
        get_chat_history,
        input_messages_key="input",
        history_messages_key="history"
    )

def invoke(llm: RunnableWithMessageHistory, input_message: str):
    session_id = get_config(ConfigTypes.SESSION_ID)

    if session_id == None or session_id == "":
        session_id = generate_session_id()
        set_config(ConfigTypes.SESSION_ID, session_id)

    response = llm.invoke(
        {"input": input_message},
        config={"configurable": {"session_id": session_id}}
    )

    return response.content

