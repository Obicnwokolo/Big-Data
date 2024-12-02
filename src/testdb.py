# Importing SQLAlchemy library
import sqlalchemy as sa
import pandas as pd

# importing connection engine pack
from sqlalchemy import create_engine, inspect, text
from urllib.parse import quote_plus
from sqlalchemy import Table, MetaData

# Creating connection strings for my database
username= "consultants"
password = "WelcomeItc@2022"
host= "18.132.73.146"
port = "5432"
database= "testdb"
ENCODED_PASSWORD = quote_plus(password)


#creating connection with database
connection_string = f"postgresql+psycopg2://{username}:{ENCODED_PASSWORD}@{host}:{port}/{database}"

#Establishing connection with engine
engine = create_engine(connection_string)
#cursor = connection_string.cursor()

try:
    with engine.connect() as connection:
        print("connection successful")
except Exception as e:
    print("connection failed:", e)

# Read Table from database
df = pd.read_sql_table("aapl",engine)
print(df.head())

# Writing new table to te database
customers = text("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);
""")
try:
    with engine.connect() as connection:
        connection.execute(customers)
        print("Table created successfully")
except Exception as e:
    print("Failed to creat table")
    print(f"Error:{e}")



# INSERT INTO users
sql_query = text("""
    INSERT INTO users(id, name, email)
    VALUES
        (01, 'Muhammed', 'kara34@hotmail.com'),
        (02, 'Ali', 'kar3445534@hotmail.com')
""")

connection.commit()

# Read csv from python as data frame and load it to sql
data_load = pd.read_csv("C:/Users/chigb/Downloads/5_fraud_records.csv")

print(data_load.head())

# load dataframe to sql
try:
    data_load.to_sql('Fraud_table',con=engine, if_exists= 'replace', index= False)
    print("Data successfully added to database")
except Exception as e:
    print(f"An error occored: {e}")