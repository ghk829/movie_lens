from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Users,Items,Ratings
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