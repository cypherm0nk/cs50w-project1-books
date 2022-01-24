# Project 1 - Books
 
## Web Programming with Python and JavaScript

### Harvard University | EDX

- [About Project](#about-project)
- [Requirements](#requirements)
- [Project Files](#project-files)
	- [base-layout](#base_layout)
	- [index](#index)
	- [register](#register)
	- [login](#login)
	- [books](#books)
	- [book](#book)
	- [import](#import)
	- [application](#application)
-[Additional Resources](#additional-resources)

## About Project
To meet [Requirement 8](#requirement-8) This is the documentation of my project1 in which I show in detail the features of my project of book reviews website.
## Requirements
Below I will explain each of the requirements and the files that meet them.
#### Requirement 1
**Registration**: Users should be able to register for your website, providing (at minimum) a username and password.
#### Requirement 2
**Login**: Users, once registered, should be able to log in to your website with their username and password.
#### Requirement 3
**Logout**: Logged in users should be able to log out of the site.
#### Requirement 4
**Import**: Provided for you in this project is a file called `books.csv`, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN number, a title, an author, and a publication year. In a Python file called `import.py` separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running `python3 import.py` to import the books into your database, and submit this program with the rest of your project code.
#### Requirement 5
**Search**: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
#### Requirement 6
**Book Page**: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.
#### Requirement 7
**Review Submission**: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.
#### Requirement 8
**Goodreads Review Data**: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.
#### Requirement 9
**API Access**: If users make a GET request to your website’s `/api/<isbn>` route, where `<isbn>` is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format:
```
{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}

```
If the requested ISBN number isn’t in your database, your website should return a 404 error.

## Project Files

This project has 7 files that are:
- base_layout.html
- index.html
- register.html
- login.html
- books.html
- book.html
- import.py
- application.py

In the HTML files I am using the bootstrap framework. In addition, I'm using flask and Jinja2 for the templates.
###  base_layout
In this file we have the template base where I used the Bootstrap Navbar components in addition to css and javascript.
To satisfy [Requirement 3](#requirement-3), I created in Navbar a link to the logout option that appears when the user is logged in.
![Visão Desktop do website](https://i.imgur.com/iAZ8PTf.png)
### index
In this file I'm using the components jumbotron, breadcrumb,alert and form validation from the bootstrap.
Here I also have a search form that calls the search route to satisfy [Requirement 5](#requirement-5).

   ````html
<form  action="/search"  method="GET"  class="needs-validation"  novalidate>
<div  class="form-group">
<h5  class="card-title"><label  for="idsearch">Search for a book(ISBN, Title or Author): </label></h5>
<input  class="form-control"  type="text"  id="idsearch"  placeholder="Search"  aria-label="Search"  name="s"
required>
<div  class="invalid-feedback">
The search cannot be empty!
</div>
</div>
<button  type="submit"  class="btn btn-success">SEARCH</button>
</form>
   ````


![Visão Desktop do website](https://i.imgur.com/IhTPT8Q.jpg)


### register
In this file I created a registration form to satisfy the [Requirement 1](#requirement-1).
Here I validate the data entry so that the name, username and password are mandatory in addition to validating the password 2 times to confirm.
```html
<form  action="/register"  method="POST"  class="needs-validation"
oninput='password2.setCustomValidity(password2.value  !=  password.value  ? "Passwords do not match." : "")'
novalidate>
<div  class="form-group">
<label  for="textName">Name</label>
<input  type="text"  class="form-control"  name="name"  id="textName"  required>
<div  class="valid-feedback">
Looks good!
</div>
<div  class="invalid-feedback">
Please provide a name.
</div>
</div>
<div  class="form-group">
<label  for="textUsername">Username</label>
<input  type="text"  class="form-control"  name="username"  id="textUsername"  required>
<div  class="valid-feedback">
Looks good!
</div>
<div  class="invalid-feedback">
Please provide a username.
</div>
</div>
<div  class="form-group">
<label  for="textPassword">Password</label>
<input  type="password"  class="form-control"  name="password"  id="textPassword"  required>
<div  class="valid-feedback">
Looks good!
</div>
<div  class="invalid-feedback">
Please provide a password.
</div>
</div>
<div  class="form-group">
<label  for="textPassword2">Password</label>
<input  type="password"  class="form-control"  name="password2"  id="textPassword2"  required>
<div  class="valid-feedback">
Looks good!
</div>
<div  class="invalid-feedback">
Passwords do not match.
</div>
</div>
<button  type="submit"  class="btn btn-success">Create account</button>
</form>
```
![Visão Desktop do website](https://i.imgur.com/BahMEIY.png)
### login
In it I use the Navbar and Breadcrumb components of the bootstrap to meet [Requirement 2](#requirement-2).
```html
<form  action="/login"  method="POST"  class="needs-validation"  novalidate>
<div  class="form-group">
<label  for="textUsername">Username</label>
<input  type="text"  class="form-control"  name="username"  id="textUsername"  required>
<div  class="invalid-feedback">
Please provide a username
</div>
</div>
<div  class="form-group">
<label  for="textPassword">Password</label>
<input  type="password"  class="form-control"  name="password"  id="textPassword"required>
<div  class="invalid-feedback">
Please enter the password!
</div>
</div>
<button  type="submit"  class="btn btn-success my-1">Login</button>
<div  class="custom-control my-1 mr-sm-2">
<a  href="{{url_for('register')}}">Don't have an account? Register here</a>
</div>
</form>
```
![Visão Desktop do website](https://i.imgur.com/gmBgOdi.png)
### books
Here, in order to satisfy [Requirement 5](#requirement-5), I created a list that is filled with the result of the book consultation. I used the bootstrap grid system and the card component to do this.
```html
<div  class="container">
{%for  book  in  books%}
{% if  loop.first %}<div  class="row">{%endif%}
<a  href="{{url_for('book',id=book.id)}}">
<div  class="col"><div  class="card"  style="width: 18rem;">
<svg  class="card-img-top bi bi-book"  width="100px"  height="100px"  viewBox="0 0 16 16"  fill="#F2D489"  xmlns="http://www.w3.org/2000/svg">
<path  fill-rule="evenodd"  d="M3.214 1.072C4.813.752 6.916.71 8.354 2.146A.5.5 0 0 1 8.5 2.5v11a.5.5 0 0 1-.854.354c-.843-.844-2.115-1.059-3.47-.92-1.344.14-2.66.617-3.452 1.013A.5.5 0 0 1 0 13.5v-11a.5.5 0 0 1 .276-.447L.5 2.5l-.224-.447.002-.001.004-.002.013-.006a5.017 5.017 0 0 1 .22-.103 12.958 12.958 0 0 1 2.7-.869zM1 2.82v9.908c.846-.343 1.944-.672 3.074-.788 1.143-.118 2.387-.023 3.426.56V2.718c-1.063-.929-2.631-.956-4.09-.664A11.958 11.958 0 0 0 1 2.82z"/>
<path  fill-rule="evenodd"  d="M12.786 1.072C11.188.752 9.084.71 7.646 2.146A.5.5 0 0 0 7.5 2.5v11a.5.5 0 0 0 .854.354c.843-.844 2.115-1.059 3.47-.92 1.344.14 2.66.617 3.452 1.013A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.276-.447L15.5 2.5l.224-.447-.002-.001-.004-.002-.013-.006-.047-.023a12.582 12.582 0 0 0-.799-.34 12.96 12.96 0 0 0-2.073-.609zM15 2.82v9.908c-.846-.343-1.944-.672-3.074-.788-1.143-.118-2.387-.023-3.426.56V2.718c1.063-.929 2.631-.956 4.09-.664A11.956 11.956 0 0 1 15 2.82z"/>
</svg>
<div  class="card-body">
<h5  class="card-title">{{ book.title }}</h5>
<p  class="card-text">ISBN: {{ book.isbn }}</p>
</div>
<ul  class="list-group list-group-flush">
<li  class="list-group-item">Author: {{ book.author }}</li>
<li  class="list-group-item">Year: {{ book.year }}</li>
</ul>
</div></div></a>
{% if  loop.index  is  divisibleby(3) %}
</div>
<div  class="row">{% endif %}
{% if  loop.last %}</div>{% endif %}
{% endfor %}
</div>
{%endif%}
</div>
```
![Visão Desktop do website](https://i.imgur.com/d5BXHSo.png)
### book
To satisfy [Requirement 6](#requirement-6), I created this book page that displays all the data requested in the requirement.
```html
<div  class="card mt-4">
<div  class="card-body">
<h3  class="card-title">{{ book.title }}</h3>
<dl  class="row">
<dt  class="col-sm-3">ISBN:</dt>
<dd  class="col-sm-9">{{ book.isbn }}</dd>
<dt  class="col-sm-3">Author:</dt>
<dd  class="col-sm-9">{{ book.author }}</dd>
<dt  class="col-sm-3">Year:</dt>
<dd  class="col-sm-9">{{ book.year }}</dd>
<dt  class="col-sm-3">Total Ratings:</dt>
<dd  class="col-sm-9">{{ book.count_ratings }}</dd>
<dt  class="col-sm-3">Rate:</dt>
<dd  class="col-sm-9">{{'%0.2f'|format(book.total_rating|float)}}</dd>
{%if  goodreads: %}
<dt  class="col-sm-3">GoodReads Total Ratings:</dt>
<dd  class="col-sm-9">{{goodreads.ratings_count}}</dd>
<dt  class="col-sm-3">GoodReads Average Ratings:</dt>
<dd  class="col-sm-9">{{goodreads.average_rating}}</dd>
{%endif%}
</dl>
</div>
</div>
```
![Visão Desktop do website](https://i.imgur.com/WPw7zcX.png)
I also created in this file the form for submitting reviews and displaying reviews, ratings and comments to satisfy the  [Requirement 7](#requirement-7).
This is the form for submitting reviews where I use the validation to request a rate and a comment.
```html
<form  action="/review"  method="POST"  class="needs-validation"  Fnovalidate>
<div  class="form-group">
<div  class="form-group">
<label  for="exampleFormControlSelect1">My rating:</label>
<select  class="form-control"  name="myRating"  id="selectMyRating">
<option>1</option>
<option>2</option>
<option>3</option>
<option>4</option>
<option>5</option>
</select>
</div>
<label  for="textComment">Comment</label>
<textarea  type="text"  class="form-control"  name="comment"  id="textComment"  required></textarea>
<div  class="valid-feedback">
Looks good!
</div>
<div  class="invalid-feedback">
Please provide a name.
</div>
</div>
<hr>
<button  type="submit"  class="btn btn-success">Send Review</button>
</form>
```
Here the reviews that come from the bank are read in a loop using jinja2.
```html
<div  class="card card-outline-secondary my-4">
<div  class="card-header">
Book Reviews
</div>
<div  class="card-body">
{%if  reviews: %}
{% for  review  in  reviews %}
<h5  class="card-title">{{review.name}} - Rated it:{{'%0.2f'|format(review.rating|float)}}</h5>
<p>{{review.comment}}</p>
<small  class="text-muted">Posted on {{ review.datetime.strftime('%B %d, %Y %I:%M:%S') }}</small>
<hr>
{%endfor%}
{%else%}
<p>There is no review for this book yet!</p>
{%endif%}
</div>
</div>
```
![Visão Desktop do website](https://i.imgur.com/mh3XTUy.png)
I used the bootstrap grid, card, data formatting from jinja2 and form system in addition to form validation.
### import
To satisfy [Requirement 4](#requirement-4) I created this file that reads a books.csv file and inserts all the books in the database in the books_tb table.
Here I open the books.csv file, read its contents and take the connection string as a database.
```python
f = open("books.csv")
reader = csv.reader(f)
engine = create_engine(os.getenv("DATABASE_URL"))
```
In this loop I read each record in the file and insert it in the books_tb table.
```python
for isbn, title, author,year in reader:
	if isbn!="isbn":
	db = scoped_session(sessionmaker(bind=engine))
	db.execute("INSERT INTO books_tb (isbn, title, author,year) VALUES (:isbn, :title, :author,:year)",
	{"isbn": isbn, "title": title, "author": author,"year":year})
	db.commit()
	print(f"Added book isbn:{isbn}, title:{title} author: {author}, year:{year}.")
```
### application
This file contains the entire backend of the application and I will explain in detail below.
I created a constant called LOGIN_PAGE to save the "/ login" path.

```python
LOGIN_PAGE="/login"
```
Create the classes below to store the data returned from the goodread api and the data of the logged in user.
```python
class  GoodReads():
	def  __init__(self,ratings_count,average_rating):
		self.ratings_count=ratings_count
		self.average_rating=average_rating
class  Login:
	def  __init__(self,id,username,name,is_authenticated,book_id):
		self.id=id
		self.username=username
		self.name=name
		self.is_authenticated=is_authenticated
		self.book_id=book_id
```
The function below checks whether a user is logged in or not returning true if logged in or false if not.
```python
def  is_authenticated():
	if  'user'  in session:
		user=session['user']
	if user and user.is_authenticated:
		return  True
	else:
		return  False
	else:
		return  False
```
The get_good_reads_data function receives an ISBN and queries in the goodreads API satisfying the [Requirement 8](#requirement-8).
```python
def  get_good_reads_data(isbn):
	url = "https://www.goodreads.com/book/review_counts.json?key=TeqjeIg8GqVWTTlWOSl6g&isbns="+isbn.strip()
	payload = {}
	headers = {
	'Content-Type': 'application/json',
	'Cookie': 'ccsid=997-1496611-0053932; locale=en; _session_id2=7b2605e380dc5a8cae7b4d4448f14dd6'
	}
	response = requests.request("GET", url, headers=headers, data = payload)
	response=json.loads(response.text.encode('utf8'))
	reviews=response['books']
	for review in reviews:
		goodreads=GoodReads(review['ratings_count'],review['average_rating'])
	return goodreads
```
The encrypt_password function encrypts the password using the sha256 algorithm.
```python
def  encrypt_password(password):
	hash_object=hashlib.sha256(password.encode('utf-8'))
	return hash_object.hexdigest()
```
The get login function receives a username and password then consults it in the database and if it returns data it returns a Login object with the pre-filled data if it does not return the object without all the filled data.
```python
def  get_login(username, password):
	password_hash=encrypt_password(password)
	SQL=("SELECT id,name,username "
	"FROM users_tb "
	"WHERE username=:username and password=:password ")
	user=db.execute(SQL,{"username":username,"password":password_hash}).fetchone()
	if user is  None:
		return Login(id,username,"",False,0)
	else:
		return Login(user.id,user.username,user.name,True,0)
```
The route "/" checks if the user is logged in, if not, send to the login screen, if not send to the index page to search for books as per [Requirement 5](#requirement-5) .
```python
@app.route("/")
def  index():
	if  not is_authenticated():
		return redirect(LOGIN_PAGE)
	return render_template("index.html")
```
The "/ review" route receives the data from the review form and inserts it in the database as [Requirement 7](#requirement-7).
```python
@app.route("/review",methods=['POST'])
def  review():
	if  not is_authenticated():
		return redirect(LOGIN_PAGE)
	try:
		user=session['user']
		rate=request.form.get('myRating')
		comment=request.form.get('comment')
		SQL=("INSERT INTO reviews_tb(book_id, user_id, comment, rating,datetime) VALUES (:book_id, :user_id, :comment, :rating,now())")
		db.execute(SQL,{"book_id":user.bookId,"user_id":user.id,"comment":comment,"rating":rate})
		db.commit()
		flash("Review successfully posted!","success")
	except:
		flash("The user can only post one review per book.","danger")
	return redirect(url_for('book',id=user.bookId))
```
The "/ register" route receives the data from the registration form and inserts it in the users_tb table as [Requirement 1](#requirement-1).
```python
@app.route("/register",methods=['GET','POST'])
def  register():
	if is_authenticated():
		return redirect("/")
	try:
		if request.method=='GET':
		return render_template("register.html")
		elif request.method=='POST':
		name=request.form.get('name')
		username=request.form.get('username')
		password=request.form.get('password')
		password=encrypt_password(password)
		SQL=("INSERT INTO users_tb(name, username, password) VALUES (:name,:username,:password)")
		db.execute(SQL,{"name":name,"username":username,"password":password})
		db.commit()
		flash("User successfully registered!","success")
	except:
		flash("An error occurred while trying to register the user!","danger")
	return redirect("/register")
```
The "/ login" route receives the user and password and calls the function to perform the login according to the [Requirement 2](#requirement-2).
```python
@app.route("/login",methods=['GET','POST'])
def  login():
	if request.method=='GET':
		return render_template("login.html")
	elif request.method=='POST':
		username=request.form.get('username')
		password=request.form.get('password')
		user=get_login(username,password)
		session['user']=user
		if user is  None  or  not user.is_authenticated:
			flash("Sorry, the username or password you entered do not match. Please try again.","danger")
		return render_template("login.html")
	else:
		flash("Login sucess!","success")
		return redirect("/")
```
The "/ logout" route clears the user's session as per [Requirement 3](#requirement-3).
```python
@app.route("/logout")
def  logout():
	session.clear()
	flash("Logout successful!","success")
	return redirect("/")
```
The "/ search" route searches for books in the database by ISBN, Title or Author as per  [Requirement 5](#requirement-5).
```python
@app.route("/search",methods=["GET"])
def  books():
	if  not is_authenticated():
		return redirect(LOGIN_PAGE)
	# Check book id was provided
	if  not request.args.get("s"):
		flash("The search cannot be empty!","danger")
		return render_template("books.html")
	query=request.args.get("s").strip()
	query = "%" + query + "%"
	query = query.title()
	sql=("SELECT id, isbn, title, author, year FROM books_tb WHERE "
	"isbn LIKE :query OR "
	"title LIKE :query OR "
	"author LIKE :query LIMIT 15")
	books = db.execute(sql,{"query":query}).fetchall()
	if books is  None  or  len(books)==0:
		flash("No results.!","danger")
	return render_template("books.html", books=books)
```
The "/ book" route receives a book ID and fetches its data from the database as per [Requirement 6](#requirement-6)in addition it queries the ISBN in the goodreads api and returns the data as per [Requirement 8](#requirement-8).
```python
@app.route("/book/<int:id>")
def  book(id):
	if  not is_authenticated():
		return redirect(LOGIN_PAGE)
	sql=(" SELECT B.isbn, B.title, B.author, B.year,COALESCE(COUNT(RV.id),0)AS count_ratings, COALESCE(AVG(RV.rating),0) AS total_rating "
	"FROM books_tb AS B "
	"LEFT JOIN reviews_tb AS RV "
	"ON B.id=RV.book_id "
	"WHERE b.id = :query "
	"GROUP BY B.isbn, B.title, B.author, B.year")
	book = db.execute(sql,{"query":id}).fetchone()
	if  not  id  or book is  None:
		flash("Book not found!","danger")
		return render_template("book.html", book=book)
	sql=(" SELECT U.name,RV.id,book_id,RV.user_id,RV.comment,RV.rating,RV.datetime FROM reviews_tb AS RV "
	"INNER JOIN users_tb AS U "
	"ON RV.user_id=U.id "
	"WHERE RV.book_id=:query")
	reviews=db.execute(sql,{"query":id}).fetchall()
	goodreads=get_good_reads_data(book.isbn)
	session['user'].bookId=id
	return render_template("book.html", book=book,reviews=reviews,goodreads=goodreads)
```
The "/ api" route receives an ISBN and searches the database and if it finds the information it returns a JSON with the data as per the [Requirement 9](#requirement-9)
```python
@app.route("/api/<string:isbn>",methods=['GET'])
def  books_api(isbn):
	SQL=("SELECT isbn, title, author, year, "
	"COALESCE(COUNT(reviews_tb.id),0) as review_count, "
	"COALESCE(AVG(reviews_tb.rating),0) as average_score "
	"FROM books_tb "
	"LEFT JOIN reviews_tb "
	"ON books_tb.id = reviews_tb.book_id "
	"WHERE isbn = :isbn "
	"GROUP BY isbn, title, author, year ")
	book = db.execute(SQL, {"isbn": isbn.strip()}).fetchone()
	if book is  None:
		return jsonify({"error": "Invalid isbn"}), 404
	return jsonify({
	"title": book.title,
	"author": book.author,
	"isbn": book.isbn,
	"review_count": book.review_count,
	"average_score": float(book.average_score)
	})
```
To run the application use the environment variables with the data below:

$env:FLASK_APP="application.py"
$env:FLASK_DEBUG=1
$env:DATABASE_URL="postgres://ptqunjtqfzwnhr:756a10454d23f7e196c037898df7aeccfac861cdecead5249c098c7c3e8d887c@ec2-52-23-14-156.compute-1.amazonaws.com:5432/d2ra74lfga4bq6"



