import streamlit as st
from utility import get_data

st.set_page_config(layout="wide")
st.markdown("# Welcome to London AirBnb booking dataset exploration !")

# get data
data = get_data(3000)

col_1, col_2, col_3, col4 = st.columns(4)

# let the user pick the column he wants to display
with col_1: 
    st.header("Column selection")
    columns = st.multiselect("Choose the column you want to display", data.columns)

with col_2: 
    st.header("Neighbourhood")
    hood_options = st.multiselect('Which neighbourhood do you want to pick ? ', data["neighbourhood"].unique())
    # handling the case in which the user does not care about the neighbourhood
    if st.checkbox("All Neighbourhoods"): 
        hood_options = data["neighbourhood"].unique()

with col_3:
    st.header("Max price")
    max_price = st.slider("Pick a max price", min_value=0, max_value=500) 

with col4: 
    st.header("Room type")
    # we build a dict with room types as key and boolean as value representing weither or not this room type has been selected
    room_types_dict = {room_type: st.checkbox(room_type) for room_type in data["room_type"].unique()}
    selected_room_types = [room_type for room_type, selected in room_types_dict.items() if selected]

# display dataframe and plot
results = data[(data.price < max_price) & (data.neighbourhood.isin(hood_options)) & (data.room_type.isin(selected_room_types))]
st.session_state.results = results

col1, col2 = st.columns(2)

with col1:  
    if st.sidebar.checkbox("Display dataframe"):   
        st.dataframe(results[columns])
        st.write(str(len(results))+" results")

with col2:
    # display in the map
    if st.sidebar.checkbox("Display map"):
        st.map(results)

# check the code
if st.checkbox("Display code of the page"):
    with open("./Main_Page.py", 'r') as file:
        st.code(file.read(), language='python')
