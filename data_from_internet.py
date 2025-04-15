import requests
from bs4 import BeautifulSoup
import json
import os

url = 'https://en.wikipedia.org/wiki/ASEAN'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table')

urban_table = None

for t in tables:
    if 'Core city' in t.text:
        urban_table = t
        break


rows = urban_table.find_all('tr')
headers = [h.get_text(strip=True) for h in rows[0].find_all(["th", "td"])]

core_city_idx = headers.index("Core city")
country_idx = headers.index("Country")
population_idx = headers.index("Population")
area_idx = 3

countries_dictionary = {}

for r in rows[1:]:
    cols = r.find_all(["th", "td"])

    city_name = cols[core_city_idx].get_text(strip=True)
    country_name = cols[country_idx].get_text(strip=True)
    pop = int(cols[population_idx].get_text(strip=True).replace(',', ''))
    area = float(cols[area_idx].get_text(strip=True).replace(',', ''))

    pop_density = round(pop / area, 2)

    data = {
        'Core city': city_name,
        'Population': pop,
        'Area': area,
        'Population density': pop_density,
    }

    if country_name not in countries_dictionary:
        countries_dictionary[country_name] = []

    countries_dictionary[country_name].append(data)

for key, value in countries_dictionary.items():
    total_area = 0
    total_population = 0

    for v in value:
        total_area += v['Area']
        total_population += v['Population']

    pop_dens = total_population / total_area

    new_data = {}
    new_data['Population density'] = round(pop_dens, 2)
    value.append(new_data)


print(json.dumps(countries_dictionary, indent=2))


file_path = "countries_info.json"
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
else:
    existing_data = {}


if countries_dictionary != existing_data:
    # Save the dictionary to a JSON file only if there is new or updated data
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(countries_dictionary, f, indent=2, ensure_ascii=False)



