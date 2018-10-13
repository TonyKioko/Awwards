from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validationq
        if form.is_valid():
            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration.html', {'form': form})

@login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"

    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    context ={"profiles":profiles,"projects":projects,"reviews":reviews,"message":message}

    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    # comments = Comments.objects.all()
    users = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()

    try :
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)


    projects = Project.get_profile_pic(profile.id)
    return render(request, 'registration/profile.html', {'title':title,'profile':profile,"projects":projects, 'profile_details':profile_details,"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    title="Edit"
    profile = User.objects.get(username=request.user)
    try :
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = ProfileForm()

    return render(request, 'registration/update_profile.html', {'form':form, 'profile_details':profile_details})

@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login/')
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
