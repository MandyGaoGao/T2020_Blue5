import os
from flask import send_from_directory,Flask,render_template,redirect,url_for,request,session,json,current_app as app
from flask_session import Session
app = Flask(__name__)
app.secret_key = "super secret key"





# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
def data():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, 'data', 'test_data.json')
    with open(filename) as test_file:
        data = json.load(test_file)
    #print(data["menu"]["id"])
    return data
    #return render_template('index.html', data=data)

def account_data():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, 'data', 'account.json')
    with open(filename) as test_file:
        data = json.load(test_file)
    print(data)
    return data
def msg():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, 'data', 'msg.json')
    with open(filename) as test_file:
        data = json.load(test_file)
    print(data)
    return data

def message_data():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, 'data', 'message.json')
    with open(filename) as test_file:
        data = json.load(test_file)
    print(data)
    return data
def trans_data():
    filename = os.path.join(app.static_folder, 'data', 'transaction.json')
    with open(filename) as test_file:
        data = json.load(test_file)
    return data
#######################################
@app.route("/acct_view")
def acct_view():
    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        user=session["username"]
    dic=data()[str(user)]
    t1=dic["userName"]
    t2=dic["customerId"]
    t3=dic["gender"]
    t4=dic["firstName"]
    t5=dic["lastName"]
    t6=dic["lastLogIn"]
    t7=dic["dateOfBirth"]
    t8=dic["accountId"]
    t9=dic["type"]
    t10=dic["displayName"]
    t11=dic["accountNumber"]


    return render_template("accounts-view.html",t1=t1,t2=t2,t3=t3,t4=t4,t5=t5,t6=t6,t7=t7,t8=t8,t9=t9,
            t10=t10,t11=t11,)




@app.route("/filter")
def filter():
    return render_template("filter.html")
@app.route("/trans")
def trans():
    dic=trans_data()
    return render_template("transactions-view.html",dic=dic)
@app.route("/massege-view")
def viewmsg():

    if 'username' not in session:
        return redirect(url_for("login"))
    else:
        user=session["username"]
    dic=message_data()
    d=dic["message"]
    print("\n\n\n\n\n")
    print(d[0]["type"])
    return render_template("messages-view.html",dic=d)
@app.route("/stats")
def stats():
    return render_template("stats.html" )

############################################
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
@app.route('/node_modules/<path:path>')
def send_node(path):
    return send_from_directory('node_modules', path)
#########################################
@app.route("/all_msg")
def all_msg():
    dic=message_data()
    return dic
@app.route("/msg")
def msg_detail():
    return msg()


@app.route("/all_acct")
def all_acct():
    dic=account_data()
    return dic

@app.route("/all_detail")
def result():
    dic=data()
    return render_template("result.html",result=dic)

@app.route("/detail")
def result_user():
    if 'username' not in session: 
        return redirect(url_for("login"))
    else:
        user=session["username"]
    dic=data()
    return render_template("result_user.html",result=dic[str(user)])

@app.route("/add")
def add():
    return render_template("index.html")

@app.route('/')
def index():
    #return '<html><body><h1>Hello yy</h1></body></html>'
    if "username" in session:
        username=session["username"]
        return 'Logged in as ' + username + "<br><b><a href = '/logout'>click here to log out</a></b>"
    else:
        return "You are not logged in <br><a href = '/login'></b>click here to log in</b></a>"


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form.get("nm")
        passw=request.form.get("password").encode("utf-8")
        #verify_passw = SQLservice_User.SQL_User_db().get_password(usern).encode('utf-8')
        #print(passw, verify_passw, type(verify_passw))
        #if passw == verify_passw:
        session["username"]=user
        return redirect(url_for("success",name=user))
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("index"))

@app.route("/succes/<name>")
def success(name):
    return 'log in as ' + name + "<br><b><a href = '/logout'>click here to log out</a></b>"+"<br><b><a href = '/detail'>click here to check simple acct details</a></b>"+"<br><b><a href = '/acct_view'>click here to check all acct records</a></b>"


if __name__ == '__main__':
   app.run(debug=True)                
