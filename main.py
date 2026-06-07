# pip install python-dotenv
# pip install langchain-openai
# pip install streamlit

from langchain_openai import ChatOpenAI
import streamlit as st

# ⚠️ 중요: 아래 따옴표 안에 발급받으신 그 엄청나게 긴 sk-proj-... 키를 통째로 붙여넣으세요!
chat_model = ChatOpenAI(api_key="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")

# [교수님 원안 주석 유지]
# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써줘.")
# print(result.content)

# [Streamlit 웹 화면 UI 구성]
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)