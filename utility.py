import streamlit as st
import pandas as pd

# if the input parameters 
# value of any external variable used in the function
# The body of the function
# The body of any function used inside in the function
# are all the same
# function is not executed
# get data and store them into cache not to retrieve them everytime an streamlit element in modified
@st.cache()
def get_data(sample_size): 

    # get raw data from csv
    data = pd.read_csv("./listings.csv")

    # remove empty columns not to overload displaying
    data = data.drop(columns = ["neighbourhood_group", "license", "id", "host_id"])

    # remove index as we do not need them in the workshop
    data.reset_index(inplace=True)

    return data.sample(sample_size)

# # storing widgets as variables
# x = st.sidebar.slider('Height of line chart')
# st.write(x, 'squared is', x * x)


# # selectbox for options
# option = st.sidebar.selectbox(
#     'Who is your favorite writer ?',
#      ["Victor Hugo", "Guy de Maupassant", "Racine"])


# with tab1: 
#     with st.form(key='my_form'):
#         username = st.text_input('Username')
#         password = st.text_input('Password')
#         st.form_submit_button('Login')


def get_bar_chart_data(data, bins, field): 
    bar_chart_data = data[[field]]
    bar_chart_data = bar_chart_data.groupby(pd.cut(bar_chart_data[field], bins)).count()
    bar_chart_data.columns = ["count"]
    bar_chart_data[field] = list(bins)[:-1]
    return bar_chart_data


# sample data with slider
# sample_size = st.slider("Select sample size", min_value=1, max_value=500, value=(st.session_state.sample_size if "sample_size" in st.session_state else 250))
# st.session_state.sample_size = sample_size