import os
try:
  import engine
  import view
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
  import pandas as pd
  import numpy as np
  from sklearn.preprocessing import LabelEncoder, OneHotEncoder
  import matplotlib.pyplot as plt
  from sklearn.preprocessing import LabelEncoder
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler
  import seaborn as sns
  from sklearn import metrics
  from sklearn.linear_model import LogisticRegression
  #-----------------------------UI--------------

  from flask_wtf import Form
  from wtforms import TextField
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

class MainProgram:
  #calling MLEngine instance
  obj=engine.MLEngine()
  obj.modelTraining()
  vObj=view.UI()
  vObj.invoke()


# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8005))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

