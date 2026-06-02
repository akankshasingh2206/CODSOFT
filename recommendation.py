import pandas as pd
from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
today = datetime.now().strftime("%d-%m-%Y")

books = pd.read_csv("books.csv")

books["features"] = (
    books["genre"] + " " +
    books["author"] + " " +
    books["rating"].astype(str)
)

vectorizer = CountVectorizer()

feature_matrix = vectorizer.fit_transform(
    books["features"]
)

similarity = cosine_similarity(feature_matrix)
def output_area():
    output_area.insert(
    END,
    "📚 Welcome to Book Buddy!\n\n"
)

def recommend_books():

    result.delete("1.0", END)

    book_name = book_input.get()

    try:

        index = books[
            books["title"].str.lower()
            == book_name.lower()
        ].index[0]

        scores = list(
            enumerate(similarity[index])
        )

        scores = sorted(
            scores,
            key=lambda x: x[1],
            reverse=True
        )

        result.insert(
            END,
            "Recommended Books:\n\n"
        )

        for book in scores[1:6]:

            row = books.iloc[book[0]]

            result.insert(
                END,
                f"Title: {row['title']}\n"
            )

            result.insert(
                END,
                f"Author: {row['author']}\n"
            )

            result.insert(
                END,
                f"Rating: {row['rating']}\n\n"
            )

    except:
        result.insert(
            END,
            "Book not found!"
        )

root = Tk()

root.title(
    "Book Recommendation System"
)

root.geometry("750x650")
root.configure(bg="#1e1e1e")

heading = Label(
    root,
    text=f"Book Recommendation System\nDate: {today}",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
heading.pack(pady=12)

label = Label(
    root,
    text="Enter Book Name:"
)

label.pack()

book_input = Entry(
    root,
    width=45
)

book_input.pack(pady=12)

button = Button(
    root,
    text="Recommend",
    command=recommend_books
)

button.pack(pady=10)

result = Text(
    root,
    height=18,
    width=67,bg="#2d2d2d",fg="white"
)

result.pack(pady=12)

root.mainloop()