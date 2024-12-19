from faker import Faker
import random
import csv
import pandas as pd
from sqlalchemy import create_engine

# -------------------------------------------> THIS LINE IS COMMENTED SINCE CSVs ARE ALREADY CREATED...
# # Create an instance of the Faker class
# fake = Faker()

# # Function to generate a random phone number
# def generate_phone_number():
#     return random.randint(5035001320, 5538884599)

# def generate_email(first_name, last_name):
#     # Take first three letters of the last name and append to the first name
#     last_name_part = last_name[:3].lower() if len(last_name) > 2 else last_name.lower()
#     return first_name.lower() + last_name_part + "@library.com"
# # Create a list to store member data
# members = []

# # Generate 1000 random members
# for _ in range(1000):
#     member_id = None  # AUTO_INCREMENT will handle this in DB
#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     mail = generate_email(first_name,last_name)
#     phone_num = generate_phone_number()
#     membership_date = fake.date_this_decade()  # random date from the last 10 years

#     # Add the member data to the list
#     members.append([member_id, first_name, last_name, mail, phone_num, membership_date])

# # Save the generated data to a CSV file
# with open('members.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['member_id', 'first_name', 'last_name', 'mail', 'phone_num', 'membership_date'])
#     writer.writerows(members)

# print("CSV file 'members.csv' generated with 1000 random members.")

db_user = 'root'
db_password = 'yourpassword' #-> write your OWN password when you run it.
db_host = 'localhost'
db_name = 'librarydb'

connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
engine = create_engine(connection_string)

members_df = pd.read_csv('members.csv')
members_df.to_sql('members', con=engine, if_exists='append', index=False)
print("Data from 'members.csv' has been successfully inserted into the 'members' table.")