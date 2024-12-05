# Importing SQLAlchemy library
import sqlalchemy as sa
import pandas as pd

# importing connection engine pack
from sqlalchemy import create_engine, inspect, text
from sqlalchemy import Table, MetaData

# Creating connection strings for my database
username= "consultants"
password = "WelcomeItc@2022"
host= "18.132.73.146"
port = "5432"
database= "testdb"


#creating database connectionw string

engine = create_engine('postgresql://consultants:WelcomeItc%402022@18.132.73.146:5432/testdb')


fraud_data = pd.read_sql("fraud_table",engine)

#CREATING FLASK API
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

fraud = fraud_data.to_dict(orient='records')

@app.route('/data', methods=['GET'])
def get_data():
    def get_single_record(id):
        record = next((item for item in fraud_data if item['fraud_id'] == id), None)
    data = fraud
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data from database"}), 500

if __name__ == '__main__':
    # Run the app
  app.run(host='0.0.0.0', port=2020, debug=True)

