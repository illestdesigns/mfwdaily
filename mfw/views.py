from django.shortcuts import render_to_response
from datetime import *
from mfw.models import MFW, MFWLink

import sys
# Create your views here.

from django import forms

from gmapi import maps
from gmapi.forms.widgets import GoogleMap


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':500, 'height':300}))


def index(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(38, -97),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    context = {'form': MapForm(initial={'map': gmap})}
    return render_to_response('index.html', context)

def home(request):
	
	gmap = maps.Map(opts = {
        'center': maps.LatLng(38.873198, -77.007438),
        #'mapTypeId': maps.MapTypeId.ROADMAP,
        'mapTypeId': maps.MapTypeId.HYBRID,
        'zoom': 16,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
	#return render_to_response('index.html', context)

 	content = {
		'title' : 'title here',
		'body' : 'body here',
	}

	#entries = Coins.objects.all() #first 10 posts [10] would be 10th or [5:10] 5-10
	#print >>sys.stderr, 'Coins ====='
	#print >>sys.stderr, entries

	#latest = Coins.objects.get_most_recent_coins()
	#current_mfw = MFW.objects.all()[:1]
	#current_mfw = MFW.objects.all().order_by('-id')
	current_mfw = MFW.objects.filter(active = True).order_by('-mfw_date').values() #checks for object from today

	#cursor.execute("""
	#    SELECT *
	#	FROM mfw_mfw where """)
	#result_list = cursor.fetchall()
	links = []
	this_mfw = []
	all_links = []

	if current_mfw: #if there is an object from today
		print >> sys.stderr, current_mfw
		print >> sys.stderr, current_mfw[0]
		print >> sys.stderr, current_mfw[0]['id']
		#print >> sys.stderr, datetime.today()
		print >> sys.stderr, datetime.today().date()
		this_mfw = current_mfw[0]

		#mfw_links = MFWLink.objects.filter(mfw_object_id = current_mfw[0]['id']).values()
		
		for mfw_item in current_mfw:
			mfw_links = MFWLink.objects.filter(mfw_object_id = mfw_item['id']).values()
			all_links.append(mfw_links)

		if mfw_links:
			print >> sys.stderr, 'LINKS===='
			print >> sys.stderr, mfw_links
			links = mfw_links

		if all_links:
			print >> sys.stderr, 'ALL LINKS===='
			print >> sys.stderr, all_links

	#current_links = MFWLinks.
	#test = current_mfw.mfwlink_set.all()
	#print >> sys.stderr, test

	return render_to_response('index.html', {'varsIn':{'MFW' : this_mfw , 'MFWLink' : all_links, 'MFWList' : current_mfw, 'form' : MapForm(initial={'map': gmap}) }})

	#return render_to_response('index.html')
	#return render_to_response('index.html', content)