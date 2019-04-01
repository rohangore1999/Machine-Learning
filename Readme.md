# Amazon-on-summary-using-KNN
* Amazon Fine Food Reviews dataset you can get here: https://www.kaggle.com/snap/amazon-fine-food-reviews It is a classification problem. Model which used is K-nearest neighbors (KNN) for classification. Here we have to predict whether the given review is positive or negative (ie. score 0 (negative) or (positive) 1). Amazon_Summary_KNN.ipynb we take 50% negative review and 50% positive review and give to model.And it gives the accuracy of the predicted review. Amazon_Summary_skewed_by_KNN.ipynb we take more positive review (score(1)) than negative review (score(0)) just to check if we get better accuracy doing this. If you want to see how Bag-of-Words(BOW),TFIDF,Word-to-Vector(W2V) work check BOW-TFIDF-W2V-DUMMY.ipynb. Here is one way for cleaning, text preprocessing, exploratory data analysis (EDA) you can check EDA_Cleaning_Preprocessing.ipynb.

# Black Friday(Kaggle Competition) 
* Black Friday Dataset :- https://www.kaggle.com/mehdidag/black-friday. Here target feature is 'Purchase'. I ve perform EDA(Exploratory Data Analysis), Data Cleaning and that data give to Model to predict. And last save the best model (consider more r2 score as best model).

# Customer Segments Dataset
Our client is an online retailer based in the UK. They sell all-occasion gifts, and many of their customers are wholesalers.
Most of their customers are from the UK, but they have a small percent of customers from other countries.
They want to create groups of these international customers based on their previous purchase patterns.
Their goal is to provide more tailored services and improve the way they market to these international customers.
The retailer has hired us to help them create customer clusters, a.k.a "customer segments" through a data-driven approach.They've provided us a dataset of past purchase data at the transaction level.Our task is to build a clustering model using that dataset.Our clustering model should factor in both aggregate sales patterns and specific items purchased.
