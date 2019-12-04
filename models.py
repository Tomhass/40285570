from flask import Flask, render_template
import sqlite3 as sql

def insertUser(username, password, email):
	try:
		render_template('/home.html')
		con = sql.connect("users.db")
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS users(userID INTEGER PRIMARY KEY, username VARCHAR(20), password VARCHAR(20), email VARCHAR(30))")
		cur.execute("SELECT username FROM users WHERE (username = ?) OR (email = ?)", (username,email))
		existing = cur.fetchone()

		if(existing):
			return render_template('/home.html')
		else:
			cur.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username, password, email))
			return render_template('/login.html')

		con.commit()
		con.close()
	except:
		render_template('/home.html')




