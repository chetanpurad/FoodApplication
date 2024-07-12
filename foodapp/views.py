from django.http import HttpResponse
from django.shortcuts import redirect, render

from foodapp.models import *
from foodapp.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    reg_list=Details.objects.all()
    context={
        'reg_list':reg_list,
    }
    return render(request,'home.html',context)

# def register(request):
#     form=UserCreationForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('register.html')

#     return render(request,'register.html')

# def register(request):
#     if  request.method == 'POST':
#         username=request.POST.get( "username" )
#         email=request.POST.get( "email" )
#         phone=request.POST.get("phone")

#         register=Details(username=username,email=email,phone=phone)
#         register.save()
#     return render(request,'register.html')

# def add_item(request):
#     if request.method=='POST':
#         item_name=request.POST.get( "item_name" )
#         item_desc=request.POST.get("item_desc")
#         item_price=request.POST.get("item_price")
#         item_image=request.POST.get("item_image")
#         addItem = Items(item_name=item_name,item_desc=item_desc,item_price=item_price,item_image=item_image)
#         addItem.save()
#     return render(request,'add_items.html')

def add_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foodapp:items')
    return render(request,'add_items.html',{'form':form})

@login_required
def item_list(request):
    item_list=Items.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,"items.html",context)
        
def detail_item(request,item_id):
    item_detail=Items.objects.get(pk=item_id)
    context={
        'item_detail':item_detail,      
    }
    return render(request,"buy_item.html",context)

       
def update_item(request,id):
    item=Items.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('foodapp:add_items')
    return render(request,'add_items.html',{"form":form})  

def  delete_item(request,id):
    item=Items.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('foodapp:items')
    
    return render(request,'delete_msg.html',{"item":item})
    
