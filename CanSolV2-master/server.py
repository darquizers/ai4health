import os
try:
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
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server
# Start of  ML engine -----

  def modelTraining(self):
      path = 'C:\\Hack the thrown\\FinalSolution\\ai4health\\CanSolV2-master\\bc-data.csv'
      data = pd.read_csv(path)
      df = data.copy()
      # df.head()
      # df.nunique()
      # df.info()
      # df['diagnosis'].value_counts()
      # df.describe()
      # df_columns = list(df.columns)
      # df_columns
      X = df.iloc[:, 2:-1].values
      Y = df.iloc[:, 1].values
      labelencoder_Y = LabelEncoder()
      Y = labelencoder_Y.fit_transform(Y)
      X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
      sc = StandardScaler()
      X_train = sc.fit_transform(X_train)
      X_test = sc.transform(X_test)
      classifier = LogisticRegression(random_state=0, solver='liblinear')
      classifier.fit(X_train, Y_train)
      y_pred = classifier.predict(X_test)
      score = classifier.score(X_test, Y_test)
      cm = metrics.confusion_matrix(y_pred, Y_test)
      plt.figure(figsize=(9, 9))
      sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
      plt.ylabel('Actual label')
      plt.xlabel('Predicted label')
      all_sample_title = 'Accuracy Score: {0}'.format(score)
      plt.title(all_sample_title, size=15)
      plt.savefig('toy_Digits_ConfusionSeabornCodementor.png')



# End of ML engine -----------






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

