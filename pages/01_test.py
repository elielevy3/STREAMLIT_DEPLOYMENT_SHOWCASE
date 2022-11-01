import streamlit as st

st.markdown("Hello this is another page of your application")

st.dataframe(st.session_state.results)