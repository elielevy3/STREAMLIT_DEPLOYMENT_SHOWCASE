from re import I
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_icon="🏠", page_title="Airbnb data exploration")

st.title("Welcome to Airbnb data exploration 🏠")

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

data = get_data(3000)

col1, col2, col3, col4 = st.columns(4)

with col1: 
    st.header("Column Selection")
    selected_cols = st.multiselect("Pick columns", data.columns)
    if st.checkbox("All columns"): 
        selected_cols = data.columns

with col2: 
    st.header("Neighbourhood")
    selected_hoods = st.multiselect("Pick your neighbourhood", data["neighbourhood"].unique())
    if st.checkbox("All Neighbourhood"): 
        selected_hoods = data["neighbourhood"].unique()

with col3: 
    st.header("Max Price")
    min_price, max_price = st.slider("Pick your min and max price", value=(0, 1000))

with col4: 
    st.header("Select room type")
    room_types_dict = {room_type: st.checkbox(room_type) for room_type in data["room_type"].unique()}
    selected_room_types = [room_type for room_type, selected in room_types_dict.items() if selected]

filtered_data = data[(data["neighbourhood"].isin(selected_hoods)) & (data["price"] <= max_price) & (data["price"] >= min_price) & (data["room_type"].isin(selected_room_types))]
st.session_state.results = filtered_data

col_df, col_map = st.columns([1, 2])

with col_df: 
    if st.sidebar.checkbox("Display dataframe"):
        st.dataframe(filtered_data[selected_cols])
        st.write(len(filtered_data), "rooms")

with col_map: 
    if st.sidebar.checkbox("Display map"):
        st.map(filtered_data[["latitude", "longitude"]])


if st.checkbox("Display code"): 
    with open("./main_demo_2.py", "r") as file: 
        st.code(file.read(), language="python")

# st.map() on doit donner lon et lat 
# limite avec les colonnes selectionnés que dans st.dataframe()