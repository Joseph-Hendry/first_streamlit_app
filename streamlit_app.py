import streamlit

# Set title
streamlit.title('New Healthy Diner')

# Set header
streamlit.header('Breakfast Menu')

# Set text
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Smoothie Header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Include Panda
import pandas

# Read the list
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set the index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display a picker
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display a table
streamlit.dataframe(my_fruit_list)