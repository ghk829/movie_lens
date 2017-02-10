import pandas as pd
import sqlite3
import numpy as np
import sys
i=input("Enter a number: first_user_id \n")
j=input("Enter a number: second_user_id \n")
def sim_function(i,j):
	return np.exp(-sum([pow(int(df[(df.user_id==user[i])&(df.item_id==item)].rating)-int(df[(df.user_id==user[j])&(df.item_id==item)].rating),2)
	for item in df[df.user_id==user[i]].ix[:,1].values if item in df[df.user_id==user[j]].ix[:,1].values]))
if __name__=="__main__":
	con = sqlite3.connect("./db.sqlite3")
	sql = "select user_id,item_id,rating from ratings_ratings"
	df=pd.read_sql(sql=sql,con=con)
	user=df.ix[:,0].unique()
	nuser=user.size
	item=df.ix[:,1].unique()
	nitem=item.size
	ratings_m = pd.DataFrame(np.zeros((nuser,nitem)))
	print sim_function(i,j)