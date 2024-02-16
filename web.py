import streamlit as st
st.title("My website")
st.subheader("Python codes")
st.markdown("here are some python codes you can use in your coding")
st.code(""" for i in range(1, 11):
               print(i)""")
name = st.text_input("Enter your name:")
fathers_name= st.text_input("Enter your fathers name:")
address = st.text_area("Enter your address")
Standard = st.selectbox("Enter your class:", (1,2,3,4,5,6,7,8,9,10,11,12))
age = st.number_input("Enter your age")
button = st.button("Done")
if button:
    st.markdown(f"""Name:{name}
                   Fathers Name:{fathers_name}
                   Address:{address}
                   Standard Name:{Standard}
                   age = {age}""")