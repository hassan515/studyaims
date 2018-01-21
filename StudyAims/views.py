from django.shortcuts import render, redirect ,  get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.contrib.sites.shortcuts import get_current_site
from django.template.context_processors import csrf
from django.contrib.auth.models import User, Group
from django.db.models import Q
from StudyAims.models import StdPersonalInfo,  StudentLanguage, UserType , StudentFuture, AgentCompanyInfo
from StudyAims.forms import   PersonalInfoForm, RegisterStudentForm, StudentLanguageForm, StudentFutureForm, StudentImageForm,  AgentCompanyInfoForm, AgentCompanyRegisterationInfoForm, AgentExpertiseForm, AgentLogoForm , AgentServicesOfferedForm
from StudyAims.filters import UserFilter, FilterAgents
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm



def index(request):

    return render(request, "StudyAims/index.html")
@login_required
def profile_edit(request, pk):
    #personal = get_object_or_404(StdPersonalInfo, pk=pk)
    related = User.objects.select_related().all()
    user = get_object_or_404(related, pk=pk)
    profile = user.stdpersonalinfo
    profile_form = PersonalInfoForm(data=request.POST, instance=profile)
    if request.method == "POST":
        profile_form = PersonalInfoForm(request.POST,instance=profile )
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            #post.published_date = timezone.now()
            profile.save()
            return redirect('/StudyAims/dashboard')
    else:
        profile_form = PersonalInfoForm( instance=profile)
    return render(request, 'StudyAims/edit-information.html', {'profile_form': profile_form, 'pk':pk, 'user':user })


@login_required
def agent_profile_edit(request, pk):
    #personal = get_object_or_404(StdPersonalInfo, pk=pk)
    related = User.objects.select_related().all()
    user = get_object_or_404(related, pk=pk)
    profile = user.agentcompanyinfo
    form = AgentCompanyInfoForm(data=request.POST, instance=profile)
    if request.method == "POST":
        form = AgentCompanyInfoForm(request.POST,instance=profile )
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            #post.published_date = timezone.now()
            profile.save()
            return redirect('/StudyAims/agent_dashboard')
    else:
        form = AgentCompanyInfoForm(instance=profile)
    return render(request, 'StudyAims/agent-profile-edit.html', {'form': form, 'pk':pk, 'user':user })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/StudyAims/dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'StudyAims/change-password.html', {
        'form': form
    })

@login_required
def search_students(request):
    users = User.objects.all()
    f = UserFilter(request.GET, queryset=StdPersonalInfo.objects.all())

    #p = PersonalFilter(request.GET, queryset=StdPersonalInfo.objects.all())
    #p = PersonalFilter(request.GET, queryset=StdPersonalInfo.objects.all())
    #f = User.objects.all().select_related('stdpersonalinfo_set', 'studentqualifications_set')
    return render(request, 'StudyAims/search-students.html', {'filter': f, 'user': users })

@login_required
def search_agents(request):
    users = User.objects.all()
    f = FilterAgents(request.GET, queryset=AgentCompanyInfo.objects.all())

    #p = PersonalFilter(request.GET, queryset=StdPersonalInfo.objects.all())
    #p = PersonalFilter(request.GET, queryset=StdPersonalInfo.objects.all())
    #f = User.objects.all().select_related('stdpersonalinfo_set', 'studentqualifications_set')
    return render(request, 'StudyAims/search-agents.html', {'filter': f, 'user': users })

# Create your views here.
def register(request):
    registered = False
    user_form = RegisterStudentForm(data = request.POST)
    #user_type = UserTypeForm(data = request.POST)
    #profile_form = PersonalInfoForm(data = request.POST)
    #qualify_form = StdQualificationForm(data = request.POST)
    #user_form = RegisterStudentForm(data = request.POST)
    if request.method == 'POST':
        #user_type = UserTypeForm(data = request.POST)
        user_form = RegisterStudentForm(data = request.POST)
        #profile_form = PersonalInfoForm(data = request.POST)
        #qualify_form = StdQualificationForm(data = request.POST)

        #User_CHOICES = request.POST.get("User_CHOICES", None)
        #g = Group.objects.get(name='Students')
        #a = Group.objects.get(name='Agents')

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            #user.save(commit = False)
            #user_type.user = user
            #user.save()
            #u_type = user_type.save(commit = False)
            #u_type.user = user
            #u_type.save()

            user_perm = request.POST.get("user_perm", None)
            if user_perm in ["Student"]:

                #g = Group.objects.get_or_create(name="Student")
                ##std = Group.objects.get(name='Students')
                #
            #    user.save()

            #    t = UserType.objects.filter(student_type)

            #    t.student_type = "Yes"
            #    t.save(commit = False)
            #    t.user = user  # change field
            #    T.save()
                user.save()
                return redirect(reverse('index'))

                #request.user.groups.add(g)

                #user.groups.add("g")

            else:
                #a = Group.objects.get_or_create(name="Agent")
                #agnt = Group.objects.get(name='Agents')

                #user.groups.add(agnt)
                user.save()

                return redirect(reverse('index'))



        else:
            #print(user_type.errors)
            print(user_form.errors)




    else:
        user_form = RegisterStudentForm()
    #    profile_form = PersonalInfoForm()
    #    qualify_form = StdQualificationForm(data = request.POST)
        #user_type = UserTypeForm()
    return render(request, 'StudyAims/register.html',{'user_form':user_form,'registered':registered})



def user_login(request):
    err = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_type =  request.POST.get('student_type')
        agent_type =  request.POST.get('agent_type')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                if student_type :
                    login(request,user)
                    if StdPersonalInfo.objects.filter(user= request.user).exists():
                        return HttpResponseRedirect(reverse_lazy('StudyAims:dashboard'))
                    else:
                        return HttpResponseRedirect(reverse_lazy('StudyAims:update_personal'))
                elif agent_type:

                    login(request,user)
                    if AgentCompanyInfo.objects.filter(user= request.user).exists():
                        return HttpResponseRedirect(reverse_lazy('StudyAims:agent_dashboard'))
                    else:
                        return HttpResponseRedirect(reverse_lazy('StudyAims:update_agent_company_info'))
                else:
                    err = "Please Select a User Type"
                    return render(request,'StudyAims/login.html',{'err':err})
                #global user_variable
                #user_variable = request.user
                #print(user_variable)
                #g = Group.objects.get(name='Students')
                #a = Group.objects.get(name='Agents')
                #users_as_agent = UserType.objects.get(name="Agents").user_set.all()
                #users_in_student = Group.objects.get(name="Students").user_set.all()
                #if user in users_in_group and user.agentcompanyinfo.address == '':

                #    return HttpResponseRedirect(reverse_lazy('StudyAims:update_agent_company_info'))
                #agent = UserType.objects.filter('Agent')
                #student = UserType.objects.filter('Student')
                #user_in_group = UserType.objects.all(user)


                #if  user.user_in_group.agent == 'True' and user.user_in_group.student == 'False':
                    #return HttpResponseRedirect(reverse_lazy('StudyAims:update_agent_company_info'))
                #elif users_in_student and user.stdpersonalinfo.address == '':
                #    return HttpResponseRedirect(reverse_lazy('StudyAims:update_personal'))
            #    else:


            else:
                return HttpResponse("Account Not active!")

        else:
            print("Someone tried to login!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'StudyAims/login.html',{'err':err})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#@login_required
#def update_personal_information(request):
    #user = request.user
    #prof_form = PersonalInfoForm(request.POST)
    #print(user)
    #reg_Form = EditRegForm(request.POST)
    #user.id = request.user.id

#    if request.method == 'POST':

#        prof_form = PersonalInfoForm(data = request.POST)

        #reg_Form = EditRegForm(request.POST)
#        if prof_form.is_valid():
            #form = PersonalInfoForm(request.POST)
            #gender = request.POST.get("gender")
#            print(gender)
#            profile = prof_form.save()
#            profile.user = user
            #profile.user.id = user.id

            #profile.user.id = request.user.id
#            profile.save()
#            print (user)


#            return HttpResponseRedirect(reverse_lazy('StudyAims:update_qualification'))
#        else:
#            print(prof_form.errors)

        #else:
            #print(form.errors)


#    else:
#        prof_form = PersonalInfoForm()
#    return render(request, 'StudyAims/UpdateStudent.html',{'prof_form':prof_form})

@login_required
def update_personal(request):
    user = request.user
    form = PersonalInfoForm(data = request.POST)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            pro = form.save(commit=False)
        #    user = request.user
        #    user_id = request.user.id
            pro.user = user
            #StudyAims_studentqualifications.user_id = user_id
            #print(user_id)
            pro.save()
            #return redirect(reverse('index'))
            return HttpResponseRedirect(reverse_lazy('StudyAims:dashboard'))

    else:
        form = PersonalInfoForm()
        print(form.errors)
    return render(request,'StudyAims/UpdateStudent.html', {'form': form})

#@login_required
#def update_qualification(request):
#    user = request.user
#    form = StdQualificationForm(data = request.POST)
#    if request.method == 'POST':
#        form = StdQualificationForm(request.POST)
#        if form.is_valid():
#            pro = form.save(commit=False)
        #    user = request.user
        #    user_id = request.user.id
#            pro.user = user
            #StudyAims_studentqualifications.user_id = user_id
            #print(user_id)
#            pro.save()
            #return redirect(reverse('index'))
#            return HttpResponseRedirect(reverse_lazy('StudyAims:update_language_skills'))

#    else:
#        form = StdQualificationForm()
#    return render(request,'StudyAims/UpdateStudent2.html', {'form': form})

@login_required
def update_language_skills(request):
    user = request.user
    form = StudentLanguageForm(data = request.POST)
    if request.method == 'POST':
        form = StudentLanguageForm(request.POST)
        if form.is_valid():
            lang = form.save(commit=False)
            lang.user = user
            lang.save()
            #return redirect(reverse('index'))
            return HttpResponseRedirect(reverse_lazy('StudyAims:update_future_plans'))

    else:
        form = StudentLanguageForm()
    return render(request, 'StudyAims/UpdateStudent3.html', {'form': form})

@login_required
def update_future_plans(request):
    user = request.user
    form = StudentFutureForm(data = request.POST)
#    reg_form = RegisterStudentForm(data = request.POST)
    if request.method == 'POST':
        form = StudentFutureForm(request.POST)
        #reg_form = RegisterStudentForm(request.POST)
        if form.is_valid():
            #reg_form.save()
            future = form.save(commit=False)
            future.user = user
            future.save()
            return HttpResponseRedirect(reverse_lazy('StudyAims:dashboard'))
            #return HttpResponseRedirect(reverse_lazy('basic_app:update_profile_pic'))

    else:
        form = StudentFutureForm
    return render(request, 'StudyAims/UpdateStudent4.html', {'form': form})

@login_required
def update_profile_pic(request):

    user = request.user
    form = StudentImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = StudentImageForm(request.POST, request.FILES)
        if form.is_valid():
            if 'profile_pic' in request.FILES:


                pict = form.save(commit=False)
                pict.profile_pic = request.FILES['profile_pic']
                pict.user = user
                pict.save()
                return HttpResponseRedirect(reverse_lazy('StudyAims:dashboard'))

    else:
        form = StudentImageForm
    return render(request, 'StudyAims/update_pic.html', {'form': form})
    #return render(request, 'basic_app/update_pic.html')

#@login_required

def dashboard(request):
    current_user = request.user
    #dash_b = User.objects.filter(current_user.id)
    #person = current_user.studentpersonalinfo.contact_number
    #print(current_user.studentpersonalinfo.contact_number)

    #qual = StdQualification.objects.filter()

    return render(request, 'StudyAims/dashboard.html',{'current_user':current_user})


@login_required
def update_agent_company_info(request):
    user = request.user
    form = AgentCompanyInfoForm(data = request.POST)
#    reg_form = RegisterStudentForm(data = request.POST)
    if request.method == 'POST':
        form = AgentCompanyInfoForm(request.POST)
        #reg_form = RegisterStudentForm(request.POST)
        if form.is_valid():
            #reg_form.save()
            future = form.save(commit=False)
            future.user = user
            future.save()
            return HttpResponseRedirect(reverse_lazy('StudyAims:agent_dashboard'))
            #return HttpResponseRedirect(reverse_lazy('basic_app:update_profile_pic'))

    else:
        form = AgentCompanyInfoForm
        #print(form.errors)
    return render(request, 'StudyAims/UpdateAgent.html', {'form': form})

@login_required
def update_company_registration(request):
    user = request.user
    form = AgentCompanyRegisterationInfoForm(data = request.POST)
#    reg_form = RegisterStudentForm(data = request.POST)
    if request.method == 'POST':
        form = AgentCompanyRegisterationInfoForm(request.POST)
        #reg_form = RegisterStudentForm(request.POST)
        if form.is_valid():
            #reg_form.save()
            future = form.save(commit=False)
            future.user = user
            future.save()
            return HttpResponseRedirect(reverse_lazy('StudyAims:update_company_services'))
            #return HttpResponseRedirect(reverse_lazy('basic_app:update_profile_pic'))

    else:
        form = AgentCompanyRegisterationInfoForm
    return render(request, 'StudyAims/UpdateAgent2.html', {'form': form})


@login_required
def update_company_services(request):
    user = request.user
    form = AgentServicesOfferedForm(data = request.POST)
#    reg_form = RegisterStudentForm(data = request.POST)
    if request.method == 'POST':
        form = AgentServicesOfferedForm(request.POST)
        #reg_form = RegisterStudentForm(request.POST)
        if form.is_valid():
            #reg_form.save()
            future = form.save(commit=False)
            future.user = user
            future.save()
            return HttpResponseRedirect(reverse_lazy('StudyAims:update_agent_expertise'))
            #return HttpResponseRedirect(reverse_lazy('basic_app:update_profile_pic'))

    else:
        form = AgentServicesOfferedForm
    return render(request, 'StudyAims/UpdateAgent3.html', {'form': form})

@login_required
def update_agent_expertise(request):
    user = request.user
    form = AgentExpertiseForm(data = request.POST)
#    reg_form = RegisterStudentForm(data = request.POST)
    if request.method == 'POST':
        form = AgentExpertiseForm(request.POST)
        #reg_form = RegisterStudentForm(request.POST)
        if form.is_valid():
            #reg_form.save()
            future = form.save(commit=False)
            future.user = user
            future.save()
            return HttpResponseRedirect(reverse_lazy('StudyAims:agent_dashboard'))
            #return HttpResponseRedirect(reverse_lazy('basic_app:update_profile_pic'))

    else:
        form = AgentExpertiseForm
    return render(request, 'StudyAims/agent-expertise.html', {'form': form})



@login_required
def agent_dashboard(request):
    current_user = request.user
    #dash_b = User.objects.filter(current_user.id)
    #person = current_user.studentpersonalinfo.contact_number
    #print(current_user.studentpersonalinfo.contact_number)

    #qual = StdQualification.objects.filter()

    return render(request, 'StudyAims/agent_dashboard.html',{'current_user':current_user})



@login_required
def student_search(request):
    current_user = request.user

    all_users = User.objects.all()
    degree = request.POST.get('Degree')
    print(degree)
    Subject = request.POST.getlist('Subject')
    Passing_Year = request.POST.getlist('Passing_Year')
    percentage = request.POST.getlist('percentage')
    eng_lang = request.POST.getlist('eng_lang')
    language = request.POST.getlist('language')
    Study_Gap = request.POST.getlist('Study_Gap')
    Job_Experience = request.POST.getlist('Job_Experience')
    desired_degree = request.POST.getlist('desired_degree')
    desired_subject = request.POST.getlist('desired_subject')
    desired_country = request.POST.getlist('desired_country')
    desired_budget = request.POST.getlist('desired_budget')
    desired_sch = request.POST.getlist('desired_sch')
    qualification_filter = StudentQualifications.objects.filter(Q(highest_qualification=degree) & Q(subject=Subject) & Q(passing_year= Passing_Year) & Q(percentage=percentage) & Q(study_gap1=Study_Gap) & Q(experience1 = Job_Experience))
    future_plan_filter = StudentFuture.objects.filter(Q(desired_degree=desired_degree) & Q(desired_subject=desired_subject ) & Q(desired_country=desired_country) & Q(scholarships=desired_sch) & Q(budget=desired_budget))
    language_filter = StudentLanguage.objects.filter(Q(english_language= eng_lang) & Q(other_Language=language))

    return render(request, "StudyAims/search-students.html", {'current_user': current_user, 'all_users':all_users, 'qualification_filter':qualification_filter, 'future_plan_filter':future_plan_filter,'language_filter':language_filter})
