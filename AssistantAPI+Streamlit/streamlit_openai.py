from openai import OpenAI
import streamlit as st
import time

assistant_id = "asst_hgAdGncKbpUrxLCnSjlv6Mef"
# thread_id = "thread_g4iieAcxug12JyiFFdpM5rDY"

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password",value=" ")
    
    client = OpenAI(api_key=openai_api_key)
    
    thread_id = st.text_input("Thread ID")
    thread_btn = st.button("Create a new thread")
    
    if thread_btn: 
        thread = client.beta.threads.create()
        thread_id = thread.id # thread_NhwJvYxk1zDrs5CzyyLO8q4s
        
        st.subheader(f"{thread_id}",divider="rainbow")
        st.info("스레드가 생성되었습니다.")
        
        
st.title("💬 Travel Panda Seoul Expert")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "서울 여행 같이 가볼까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
        
    if not thread_id:
        st.info("Please add your thread ID to continue.")
        st.stop()


    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
    )
    # print(response)
    
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    print(run)
    run_id = run.id
    
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status == "completed":
            break
        else:
            time.sleep(2)
        print(run)
        
    thread_messages = client.beta.threads.messages.list(thread_id)
    #print(thread_messages.data)
    
    msg = thread_messages.data[0].content[0].text.value
    # print(msg)
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    



