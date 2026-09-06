import requests
from datetime import datetime, timedelta

API_KEY = "get_your_api_bruh"

years_back = int(input("Years in the past to check: "))
years_forward = int(input("Years in the future to check: "))
search_name = input("Asteroid name: ").lower()

today = datetime.now().date()
start_date = today - timedelta(days=years_back * 365)
end_date = today + timedelta(days=years_forward * 365)

print(f"\nSearching between {start_date} and {end_date} ...\n")

url = f"https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={API_KEY}"
response = requests.get(url)
if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    exit()

data = response.json()
neos = data["near_earth_objects"]
 
found = False

SAFE_DISTANCE_KM = 7_500_000

for neo in neos:
    if search_name in neo["name"]:
        found = True
        print("Asteroid Found")

        for approach in neo["close_approach_data"]:
            date_str = approach["close_approach_date"]
            approach_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if start_date <= approach_date <= end_date:
                distance_km = float(approach["miss_distance"]["kilometers"])
                status = "SAFE" if distance_km >= SAFE_DISTANCE_KM else "UNSAFE"

                print("\n--- Approach Event ---")
                print("Date:", approach["close_approach_date_full"])
                print("Miss distance (km):", distance_km)
                print("Speed (km/h):", approach["relative_velocity"]["kilometers_per_hour"])
                print("Status:", status)

        break

if not found:
    print(" Asteroid not found.")

