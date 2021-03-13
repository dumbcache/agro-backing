from flask import Flask,render_template,url_for,request,jsonify,redirect,flash
import json
from db_connect import connect
from db_user import user_details
from panda_data import data
from db_farmer_search import send_details,farmer_info
from sms import sendSms
from login_verify import login_verify
from db_get import after_register
from analysis import analysis


app=Flask(__name__)
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT']=1
app.secret_key=b'd5d7cd4eb3af4fd2490e33f585a9bf0171e3a35d4fbd027f'

""" creating different routes for different webpages """
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def aboutus():
    return render_template('aboutus.html')

@app.route('/farmerinfo',methods=['POST','GET'])
def farmerinfo():
    username=request.form['username']
    print(username)
    result=farmer_info(username)
    result[0][4]=result[0][4].title()
    print(result)
    stat1,stat2,stat3,stat41,stat42=analysis(result)
    print(stat1,stat2,stat3,stat41,stat42)
    return render_template('farmerinfo.html',result=result,stat1=stat1,stat2=stat2,stat3=stat3,stat41=stat41,stat42=stat42)

@app.route('/farmersearch',methods=['POST','GET'])
def farmersearch():
    print(request.form)
    result=send_details(request.form)
    return render_template('farmerlist.html',result=result)
    

@app.route('/services',methods=['POST','GET'])
def services():
    with open('datasets/dat.json','r') as f:
        datalist=json.load(f)
    dist=list(datalist.keys()) 
    # with open('datasets/crops.json','r') as g:
    #     crops=json.load(g)
    crop=data()
    crops=crop['crop'].unique()
    return render_template('farmersearch.html',datalist=datalist,districts=dist,crops=list(crops))

@app.route('/registersubmit',methods=['POST'])
def registersubmit():
    c=request.form
    # if "" not in dict(c).values():
    print(c)
    username=user_details(dict(c))
    # username='gopi@46400'
    conn=connect()
    details=after_register(conn,username)
    flash(details,'success')
    return redirect(url_for('register'))

@app.route('/contact')
def contactus():
    return render_template('contactus.html')


@app.route('/register',methods=['GET'])
def register():
    with open('datasets/dat.json','r') as f:
        datalist=json.load(f)
    dist=list(datalist.keys())  
    with open("datasets/arable.json") as f:
        crops=json.load(f)
    print(type(crops))
    values=list(crops.values())
    crops1=values[0]+values[1]+values[2]+values[3]
    return render_template('register.html',datalist=datalist,districts=dist,crop=crops,crops1=crops1)


@app.route('/arable',methods=['GET','POST'])
def arable():
    with open('datasets/arable.json') as f:
        crops=json.load(f)
    return render_template('arable.html',datalist=crops)

@app.route('/view')
def viewProfile():
    return render_template('login.html')

@app.route('/notify',methods=['GET','POST'])
def notify():
    data=request.form
    sendSms(dict(data))
    return jsonify({"msg":"your response is sent"})

@app.route('/login_verify',methods=['GET','POST'])
def verify():
    data=request.form
    print(data)
    result=login_verify(dict(data))
    print(result)
    if result==False:
        return jsonify({"msg":"invalid details"})
    else:
        return render_template('hello.html',result=result)

""" main app calling """
if __name__=="__main__":
    app.run(debug=True)