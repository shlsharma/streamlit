import streamlit as st

st.title('Streamlit Demo Sahil Sharma')

st.header('Heading of streamlit')

st.subheader('sub-heading of streamlit')

st.text('This is an example text')

st.success("Sucess")

st.warning("Warning")

st.info("Information")

st.error("Error")

if st.checkbox('Select/Unselect'):
    st.text('User selected the checkbox')
else:
    st.text('User has not selected the checkbox')

state = st.radio("what is your favourite color", ('Red', 'Green', 'Yellow'))

if state == 'Green':
    st.success('Thats my favourite color as well')

occupation = st.selectbox('what do you do?', ('Student', 'Vlogger', 'Engineer'))

st.text(f'Selected option is {occupation}')

if st.button("Example Button"):
    st.error("You clicked it")
