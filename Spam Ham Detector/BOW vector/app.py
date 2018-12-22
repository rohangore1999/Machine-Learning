from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
	df=pd.read_csv("spam.csv")
	df_data=df[["v2","score"]]
	
	#Feature & labels
	df_x=df_data['v2']
	df_y=df_data.score

	#extract feature with Countvectorizer
	corpus=df_x
	cv=CountVectorizer(binary=False)
	X = cv.fit_transform(corpus)
	# cv=CountVectorizer()
	# X=cv.fit_transform(corpus) #fit the data

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test=train_test_split(X, df_y, test_size=0.33, random_state=42)

	#naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB
	clf=MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)

	if request.method == 'POST':
		mail=request.form['mail']
		data=[mail]
		vect= cv.transform(data).toarray()
		my_prediction= clf.predict(vect)
	return render_template("result.html",prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)