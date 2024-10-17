import csv
import json
from collections import defaultdict
from statistics import mean

# Input and output file paths
input_json = 'data/global_land_temperatures_by_city_malaysia.json'
output_json_major_cities = 'data/major_cities_temperature_malaysia.json'
output_json_avg_temp = 'data/average_temperature_malaysia.json'

# List of major cities in Malaysia
major_cities = ["Kuala Lumpur", "George Town", "Johor Bahru", "Ipoh", "Shah Alam", "Petaling Jaya", "Kota Kinabalu", "Kuching"]

# Load the JSON data
with open(input_json, mode='r', encoding='utf-8') as file:
    temperature_data = json.load(file)

# Dictionary to hold data for major cities and combined average temperature
major_city_temperatures = defaultdict(lambda: defaultdict(list))
combined_temperatures = defaultdict(list)

# Process the data to filter for major cities and calculate combined average
for record in temperature_data:
    city = record['City']
    date = record['Date']
    temp = record['AverageTemperature']
    
    # If the city is a major city, store it in the major cities dictionary
    if city in major_cities:
        major_city_temperatures[city][date].append(temp)
    
    # Add temperature to combined temperature for overall average
    combined_temperatures[date].append(temp)

# Prepare data for major cities JSON output
output_major_cities = []

for city, dates in major_city_temperatures.items():
    for date, temps in dates.items():
        avg_temp = mean(temps)  # Calculate average temperature for each date
        output_major_cities.append({
            'City': city,
            'Date': date,
            'AverageTemperature': avg_temp
        })

# Prepare data for combined average temperature JSON output
output_avg_temp = []

for date, temps in combined_temperatures.items():
    avg_temp = mean(temps)  # Calculate overall average temperature for each date
    output_avg_temp.append({
        'Date': date,
        'AverageTemperature': avg_temp
    })

# Write the major cities data to JSON file
with open(output_json_major_cities, mode='w', encoding='utf-8') as json_file:
    json.dump(output_major_cities, json_file, indent=4)

# Write the combined average temperature data to JSON file
with open(output_json_avg_temp, mode='w', encoding='utf-8') as json_file:
    json.dump(output_avg_temp, json_file, indent=4)

print(f"Data for major cities has been written to {output_json_major_cities}")
print(f"Combined average Malaysian temperature has been written to {output_json_avg_temp}")
