from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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

def department_signal(request):
    template = loader.get_template('home/department/signal.html')
    return HttpResponse(template.render())


def department_it(request):
    template = loader.get_template('home/department/it.html')
    return HttpResponse(template.render())


def department_telecom(request):
    template = loader.get_template('home/department/telecom.html')
    return HttpResponse(template.render())


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
    template = loader.get_template('home/infrastructure/hostels.html')
    return HttpResponse(template.render())

def infrastructure_hostels_yamuna(request):
    template = loader.get_template('home/infrastructure/hostels.html')
    return HttpResponse(template.render())

def infrastructure_hostels_krishna(request):
    template = loader.get_template('home/infrastructure/hostels.html')
    return HttpResponse(template.render())

def infrastructure_hostels_ganga(request):
    template = loader.get_template('home/infrastructure/hostels.html')
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

@login_required
def innovations(request):
    context = {'user': request.user}
    return render(request, 'research/innovations.html', context)

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
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
