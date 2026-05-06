import requests
import pandas as pd

url = "https://anapioficeandfire.com/api/books"

response = requests.get(url)

if response.status_code == 200:
    books = response.json()

    book_dict = {}

    for book in books:
        name = book["name"]
        pages = book["numberOfPages"]
        release_date = book["released"]
        isbn = book["isbn"]
        publisher = book["publisher"]

        book_dict[name] = [pages, release_date, isbn, publisher]

    print(book_dict)

    # Convert dictionary to DataFrame
    df = pd.DataFrame.from_dict(
        book_dict,
        orient='index',
        columns=["Pages", "Release Date", "ISBN", "Publisher"]
    )

    df.index.name = "Book Name"

    # Save CSV
    df.to_csv("books_data.csv")

    print("CSV file created successfully!")

else:
    print("Error fetching books")