import requests
import pandas as pd

url = "https://anapioficeandfire.com/api/characters?pageSize=50"

all_characters = []

while url:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for character in data:
            name = character["name"]

            if not name:
                continue

            tv_series = character["tvSeries"]
            season_count = len(tv_series)

            all_characters.append({
                "Character Name": name,
                "Season Appearances": season_count
            })
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            url = None

    else:
        print("Error fetching characters")
        break


sorted_characters = sorted(
    all_characters,
    key=lambda x: x["Season Appearances"],
    reverse=True
)


df = pd.DataFrame(sorted_characters)
df.to_excel("characters_data.xlsx", index=False)

print("Excel file created successfully!")
print(f"Total characters fetched: {len(sorted_characters)}")