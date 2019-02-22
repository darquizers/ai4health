
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


class MLEngine:

    def modelTraining(self):
        # Reading the data set into engine.
        path = 'C:\\Hack the thrown\\FinalSolution\\ai4health\\CanSolV2-master\\raw-data\\bc-data.csv'
        data = pd.read_csv(path)
        df = data.copy()
        #df.head()
        #df.nunique()
        #df.info()
        #df['diagnosis'].value_counts()
        #df.describe()
        #df_columns = list(df.columns)
        #df_columns

        # Data cleaning ( removing null , duplicates etc.)
        X = df.iloc[:, 2:-1].values
        Y = df.iloc[:, 1].values

        # Converting strings to binary for algo fitment
        labelencoder_Y = LabelEncoder()
        Y = labelencoder_Y.fit_transform(Y)

        #Spliting the data set into test data and training the data( 25% - 75%) model
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)


        #plotting where the raw data stands without data analytics
        plt.plot(X_train,'ro')
        plt.plot(Y_train,'g^')
        plt.title('cansol-trained-model-AS-IS')
        plt.grid()
        plt.savefig('cansol-trained-model-as-is.png')


        #Transforming training data models ()75%  to scale
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        #Applying the algorithm to prediction of "False +ve and False -ve"
        classifier = LogisticRegression(random_state = 0,solver='liblinear')
        classifier.fit(X_train, Y_train)
        y_pred = classifier.predict(X_test)
        score = classifier.score(X_test, Y_test)
        cm = metrics.confusion_matrix(y_pred,Y_test)
        plt.figure(figsize=(9,9))

        #plotting binary classification of Raw-data based on our trained model
        plt.plot(y_pred,'g^')
        plt.title('1= +ve Cancer-malignant; 0=-Ve Cancer-benign')
        plt.grid()
        #plt.show()
        plt.savefig('cansol-classi-prediction.png')

        #seaborn is used to plot the confusion matrix
        sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
        plt.ylabel('Actual label');
        plt.xlabel('Predicted label');
        all_sample_title = 'Malignant-Benign Accu Score(%): {0}'.format(score)
        plt.title(all_sample_title, size = 15);
        plt.savefig('cansol-confusion-matrix.png')


#a=MLEngine()
#a.modelTraining()



