import sys
import itertools
from math import sqrt
from operator import add
from os.path import join, isfile, dirname
from pyspark import SparkConf, SparkContext
from pyspark.mllib.recommendation import ALS
from pyspark.mllib.recommendation import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Users,Items,Ratings,Recommend

# Create your views here.

syntax = '''
select a.item_id,item_title, round(avg(rating),1) as rating 
from ratings_ratings a 
join ratings_items b on a.item_id=b.item_id  
group by a.item_id'''


def item_list(request):
    item_list = Items.objects.raw(syntax)[:20]
    context = {'item_list':item_list}
    return render(request, 'ratings/item_list.html', context)
syntax2 = '''
select b.id, url, item_title,rating
from ratings_items a 
join ratings_recommend b on a.item_id=b.item_id where b.user_id=196'''	
def recommend_list(request):
	recommend_list = Recommend.objects.raw(syntax2)[:20]
	context = {'recommend_list':recommend_list}
	return render(request, 'ratings/recommend_list.html', context)