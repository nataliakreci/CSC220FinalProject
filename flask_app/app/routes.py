from app import app
from flask import render_template
import sqlite3
from sqlite3 import Error
import json
from flask import Flask, jsonify, request, redirect, url_for 
from app.forms import LoginForm, RegistrationForm
from flask import flash
from .models import User
from flask_login import current_user, login_user
from flask_login import login_required, logout_user
from app import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from functools import wraps

admin = Admin(app, name='clickclacktype', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("Error")
        print(e)
        
def select_all_images():
    """
    Query all rows in the image table
    """
    conn = create_connection("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM image")
 
    rows = cur.fetchall()
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
    cur.close()
    conn.commit()
    conn.close()
    return r

def select_one_hand(hand):
    """
    Query all words in the table hands, according to the hand. 4 for left and 5 for right
    """
    conn = create_connection("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hands where num= ?", (hand,))
 
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
    conn = create_connection("app.db")
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
    conn = create_connection("app.db")
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
    conn = create_connection("app.db")
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
    conn = create_connection("app.db")
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
    conn = create_connection("app.db")
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
    conn = create_connection("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM image EXCEPT SELECT image.image, word, num FROM image, (SELECT image, username FROM user_tried_images WHERE username=? UNION SELECT image, username FROM user_known_images WHERE username=?) as seen WHERE image.image= seen.image", (username,username))
    rows = cur.fetchall()
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
    cur.close()
    conn.commit()
    conn.close()
    return r

def select_untried_words_level_user(username, level):
    """
    Query all untried word of a user in the user_tried_images and the user_known_images table at a specific level
    """
    conn = create_connection("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM image WHERE image.num=? EXCEPT SELECT image.image, word, num FROM image, (SELECT image, username FROM user_tried_images WHERE username=? UNION SELECT image, username FROM user_known_images WHERE username=?) as seen WHERE image.image= seen.image;", (level, username,username))
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
    conn = create_connection("app.db")
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
    Create an association user - word into the user_known_images table
    """
    conn = create_connection("app.db")
    sql = ''' INSERT INTO image(image, word, num)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    r=cur.execute(sql, word)
    cur.close()
    conn.commit()
    conn.close()
    return r
    
def select_image(image):
	"""
    Select a specific image
    """
	conn = create_connection("app.db")
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
	return render_template('index.html', title='Home')

@app.route('/images')
def images():
	query = select_all_images()
	return render_template('word_list.html', title='Images', images=query)

@app.route('/known')
@login_required
def known_words():
	query = select_known_words_user(current_user.username)
	return render_template('known_list.html', title='Known', images=query)

@app.route('/tried')
@login_required
def tried_words():
	query = select_tried_words_user(current_user.username)
	return render_template('tried_list.html', title='Tried', images=query)

@app.route('/untried')
@login_required
def untried_words():
	if current_user.is_authenticated:
		user = {'username': current_user.username}
	else:
		user = {'username': 'User'}
	query = select_untried_words_user(current_user.username)
	return render_template('untried_list.html', title='Untried', user=user, images=query)
    
@app.route('/play')
def play():
	query = select_untried_words_user(current_user.username)
	return render_template('play.html', title='Play', images=query, level='all')

@app.route('/play_easy')
@login_required
def play_easy():
	query = select_untried_words_level_user(current_user.username, 1)
	return render_template('play.html', title='Play Easy', images=query, level='easy')
	
@app.route('/play_medium')
@login_required
def play_medium():
	query = select_untried_words_level_user(current_user.username, 2)
	return render_template('play.html', title='Play Medium', images=query, level='medium')
	
@app.route('/play_hard')
@login_required
def play_hard():
	query = select_untried_words_level_user(current_user.username, 3)
	return render_template('play.html', title='Play Hard', images=query, level='hard')

@app.route('/play_for_fun')
def play_for_fun():
	query = select_all_images()
	return render_template('practice.html', title='Play for Fun', images=query, image=1, mode="all")

@app.route('/practice_left')
def practice_left():
	query = select_one_hand(4)
	return render_template('practice.html', title='Play for Fun', images=query, image=0, mode="left")
	
@app.route('/practice_right')
def practice_right():
	query = select_one_hand(5)
	return render_template('practice.html', title='Play for Fun', images=query, image=0, mode="right")

@app.route('/my_account')
@login_required
def my_account():
	return render_template('my_account.html', title='My Account')

@app.route('/_add_image_known')
@login_required
def add_image_know():
	input = request.args.get('input')
	time = request.args.get('time')
	known_word = (time, current_user.username, input+".png")
	remove_from_tried(current_user.username, input+".png")
	add_known_word_user(known_word)
	return jsonify(result=input+" known")
	
@app.route('/_add_image_tried')
@login_required
def add_image_tried():
    input = request.args.get('input')
    user = {'username': current_user.username}
    tried_word = (current_user.username, input+".png")
    remove_from_tried(current_user.username, input+".png")
    add_tried_word_user(tried_word)
    return jsonify(result=input+" tried")
    
@app.route('/restart')
@login_required
def restart():
	restart_words(current_user.username)
	return render_template('brand_new.html', title='Restarted')


# Wrapper to authorize admin only
def admin_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.admin == 0:
        	logout_user()
        	return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/admin_add')
@login_required
@admin_access
def admin_add():
	return render_template('admin_add.html')

@app.route('/_add')
@login_required
@admin_access
def add():
	input_image = request.args.get('input_image')
	input_word = request.args.get('input_word')
	if (select_image(input_image)):
		result= input_word+" could not be added. The image already exists."
		return jsonify(result=result) 
	else:
		word = (input_image, input_word, 1)
		print(add_word(word))
		result= input_word +" has been added."
		return jsonify(result=result)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('my_account'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))   
    
@app.route('/change_password')
@login_required
def change_password():
    return render_template('password_change.html') 

@app.route('/_password_changed')
@login_required
def password_changed():
	user= current_user
	input_password = request.args.get('password')
	user.set_password(input_password)
	db.session.commit()
	return jsonify(result="Your password has been changed.")     
     

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)