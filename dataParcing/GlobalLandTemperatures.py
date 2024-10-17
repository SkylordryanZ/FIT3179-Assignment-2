import csv
import json

# Input and output file paths for GlobalLandTemperatures
csv_file = 'data\GlobalTemperatures.csv'
json_file = 'data\global_land_temperatures.json'

# Prepare list to store the converted data
data_list = []

# Open the CSV file and read its content
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_list.append({
            "Date": row["dt"],
            "LandAverageTemperature": float(row["LandAverageTemperature"]) if row["LandAverageTemperature"] else None,
            "LandAverageTemperatureUncertainty": float(row["LandAverageTemperatureUncertainty"]) if row["LandAverageTemperatureUncertainty"] else None,
            "LandMaxTemperature": float(row["LandMaxTemperature"]) if row["LandMaxTemperature"] else None,
            "LandMaxTemperatureUncertainty": float(row["LandMaxTemperatureUncertainty"]) if row["LandMaxTemperatureUncertainty"] else None,
            "LandMinTemperature": float(row["LandMinTemperature"]) if row["LandMinTemperature"] else None,
            "LandMinTemperatureUncertainty": float(row["LandMinTemperatureUncertainty"]) if row["LandMinTemperatureUncertainty"] else None,
            "LandAndOceanAverageTemperature": float(row["LandAndOceanAverageTemperature"]) if row["LandAndOceanAverageTemperature"] else None,
            "LandAndOceanAverageTemperatureUncertainty": float(row["LandAndOceanAverageTemperatureUncertainty"]) if row["LandAndOceanAverageTemperatureUncertainty"] else None
        })

# Write the JSON data to the output file
with open(json_file, mode='w') as file:
    json.dump(data_list, file, indent=2)

print("GlobalLandTemperatures CSV data has been converted to JSON!")
