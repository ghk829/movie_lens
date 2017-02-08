import pandas as pd
import sqlite3
df=pd.read_csv("C:\Users\evalue\git\My_Turing\python\movie_lens\data\item_info.csv",header=None)
df= df.ix[:,[0,1,4]]
df.columns=["item_id" , "item_title" , "url"]
con = sqlite3.connect("C:\Users\evalue\git\My_Turing\python\movie_lens\db.sqlite3")
df.to_sql("ratings_items",con=con,index=False,if_exists='append')