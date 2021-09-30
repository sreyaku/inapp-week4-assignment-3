import sqlite3
con = sqlite3.connect("database.sqlite")
cursor = con.cursor()

# a) Counts all the rows in the Teams table
print('Count of all rows:')
cursor.execute("SELECT COUNT(*) FROM Teams")
print(cursor.fetchall())

# b) Print all the unique values that are included in the Season column in the Teams table
print('unique values in season column :')
cursor.execute("SELECT DISTINCT(Season) FROM TEAMS")
results = cursor.fetchall()
for row in results:
    print(row[0])

# c) Print the largest and smallest stadium capacity that is included in the Teams table
cursor.execute("SELECT MAX(StadiumCapacity),MIN(StadiumCapacity) FROM Teams")
results = cursor.fetchall()
for row in results:
    print("Largest Stadium Capacity:",row[0])
    print("Smallest Stadium Capacity:", row[1])

# d) Print the sum of squad players for all teams during the 2014 season from the Teams table [Answer - 1164]
cursor.execute("SELECT SUM(KaderHome) FROM Teams WHERE Season = '2014'")
results = cursor.fetchall()
for row in results:
    print("Sum od squad players:", row[0])

# e) Query the Matches table to know how many goals did Man United score during home games on average? [Answer - 2.16]
cursor.execute("SELECT ROUND(AVG(FTHG),2) FROM Matches WHERE HomeTeam = 'Man United'")
results = cursor.fetchall()
for row in results:
    print(" Total goals:",row[0])
con.commit()
con.close()