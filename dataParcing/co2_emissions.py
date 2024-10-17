import csv
import json

# Input and output file paths for CO₂ Emissions
csv_file = 'data\\04_CO2_Emissions_Emissions_Intensities_and_Emissions_Multipliers.csv'
json_file = 'data\co2_emissions_malaysia_australia.json'

# Prepare list to store the filtered and converted data
data_list = []

# Open the CSV file and read its content
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Filter only for Australia and Malaysia data
        if row["Country"] in ["Australia", "Malaysia"]:
            for year in range(1995, 2019):  # Loop through years from 1995 to 2018
                year_str = str(year)
                co2_emissions = float(row[year_str]) if row[year_str] else None  # Handle missing data
                data_list.append({
                    "Country": row["Country"],
                    "ISO2": row["ISO2"],
                    "ISO3": row["ISO3"],
                    "Industry": row["Industry"],
                    "Year": int(year),
                    "CO2_emissions": co2_emissions
                })

# Write the filtered data to the JSON file
with open(json_file, mode='w') as file:
    json.dump(data_list, file, indent=2)

print("CO₂ Emissions CSV data (filtered for Malaysia and Australia) has been converted to JSON!")
