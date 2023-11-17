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

# Create a picker
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

# Display table
streamlit.dataframe(fruits_to_show)

# Fruityvice header
streamlit.header("Fruityvice Fruit Advice!")

# Add a selector for the fruit
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# Request API
import requests

# Send GET request
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")

# Normalize json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Display the json in a table
streamlit.dataframe(fruityvice_normalized)

# Import snowflake connector
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)