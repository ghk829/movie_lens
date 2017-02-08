import pandas as pd
import sqlite3
df=pd.read_csv("C:\Users\evalue\git\My_Turing\python\movie_lens\data\u.data",sep='\t',header=None)
df.columns=["user_id" , "item_id" , "rating" , "timestamp"]
con = sqlite3.connect("C:\Users\evalue\git\My_Turing\python\movie_lens\db.sqlite3")
df.to_sql("ratings_ratings",con=con,index=False,if_exists='append')