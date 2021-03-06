from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponse
from .forms import ProfileForm,ImageForm,CommentsForm
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required(login_url='/accounts/login/')
def home(request):
    image = Image.objects.all()
    profile = Profile.objects.all()

    return render(request,'welcome.html', {"profile":profile,"image":image})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect('welcome')

    else:
        form = ProfileForm()
    return render(request,'profile.html', {"form": form})        

@login_required(login_url='/accounts/login/')
def images(request,image_id):
    image = Image.objects.get(id = image_id)
    
    return render(request,"picture.html", {"image":image})

#   return redirect('Welcome')    

@login_required(login_url='/accounts/login/')
def profil(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get()
    images = Image.objects.filter(user = user).all()
    form=ProfileForm()
    return render(request,"all-images/profil.html",{"profile":profile,"user":user,"images":image,"form":form})

@login_required(login_url='/accounts/login/')
def description(request,image_id):
    image = Image.objects.get(id = image_id)
    comments = Comments.objects.filter(image = image.id).all() 
    return render(request,'description.html',{"image":image,"comments":comments})


def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

            return redirect('welcome')

    else:
        form = ImageForm()
    return render(request, 'picture.html', {"form": form})

def comments(request):
    current_user=request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user = current_user
            comment.save()

        return redirect('welcome')
    else:
        form= CommentsForm()
    return render(request,'comment.html',{"form":form})



