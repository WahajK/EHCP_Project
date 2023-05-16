from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import asyncio
from aiocoap import *
from datetime import datetime
from flask_wtf import FlaskForm, RecaptchaField
import subprocess
import mysql.connector

views = Blueprint('views', __name__)

class CaptchaForm(FlaskForm):
    recaptcha = RecaptchaField()

@views.route('/', methods=['GET', 'POST'])
def home():
    form = CaptchaForm()
    fp = open("Logs/Logs.txt","a")
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    mac_address = subprocess.check_output(["arp", "-a", request.remote_addr]).decode()
    print(mac_address)
    if request.method == 'POST':
        if not form.validate():
            flash(f"Invalid Recaptcha",category="error")
            return render_template("login.html", form=form)
        username = request.form.get("username")
        password = request.form.get("password")
        fp.write("Time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        fp.write("\nLogin attempt from: "+request.remote_addr+"\n")
        fp.write("\nXFF IP of Connection : "+client_ip+"\n")
        fp.write(f"Username: {username}" + "\nPassword: " + password + "\n")
        ret = run_query(username,password)
        if ret == []:
            fp.write("Login Failed\n")
            fp.write("-----------------------------------------------\n")
            flash(f"Incorrect Username or Password",category="error")
            return render_template("login.html", form=form)
        else:
            session['messages'] = ret
            fp.write("Login Successful\n")
            fp.write("-----------------------------------------------\n")
            return redirect(url_for('views.login_home'))
    else:
        fp.write("Time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        fp.write("\nConnection Established from: "+request.remote_addr+"\n")
        fp.write("\nXFF IP of Connection : "+client_ip+"\n")
        fp.write("\nMAC Address of connection: "+mac_address+"\n")
        fp.write("-----------------------------------------------\n")
        return render_template("login.html", form=form)

@views.route('/login')
def login_home():
    response = session['messages']
    print(response)
    session.clear()
    return render_template("home.html",user = response[0][0])

def run_query(username,password):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="webapp",
        auth_plugin='auth_socket',
    )
    
    cursor = cnx.cursor()

    query = "SELECT * FROM user where id = '{}' and password = '{}'".format(username,password)
    cursor.execute(query)

    rows = cursor.fetchall()

    # Clean up
    cursor.close()
    cnx.close()

    return rows
    