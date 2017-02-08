import pandas as pd
import sqlite3
df=pd.read_csv("C:\Users\evalue\git\My_Turing\python\movie_lens\data\u.user",sep='|',header=None)
df.columns=["user_id" , "age" , "gender" , "occupation","zip_code"]
con = sqlite3.connect("C:\Users\evalue\git\My_Turing\python\movie_lens\db.sqlite3")
df.to_sql("ratings_users",con=con,index=False,if_exists='append')