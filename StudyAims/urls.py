from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static
app_name = 'StudyAims'

urlpatterns = [
    url(r'^login/',views.user_login,name='user_login'),
    url(r'^dashboard/', views.dashboard , name = 'dashboard') ,
    url(r'^update_personal/', views.update_personal , name='update_personal'),
    url(r'^update_qualification/', views.update_qualification , name='update_qualification'),
    url(r'^update_language_skills/', views.update_language_skills , name='update_language_skills'),
    url(r'^update_future_plans/', views.update_future_plans , name='update_future_plans'),
    url(r'^update_profile_pic/', views.update_profile_pic , name='update_profile_pic'),
    url(r'^register_student/',views.register,name='register_student'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),

    # Agent Urls ####
    url(r'^update_agent_company_info/', views.update_agent_company_info , name='update_agent_company_info'),
    url(r'^update_company_registration/', views.update_company_registration , name='update_company_registration'),
    url(r'^update_company_services/', views.update_company_services , name='update_company_services'),
    url(r'^update_agent_expertise/', views.update_agent_expertise , name='update_agent_expertise'),
    url(r'^update_profile_pic/', views.update_profile_pic , name='update_profile_pic'),
    url(r'^agent_dashboard/', views.agent_dashboard , name = 'agent_dashboard') ,
    #url(r'^UpdateStudent/$', views.update_profile, name='UpdateStudent'),


    #url(r'^UpdateStudent2/', views.StdQualification, name='update_qualification'),



]
