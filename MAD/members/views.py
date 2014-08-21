# Create your views here.

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict


from models import *
from django.conf import settings


def home(request):
  return render_to_response("members/home.html", {})

def about(request):
  return render_to_response("members/about.html", {})

def apps(request):
  return render_to_response("members/apps.html", {})