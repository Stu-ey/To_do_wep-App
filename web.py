import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_a = st.session_state["new_todo"] + "\n"
    todos.append(todo_a)
    functions.write_todos(todos)


st.title("My 'To-do' App")
st.subheader("This is very basic!")
st.write("Hopefully you be more <b>productive!!</b>",
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",
              placeholder="Enter a to-do...",
              on_change=add_todo,
              key="new_todo")
