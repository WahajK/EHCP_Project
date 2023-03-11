from flask import Blueprint, render_template, request, flash, redirect, url_for, session
import asyncio
from aiocoap import *
from datetime import datetime
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    fp = open("Logs/Logs.txt","a")
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        flag = "0"
        fp.write("Time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        fp.write("\nLogin attempt from: "+request.remote_addr+"\n")
        fp.write(f"Username: {username}" + "\nPassword: " + password + "\n")
        if "'" in username or '"' in username:
            flag = "1"
            fp.write("\nSQL Injection Detected\n")
        ret = asyncio.run(coap_get(username,password,flag))
        if ret == b'[]':
            if flag == "1":
                fp.write("SQL Injection Failed\n")
            else:
                fp.write("Login Failed\n")
            fp.write("-----------------------------------------------\n")
            flash("Incorrect Username or Password",category="error")
            return render_template("login.html")
        else:
            responses = ret.decode("utf-8").replace("[","").replace("]","").replace("(","").replace(")","").replace(" ","").replace("'","").split(",")
            session['messages'] = responses
            if flag == "1":
                fp.write("SQL Injection Successful\n")
            else:
                fp.write("Login Successful\n")
            fp.write("-----------------------------------------------\n")
            return redirect(url_for('views.login_home'))
    else:
        fp.write("Time: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        fp.write("\nConnection Established from: "+request.remote_addr+"\n")
        fp.write("-----------------------------------------------\n")
        return render_template("login.html")

@views.route('/login')
def login_home():
    response = session['messages']
    print(response)
    session.clear()
    return render_template("home.html",username = response[0], dev_name = response[2], battery = response[3], status = response[4], calories = response[5], step_walked = response[6], heart_rate = response[7], exercise_time = response[8], miles_run = response[9], age = response[10], bp = response[11])

async def coap_get(username,password,flag):
    protocol = await Context.create_client_context()
    request = Message(
        code=GET,
        uri='coap://127.0.0.1/SQL_Data',
        payload=f"{username}+{password}+{flag}".encode("utf8"),
    )

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        return response.payload
    