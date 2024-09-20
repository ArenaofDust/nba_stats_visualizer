# LAC_FULLSTACK_QUESTION_SET

1. I wanted to stay in New York City. I also got into NYU but Fordham was much cheaper with financial aid. I took computer programming classes in high school, loved them, and decided to major in computer science after I did more research about the field. I loved the possibility for career growth and the ability to work on many different things.
2. Languages: C++, Python, JavaScript, SQL | Libraries: REACT / Node.js (Used Django a few times during school) | 
    - All languages were used in school and have been used for personal projects and school assignments
    - REACT / NODE.js and Django: Used for personal projects
3. ANKI - Spotify - LetterBoxd
    - ANKI: Everything about the app is perfect but the user interface is outdated and editing flashcards can be annoying. I think that there could be better instructions, through some sort of modal, for editing cards instead of displaying a row of svg images when the edit button is pressed. 

    - Spotify: Local Files - There needs to be official documentation on local files and how to properly upload them and keep them active in your playlist. I hate adding dozens of song files and having them quietly grey out days later

    - LetterBoxd: There are no translations for reviews in other languages. I think that there should be an option to translate all reviews to the language that a person speaks. There could be a translation button that prompts that behavior

4. Multithreaded programs for my operating systems class. I remember that being a very hard concept to understand
5. NBA, NFL, CSMajors, CSCareerQuestions reddit forums everyday. I follow a few basketball stats people on twitter. I mainly read content about upcoming prospects and a lot of times, it seems like it comes down to mainstream stats, who has the highest BPM, and the "eye test"(Read). Bleacher Report and House of Highlights everyday (Watch).  
6. REACT / NODE.JS through THEODINPROJECT and YOUTUBE playlists. 

7. I truly love basketball. I played all my life and was captain of the varsity team in high school (I have proof of this). I would be a lot more motivated to develop my technical skills under the edifice of a sports organization because I would be contributing to a childhood love of mine

8. FINAL QUESTION
    - I used AI to help me understand some of my program errors and what was wrong with my docker files, I also used it to help with styling pages


# APPROACHES 
1. I chose primary keys based on which values were the same (team ids) and which values had to be unique (other_id). I was stuck for a long time because I made nba_team_id and glg_team_id a composite key. However, when runnig the program, PHX did not have a glg_team_id and I removed  it. Creating the tables was the easiest part though (if I did it right). 
    - Problems: Transferring data to the tables was also straightforward until I wanted to view the results. I wasn't very familiar with Docker so I spent hours figuring out why the db container kept stopping immediately after starting (something my frontend also did), and why changes were not showing up in the table (I kept logging into the database on localhost and not the docker database, which had proper, fully populated tables **face palm). I consulted the internet and CHATGPT (which wasn't of much help on this part but did come through for the frontend errors). Very frustrating
2. SQL QUERIES
    - 2A. I labeled the winner and loser for each game based on home and away scores with final scores CTE. I counted total games, wins, losses for each team and did a UNION ALL for home and away games for team_record CTE. Team_names was a simple select statement. The final main select statement joined the team record with the team names, calculated win percentage with the case ( CASE WHEN rs.games_played > 0 THEN rs.wins::FLOAT / rs.games_played ELSE 0) and ordered the results of the calculation in DESC

    - 2B. For final_scores CTE, I used DATE_TRUNC to get the current month. For the team_record CTE, it was the same as 2a but for the month. For home and away game CTES, I seperately counted the home and away games for each team for the current month. For ranked_stats CTE, I used coalesce for the case that a team had not played a home or away game for that month and then used Rank to rank the teams based on how many games (home, away, and total) they had played in that month. I then used LEFT JOINS to combine records with stats from home and away games, even for teams who had not played in the current month. The last select statement combined the stats with the names of the teams and calculated win percentage again and ordered by win percentage DESC

5. I skipped to five because I felt like configuring Docker with my backend and frontend for the visualization would take up a lot of time (it did). 
    - Problems: Frontend kept ending immediately. I changed the port from 5000 to 5001 (did the same for the database) (5432:5432 to 6543:5432), someone on stackoverflow had done it and it workeed so I tried it and it worked. I also added "WATCHPACK_POLLING=true" to the frontend package.json which seemed to fix the problem.

    - Problems: Could not properly display data for both pages based on the head coach and statistician roles

    - Problems: If I was more familiar with Docker, I think I could have resolved some more of the issues


# Instructions

1. CREATE A .ENV file (in root directory) and insert your values. Let me know if you need mine
    - POSTGRES_DB=
      POSTGRES_USER=
      POSTGRES_PASSWORD=
      POSTGRES_HOST=
      JWT_SECRET=

2. (Docker-compose build to build) - (docker-compose up to run) - (docker-compose down to stop and remove)