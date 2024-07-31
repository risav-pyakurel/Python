#file to handle main flow of data & bitwise operator

import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)

        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {  #new dictionary contains all of the diff data we want to add into csv file
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  #opened a csv file in append mode,used context manager
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry added successful")

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]




def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction( dd-mm-yyyy) or enter for today's date: ", allow_default=True
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add()
