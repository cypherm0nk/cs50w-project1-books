import os,requests,json,hashlib
from flask import Flask, session, render_template, jsonify, request,redirect,flash,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
LOGIN_PAGE="/login"
app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

class GoodReads():
    def __init__(self,ratings_count,average_rating):
        self.ratings_count=ratings_count
        self.average_rating=average_rating

class Login:
    def __init__(self,id,username,name,is_authenticated,book_id):
        self.id=id
        self.username=username
        self.name=name
        self.is_authenticated=is_authenticated
        self.book_id=book_id


# FUNCTIONS
def is_authenticated():
    if 'user' in session:
        user=session['user']
        if user and user.is_authenticated:
            return True
        else:
            return False
    else:
        return False

def get_good_reads_data(isbn):
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

def encrypt_password(password):
    hash_object=hashlib.sha256(password.encode('utf-8'))
    return hash_object.hexdigest()

def get_login(username, password):
        password_hash=encrypt_password(password)
        SQL=("SELECT id,name,username "
                "FROM users_tb "
                "WHERE username=:username and password=:password ")
        user=db.execute(SQL,{"username":username,"password":password_hash}).fetchone()
        if user is None:
            return   Login(id,username,"",False,0)
        else:
            return Login(user.id,user.username,user.name,True,0)


@app.route("/")
def index():
    if not is_authenticated():
        return redirect(LOGIN_PAGE)

    return render_template("index.html")

@app.route("/review",methods=['POST'])
def review():
    if not is_authenticated():
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

@app.route("/register",methods=['GET','POST'])
def register():
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

@app.route("/login",methods=['GET','POST'])
def login():

    if request.method=='GET':
        return render_template("login.html")
    elif request.method=='POST':        
        username=request.form.get('username')
        password=request.form.get('password')
        user=get_login(username,password)
        session['user']=user
        if user is None or not user.is_authenticated:
            flash("Sorry, the username or password you entered do not match. Please try again.","danger")
            return render_template("login.html")
        else:
            flash("Login sucess!","success")
            return redirect("/")


@app.route("/api/<string:isbn>",methods=['GET'])
def books_api(isbn):
    SQL=("SELECT isbn, title, author, year, "
                        "COALESCE(COUNT(reviews_tb.id),0) as review_count, "
                        "COALESCE(AVG(reviews_tb.rating),0) as average_score "
                        "FROM books_tb "
                        "LEFT JOIN reviews_tb "
                        "ON books_tb.id = reviews_tb.book_id "
                        "WHERE isbn = :isbn "
                        "GROUP BY isbn, title, author, year ")
    book = db.execute(SQL, {"isbn": isbn.strip()}).fetchone()
    if book is None:
        return jsonify({"error": "Invalid isbn"}), 404
        
    return jsonify({
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "review_count": book.review_count,
            "average_score": float(book.average_score)
        })
        
@app.route("/logout")
def logout():
    session.clear()
    flash("Logout successful!","success")
    return redirect("/")
    
@app.route("/search",methods=["GET"])
def books():
    if not is_authenticated():
        return redirect(LOGIN_PAGE)
    # Check book id was provided
    if not request.args.get("s"):
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
    if books is None or len(books)==0:
        flash("No results.!","danger")
    return render_template("books.html", books=books)

@app.route("/book/<int:id>")
def book(id):
    if not is_authenticated():
        return redirect(LOGIN_PAGE)
    
    sql=(" SELECT B.isbn, B.title, B.author, B.year,COALESCE(COUNT(RV.id),0)AS count_ratings, COALESCE(AVG(RV.rating),0) AS total_rating " 
                        "FROM books_tb AS B "
                        "LEFT JOIN reviews_tb AS RV "
                        "ON B.id=RV.book_id "
                        "WHERE b.id = :query "
                        "GROUP BY B.isbn, B.title, B.author, B.year")
    book = db.execute(sql,{"query":id}).fetchone()
    if not id or book is None:
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