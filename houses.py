import requests

url = "https://anapioficeandfire.com/api/houses?pageSize=50"

all_houses = []

while url:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for house in data:
            house_name = house["name"]
            region = house["region"]

            if house_name:   # avoid empty names
                all_houses.append((house_name, region))

        # Pagination handling
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            url = None
    else:
        print("Error fetching data")
        break

# Sort alphabetically by house name
all_houses.sort(key=lambda x: x[0])

# Write to text file
with open("houses_list.txt", "w", encoding="utf-8") as file:
    for house, region in all_houses:
        file.write(f"{house} - {region}\n")

print("House list created successfully!")
print(f"Total houses fetched: {len(all_houses)}")