import pymysql
import getpass
import os
import hashlib
from  random import randint
import time

from flask import Flask, session

#PUSSY DON'T STEAL MY CODE GIMME CREDIT "MED MORTADHA"

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = pymysql.connect(host="bzmccpy2hojlgxphx4mz-mysql.services.clever-cloud.com", user="umjxvz1raf0yrnar", password="qW4gHdtuatg5NJkprX93", db="bzmccpy2hojlgxphx4mz")

cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), dangers INT DEFAULT 0, password VARCHAR(255))"
cursor.execute(sql)

def register():
    email = input("Enter your email: ")
    password = getpass.getpass("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    sql = "INSERT INTO users (email, dangers, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, (email, 0, hashed_password))
    db.commit()
    print("Registration successful!")

def login():
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    sql = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(sql, (email, hashed_password))
    result = cursor.fetchone()
    if result:
        session['user_email'] = email
        user_email = session.get('user_email')
        print("Login successful!")
        f = 0
        while True:
            new_f = randint(10,1000)
            print(new_f)
            if new_f != f:
                f = new_f
                dangers = f
                update_database(user_email, dangers)
                time.sleep(10)
    else:
        print("Invalid email or password.")


def update_database(user_email, dangers):
    sql = "UPDATE users SET dangers = %s WHERE email = %s"
    cursor.execute(sql, (dangers, user_email))
    db.commit()
    print("Database updated successfully.")

def main():
   login()

if __name__ == "__main__":
    main()
