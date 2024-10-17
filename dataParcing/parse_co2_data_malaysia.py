import csv
import json
from collections import defaultdict

# Paths for input CSV files
input_csv_emissions = 'rawData/04_CO2_Emissions_Emissions_Intensities_and_Emissions_Multipliers.csv'

# Output JSON file paths
output_emissions_json = 'data/co2_emissions_over_time.json'
output_intensity_json = 'data/co2_emissions_intensity_over_time.json'

# Lists to hold the parsed data
emissions_data = []
intensity_data = []

# Mapping years to CSV columns (assumes years start from a specific column)
years = [str(year) for year in range(1995, 2018)]  # Years from 1995 to 2017

# Dictionaries to store totals by industry
emissions_totals = defaultdict(float)
intensity_totals = defaultdict(float)

# Parse the data and calculate totals for each industry
with open(input_csv_emissions, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row['Country'] == 'Malaysia':  # Filter for Malaysia only
            if row['Indicator'] == 'CO2 emissions':  # Filter for CO2 emissions
                for year in years:
                    if row[year]:
                        emissions_totals[row['Industry']] += float(row[year])
            elif row['Indicator'] == 'CO2 emissions intensities':  # Filter for CO2 emissions intensities
                for year in years:
                    if row[year]:
                        intensity_totals[row['Industry']] += float(row[year])

# Get the top 5 industries based on totals
top_5_emissions = sorted(emissions_totals.items(), key=lambda x: x[1], reverse=True)[:5]
top_5_intensity = sorted(intensity_totals.items(), key=lambda x: x[1], reverse=True)[:5]

top_5_emissions_industries = [industry for industry, _ in top_5_emissions]
top_5_intensity_industries = [industry for industry, _ in top_5_intensity]

# Parse again and only include data for the top 5 industries
with open(input_csv_emissions, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row['Country'] == 'Malaysia':  # Filter for Malaysia only
            if row['Indicator'] == 'CO2 emissions' and row['Industry'] in top_5_emissions_industries:
                for year in years:
                    if row[year]:
                        emissions_data.append({
                            'Year': year,
                            'CO2_Emissions': float(row[year]),
                            'Industry': row['Industry']
                        })
            elif row['Indicator'] == 'CO2 emissions intensities' and row['Industry'] in top_5_intensity_industries:
                for year in years:
                    if row[year]:
                        intensity_data.append({
                            'Year': year,
                            'CO2_Emissions_Intensity': float(row[year]),
                            'Industry': row['Industry']
                        })

# Write the parsed data to JSON files
with open(output_emissions_json, 'w', encoding='utf-8') as f:
    json.dump(emissions_data, f, indent=4)

with open(output_intensity_json, 'w', encoding='utf-8') as f:
    json.dump(intensity_data, f, indent=4)

print(f"Data successfully written to {output_emissions_json} and {output_intensity_json}")
