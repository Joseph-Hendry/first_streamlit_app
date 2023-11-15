import streamlit

# Set title
streamlit.title('My Parents New Healthy Diner')

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

# Display a picker
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display a table
streamlit.dataframe(my_fruit_list)