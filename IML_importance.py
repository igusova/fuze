import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=241)
data = pandas.read_csv("Python_Code/titanic.csv", index_col='PassengerId')
b = data[['Pclass','Age','Sex','Fare','Survived']]
b=b.replace('male',1)
b=b.replace('female',0)
b = b.dropna()
y=b['Survived'].values
b = b[['Pclass','Age','Sex','Fare']]
x = b.values
clf =clf.fit(x, y)
importances = clf.feature_importances_
