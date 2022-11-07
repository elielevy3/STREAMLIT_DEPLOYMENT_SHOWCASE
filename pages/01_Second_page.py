import streamlit as st
import pandas as pd

st.markdown("Hello this is another page of your application to show the DataFrame in full page")
# check if results are already stored in session state or not

if "results" in st.session_state: 
    st.dataframe(st.session_state.results)
    st.write(len(st.session_state.results), "rooms")
else: 
    st.dataframe(pd.DataFrame())