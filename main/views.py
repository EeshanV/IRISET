from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import generic

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

#Home

def directorMessage(request):
    template = loader.get_template('home/directorMessage.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('home/about.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def management(request):
    template = loader.get_template('home/management.html')
    return HttpResponse(template.render())

def management_gazetted(request):
    template = loader.get_template('home/management/gazetted.html')
    return HttpResponse(template.render())

def management_ngSignal(request):
    template = loader.get_template('home/management/ngSignal.html')
    return HttpResponse(template.render())

def management_ngTelecom(request):
    template = loader.get_template('home/management/ngTelecom.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def department(request):
    template = loader.get_template('home/department.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def department_signal(request):
    template = loader.get_template('home/department/signal.html')
    return HttpResponse(template.render())

def department_signal_block(request):
    template = loader.get_template('home/department/signal/block_signalling_laboratory.html')
    return HttpResponse(template.render())

def department_signal_electrical(request):
    template = loader.get_template('home/department/signal/electrical_signalling_laboratory.html')
    return HttpResponse(template.render())

def department_signal_kavach(request):
    template = loader.get_template('home/department/signal/kavach_lab.html')
    return HttpResponse(template.render())

def department_signal_outdoor(request):
    template = loader.get_template('home/department/signal/outdoor_signalling_laboratory.html')
    return HttpResponse(template.render())

def department_signal_power(request):
    template = loader.get_template('home/department/signal/power_systems_laboratory.html')
    return HttpResponse(template.render())

def department_signal_train(request):
    template = loader.get_template('home/department/signal/train_detection_laboratory.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def department_it(request):
    template = loader.get_template('home/department/it.html')
    return HttpResponse(template.render())

def department_it_computer(request):
    template = loader.get_template('home/department/it/computer_lab.html')
    return HttpResponse(template.render())

def department_it_network(request):
    template = loader.get_template('home/department/it/networking_lab.html')
    return HttpResponse(template.render())

def department_it_passenger(request):
    template = loader.get_template('home/department/it/passenger.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def department_telecom(request):
    template = loader.get_template('home/department/telecom.html')
    return HttpResponse(template.render())

def department_telecom_control(request):
    template = loader.get_template('home/department/telecom/control.html')
    return HttpResponse(template.render())
    
def department_telecom_outdoor(request):
    template = loader.get_template('home/department/telecom/outdoor_telecom.html')
    return HttpResponse(template.render())
    
def department_telecom_telephony(request):
    template = loader.get_template('home/department/telecom/telephony.html')
    return HttpResponse(template.render())
    
def department_telecom_transmission(request):
    template = loader.get_template('home/department/telecom/transmission_system.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def department_coeKavach(request):
    template = loader.get_template('home/department/coeKavach.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def infrastructure(request):
    template = loader.get_template('home/infrastructure.html')
    return HttpResponse(template.render())

def infrastructure_lecture(request):
    template = loader.get_template('home/infrastructure/lecture.html')
    return HttpResponse(template.render())

def infrastructure_lecture_classrooms(request):
    template = loader.get_template('home/infrastructure/lecture.html')
    return HttpResponse(template.render())

def infrastructure_lecture_digital_classrooms(request):
    template = loader.get_template('home/infrastructure/lecture.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def infrastructure_auditorium(request):
    template = loader.get_template('home/infrastructure/auditorium.html')
    return HttpResponse(template.render())

def infrastructure_auditorium_indoor(request):
    template = loader.get_template('home/infrastructure/auditorium.html')
    return HttpResponse(template.render())

def infrastructure_auditorium_outdoor(request):
    template = loader.get_template('home/infrastructure/auditorium.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def infrastructure_hostels(request):
    template = loader.get_template('home/infrastructure/hostels.html')
    return HttpResponse(template.render())

def infrastructure_hostels_kaveri(request):
    template = loader.get_template('home/infrastructure/kaveri.html')
    return HttpResponse(template.render())

def infrastructure_hostels_yamuna(request):
    template = loader.get_template('home/infrastructure/yamuna.html')
    return HttpResponse(template.render())

def infrastructure_hostels_krishna(request):
    template = loader.get_template('home/infrastructure/krishna.html')
    return HttpResponse(template.render())

def infrastructure_hostels_ganga(request):
    template = loader.get_template('home/infrastructure/ganga.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def infrastructure_sports(request):
    template = loader.get_template('home/infrastructure/sports.html')
    return HttpResponse(template.render())

def infrastructure_sports_indoor(request):
    template = loader.get_template('home/infrastructure/sports.html')
    return HttpResponse(template.render())

def infrastructure_sports_outdoor(request):
    template = loader.get_template('home/infrastructure/sports.html')
    return HttpResponse(template.render())

#######################################################################################################################################

def events(request):
    template = loader.get_template('home/events.html')
    return HttpResponse(template.render())

def annualReport(request):
    template = loader.get_template('home/annualReport.html')
    return HttpResponse(template.render())


# trainee resources

def briefing(request):
    template = loader.get_template('trainee/briefing.html')
    return HttpResponse(template.render())

def courseCalender(request):
    template = loader.get_template('trainee/courseCalender.html')
    return HttpResponse(template.render())

def traineeManagement(request):
    template = loader.get_template('trainee/traineeManagement.html')
    return HttpResponse(template.render())

def contentManagement(request):
    template = loader.get_template('trainee/contentManagement.html')
    return HttpResponse(template.render())

def libraryAccess(request):
    template = loader.get_template('trainee/libraryAccess.html')
    return HttpResponse(template.render())

def onlineExam(request):
    template = loader.get_template('trainee/onlineExam.html')
    return HttpResponse(template.render())

def discussionForm(request):
    template = loader.get_template('trainee/discussionForm.html')
    return HttpResponse(template.render())

# staff resources

def darpan(request):
    template = loader.get_template('staff/darpan.html')
    return HttpResponse(template.render())

def gyandeep(request):
    template = loader.get_template('staff/gyandeep.html')
    return HttpResponse(template.render())

def sop(request):
    template = loader.get_template('staff/sop.html')
    return HttpResponse(template.render())

# research
def coeKavach(request):

    template = loader.get_template('research/coeKavach.html')
    return HttpResponse(template.render())

def _5g(request):
    template = loader.get_template('research/_5g.html')
    return HttpResponse(template.render())

def faculty(request):
    template = loader.get_template('research/faculty.html')
    return HttpResponse(template.render())

def mous(request):
    template = loader.get_template('home/mous.html')
    return HttpResponse(template.render())

from .forms import PostForm
def innovations(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
        else:
            form=PostForm()
    return render(request, 'research/innovations.html', {'form': form})

from .models import Post
def all_posts(request):
    all_posts = Post.objects.all()
    unique_usernames = set(post.user.username for post in all_posts)

    posts_data = []
    for post in all_posts:
        file_url = None
        if post.file:
            file_url = post.file.url
            print(f"File URL for post {post.id}: {file_url}")  # Print the file URL

        post_info = {
            'content': post.content,
            'file_name': post.file.name.split('/')[-1] if post.file else None,
            'file_url': file_url
        }
        posts_data.append(post_info)

    context = {'posts': posts_data, 'unique_usernames': list(unique_usernames)}
    return render(request, 'research/innovations.html', context)


from django.contrib.auth.models import User
def user_posts(request, username):
    user = User.objects.get(username=username)
    user_posts = Post.objects.filter(user=user)

    post_data = []
    for post in user_posts:
        file_url = None
        if post.file:
            file_url = post.file.url

        post_info = {
            'content': post.content,
            'file_name': post.file.name.split('/')[-1] if post.file else None,
            'file_url': file_url
        }
        post_data.append(post_info)

    return JsonResponse({'posts': post_data})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('all_posts') 
    else:
        form = PostForm()
    return render(request, 'research/create_post.html', {'form': form})
#</li><h1>hello</h1></ol><img src=x onmouseover="alert('xxs')">
# notification

def selections(request):
    template = loader.get_template('notifications/selections.html')
    return HttpResponse(template.render())

def notifications(request):
    template = loader.get_template('notifications/notifications.html')
    return HttpResponse(template.render())

def railwaySites(request):
    template = loader.get_template('notifications/railwaySites.html')
    return HttpResponse(template.render())

# contact

def reaching(request):
    template = loader.get_template('contact/reaching.html')
    return HttpResponse(template.render())

def telephone(request):
    template = loader.get_template('contact/telephone.html')
    return HttpResponse(template.render())

def disclaimer(request):
    template = loader.get_template('contact/disclaimer.html')
    return HttpResponse(template.render())

def privacyPolicy(request):
    template = loader.get_template('contact/privacyPolicy.html')
    return HttpResponse(template.render())

def sexualHarassment(request):
    template = loader.get_template('contact/sexualHarassment.html')
    return HttpResponse(template.render())

def rti(request):
    template = loader.get_template('contact/rti.html')
    return HttpResponse(template.render())

def nonRailway(request):
    template = loader.get_template('contact/nonRailway.html')
    return HttpResponse(template.render())

def links(request):
    template = loader.get_template('contact/links.html')
    return HttpResponse(template.render())

def logout_view(request):
    logout(request)
    #template = loader.get_template('research/innovations.html')
    #return HttpResponse(template.render())
    return all_posts(request)
