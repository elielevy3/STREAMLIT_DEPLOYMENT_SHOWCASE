import streamlit as st
import pandas as pd
import numpy as np

# if the input parameters 
# value of any external variable used in the function
# The body of the function
# The body of any function used inside in the function
# are all the same
# function is not executed
@st.cache()
def get_chart_data(): 
    return pd.DataFrame(
     np.random.randn(10, 10),
     columns=["col"+str(i) for i in range(1, 11)])

@st.cache()
def get_map_data(): 
    return pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

@st.cache()
def get_line_data(): 
    return pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# get data and store them into cache not to retrieve them everytime an streamlit element in modified
@st.cache()
def get_data(sample_size): 

    # get raw data from csv
    data = pd.read_csv("./data/listings.csv")

    # remove empty columns not to overload displaying
    data = data.drop(columns = ["neighbourhood_group", "license", "id", "host_id"])

    # remove index as we do not need them in the workshop
    data.reset_index(inplace=True)

    return data.sample(sample_size)


# ###### SIDEBAR #######

# # using keys for widget instead of storing them as variable
# a = st.text_input("What's your name", key="name")
# st.write("Hello "+a+" !")

# # storing widgets as variables
# x = st.sidebar.slider('Height of line chart')
# st.write(x, 'squared is', x * x)


# # selectbox for options
# option = st.sidebar.selectbox(
#     'Who is your favorite writer ?',
#      ["Victor Hugo", "Guy de Maupassant", "Racine"])

# 'You selected: ', option


# # charts and map

# if st.sidebar.checkbox("Display map"):
#     map_data = get_map_data()
#     st.map(map_data)

# if st.sidebar.checkbox("Display line chart"):
#     st.line_chart(get_line_data(), height=x*10)

# if st.sidebar.checkbox("Display dataframe"):
#     dataframe = get_chart_data()
#     st.dataframe(dataframe.style.highlight_max(axis=0))


# st.write("------------")

# left_column, right_column = st.columns(2)

# with left_column: 
#     st.button("Press me!")

# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")



# test = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })


# a = st.write(test)
# b = st.dataframe(test)


# with st.echo():
#    st.write('Code will be executed and printed')

# tab1, tab2 = st.tabs(["Form", "Tab2"])
# tab2.write("this is tab 2")

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