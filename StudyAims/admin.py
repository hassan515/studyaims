from django.contrib import admin
from StudyAims.models import *
from django.contrib.auth.admin import UserAdmin
from .models import User


#admin.site.register(User, UserAdmin)

# Register your models here.
#admin.site.register(RegisterStudent)
#admin.site.register(AgentCompanyRegisterationInfo)
#admin.site.register(UserType)
#admin.site.register(StudentImage)
#admin.site.register(AgentLogo)
admin.site.register(StdPersonalInfo)
admin.site.register(Country_Deal)
#admin.site.register(Countries)
#admin.site.register(CityList)
#admin.site.register(StateList)
#admin.site.register(PassingYear)
#admin.site.register(HighestQualification)
#admin.site.register(SubjectList)
#admin.site.register(ProgramDuration)
#admin.site.register(Percentage)
#admin.site.register(StudentLanguage)
#admin.site.register(StudentFuture)
#admin.site.register(AgentMobileNumber)
admin.site.register(AgentCompanyRegisterationInfo)
#admin.site.register(AgentCompanyInfo)
#admin.site.register(AgentExpertise)
#admin.site.register(AgentServicesOffered)
