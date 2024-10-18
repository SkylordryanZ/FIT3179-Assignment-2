import csv
import json
from collections import defaultdict
from statistics import mean

# Input and output file paths
input_csv = 'rawData/GlobalLandTemperaturesByCity.csv'  
output_json = 'data/global_land_temperatures_by_city_malaysia.json'

# Dictionary of predefined city coordinates in Malaysia
city_coordinates = {
    'Alor Setar': {'Latitude': 6.1248, 'Longitude': 100.3673},
    'Kuala Lumpur': {'Latitude': 3.1390, 'Longitude': 101.6869},
    'George Town': {'Latitude': 5.4141, 'Longitude': 100.3288},
    'Johor Bahru': {'Latitude': 1.4927, 'Longitude': 103.7414},
    'Ipoh': {'Latitude': 4.5975, 'Longitude': 101.0901},
    'Kota Kinabalu': {'Latitude': 5.9804, 'Longitude': 116.0735},
    'Kuching': {'Latitude': 1.5533, 'Longitude': 110.3592},
    'Malacca': {'Latitude': 2.1896, 'Longitude': 102.2501},
    'Shah Alam': {'Latitude': 3.0738, 'Longitude': 101.5183},
    'Petaling Jaya': {'Latitude': 3.1073, 'Longitude': 101.6067},
    'Subang Jaya': {'Latitude': 3.0436, 'Longitude': 101.5805},
    'Seremban': {'Latitude': 2.7297, 'Longitude': 101.9381},
    'Miri': {'Latitude': 4.3999, 'Longitude': 113.9914},
    'Sibu': {'Latitude': 2.2877, 'Longitude': 111.8250},
    'Sandakan': {'Latitude': 5.8456, 'Longitude': 118.0570},
    'Tawau': {'Latitude': 4.2444, 'Longitude': 117.8916},
    'Putrajaya': {'Latitude': 2.9264, 'Longitude': 101.6964},
    'Langkawi': {'Latitude': 6.3628, 'Longitude': 99.8106},
    'Kuantan': {'Latitude': 3.8140, 'Longitude': 103.3390},
    'Kangar': {'Latitude': 6.4338, 'Longitude': 100.1987},
    'Labuan': {'Latitude': 5.2831, 'Longitude': 115.2309},
    'Bintulu': {'Latitude': 3.1664, 'Longitude': 113.0364},
    'Kuala Terengganu': {'Latitude': 5.3302, 'Longitude': 103.1408},
    'Temerloh': {'Latitude': 3.4556, 'Longitude': 102.4206},
    'Bentong': {'Latitude': 3.5187, 'Longitude': 101.9116},
    'Bukit Mertajam': {'Latitude': 5.3630, 'Longitude': 100.4667},
    'Kota Bharu': {'Latitude': 6.1254, 'Longitude': 102.2383},
    'Muar': {'Latitude': 2.0442, 'Longitude': 102.5689},
    'Raub': {'Latitude': 3.7928, 'Longitude': 101.8575},
    'Genting Highlands': {'Latitude': 3.4224, 'Longitude': 101.7927},
    'Klang': {'Latitude': 3.0449, 'Longitude': 101.4493},
    'Nilai': {'Latitude': 2.8132, 'Longitude': 101.7977},
    'Port Dickson': {'Latitude': 2.5220, 'Longitude': 101.7958},
    'Taiping': {'Latitude': 4.8549, 'Longitude': 100.7407},
    'Teluk Intan': {'Latitude': 4.0257, 'Longitude': 101.0213},
    'Dungun': {'Latitude': 4.7562, 'Longitude': 103.3959},
    'Tumpat': {'Latitude': 6.1962, 'Longitude': 102.1700},
    'Jitra': {'Latitude': 6.2685, 'Longitude': 100.4224},
    'Pasir Mas': {'Latitude': 6.0498, 'Longitude': 102.1397},
    'Kluang': {'Latitude': 2.0304, 'Longitude': 103.3179},
    'Segamat': {'Latitude': 2.5148, 'Longitude': 102.8158},
    'Batu Pahat': {'Latitude': 1.8548, 'Longitude': 102.9333},
    'Sungai Petani': {'Latitude': 5.6470, 'Longitude': 100.4870},
    'Alor Gajah': {'Latitude': 2.3805, 'Longitude': 102.2060},
    'Bukit Kayu Hitam': {'Latitude': 6.6406, 'Longitude': 100.4295},
    'Arau': {'Latitude': 6.4216, 'Longitude': 100.2756},
    'Gua Musang': {'Latitude': 4.8843, 'Longitude': 101.9682},
    'Tanah Merah': {'Latitude': 5.8052, 'Longitude': 102.1465},
    'Pontian': {'Latitude': 1.4867, 'Longitude': 103.3907},
    'Ulu Tiram': {'Latitude': 1.6034, 'Longitude': 103.8226},
    'Rawang': {'Latitude': 3.3219, 'Longitude': 101.5764},
    'Lumut': {'Latitude': 4.2304, 'Longitude': 100.6293},
    'Pekan': {'Latitude': 3.4939, 'Longitude': 103.3896},
    'Papua': {'Latitude': 2.8932, 'Longitude': 101.8743}
}


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

            if city in city_coordinates:  # Only process cities with known coordinates
                if temp is not None:
                    city_temperatures[city][date].append(temp)

# Prepare data for JSON output
output_data = []

for city, dates in city_temperatures.items():
    coordinates = city_coordinates[city]  # Get the city's coordinates
    for date, temps in dates.items():
        avg_temp = mean(temps)  # Calculate average temperature for each date
        output_data.append({
            'City': city,
            'Date': date,
            'AverageTemperature': avg_temp,
            'Latitude': coordinates['Latitude'],   # Add latitude
            'Longitude': coordinates['Longitude']  # Add longitude
        })

# Write the aggregated data to a JSON file
with open(output_json, mode='w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Aggregated temperature data by city in Malaysia with coordinates has been written to {output_json}")
