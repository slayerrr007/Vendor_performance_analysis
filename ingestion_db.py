
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time


# --------------------------------
# 3. Create SQLite database engine
# --------------------------------

engine = create_engine("sqlite:///inventory.db")

# --------------------------------
# 4. Function to ingest data into DB
# --------------------------------

def ingest_db(df, table_name, engine):
    """Ingest dataframe into database table."""

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    logging.info(f"Successfully ingested {table_name} into database")


# --------------------------------
# 5. Function to load raw CSV data
# --------------------------------

def load_raw_data():

    """Load CSV files and ingest them into database."""

    start = time.time()

    logging.info("Starting data ingestion")

    for file in os.listdir():

        if file.endswith(".csv"):

            try:
                df = pd.read_csv(file)

                print(f"Ingesting {file} - Shape: {df.shape}")

                logging.info(f"Ingesting {file} into database")

                ingest_db(df, file[:-4], engine)

            except Exception as e:

                logging.error(f"Error ingesting {file}: {e}")

                print(f"Error processing {file}: {e}")

    end = time.time()

    total_time = (end - start) / 60

    logging.info("-------------Ingestion complete-------------")

    logging.info(f"Total Time Taken: {total_time:.2f} minutes")

    print("--------------------------------")
    print("Data ingestion completed!")
    print(f"Total time taken: {total_time:.2f} minutes")


# --------------------------------
# 6. Execute the ingestion process
# --------------------------------

if __name__ == "__main__":

    load_raw_data()
