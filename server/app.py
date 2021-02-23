from flask import Flask, render_template, request, Response, jsonify
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

#create/update or delete account
@app.route('/login', methods=["GET", "POST", "DELETE", "PATCH"])
def Login():
    
#    create an account
    if request.method == 'POST':
        try:
            conn = connection()
            cursor = conn.cursor()
            parameters = request.json
            username = parameters['username']
            password = parameters['password']
            email = parameters['email']
            cursor.execute("INSERT INTO user(username, password, email) VALUES (?, ?, ?)",[username, password, email])
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
                    "You added a new login account in the database.",
                     mimetype="text/html",
                     status=201
                )
#   login to an account
    elif request.method == 'GET':
        print('GETTING A USER')
        try:
            conn = connection()
            cursor = conn.cursor()
            parameters = request.json
            print(parameters)
            username = parameters['username']
            password= parameters['password']
            cursor.execute("SELECT * FROM user WHERE username=? AND password=?", [username, password])
            result = cursor.fetchone()
            if result.username == username and result.password == password:
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
#     # Edit an account
#     elif request.method == 'PATCH':
#         try:
#             conn = connection()
#             cursor = conn.cursor()
#             new_password = request.json
#             new_email = request.json
#             userid = 3
#             cursor.execute("UPDATE user SET password=?, email=? WHERE userid=?", [new_password, new_email, userid])
#             conn.commit()
#         except mariadb.OperationalError:
#             return Response("connection problem", mariadb.OperationalError)
#         finally:
#             if (cursor != None):
#                 cursor.close()
#             if (cursor != None):
#                 conn.rollback()
#                 conn.close()
#                 return Response(
#                     "You updated your password",
#                      mimetype="text/html",
#                      status=201
#                 )    
# #   delete an account
#     elif request.method == 'DELETE':
#         try:
#             conn = connection()
#             cursor = conn.cursor()
#             userid = request.json
#             cursor.execute("DELETE FROM user WHERE userid=?", [userid])
#             conn.commit()
#         except mariadb.OperationalError:
#             return Response("connection problem", mariadb.OperationalError)
#         finally:
#             if (cursor != None):
#                 cursor.close()
#             if (cursor != None):
#                 conn.rollback()
#                 conn.close() 
#                 return Response(
#                      "You deleted your account from the database",
#                      mimetype="text/html",
#                      status=201
#                 )                
#     else:
#         return Response(
#             "There was an error!",
#             mimetype="text/html",
#             status=401
#         )     

# create, view, edit and delete a blog post
@app.route('/blog', methods=["GET", "POST", "DELETE", "PATCH"])
def blogbook():

    #view all blog posts
    if request.method == 'GET':
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM blogs")
            result = cursor.fetchall()
            user_blogs=[]
            for i in result:
                blog={
                   "blogid" : i[0], 
                    "userid": i[1],
                    "username": i[2],
                    "blog_content": i[3],
                    "created": i[4]
                }
                user_blogs.append(blog)
                print(blog)
        except mariadb.OperationalError:
            return Response("connection problem", mariadb.OperationalError)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close() 
                return Response(
                    json.dumps(user_blogs, default=str),
                    mimetype="application/json",
                    status = 200
                )
#create a blog post
    elif request.method == 'POST':
        try:
            conn = connection()
            cursor = conn.cursor()
            userid = 2
            username = "Sam"
            blog_content = "I have an event to tell you about..."
            created = "2021-02-19"
            cursor.execute("INSERT INTO blogs(userid, username, blog_content, created) VALUES (?, ?, ?, ?)",[userid, username, blog_content, created])
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
                    "You added a new blog post to the database.",
                     mimetype="text/html",
                     status=201
                )
    #update a blog post
    elif request.method == 'PATCH':
        try:
            conn = connection()
            cursor = conn.cursor()
            blog_content = "I changed my post."
            blogid=6
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
                    "You updated your blog post",
                     mimetype="text/html",
                     status=201
                )    
#delete a blog post
    elif request.method == 'DELETE':
        try:
            conn = connection()
            cursor = conn.cursor()
            blogid = 7
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


