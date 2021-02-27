from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json
import dbcreds
import mariadb
import sys


app = Flask(__name__)
CORS(app)

def connection():
    return mariadb.connect(
        user = dbcreds.user,
        password = dbcreds.password,
        host = dbcreds.host,
        port = dbcreds.port,
        database = dbcreds.database   
    )


@app.route('/login', methods=["POST", "GET"])
def login():
#   login to an account
    result = None
    if request.method == 'POST':
        conn = None
        cursor = None
        parameters = request.get_json()
        print(parameters)
        username = parameters["username"]
        password = parameters["password"]
        print('Logging in')
        try:
            print("inside try")
            conn = connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("INSERT INTO user(username, password) VALUES(?, ?)", [username, password])
            conn.commit()
            result = cursor.fetchone()
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close() 
                return Response(
                    "Logged In"
                    mimetype="application/json",
                    status = 200
                )
#get the userid of the current user
    if request.method == 'GET':
        conn = None
        cursor = None
        # result = ""
        parameters = request.get_json()
        username = parameters['username']
        password= parameters['password']
        try:
            print("inside try")
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username=? AND password=?", [username, password])
            result = cursor.fetchall()
            print(result)
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close() 
                return Response(
                    json.dumps(result, default=str),
                    mimetype="application/json",
                    status = 200
                )
    else:
        return Response(
            "There was an error!",
            mimetype="text/html",
            status=401
        )

#    create an account
@app.route('/account', methods=["POST"])
def signup():
    if request.method == 'POST':
        conn = None
        cursor = None
        result = None
        parameters = request.get_json()
        print(parameters)
        username = parameters['username']
        password = parameters['password']
        email = parameters['email']
        try:
            conn = connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("INSERT INTO user(username, password, email) VALUES (?, ?, ?)",[username, password, email])
            conn.commit()
            result = cursor.rowcount
            print(result)
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)
        finally:
            if (cursor != None):
                cursor.close()
            if (conn != None):
                conn.rollback()
                conn.close()  
                return Response(
                    "You added a new login account in the database.",
                    mimetype="text/html",
                    status=201
                )
    else:
        return Response(
            "There was an error!",
            mimetype="text/html",
            status=401
        )

# create, view, edit and delete a blog post
@app.route('/blog', methods=["GET", "POST", "DELETE", "PATCH"])
def blogbook():

    #view all blog posts
    if request.method == 'GET':
        conn = None
        cursor = None

        try:
            conn = connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM blogs")
            result = cursor.fetchall()
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close() 
                return Response(
                    json.dumps(result, default=str),
                    mimetype="application/json",
                    status = 200
                )
            else:
                return Response(
                    "something went wrong",
                    mimetype="text/html",
                    status=500
                )
#create a blog post
    elif request.method == 'POST':
        conn = None
        cursor = None
        result = None
        parameters = request.get_json()
        userid = parameters["userid"]
        username = parameters["username"]
        blog_content = parameters["blog_content"]
 
        try:
            conn = connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("INSERT INTO blogs(userid, username, blog_content) VALUES (?, ?, ?)",[userid, username, blog_content])
            conn.commit()
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)
        finally:
            if (cursor != None):
                cursor.close()
            if (conn != None):
                conn.rollback()
                conn.close()  
                return Response(
                    json.dumps(result, default=str),
                    "You added a new blog post to the database.",
                    mimetype="text/html",
                    status=201
                )
    #update a blog post
    elif request.method == 'PATCH':
        conn = None
        cursor = None
        result = None
        parameters = request.get_json()
        blogid = parameters['blogid']
        blog_content = parameters['blog_content']
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE blogs SET blog_content=? WHERE blogid=?", [blog_content, blogid])
            conn.commit()
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)
        finally:
            if (cursor != None):
                cursor.close()
            if (cursor != None):
                conn.rollback()
                conn.close()
                return Response(
                    json.dumps(result, default=str),
                    "You updated your blog post",
                    mimetype="text/html",
                    status=201
                )    
#delete a blog post
    elif request.method == 'DELETE':
        conn = None
        cursor = None
        result = None
        parameters = request.get_json()
        blogid = parameters['blogid']
        try:
            conn = connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("DELETE FROM blogs WHERE blogid=?", [blogid])
            conn.commit()
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)
        finally:
            if (cursor != None):
                cursor.close()
            if (cursor != None):
                conn.rollback()
                conn.close() 
                return Response(
                    json.dumps(result, default=str),
                     "You deleted your blog post from the database",
                    mimetype="text/html",
                    status=201
                )                
    else:
        return Response(
            "There was an error!",
            mimetype="text/html",
            status=401
        )     


