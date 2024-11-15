import re
import re
import os
import csv

raw_data = """Rank	Player	Club	Nationality	Stat	
1.	
Jamie Vardy

Leicester City

England
23	 
2.	
Pierre-Emerick Aubameyang
-	

Gabon
22	 
2.	
Danny Ings
-	

England
22	 
4.	
Raheem Sterling
-	

England
20	 
5.	
Mohamed Salah

Liverpool

Egypt
19	 
6.	
Harry Kane
-	

England
18	 
6.	
Sadio Mané
-	

Senegal
18	 
8.	
Raúl Jiménez
-	

Mexico
17	 
8.	
Anthony Martial
-	

France
17	 
8.	
Marcus Rashford

Manchester United

England
17	 
11.	
Sergio Agüero
-	

Argentina
16	 
12.	
Tammy Abraham
-	

England
15	 
13.	
Gabriel Jesus
-	

Brazil
14	 
13.	
Chris Wood
-	

New Zealand
14	 
15.	
Dominic Calvert-Lewin

Everton

England
13	 
15.	
Richarlison
-	

Brazil
13	 
15.	
Kevin De Bruyne

Manchester City

Belgium
13	 
18.	
Riyad Mahrez
-	

Algeria
11	 
18.	
Teemu Pukki
-	

Finland
11	 
18.	
Son Heung-Min

Tottenham Hotspur

South Korea
11 
"""
def parse_raw_data(raw, year="2023/2024", statName="Goals"):
    entries = re.split(r'\d+\.\s+', raw)[1:]  # Split by rank numbers
    data = []
    for entry in entries:
        lines = [line.strip() for line in entry.strip().split("\n") if line.strip()]  # Remove empty lines
        if len(lines) >= 4:  # Ensure enough data is present
            player = lines[0]
            club = lines[1] if lines[1] != "-" else "Unknown"
            nationality = lines[2]
            try:
                stat = int(lines[3])  # Convert stat to integer
            except ValueError:
                stat = 0  # Default to 0 if stat is invalid
            data.append({"Rank": None, "Player": player, "Club": club, "Year": year, statName: stat})
    return data

# Write data to CSV
def write_to_csv(data, filename="output.csv", statName="Goals"):
    for rank, item in enumerate(data, start=1):
        item["Rank"] = rank

    fieldnames = ["Rank", "Player", "Club", "Year", statName]

    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:  # Write header only if file does not exist
            writer.writeheader()
        writer.writerows(data)

structured_data = parse_raw_data(raw_data, year="2019/2020")
write_to_csv(structured_data, filename="players_statstest.csv")
print("Data written to players_stats.csv")