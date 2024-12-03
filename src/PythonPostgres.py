# Importing SQLAlchemy library
import sqlalchemy as sa
import pandas as pd

# importing connection engine pack
from sqlalchemy import create_engine, inspect, text
from urllib.parse import quote_plus #why
from sqlalchemy import Table, MetaData

# Creating connection strings for my database
username= "consultants"
password = "WelcomeItc@2022"
host= "18.132.73.146"
port = "5432"
database= "testdb"
ENCODED_PASSWORD = quote_plus(password)


#creating database connectionw string
connection_string = f"postgresql+psycopg2://{username}:{ENCODED_PASSWORD}@{host}:{port}/{database}"

# Establishing connection with engine & database
engine = create_engine(connection_string)
#cursor = connection_string.cursor()

try:
    with engine.connect() as connection: #explain???
        print("connection successful")
except Exception as e:  #explain????
    print("connection failed:", e)

# Read csv from python as data frame and load it to sql
data_load = pd.read_csv("C:/Users/chigb/Downloads/5_fraud_records.csv")
print(data_load.head(3))

# load dataframe to sql
try:
    data_load.to_sql('fraud_table',con=engine, if_exists= 'replace', index= False)
    print("Data successfully added to database")
except Exception as e:
   print("An error occored: {e}")

connection.commit()