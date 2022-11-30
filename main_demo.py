import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Airbnb Bookings Exploration", page_icon="🏠", menu_items={"Get Help" : "https://github.com/elielevy3/STREAMLIT_DEPLOYMENT_SHOWCASE"})
st.markdown("# Welcome to London AirBnb Bookings Exploration 🏠")

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
    st.header("Column selection")
    selected_cols = st.multiselect("Choose the column you want to display", data.columns)
    if st.checkbox("All columns"): 
        selected_cols = data.columns

with col2: 
    st.header("Hoods selection")
    selected_hoods = st.multiselect("Choose the hoods you want", data["neighbourhood"].unique())
    if st.checkbox("All hoods"): 
        selected_hoods = data["neighbourhood"].unique()
    selected_hoods

with col3:
    st.header("Max price")
    min_price, max_price = st.slider("Pick your min and max price", value=(0, 1000))


with col4: 
    st.header("Room type")
    # we build a dict with room types as key and boolean as value representing weither or not this room type has been selected
    room_types_dict = {room_type: st.checkbox(room_type) for room_type in data["room_type"].unique()}
    selected_room_types = [room_type for room_type, selected in room_types_dict.items() if selected]


# display dataframe and plot
results = data[(data.price <= max_price) & (data.price >= min_price) & (data.neighbourhood.isin(selected_hoods)) & (data.room_type.isin(selected_room_types))]
st.session_state.results = results


col1, col2 = st.columns([1, 2])

with col1:  
    if st.sidebar.checkbox("Display dataframe"):   
        st.dataframe(results[selected_cols])
        st.write(len(results), "rooms")

with col2: 
    if st.sidebar.checkbox("Display map"):
        st.map(results)

if st.checkbox("Display code of the page"):
    with open("./Main_Page.py", 'r') as file:
        st.code(file.read(), language='python')
