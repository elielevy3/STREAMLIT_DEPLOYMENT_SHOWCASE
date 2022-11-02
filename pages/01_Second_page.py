import streamlit as st

st.markdown("Hello this is another page of your application to show the DataFrame in full page")
st.dataframe(st.session_state.results)