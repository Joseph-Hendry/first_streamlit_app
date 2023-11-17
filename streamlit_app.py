import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
    # Send GET request
    fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{this_fruit_choice}")

    # Normalize json
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

    return fruityvice_normalized

try:
    # Add a selector for the fruit
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        # Display the json in a table
        streamlit.dataframe(get_fruityvice_data(fruit_choice))

except URLError as e:
    streamlit.error()

# Add header
streamlit.header("The fruit load list contains:")

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_data_rows = my_cur.fetchall()

if streamlit.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Add fruit picker to add
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")