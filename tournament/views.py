from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
from django.contrib.auth.decorators import login_required
import simplejson

from models import *


def index(request):
    return render(request, 'home.html', {'tab' : 'arena'})

@login_required
def scoreboard(request):
    bots = Bot.objects.all().order_by('-points')
    challengues = Challengue.objects.filter(requested_by=request.user, played=False)
    if challengues.count() > 0:
        pending_challengues = True
    else:
        pending_challengues = False
    return render(request, 'scoreboard.html', { 'tab' : 'score',
                'bots' : bots,
                'pending_challengues' : pending_challengues})

@login_required
def upload(request):
    try:
        # get the bot for this guy
        bot = Bot.objects.get(owner=request.user)
    except ObjectDoesNotExist:
        print "creating first bot for user"
        bot = Bot()
        bot.owner = request.user
        bot.code = open('tournament/base_bot.py', 'r').read()
        bot.save()
    return render(request, 'upload.html', 
        {'tab' : 'upload',
         'bot' : bot})

def about(request):
    return render(request, 'about.html', {'tab' : 'about'})

@login_required
@csrf_exempt
@require_POST
def update_bot(request):
    if request.is_ajax():
        try:        
            bot = Bot.objects.get(owner=request.user)
            print "data: ", simplejson.loads(request.body)
        except ObjectDoesNotExist:
            print "creating first bot for user"
            bot = Bot()
            bot.owner = request.user
        bot.code = simplejson.loads(request.body)['code']
        bot.save()
    return HttpResponse('/about')
