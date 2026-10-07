import streamlit as st
st.title("메인 제목")
st.info("파란색 알림 박스")
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

st. title("주호의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

col1, col2 = st.columns(2)
with col1: 
    st. success("왼쪽 영역")
with col2:
    st.write("오른쪽 영역")

# 새로고침 시 데이터 유지
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_from"):
    name = st. text_input("이름") 
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)

import streamlit as st
tasks = [   
    "1. API 스펙 문서 작성",
    "2. 프론트엔드 컴포넌트 개발",
    "3.배포 파이프라인(CI/CD) 구축"
]

st.subheader("금일 할 일 목록!")


for task in tasks:  
    # border=true를 주면 각 반복 요소가 단정한 상자로 감싸집니다.

     with st.container(border=True):
        
        st.write(task)

        import streamlit as at

# 페이지 목록 설정

st.title("주호의 첫 streamlit 앱")

# 텍스트 출력

st.write("streamlit을 이용해 만든 웹 애플리케이션입니다.")

# 사용자 입력 받기
name = st.text_input("이름을 입력하세요:")

# 버튼 클릭 이벤트

if st.button("인사하기"):
   
    if name:

        st.success(f"안녕하세요, {name}님!!")

    else:

        st.warning("이름을 입력해주세요.")
        









