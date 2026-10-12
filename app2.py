import streamlit as st

st.title("Your tasks")
st.write("작은 계획부터 하나씩 완료해 봅시다")
st.info("오늘 해야할 일을 입력하고 등록 버튼을 눌러주세요")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.form("task_form"):
    new_task = st.text_input("새로운 할 일")
    placeholder="예: 대학 강의 복습하기"

    submitted = st.form_submit_button("+ 할 일 등록")

    if submitted:
        if new_task.strip():
            st.session_state.tasks.append({"text":new_task.strip(),"done":False})
            st.success("할 일이 등록되었습니다!")
        else:
            st.warning("할 일을 먼저 입력해 주세요.")

total = len(st.session_state.tasks)
completed = sum(1 for tasks in st.session_state.tasks if task["done"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metriC("전체 할 일", total)
with col2:
    st.metric("완료한 일", completed)

st.subheader("할 일 목록")

if not st.session_state.tasks:
    st.caption("아직 등록한 할 일이 없습니다.")

for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([5, 1, 1])

    with col1:
        if task["done"]:
            st.write(f"~~{task['text']}~~")
        else:
            st.write(task["text"])

    with col2:
        if task["done"]:
            st.write("완료")
        else:
            st.write("진행 중")

    with col3:
        if st.button("취소" if task["done"] else "완료", key=f"task_{i}"):
            task["done"] = not task["done"]
            st.rerun()
