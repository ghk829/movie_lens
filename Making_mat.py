import pandas as pd
import sqlite3
import numpy as np
con = sqlite3.connect("./db.sqlite3")
sql = "select user_id,item_id,rating from ratings_ratings"
df=pd.read_sql(sql=sql,con=con)
user=df.ix[:,0].unique()
nuser=user.size
item=df.ix[:,1].unique()
nitem=item.size
ratings_m = pd.DataFrame(.zeros((nuser,nitem)))
for i in range(nuser):
	for j in range(nitem):
		try:
			ratings_m.ix[i,j] = df[(df.user_id==user[i])&(df.item_id==item[j])]
		except:
			ratings_m.ix[i,j] = 0

if __name__="__main__":
	id=input("Enter a id: \n")
	top