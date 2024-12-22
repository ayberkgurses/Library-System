from faker import Faker
import random
import csv
import pandas as pd
from sqlalchemy import create_engine

# -------------------------------------------> THIS LINE IS COMMENTED SINCE CSVs ARE ALREADY CREATED...
# # Create an instance of the Faker class
# fake = Faker()

# # Function to generate random working hours
# def generate_working_hours():
#     hours = random.choice(["9:00 AM - 9:00 PM", "8:30 AM - 11:00 PM", "6:00 AM - 10:45 PM", "24 Hours"])
#     return hours

# def generate_library_name():
#     title = random.choice(["General", "Saint", "Professor","Governor"])
#     names = fake.name()
#     return title + " " + names + " Library"

# # Create a list to store library data
# libraries = []

# # Generate 10 random libraries
# for _ in range(10):
#     library_name = generate_library_name() # Using fake company name as the library name
#     library_city = fake.city()     # Random city name
#     working_hours = generate_working_hours()

#     # Add the library data to the list
#     libraries.append([library_name, library_city, working_hours])

# # Save the generated data to a CSV file (you can import it later into your database)
# with open('libraries.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['library_name', 'library_city', 'working_hours'])
#     writer.writerows(libraries)

# print("CSV file 'libraries.csv' generated with 10 random libraries.")

db_user = 'root'
db_password = 'yourpassword' #-> write your OWN password when you run it.
db_host = 'localhost'
db_name = 'temp'

connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
engine = create_engine(connection_string)

libraries_df = pd.read_csv('creatingDB\libraries.csv')
libraries_df.to_sql('library', con=engine, if_exists='append', index=False)
print("Data from 'libraries.csv' has been successfully inserted into the 'library' table.")