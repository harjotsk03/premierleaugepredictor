import re
import re
import os
import csv

raw_data = """Rank	Player	Club	Nationality	Stat	

Rank	Player	Club	Nationality	Stat	
1.	
George Baldock
-	

Greece
3,420	 
1.	
Conor Coady
-	

England
3,420	 
1.	
David de Gea
-	

Spain
3,420	 
1.	
Rui Patrício
-	

Portugal
3,420	 
1.	
Martin Dúbravka

Newcastle United

Slovakia
3,420	 
1.	
Ben Foster
-	

England
3,420	 
1.	
Harry Maguire

Manchester United

England
3,420	 
1.	
Jordan Pickford

Everton

England
3,420	 
1.	
Nick Pope

Burnley

England
3,420	 
1.	
Declan Rice
-	

England
3,420	 1.	
Mathew Ryan
-	

Australia
3,420	 
1.	
Kasper Schmeichel
-	

Denmark
3,420	 
1.	
James Tarkowski

Burnley

England
3,420	 
1.	
Virgil van Dijk

Liverpool

Netherlands
3,420	 
1.	
James Ward-Prowse
-	

England
3,420	 
16.	
Jonny Evans
-	

Northern Ireland
3,385	 
17.	
Enda Stevens
-	

Ireland
3,346	 
18.	
Dwight McNeil

Burnley

England
3,344	 
19.	
Aaron Ramsdale
-	

England
3,330	 
20.	
Wilfried Zaha
-	

Cote D’Ivoire
3,280	 
"""

def parse_raw_data(raw, year="2019/2020", statName="Minutes Played"):
    entries = re.split(r'\d+\.\s+', raw)[1:]  # Split by rank numbers
    data = []
    for entry in entries:
        lines = [line.strip() for line in entry.strip().split("\n") if line.strip()]  # Remove empty lines
        if len(lines) >= 4:  # Ensure enough data is present
            player = lines[0]
            club = lines[1] if lines[1] != "-" else "Unknown"
            nationality = lines[2]
            try:
                stat = int(lines[3].replace(",", ""))  # Convert stat to integer
            except ValueError:
                stat = 0  # Default to 0 if stat is invalid
            data.append({"Rank": None, "Player": player, "Club": club, "Year": year, statName: stat})
    return data

# Write data to CSV
def write_to_csv(data, filename="output.csv", statName="Minutes Played"):
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
write_to_csv(structured_data, filename="minutes_played_stats.csv")
print("Data written to minutes_played_stats.csv")