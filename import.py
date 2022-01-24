import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

f = open("books.csv")
reader = csv.reader(f)
engine = create_engine(os.getenv("DATABASE_URL"))

for isbn, title, author,year in reader: 
    if isbn!="isbn":       
        db = scoped_session(sessionmaker(bind=engine))
        db.execute("INSERT INTO books_tb (isbn, title, author,year) VALUES (:isbn, :title, :author,:year)",
        {"isbn": isbn, "title": title, "author": author,"year":year})
        db.commit()
        print(f"Added book isbn:{isbn}, title:{title} author: {author}, year:{year}.")