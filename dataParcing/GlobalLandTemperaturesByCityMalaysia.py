import csv
import json
from collections import defaultdict
from statistics import mean

# Input and output file paths
input_csv = 'rawData\GlobalLandTemperaturesByState.csv'  # Update this with your actual CSV path
output_json = 'data\global_land_temperatures_by_state_malaysia.json'

# Dictionary to hold temperature data by state
state_temperatures = defaultdict(lambda: defaultdict(list))

# Open the CSV file and process data
with open(input_csv, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        state = row['State']  # Assuming 'State' column exists in the CSV
        date = row['dt']
        temp = float(row['AverageTemperature']) if row['AverageTemperature'] else None
        
        if temp:
            state_temperatures[state][date].append(temp)

# Prepare data for JSON output
output_data = []

for state, dates in state_temperatures.items():
    for date, temps in dates.items():
        avg_temp = mean(temps)  # Calculate average temperature for each date
        output_data.append({
            'State': state,
            'Date': date,
            'AverageTemperature': avg_temp
        })

# Write the aggregated data to a JSON file
with open(output_json, mode='w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Aggregated temperature data by state has been written to {output_json}")
