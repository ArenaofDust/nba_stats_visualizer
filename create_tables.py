#import psycopg2

# Queries to create the tables to store data from dev_test_data files
def create_tables(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS team (
            team_id INT PRIMARY KEY,
            league_lk VARCHAR(10),
            team_name VARCHAR(255),
            team_name_short VARCHAR(10),
            team_nickname VARCHAR(50) 
        );

        """
    )
    # glg_team_id allows null since PHX did not have a glg team 
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS team_affiliate (
            nba_team_id INTEGER,
            nba_abrv VARCHAR(10),
            glg_team_id BIGINT,
            glg_abrv VARCHAR(10),
            PRIMARY KEY (nba_team_id),
            FOREIGN KEY (nba_team_id) REFERENCES team(team_id)
        );

        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS player (
            player_id INTEGER PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50)
        );

        """
    )

    cursor.execute(
        """
        CREATE TABLE if NOT EXISTS roster (
            team_id INTEGER,
            player_id INTEGER,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            position VARCHAR(10),
            contract_type VARCHAR(10),
            PRIMARY KEY (team_id, player_id),
            FOREIGN KEY (team_id) REFERENCES team(team_id),
            FOREIGN KEY (player_id) REFERENCES player(player_id)
        );

        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS game_schedule (
            game_id INTEGER PRIMARY KEY,
            home_id INTEGER,
            home_score INTEGER,
            away_id INTEGER,
            away_score INTEGER,
            game_date TIMESTAMP,
            FOREIGN KEY (home_id) REFERENCES team(team_id),
            FOREIGN KEY (away_id) REFERENCES team(team_id)
        );

        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lineup (
            team_id INTEGER,
            player_id INTEGER,
            lineup_num INTEGER,
            period INTEGER,
            time_in NUMERIC,
            time_out NUMERIC,
            game_id INTEGER,
            PRIMARY KEY (team_id, player_id, game_id, lineup_num),
            FOREIGN KEY (team_id) REFERENCES team(team_id),
            FOREIGN KEY (player_id) REFERENCES player(player_id),
            FOREIGN KEY (game_id) REFERENCES game_schedule(game_id)
        );

        """
    )

