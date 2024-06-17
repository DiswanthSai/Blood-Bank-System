from flask import Flask,session,redirect
from functools import wraps
import pymongo
app=Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
client=pymongo.MongoClient('localhost',27017)
db=client.sodabbs
mydb=client.hospitals
mydb2=client.req
mydb3=client.comm_req
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap