# Importing SQLAlchemy library
import sqlalchemy as sa
import pandas as pd

# importing connection engine pack
from sqlalchemy import create_engine, inspect, text
#from urllib.parse import quote_plus #why
from sqlalchemy import Table, MetaData

# Creating connection strings for my database
username= "consultants"
password = "WelcomeItc@2022"
host= "18.132.73.146"
port = "5432"
database= "testdb"
#ENCODED_PASSWORD = quote_plus(password)


#creating database connectionw string
#connection_string = "postgresql+psycopg2://{username}:{ENCODED_PASSWORD}@{host}:{port}/{database}"
engine = create_engine('postgresql://consultants:WelcomeItc%402022@18.132.73.146:5432/testdb')
#Establishing connection with engine & database
#engine = create_engine(connection_string)
#cursor = connection_string.cursor()

try:
    with engine.connect() as connection: #explain???
        print("connection successful")
except Exception as e:  #explain????
    print("connection failed:", e)

# Read csv from python as data frame and load it to sql
data_load = pd.read_csv("C:/Users/chigb/Downloads/5_fraud_records.csv")

print(data_load.head(2))

# load dataframe to sql
try:
    data_load.to_sql('fraud_table',con=engine, if_exists= 'replace', index= False)
    print("Data successfully added to database")
except Exception as e:
    print("An error occored: {e}")

connection.commit()

fraud_data = pd.read_sql_table("fraud_table",engine)

#CREATING FLASK API
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

fraud = fraud_data.to_dict(orient='records')

@app.route('/data', methods=['GET'])
def get_data():
    data = fraud
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data from database"}), 500

if __name__ == '__main__':
    # Run the app
  app.run(host='0.0.0.0', port=5310, debug=True)

