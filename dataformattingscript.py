import re
import re
import os
import csv

raw_data = """Rank	Player	Club	Nationality	Stat	

Rank	Player	Club	Nationality	Stat	
1.	
William Saliba

Arsenal

France
18	 
2.	
Gabriel Magalhães

Arsenal

Brazil
15	 
3.	
James Tarkowski

Everton

England
13	 
3.	
Ben White

Arsenal

England
13	 
5.	
Jarrad Branthwaite

Everton

England
12	 
6.	
Manuel Akanji

Manchester City

Switzerland
11	 
7.	
Tyrick Mitchell

Crystal Palace

England
10	 
8.	
Rúben Dias

Manchester City

Portugal
9	 
8.	
Josko Gvardiol

Manchester City

Croatia
9	 
8.	
Vitalii Mykolenko

Everton

Ukraine
9	 
8.	
Virgil van Dijk

Liverpool

Netherlands
9	 
12.	
Joachim Andersen
-	

Denmark
8	 
12.	
Timothy Castagne

Fulham

Belgium
8	 
12.	
Fabian Schär

Newcastle United

Switzerland
8	 
12.	
Illia Zabarnyi

Bournemouth

Ukraine
8	 
16.	
Dan Burn

Newcastle United

England
7	 
16.	
Nathan Collins

Brentford

Ireland
7	 
16.	
Diogo Dalot

Manchester United

Portugal
7	 
16.	
Antonee Robinson

Fulham

United States
7	 
16.	
Cristian Romero

Tottenham Hotspur

Argentina
7	 
"""
def parse_raw_data(raw, year="2023/2024", statName="Defender Clean Sheets"):
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
def write_to_csv(data, filename="output.csv", statName="Defender Clean Sheets"):
    for rank, item in enumerate(data, start=1):
        item["Rank"] = rank

    fieldnames = ["Rank", "Player", "Club", "Year", statName]

    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:  # Write header only if file does not exist
            writer.writeheader()
        writer.writerows(data)

structured_data = parse_raw_data(raw_data, year="2023/2024")
write_to_csv(structured_data, filename="defender_clean_sheets_stats.csv")
print("Data written to defender_clean_sheets_stats.csv")