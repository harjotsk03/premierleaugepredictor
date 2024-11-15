import re
import re
import os
import csv

raw_data = """Rank	Player	Club	Nationality	Stat	

Rank	Player	Club	Nationality	Stat	
1.	
Kevin De Bruyne

Manchester City

Belgium
20	 
2.	
Trent Alexander-Arnold

Liverpool

England
13	 
3.	
Andy Robertson

Liverpool

Scotland
12	 
4.	
Mohamed Salah

Liverpool

Egypt
10	 
4.	
David Silva
-	

Spain
10	 
4.	
Son Heung-Min

Tottenham Hotspur

South Korea
10	 
7.	
Riyad Mahrez
-	

Algeria
9	 
7.	
Adama Traoré
-	

Spain
9	 
9.	
Roberto Firmino
-	

Brazil
8	 
9.	
Harvey Barnes
-	

England
8	 
11.	
Willian
-	

Brazil
7	 
11.	
Bruno Fernandes

Manchester United

Portugal
7	 
11.	
Emiliano Buendía
-	

Argentina
7	 
11.	
Gabriel Jesus
-	

Brazil
7	 
11.	
Lucas Digne
-	

France
7	 
11.	
Sadio Mané
-	

Senegal
7	 
11.	
Bernardo Silva

Manchester City

Portugal
7	 
11.	
Marcus Rashford

Manchester United

England
7	 
19.	
César Azpilicueta
-	

Spain
6	 
19.	
João Moutinho
-	

Portugal
6	 
"""
def parse_raw_data(raw, year="2019/2020", statName="Assists"):
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
def write_to_csv(data, filename="output.csv", statName="Assists"):
    for rank, item in enumerate(data, start=1):
        item["Rank"] = rank

    fieldnames = ["Rank", "Player", "Club", "Year", statName]

    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:  # Write header only if file does not exist
            writer.writeheader()
        writer.writerows(data)

structured_data = parse_raw_data(raw_data, year="2010/2020")
write_to_csv(structured_data, filename="assists_stats.csv")
print("Data written to assists_stats.csv")