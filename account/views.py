# djangotemplates/example/views.py
from django.conf import settings

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView # Import TemplateView

from account.models import Customer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.backends import ModelBackend
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


# from django.contrib.auth import  auth_login
from django.core.urlresolvers import reverse
import json




# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"


@csrf_exempt
# @login_required
def index(request):
    print request
    if request.method == 'GET':
        print '--------'
        return render(request, 'balance.html')


@csrf_exempt
def regist(request):
    if request.method == 'GET':
        print 'come here'
        # return render_to_response('regist.html',
        #                           {'message': "\'\'"})
        return render(request, 'regist.html')
    if request.method == 'POST':
        try:
            username = str(request.POST.get('user'))
            password = str(request.POST.get('password'))
            repassword = str(request.POST.get('repassword'))
            email = str(request.POST.get('email'))
        except Exception:
            # return render_to_response('regist.html',
            #                           {'message': "Input error."})

            return HttpResponse(json.dumps({'message': "Input error."}), content_type="application/json")

        if len(User.objects.filter(email=email)) > 0:
            # return render_to_response('regist.html',
            #                           {'message': "Email exists."})
            return HttpResponse(json.dumps({'message': "Email exists."}), content_type="application/json")

        address = 'address'
        print username
        print password
        print repassword
        print email
        if repassword != password:
            # return render_to_response('regist.html',
            #                           {'message': "Passwords do not match."})
            return HttpResponse(json.dumps({'message': "Passwords do not match."}), content_type="application/json")

        user_obj = User.objects.create_user(username=username, password=password, email=email)
        # user_obj = User.objects.create(username=username, password=password, email=email, eth_addr=address)
        # user_obj.save()
        user_obj.save()
        # return HttpResponseRedirect("/login/")
        return HttpResponse(json.dumps({'message': "success"}), content_type="application/json")

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        try:
            email = str(request.POST.get('email'))
            password = str(request.POST.get('password'))
            print email
            user = User.objects.get(email=email)
            customer = Customer.objects.get(user_id=user.id)
        except Exception:
            HttpResponse(json.dumps({'message': "User not exist."}), content_type="application/json")
            # return render_to_response('login.html',
            #                           {'message': "User not exist."})

        # auth_user = authenticate(username=user.username, password=password)
        # print auth_user
        if user.check_password(password):
            # print auth_user
            print user
            print user.id
            # print request.user
            # try:
            #     auth_login(request, auth_user)
            # except Exception, e:
            #     print str(e)
            print request.user
            # print 'login success'
            # return HttpResponseRedirect('index')
            return HttpResponse(json.dumps({'message': "success",
                                            'user_id': user.id,
                                            'username': user.username,
                                            'email': user.email,
                                            'eth_addr': customer.eth_addr,
                                            'rpcport': customer.rpcport}),
                                content_type="application/json")
        else:
            # return render_to_response('login.html',
            #                           {'message': "Wrong password."})
            return HttpResponse(json.dumps({'message': "Wrong password."}), content_type="application/json")

