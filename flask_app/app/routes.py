from app import app
from flask import render_template
import sqlite3
from sqlite3 import Error
import json
from flask import Flask, jsonify, request, redirect, url_for 

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("Error")
        print(e)

def select_user(username):
	"""
    Query the user row in the user table
    """
	conn = create_connection("db.sqlite3")
	cur = conn.cursor()
	cur.execute("SELECT * FROM user WHERE username=?", (username,))
	
	rows = cur.fetchall()
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
	cur.close()
	conn.commit()
	conn.close()
	return r
        
def select_all_images():
    """
    Query all rows in the image table
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
    Query all rows of a user in the user_known_images table
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
    Create a association user - word into the user_known_images table
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
    Query all rows of user in the user_tried_images table
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
    Create an association user - word into the user_tried_images table
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
    Remove an association user - word from the user_tried_images table
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
    Query all untried word of a user in the user_tried_images and the user_known_images table
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
    
def add_word(word):
    """
    Create a association user - word into the user_known_images table
    """
    conn = create_connection("db.sqlite3")
    sql = ''' INSERT INTO image(image, word)
              VALUES(?,?) '''
    cur = conn.cursor()
    r=cur.execute(sql, word)
    cur.close()
    conn.commit()
    conn.close()
    return r
    
def select_image(image):
	"""
    Query the user row in the user table
    """
	conn = create_connection("db.sqlite3")
	cur = conn.cursor()
	cur.execute("SELECT * FROM image WHERE image=?", (image,))
	
	rows = cur.fetchall()
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
	cur.close()
	conn.commit()
	conn.close()
	return r
         
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
	return render_template('known_list.html', title='Known', user=user, images=query)

@app.route('/tried')
def tried_words():
	user = {'username': 'Megane'}
	query = select_tried_words_user('Megane')
	return render_template('tried_list.html', title='Tried', user=user, images=query)

@app.route('/untried')
def untried_words():
	user = {'username': 'Megane'}
	query = select_untried_words_user('Megane')
	return render_template('untried_list.html', title='Untried', user=user, images=query)
    
@app.route('/play')
def play():
	query = select_untried_words_user("Megane")
	return render_template('play.html', title='Play', images=query)

@app.route('/play_for_fun')
def play_for_fun():
	query = select_all_images()
	return render_template('practice.html', title='Play for Fun', images=query)

@app.route('/my_account')
def my_account():
	query = select_user("Megane")
	return render_template('my_account.html', title='My Account', information=query)

@app.route('/_add_image_known')
def add_image_know():
	input = request.args.get('input')
	time = request.args.get('time')
	user = {'username': 'Megane'}
	known_word = (time, 'Megane', input+".png")
	remove_from_tried('Megane', input+".png")
	add_known_word_user(known_word)
	print("added", time, input)
	return jsonify(result=input+" known")
	
@app.route('/_add_image_tried')
def add_image_tried():
    input = request.args.get('input')
    user = {'username': 'Megane'}
    tried_word = ('Megane', input+".png")
    remove_from_tried('Megane', input+".png")
    add_tried_word_user(tried_word)
    return jsonify(result=input+" tried")
    
@app.route('/restart')
def restart():
	user = {'username': 'Megane'}
	restart_words('Megane')
	return render_template('brand_new.html', user=user)

@app.route('/admin_add')
def admin_add():
	return render_template('admin_add.html')
	
@app.route('/_add')
def add():
	input_image = request.args.get('input_image')
	input_word = request.args.get('input_word')
	if (select_image(input_image)):
		result= input_word+" could not be added. The image already exists."
		return jsonify(result=result) 
	else:
		word = (input_image, input_word)
		print(add_word(word))
		result= input_word +" has been added."
		return jsonify(result=result)
		
    
    