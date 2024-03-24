from django.core import serializers
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .models import *
import datetime
from django.views import generic


# Create your views here.

class Home(View):
    def get(self, request):
        if not (request.user.is_authenticated):
            url = reverse_lazy('login')
            return HttpResponseRedirect(url)
        else:
            url = reverse_lazy('view-coupon')
            return HttpResponseRedirect(url)


def ViewStore(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            coupons = Coupon()
            store = Store.objects.all()
            context = {
                'stores': store
            }
            return render(request, 'home.html', context)
        else:
            url = reverse_lazy('login')
            return HttpResponseRedirect(url)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
            login(request, user)
            url = reverse_lazy('view-coupon')
            return HttpResponseRedirect(url)
        except Exception as e:
            messages.error(request, message='Invalid username or password')
            url = reverse_lazy('login')
            return HttpResponseRedirect(url)


class Loginview(LoginView):
    template_name = 'account/registration/login.html'
    success_url = reverse_lazy('view-coupon')


def Logoutview(request):
    logout(request)
    url = reverse_lazy('login')
    messages.info(request=request, message='Logged out successfully')
    return HttpResponseRedirect(url)


def search_results(request):
    if request.method == "POST":
        store = request.POST.get('store')
        value = int(request.POST.get('value'))
        if store == "" or value == "":
            return HttpResponse('Please fill valid store name and coupon value', status=404)
        store_org = Store.objects.get(id=int(store))
        coupons = Coupon.objects.filter(Store=store_org, Value=value, IsActive=True)
        if len(coupons) == 0:
            return HttpResponse('No coupons found', status=404)
        coupons = serializers.serialize('json', coupons)
        return JsonResponse({'coupons': coupons}, safe=True)


def coupon_checkout(request, code):
    if request.user.is_authenticated:
        if request.method == 'GET':
            coupon = Coupon.objects.get(Code=code, IsActive=True)
            if coupon.IsActive == True:
                context = {'coupon': coupon, 'i': 0}
                return render(request, 'checkout.html', context)
            else:
                url = reverse_lazy('view-coupon')
                return HttpResponseRedirect(url)
        elif request.method == 'POST':
            id = int(request.POST.get('id'))
            coupon = Coupon.objects.get(Id=id)
            used_Coupon = Coupon_used()
            Qty = request.POST.get('qty')
            if int(Qty) > coupon.Qty:
                return HttpResponse("Quantity too high! Please enter qty less than or equal to max availability.",
                                    status=404)
            if int(Qty) <= coupon.Qty and coupon.IsActive == True:
                coupon.Qty = coupon.Qty - int(Qty)
                if coupon.Qty == 0:
                    coupon.IsActive = False
                coupon.save()
                used_Coupon.Qty = int(Qty)
                used_Coupon.Name = coupon.Name
                used_Coupon.Code = coupon.Code
                used_Coupon.Value = coupon.Value
                used_Coupon.Store = coupon.Store.Name
                used_Coupon.Usedby = request.user
                used_Coupon.Useddate = datetime.datetime.now()
                used_Coupon.Amount_Taken = int(request.POST.get('amount'))
                used_Coupon.Remarks = request.POST.get('remarks')
                used_Coupon.save()
                return HttpResponse("Coupon is Activated successfully. Redirecting to Homepage in few seconds....")




    elif not (request.user.is_authenticated):
        url = reverse_lazy('login')
        return HttpResponseRedirect(url)
