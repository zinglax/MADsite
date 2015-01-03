# Create your views here.

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict


from models import *
from django.conf import settings
import djqscsv


site_variables = {}
site_variables["theme"] = 'a'

def get_or_none(model, **kwargs):
  # Gets object or returns none if not found
  # EX. foo = get_or_none(Member, barcode=MAD48)
  try:
    return model.objects.get(**kwargs)
  except model.DoesNotExist:
    return None


def home(request):

  # New_Member Info
  n = request.GET.get('name','')
  e = request.GET.get('email','')
  if (n != '' and e != ''):
    M = Member()
    M.name = n
    M.email = e
    M.save()

  return render_to_response("members/home.html", site_variables)

def about(request):
  return render_to_response("members/about.html", site_variables)

def apps(request):
  return render_to_response("members/apps.html", site_variables)

# New Member page, gathers email and name
def new_member(request):
  return render_to_response("members/new_member.html", site_variables)


# Members
def members(request):
  site_variables['members'] = Member.objects.all()
  return render_to_response("members/members.html", site_variables)


def export(request):
    qs = Member.objects.all()
    return djqscsv.render_to_csv_response(qs)