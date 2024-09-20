import os
import json
import psycopg2 #type: ignore
from create_tables import create_tables
from table_insertions import *

CONNECTION_PARAMETERS = {
    "host": os.environ.get("POSTGRES_HOST", "db"),
    "port": os.environ.get("POSTGRES_PORT", "5432"),
    "database": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD")
}

def main():
    try:
        print("Attempting to connect to database")

        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            print("*** Successfully connected to the database *** ")
            
            with conn.cursor() as cursor:
                create_tables(cursor)
                print("*** Created SQL Tables ***")

                try:
                    # Calling Functions to insert dev_test_data into tables
                    transfer_team_data(cursor, "dev_test_data/team.json")
                    transfer_team_affiliate_data(cursor, "dev_test_data/team_affiliate.json")
                    transfer_player_data(cursor, "dev_test_data/player.json")
                    transfer_roster_data(cursor, "dev_test_data/roster.json")
                    transfer_schedule_data(cursor, "dev_test_data/game_schedule.json")
                    transfer_lineup_data(cursor,"dev_test_data/lineup.json")

                    # Commit Insertions
                    conn.commit()
                    print("*** ALL DATA INSERTED ***")

                except psycopg2.Error as err:
                    # Undo all changes
                    conn.rollback()
                    print(f"Failed to connect to the database: {err}")
    except psycopg2.Error as err:
        print(f"Database error: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {str(err)}")

if __name__ == "__main__":
    # Stop container from exiting immediately
    main()
    while True:
        import time
        time.sleep(3600)


'''logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONNECTION_PARAMETERS = {
    "host": os.environ.get("POSTGRES_HOST", "db"),
    "port": os.environ.get("POSTGRES_PORT", "5432"),
    "database": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD")
}

# Connecting to lac_fullstack_dev database (Postgresql)
try:
    logging.info(f"Attempting to connect to database with parameters: {CONNECTION_PARAMETERS}")

    with psycopg2.connect (**CONNECTION_PARAMETERS) as conn:

        logging.info("Successfully connected to the database")
        # Cursor object for queries
        with conn.cursor() as cursor:
            # Calling create tables function 
            create_tables(cursor)

            try:
                # Calling Functions to insert dev_test_data into tables
                transfer_team_data(cursor, "dev_test_data/team.json")
                transfer_team_affiliate_data(cursor, "dev_test_data/team_affiliate.json")
                transfer_player_data(cursor, "dev_test_data/player.json")
                transfer_roster_data(cursor, "dev_test_data/roster.json")
                transfer_schedule_data(cursor, "dev_test_data/game_schedule.json")
                transfer_lineup_data(cursor,"dev_test_data/lineup.json")

                # Commit Insertions
                conn.commit()

            except psycopg2.Error as err:
                #Undo all changes
                conn.rollback()
                logging.error(f"Failed to connect to the database: {err}")
                raise
except psycopg2.DatabaseError as err:
    print(f"*** Failed Connection ***: {err} ")
    exit(1)
'''