from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    
    #Home
    path('directorMessage', views.directorMessage, name='directorMessage'),
    path('about', views.about, name='about'),

#######################################################################################################################################

    path('management', views.management, name='management'),
    path('management_gazetted', views.management_gazetted, name='management_gazetted'),
    path('management_ngSignal', views.management_ngSignal, name='management_ngSignal'),
    path('management_ngTelecom', views.management_ngTelecom, name='management_ngTelecom'),

#######################################################################################################################################
    
    path('department', views.department, name='department'),
    path('department_signal', views.department_signal, name='department_signal'),
    path('department_telecom', views.department_telecom, name='department_telecom'),
    path('department_it', views.department_it, name='department_it'),
    path('department_coeKavach', views.department_coeKavach, name='department_coeKavach'),

#######################################################################################################################################

    path('infrastructure', views.infrastructure, name='infrastructure'),
    path('infrastructure_lecture', views.infrastructure_lecture, name='infrastructure_lecture'),
    path('infrastructure_lecture_classrooms', views.infrastructure_lecture_classrooms, name='infrastructure_lecture_classrooms'),
    path('infrastructure_lecture_digital_classrooms', views.infrastructure_lecture_digital_classrooms, name='infrastructure_lecture_digital_classrooms'),

#######################################################################################################################################

    path('infrastructure_auditorium', views.infrastructure_auditorium, name='infrastructure_auditorium'),
    path('infrastructure_auditorium_indoor', views.infrastructure_auditorium_indoor, name='infrastructure_auditorium_indoor'),
    path('infrastructure_auditorium_outdoor', views.infrastructure_auditorium_outdoor, name='infrastructure_auditorium_outdoor'),

#######################################################################################################################################

    path('infrastructure_hostels', views.infrastructure_hostels, name='infrastructure_hostels'),
    path('infrastructure_hostels_kaveri', views.infrastructure_hostels_kaveri, name='infrastructure_hostels_kaveri'),
    path('infrastructure_hostels_yamuna', views.infrastructure_hostels_yamuna, name='infrastructure_hostels_yamuna'),
    path('infrastructure_hostels_krishna', views.infrastructure_hostels_krishna, name='infrastructure_hostels_krishna'),
    path('infrastructure_hostels_ganga', views.infrastructure_hostels_ganga, name='infrastructure_hostels_ganga'),

#######################################################################################################################################

    path('infrastructure_sports', views.infrastructure_sports, name='infrastructure_sports'),
    path('infrastructure_sports_indoor', views.infrastructure_sports_indoor, name='infrastructure_sports_indoor'),
    path('infrastructure_sports_outdoor', views.infrastructure_sports_outdoor, name='infrastructure_sports_outdoor'),

#######################################################################################################################################

    path('events', views.events, name='events'),
    path('annualReport', views.annualReport, name='annualReport'),

    #TraineeResources
    path('briefing', views.briefing, name='briefing'),
    path('courseCalender', views.courseCalender, name='courseCalender'),
    path('traineeManagement', views.traineeManagement, name='traineeManagement'),
    path('contentManagement', views.contentManagement, name='contentManagement'),
    path('libraryAccess', views.libraryAccess, name='libraryAccess'),
    path('onlineExam', views.onlineExam, name='onlineExam'),
    path('discussionForm', views.discussionForm, name='discussionForm'),

    #StaffResources
    path('darpan', views.darpan, name='darpan'),
    path('gyandeep', views.gyandeep, name='gyandeep'),
    path('sop', views.sop, name='sop'),
    
    #research
    path('coeKavach', views.coeKavach, name='coeKavach'),
    path('_5g', views._5g, name='_5g'),
    path('faculty', views.faculty, name='faculty'),
    path('mous', views.mous, name='mous'),
    path('innovations',  views.all_posts, name='all_posts'),
    path('posts/<str:username>/', views.user_posts, name='user_posts'),

    #notification
    path('selections', views.selections, name='selections'),
    path('notifications', views.notifications, name='notifications'),
    path('railwaySites', views.railwaySites, name='railwaySites'),

    #contacreachingt
    path('reaching', views.reaching, name='reaching'),
    path('telephone', views.telephone, name='telephone'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('privacyPolicy', views.privacyPolicy, name='privacyPolicy'),
    path('sexualHarassment', views.sexualHarassment, name='sexualHarassment'),
    path('rti', views.rti, name='rti'),
    path('nonRailway', views.nonRailway, name='nonRailway'),
    path('links', views.links, name='links'),

    path('logout_view', views.logout_view, name='logout_view'),
    path('create_post', views.create_post, name='create_post'),
]