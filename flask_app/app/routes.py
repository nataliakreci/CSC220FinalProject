from app import app
from flask import render_template
import sqlite3
from sqlite3 import Error
import json

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established")
        print("This is the version of your database: "+sqlite3.version)
        return conn
    except Error as e:
        print("Error")
        print(e)
        
def select_all_images():
    """
    Query all rows in the image table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM image")
 
    rows = cur.fetchall()
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
    cur.close()
    conn.commit()
    conn.close()
    return r
    
def select_known_words_user(username):
    """
    Query all rows in the user table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT word, record, image.image FROM user_known_images, image WHERE image.image= user_known_images.image AND username=?", (username,))
    rows = cur.fetchall()
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
    cur.close()
    conn.commit()
    conn.close()
    return r
    
def add_known_word_user(user_word):
    """
    Create a new project into the user table
    :param conn:
    :param project:
    :return: project id
    """
    conn = create_connection("db.sqlite3")
    sql = ''' INSERT INTO user_known_images(record, username,image)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user_word)
    cur.close()
    conn.commit()
    conn.close()
        
def select_tried_words_user(username):
    """
    Query all rows in the user table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT image.image, word FROM image, user_tried_images WHERE image.image=user_tried_images.image AND username=?", (username,))
 
    rows = cur.fetchall()
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
    cur.close()
    conn.commit()
    conn.close()
    return r
    
def add_tried_word_user(user_word):
    """
    Create a new project into the user table
    :param conn:
    :param project:
    :return: project id
    """
    conn = create_connection("db.sqlite3")
    sql = ''' INSERT INTO user_tried_images(username,image)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user_word)
    cur.close()
    conn.commit()
    conn.close()
    
def remove_from_tried(user, word):
    """
    Create a new project into the user table
    :param conn:
    :param project:
    :return: project id
    """
    conn = create_connection("db.sqlite3")
    sql = 'DELETE FROM user_tried_images WHERE username=? AND image=?'
    cur = conn.cursor()
    cur.execute(sql, (user, word,))
    cur.close()
    conn.commit()
    conn.close()


def select_untried_words_user(username):
    """
    Query all rows in the user table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM image EXCEPT SELECT image.image, word FROM image, (SELECT image, username FROM user_tried_images WHERE username=? UNION SELECT image, username FROM user_known_images WHERE username=?) as seen WHERE image.image= seen.image", (username,username))
    rows = cur.fetchall()
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
    cur.close()
    conn.commit()
    conn.close()
    return r    

def restart_words(username):
    """
    Delete all progress
    :param conn:
    :param username:
    """
    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute('DELETE FROM user_known_images WHERE username="Megane"')
    cur.close()
    conn.commit()
    cur = conn.cursor()
    cur.execute('DELETE FROM user_tried_images WHERE username="Megane"')
    cur.close()
    conn.commit()
    conn.close()
    

from flask import Flask, render_template, redirect, url_for          
@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Megane'}
	query = select_all_images()
	return render_template('index.html', title='Home', user=user, images=query)

@app.route('/known')
def known_words():
	user = {'username': 'Megane'}
	query = select_known_words_user('Megane')
	return render_template('known.html', title='Known', user=user, images=query)

@app.route('/tried')
def tried_words():
	user = {'username': 'Megane'}
	query = select_tried_words_user('Megane')
	return render_template('tried.html', title='Tried', user=user, images=query)

@app.route('/untried')
def untried_words():
	user = {'username': 'Megane'}
	query = select_untried_words_user('Megane')
	return render_template('untried.html', title='Untried', user=user, images=query)
    
@app.route('/play')
def play():
	query = select_untried_words_user("Megane")
	return render_template('play.html', title='Play', images=query)

@app.route('/play_for_fun')
def play_for_fun():
	query = select_all_images()
	return render_template('play_for_fun.html', title='Play for Fun', images=query)

@app.route('/know/<image>/<time>')
def know(image, time):
	user = {'username': 'Megane'}
	known_word = (time, 'Megane', image+".png")
	remove_from_tried('Megane', image+".png")
	add_known_word_user(known_word)
	return render_template('know.html', user=user, image=image, time=time)
 
@app.route('/try/<image>')
def tryy(image):
	user = {'username': 'Megane'}
	known_word = ('Megane', image+".png")
	remove_from_tried('Megane', image+".png")
	add_tried_word_user(known_word)
	return render_template('try.html', user=user, image=image)
   
@app.route('/restart')
def restart():
	user = {'username': 'Megane'}
	restart_words('Megane')
	return render_template('brand_new.html', user=user)
    
    