from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Profile,Project,User,Review
from .forms import ProfileForm,ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def home(request): 
    posts=Project.objects.all()
    if request.method == 'POST':
        form= ProjectForm(request.POST,request.FILES)
        rate = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form=ProjectForm()
    return render(request,"home.html",{"posts":posts, "form":form})


def profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.filter(user = request.user) 
    posts = Project.objects.filter(author__id=id)[::-1]
    p_form= ProfileForm()
    return render(request, "profile.html", context={"user":user,
                                                             "profile":profile,
                                                             "posts":posts,"p_form":p_form})
    


def review_form(request):
    current_user=request.user
    if request.method =="POST":
        rate = ReviewForm(request.POST)
        if rate.is_valid():
            review=rate.save(commit=False)
            review.author=current_user
            review.save()
            
            return redirect('home')
    else:
        rate = ReviewForm()
    return render(request,"home.html",{"rate":rate,"current_user":current_user})
    

def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_articles = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})