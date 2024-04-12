#importing flask
from flask import Flask, render_template, request, redirect 
import sqlite3

app = Flask(__name__)


@app.route("/") 
def home():
    
    db = sqlite3.connect('testblog.db') 
    cursor = db.cursor()
    dbposts = cursor.execute('SELECT * FROM posts').fetchall()
    print(dbposts[0])
    return render_template("home.html", posts=dbposts)


@app.route("/addposts")
def addposts():
    return render_template("createposts.html")




@app.route("/posts", methods=["POST"])
def posts():
    
    title =request.form["title"]
    body = request.form["body"]
    
    print(title)
    print(body)
    
    if len(title) > 0 and len(body) > 0:
        sql_insert_code = f'INSERT INTO posts VALUES(NULL,"{title}","{body}")'
        print(sql_insert_code)
        db = sqlite3.connect('testblog.db') 
        cursor = db.cursor()
        dbposts = cursor.executescript(sql_insert_code)
        db.commit()
        return "Great Job, post submitted"
    else:
        return redirect("/addposts")



@app.route("/posts/<post_id>")
def getpost(post_id):
    db = sqlite3.connect('testblog.db') 
    cursor = db.cursor()
    dbposts = cursor.execute(f'SELECT * FROM posts WHERE id = {post_id}').fetchone()
    print(post_id)
    print(dbposts)
    return render_template("showposts.html", title=dbposts[1], body=dbposts[2])
