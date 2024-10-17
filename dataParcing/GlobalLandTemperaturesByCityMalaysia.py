import csv
import json
from collections import defaultdict
from statistics import mean

# Input and output file paths
input_csv = 'rawData/GlobalLandTemperaturesByCity.csv'  
output_json = 'data/global_land_temperatures_by_city_malaysia.json'

# Dictionary to hold temperature data by city
city_temperatures = defaultdict(lambda: defaultdict(list))

# Open the CSV file and process data
with open(input_csv, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        country = row['Country']
        if country == 'Malaysia':  # Filter for Malaysia
            city = row['City']
            date = row['dt']
            temp = float(row['AverageTemperature']) if row['AverageTemperature'] else None
            
            if temp is not None:
                city_temperatures[city][date].append(temp)

# Prepare data for JSON output
output_data = []

for city, dates in city_temperatures.items():
    for date, temps in dates.items():
        avg_temp = mean(temps)  # Calculate average temperature for each date
        output_data.append({
            'City': city,
            'Date': date,
            'AverageTemperature': avg_temp
        })

# Write the aggregated data to a JSON file
with open(output_json, mode='w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Aggregated temperature data by city in Malaysia has been written to {output_json}")
