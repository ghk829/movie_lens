import pandas as pd
import sqlite3
import numpy as np
from scipy.stats import pearsonr
def sim_function1(i,j):
	return np.exp(-sum([pow(int(df[(df.user_id==user[i])&(df.item_id==item)].rating)-int(df[(df.user_id==user[j])&(df.item_id==item)].rating),2)
	for item in df[df.user_id==user[i]].ix[:,1].values if item in df[df.user_id==user[j]].ix[:,1].values]))
def sim_function2(i,j):
	vec1=[int(df[(df.user_id==user[i])&(df.item_id==item)].rating)
	for item in df[df.user_id==user[i]].ix[:,1].values if item in df[df.user_id==user[j]].ix[:,1].values]
	vec2=[int(df[(df.user_id==user[j])&(df.item_id==item)].rating)
	for item in df[df.user_id==user[i]].ix[:,1].values if item in df[df.user_id==user[j]].ix[:,1].values]
	return pearsonr(vec1,vec2)[0]
con = sqlite3.connect("./db.sqlite3")
sql = "select user_id,item_id,rating from ratings_ratings"
df=pd.read_sql(sql=sql,con=con)
user=df.ix[:,0].unique()
nuser=user.size
item=df.ix[:,1].unique()
nitem=item.size
def topMatches(id,n=5,similarity=sim_function1):
	scores = [(similarity(id,j-1),j-1) for j in user  if (j-1)!=id]
	scores.sort()
	scores.reverse()
	return scores[0:n]
	

if __name__="__main__":
	id=input("Enter a id: \n")
	top