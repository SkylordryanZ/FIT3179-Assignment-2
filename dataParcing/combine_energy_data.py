import json

# Input file paths
renewable_json = 'data/renewable_energy_generation.json'
non_renewable_json = 'data/non_renewable_energy_generation.json'

# Output file path
combined_output_json = 'data/combined_energy_data.json'

# Load renewable energy data
with open(renewable_json, 'r') as f:
    renewable_data = json.load(f)

# Load non-renewable energy data
with open(non_renewable_json, 'r') as f:
    non_renewable_data = json.load(f)

# Combine data into a single list
combined_data = []

# Add Renewable Energy Data
for item in renewable_data:
    combined_data.append({
        'Year': item['Year'],
        'Generation': item['Generation'],
        'Type': 'Renewable',
        'Technology': item['Technology']
    })

# Add Non-Renewable Energy Data
for item in non_renewable_data:
    combined_data.append({
        'Year': item['Year'],
        'Generation': item['Generation'],
        'Type': 'Non-Renewable',
        'Technology': item['Technology']
    })

# Write combined data to a JSON file
with open(combined_output_json, 'w') as f:
    json.dump(combined_data, f, indent=4)

print(f"Combined data has been written to {combined_output_json}")
