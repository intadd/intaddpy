# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from .models import cafeinfo

def cafe(request):
	cafes=cafeinfo.objects.filter()
	return render(request,'cafe/cafemain.html',{'cafes':cafes})



# Create your views here.
