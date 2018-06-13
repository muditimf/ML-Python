#!usr/bin/python3

from sklearn import tree

#score-result of student
# 0 means fail and 1 means pass

data=[[0,0],[35,0],[36,1],[100,1]]
output=["fail","fail","pass","pass"]

#decision tree call
algo=tree.DecisionTreeClassifier()

#trained data
trained_al=algo.fit(data,output)

#testing phase
predict=trained_al.predict([[86,1]])

#print output
print(predict)
