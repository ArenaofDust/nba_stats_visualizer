import json
#import psycopg2

# Inserts data from dev_test_data
# Handles merges,updates, and/or reloads with ON CONLFICTS AND DO UPDATES
def transfer_team_data(cursor, team_file_path):
    with open(team_file_path, 'r') as team_file: 
        team_data = json.load(team_file)

    for record in team_data:
        cursor.execute(
            """
            INSERT INTO team (team_id, league_lk, team_name, team_name_short, team_nickname)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (team_id) 
            DO UPDATE SET
                league_lk = EXCLUDED.league_lk,
                team_name = EXCLUDED.team_name,
                team_name_short = EXCLUDED.team_name_short,
                team_nickname = EXCLUDED.team_nickname;

            """, 
            (record['teamId'], record['leagueLk'], record['teamName'], record['teamNameShort'], record['teamNickname'])
        )

def transfer_team_affiliate_data(cursor, affiliate_file_path):
    with open(affiliate_file_path, 'r') as affiliate_file:
        affiliate_data = json.load(affiliate_file)

    for record in affiliate_data:
        cursor.execute(
            """
            INSERT INTO team_affiliate (nba_team_id, nba_abrv, glg_team_id, glg_abrv)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (nba_team_id) 
            DO UPDATE SET
                nba_abrv = EXCLUDED.nba_abrv,
                glg_abrv = EXCLUDED.glg_abrv;

            """, 
            (record['nba_teamId'], record['nba_abrv'], record['glg_teamId'], record['glg_abrv'])
        )

def transfer_player_data(cursor, player_file_path):
    with open(player_file_path, 'r') as player_file:
        player_data = json.load(player_file)

    for record in player_data:
        cursor.execute(
            """
            INSERT INTO player (player_id, first_name, last_name)
            VALUES (%s, %s, %s)
            ON CONFLICT (player_id) 
            DO UPDATE SET
                first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name;

            """, 
            (record['player_id'], record['first_name'], record['last_name'])
        )

def transfer_roster_data(cursor, roster_file_path):
    with open(roster_file_path, 'r') as roster_file:
        roster_data = json.load(roster_file)
    
    for record in roster_data:
        # Checking if player_id is present
        cursor.execute(
            """
            INSERT INTO player (player_id, first_name, last_name)
            VALUES(%s, %s, %s)
            ON CONFLICT (player_id) DO NOTHING;
            """,
            (record['player_id'], record['first_name'], record['last_name'])
        )

        cursor.execute(
            """
            INSERT INTO roster (team_id, player_id, first_name, last_name, position, contract_type)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (team_id, player_id) 
            DO UPDATE SET
                first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name, 
                position = EXCLUDED.position, 
                contract_type = EXCLUDED.contract_type;

            """, 
            (record['team_id'], record['player_id'], record['first_name'],
              record['last_name'], record['position'], record['contract_type'])
        )

def transfer_schedule_data(cursor, schedule_file_path):
    with open(schedule_file_path, 'r') as schedule_file:
        schedule_data = json.load(schedule_file)

    for record in schedule_data:
        cursor.execute(
            """
            INSERT INTO game_schedule (game_id, home_id, home_score, away_id, away_score, game_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (game_id) 
            DO UPDATE SET
                home_score = EXCLUDED.home_score,
                away_score = EXCLUDED.away_score,
                game_date = EXCLUDED.game_date;

            """, 
            (record['game_id'], record['home_id'], record['home_score'],
              record['away_id'], record['away_score'], record['game_date'])
        )
        
def transfer_lineup_data(cursor, lineup_file_path):
    with open(lineup_file_path, 'r') as lineup_file:
        lineup_data = json.load(lineup_file)

    for record in lineup_data:
        cursor.execute(
            """
            INSERT INTO lineup (team_id, player_id, lineup_num, period, time_in, time_out, game_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (team_id, player_id, game_id, lineup_num) 
            DO UPDATE SET
                period = EXCLUDED.period,
                time_in = EXCLUDED.time_in,
                time_out = EXCLUDED.time_out;

            """, 
            (record['team_id'], record['player_id'], record['lineup_num'],
              record['period'], record['time_in'], record['time_out'], record['game_id'])
        )