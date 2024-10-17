import csv
import json

# Define the input CSV and output JSON file paths
input_csv = "data\GlobalLandTemperaturesByCity.csv"
output_json = "data\global_land_temperatures_by_city_malaysia.json"

# Initialize an empty list to store Malaysian data
malaysia_data = []

# Open and read the CSV file
with open(input_csv, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Filter rows where the country is Malaysia
        if row['Country'] == 'Malaysia':
            # Append the relevant row data to the list
            malaysia_data.append({
                'dt': row['dt'],
                'AverageTemperature': row['AverageTemperature'],
                'AverageTemperatureUncertainty': row['AverageTemperatureUncertainty'],
                'City': row['City'],
                'Country': row['Country'],
                'Latitude': row['Latitude'],
                'Longitude': row['Longitude']
            })

# Write the filtered data to a JSON file
with open(output_json, mode='w', encoding='utf-8') as json_file:
    json.dump(malaysia_data, json_file, indent=4)

print(f"Filtered data for Malaysia has been written to {output_json}")
