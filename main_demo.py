import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Demo Uber Wyseday")

@st.experimental_singleton
def get_data(sample_size): 

    # get raw data from csv
    data = pd.read_csv("./listings.csv")

    # remove index as we do not need them in the workshop
    data.reset_index(inplace=True)

    # remove empty columns not to overload displaying
    data = data.drop(columns = ["neighbourhood_group", "license", "id", "host_id", "index"])

    # sample
    return data.sample(sample_size)


data = get_data(2000)

st.title("Welcome to Airbnb Data exploration !")

col1, col2, col3, col4 = st.columns(4)

with col1: 
    st.header("Columns selection")
    selected_cols = st.multiselect("Select your cols", data.columns)
    if st.checkbox("All columns"): 
        selected_cols = data.columns

with col2: 
    st.header("Select your hood")
    selected_hoods = st.multiselect("Select your hood", data["neighbourhood"].unique())
    if st.checkbox("All Hoods"): 
        selected_hoods = data["neighbourhood"].unique()

with col3: 
    st.header("Select price")
    max_price = st.slider("Select max price", min_value=1, max_value=1000, value=100)

with col4: 
    st.header("Select Room type")
    room_types = data["room_type"].unique()
    room_types_dict = {room_type: st.checkbox(room_type) for room_type in data["room_type"].unique()}
    selected_room_types = [room_type for room_type, selected in room_types_dict.items() if selected]

results = data[(data.price < max_price) & (data.neighbourhood.isin(selected_hoods)) & (data.room_type.isin(selected_room_types))]
st.session_state.results = results

col_1, col_2 = st.columns([1, 2])

with col_1: 

    if st.sidebar.checkbox("Display Dataframe"): 
        st.dataframe(results[selected_cols])
        st.write(f"{len(results)} results")

with col_2:
    if st.sidebar.checkbox("Display Map"): 
        st.map(results)


if st.checkbox("Display code"): 
    with open("./main_demo.py", "r") as file: 
        st.code(file.read(), language='python')