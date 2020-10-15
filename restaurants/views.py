from django.http import HttpResponse
from django.shortcuts import render_to_response, render
import datetime

def hello(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def here(request):
	
    return HttpResponse('Mom, I am here! ')
	
def add(request, a, b):
	s = int(a) + int(b)
	return HttpResponse(str(s))
	
def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	html = '<html>sum={s}<br>dif={d}<br> \
		          pro={p}<br>quo={q}</html>'.format(s=s, d=d, p=p, q=q)
	return HttpResponse(html)
	
def menu(request):
	food = { 'name':'Fried egg with tomato', 'price':60, 'comment':'Excellent', 'is_spicy':False }
	return render_to_response('menu.html', locals())
	
def menu1(request):
	food1 = { 'name':'Fried egg with tomato', 'price':60, 'comment':'Excellent food', 'is_spicy':False }
	food2 = { 'name':'Garlic Pork', 'price':100, 'comment':'High Recommend', 'is_spicy':True }
	foods = [ food1, food2 ]
	return render_to_response('menu1.html', locals())
	
