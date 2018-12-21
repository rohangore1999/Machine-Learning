Amazon Fine Food Reviews dataset you can get here: https://www.kaggle.com/snap/amazon-fine-food-reviews
It is a classification problem.
Model which used is K-nearest neighbors (KNN) for classification.
Here we have to predict whether the given review is positive or negative (ie. score 0 (negative) or (positive) 1).
Amazon_Summary_KNN.ipynb we take 50% negative review and 50% positive review and give to model.And it gives the accuracy of the predicted review.
Amazon_Summary_skewed_by_KNN.ipynb we take more positive review (score(1)) than negative review (score(0)) just to check if we get better accuracy doing this. 
If you want to see how Bag-of-Words(BOW),TFIDF,Word-to-Vector(W2V) work check BOW-TFIDF-W2V-DUMMY.ipynb.
Here is one way for cleaning, text preprocessing, exploratory data analysis (EDA) you can check EDA_Cleaning_Preprocessing.ipynb
