import pandas as pd
from sqlalchemy import create_engine

DB_USERNAME = 'root'
DB_PASSWORD = 'yourpassword' #-> write your OWN password when you run it.
DB_HOST = 'localhost' 
DB_NAME = 'librarydb'

# Create a connection to the MySQL database
engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# CSV file
csv_file = 'niceBook.csv'  
try:
    # Try reading the CSV and handle potential errors with inconsistent columns
    df = pd.read_csv(csv_file, on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# unique author names 
unique_authors = df[['Author']].dropna().drop_duplicates()
books = df[['Book Name']]

# Check existing authors in the database
existing_authors = pd.read_sql('SELECT author_name FROM authors', con=engine)

# Remove authors already in the database
new_authors = unique_authors[
    ~unique_authors['Author'].isin(existing_authors['author_name'])
]

new_authors['Author'] = new_authors['Author'].apply(lambda x: x[:255])

#Insert
if not new_authors.empty:
    # Rename 'name' column to match the database column 'author_name'
    new_authors = new_authors.rename(columns={'Author': 'author_name'})
    
    # Insert new authors into the 'authors' table
    new_authors.to_sql(
        name='authors',      # Table name in the database
        con=engine,          # Database connection
        if_exists='append',  # Add new rows without overwriting existing data
        index=False          # Don't include the DataFrame index as a column
    )
    print(f"Inserted {len(new_authors)} new authors.")
else:
    print("No new authors to add.")
