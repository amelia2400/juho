import streamlit as st
st.title("메인 제목")
st.info("빨간색 알림 박스")
st.success("초록색 성공 메세지")

col1, col2 = st.columns(2)

# 데이터 입력
name = st.text_input("이름")
btn = st.button("클릭")

# 폼 입력 & 상태 관리
with st.form("my_form"):
    submit = st.form_submit_button("전송")

st.session_state.login = True
import streamlit as st

st, title("주호의 첫 웹앱")
st,info("파이썬만으로 제작하는 UI")

col1, col2 = st.coloumns(2)
with col1: 
    st. success("왼쪽 영역")
with col2:
    st.write("오른쪽 영역")

# 새로고침 시 데이터 유지
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_from"):
    name = st. text_input("이름") 
    if st.from_submit_button("등록") and name:
        st.session_state.user_list.append(name)
        







