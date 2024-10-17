import csv
import json

# Input and output file paths
input_csv = 'rawData/10_Renewable_Energy.csv'  # Your raw data file
output_json_renewable = 'data/renewable_energy_generation.json'  # Output for renewable generation
output_json_non_renewable = 'data/non_renewable_energy_generation.json'  # Output for non-renewable generation
output_json_capacity = 'data/energy_capacity.json'  # Output for installed capacity

# Lists to hold the parsed data
renewable_data = []
non_renewable_data = []
capacity_data = []

# Open and read the CSV file
with open(input_csv, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Filter for Malaysia only
        if row['Country'] == 'Malaysia':
            # Renewable Energy Generation Data
            if row['Energy Type'] == 'Total Renewable':
                for year in range(2000, 2024):
                    if row[str(year)]:  # Check if the year column is not empty
                        renewable_data.append({
                            'Year': year,
                            'Generation': float(row[str(year)]),  # Convert to float
                            'Technology': row['Technology']
                        })
            
            # Non-Renewable Energy Generation Data
            if row['Energy Type'] == 'Total Non-Renewable':
                for year in range(2000, 2024):
                    if row[str(year)]:  # Check if the year column is not empty
                        non_renewable_data.append({
                            'Year': year,
                            'Generation': float(row[str(year)]),  # Convert to float
                            'Technology': row['Technology']
                        })
            
            # Installed Capacity Data
            if row['Energy Type'] in ['Total Renewable', 'Total Non-Renewable']:
                for year in range(2000, 2024):
                    if row[str(year)]:  # Check if the year column is not empty
                        capacity_data.append({
                            'Year': year,
                            'Capacity': float(row[str(year)]),  # Convert to float
                            'Technology': row['Technology']
                        })

# Write the data to JSON files
with open(output_json_renewable, mode='w', encoding='utf-8') as json_file:
    json.dump(renewable_data, json_file, indent=4)

with open(output_json_non_renewable, mode='w', encoding='utf-8') as json_file:
    json.dump(non_renewable_data, json_file, indent=4)

with open(output_json_capacity, mode='w', encoding='utf-8') as json_file:
    json.dump(capacity_data, json_file, indent=4)

print(f"Parsed data has been written to {output_json_renewable}, {output_json_non_renewable}, and {output_json_capacity}")
