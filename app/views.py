from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from app.models import *
from app.forms import *

# Create your views here.

# @login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"

    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    context ={"profiles":profiles,"projects":projects,"reviews":reviews,"message":message}

    return render(request,'index.html',context)

# @login_required(login_url='/accounts/login')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
            # messages.success(request, "Image uploaded!")
			return redirect('index')
	else:
			form = ProjectForm()
            # context= {"form":form}
	return render(request, 'project.html',{"form":form})


# @login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    project = get_object_or_404(Image, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.image = image
            reviews.user = current_user
            reviews.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {"user":current_user,"form":form})


def search_projects(request):
    # profile = Profile.get_profile()

    # if 'caption' in request.GET and request.GET["caption"]:
    if 'title' in request.GET and request.GET["title"]:

        search_term = request.GET.get("title")
        found_projects = Project.search_by_title(search_term)
        message = f"{search_term}"
        print(search_term)

        context = {"found_projects":found_projects,"message":message}

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        # context={"message":message}
        return render(request, 'search.html',{"message":message})
