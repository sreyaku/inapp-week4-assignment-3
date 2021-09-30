import sqlite3
con = sqlite3.connect("database.sqlite")
cursor = con.cursor()

# a)Write a query that returns the HomeTeam, FTHG (number of home goals scored in a game) and FTAG (number of away goals scored in a game) from the Matches table. Only include data from the 2010 season and where ‘Aachen’ is the name of the home team. Return the results by the number of home goals scored in a game in descending order.

print('returning the HomeTeam, FTHG (number of home goal and FTAG')
cursor.execute("SELECT HomeTeam,FTHG,FTAG FROM Matches WHERE HomeTeam ='Aachen' AND Season =2010 ORDER BY FTHG DESC,FTAG ASC;")
print(cursor.fetchall())

# b)Print the total number of home games each team won during the 2016 season in descending order of number of home games from the Matches table.
print("Homegames won during 2016 in descending order")
cursor.execute("SELECT HomeTeam,COUNT(FTR) AS Total_Home_Wins FROM Matches WHERE FTR ='H' AND Season ='2016' GROUP BY HomeTeam ORDER BY COUNT(FTR) DESC;")
print(cursor.fetchall())

#c)Write a query that returns the first ten rows from the Unique_Teams table
print("First Ten Rows Of Unique_Teams_Table")
cursor.execute("SELECT * FROM Unique_Teams LIMIT 10;")
print(cursor.fetchall())

#d)Print the Match_ID and Unique_Team_ID with the corresponding Team_Name from the Unique_Teams and Teams_in_Matches tables. Use the WHERE statement first and then use the JOIN statement to get the same result.
print("Match_ID and Unique_Team_ID ")
cursor.execute("SELECT * FROM Teams_in_Matches ,Unique_Teams WHERE Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID;")
print(cursor.fetchall())

#using join
print("using join ")
cursor.execute("SELECT * FROM Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID;")
print(cursor.fetchall())

#e)Write a query that joins together the Unique_Teams data table and the Teams table, and returns the first 10 rows
print("First 10 rows of unique_teams and teams _table")
cursor.execute("SELECT * FROM Unique_Teams JOIN Teams ON Unique_Teams.TeamName =Teams.TeamName LIMIT 10;")
print(cursor.fetchall())

#f)Write a query that shows the Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table. Only return the first five rows.
print("required details")
cursor.execute("SELECT Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,Teams.ForeignPlayersHome FROM Unique_Teams JOIN Teams ON Unique_Teams.TeamName=Teams.TeamName LIMIT 5:")
print(cursor.fetchall())
#g)Write a query that shows the highest Match_ID for each team that ends in a “y” or a “r”. Along with the maximum Match_ID, display the Unique_Team_ID from the Teams_in_Matches table and the TeamName from the Unique_Teams table.
print("highest Match_ID for each team that ends in a “y” or a “r”")
cursor.execute("SELECT MAX(Match_ID),Teams_in_Matches.Unique_Team_ID,TeamName FROM Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID =Unique_Teams.Unique_TEAM_ID WHERE (TeamName lIKE '%y')OR(TeamName LIKE '%r')GROUP BY Teams_in_Matches.Unique_Team_ID,TeamName:")
print(cursor.fetchall())
