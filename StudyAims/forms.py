from django import forms
from django.contrib.auth.models import User
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, Field
#from crispy_forms.bootstrap import FormActions

#from django.localflavor.us.forms import PhoneNumberField
from StudyAims.models import  StdPersonalInfo, Countries, CityList, HighestQualification ,StudentLanguage, StudentQualifications, SubjectList, ProgramDuration, Percentage, PassingYear, StudentFuture, StudentImage, AgentMobileNumber, AgentCompanyInfo, AgentCompanyRegisterationInfo, AgentServicesOffered, AgentExpertise,AgentLogo, Budget, StateList, AgentFees
from django.utils.safestring import mark_safe



class HorizRadioRenderer(forms.RadioSelect):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

User_CHOICES = (
    ("Student", "Student"),
    ("Agent", "Agent"),
)

class RegisterStudentForm(forms.ModelForm):

    #user_perm =  forms.ChoiceField(initial=0, choices=User_CHOICES,
    #             widget=forms.forms.RadioSelect(attrs={
    #    'display': 'inline-block'
    #})
    user_perm = forms.ChoiceField(widget=forms.RadioSelect(render=HorizRadioRenderer),choices=User_CHOICES , label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full Name'}),
                  max_length=50, label='')

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter a User name'}),
                  max_length=50, label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),
                  max_length=50, label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),
                  max_length=50, label='')

#,

    class Meta():
        model = User
        fields = ('user_perm','first_name','username', 'email', 'password')
#class EditRegForm(forms.Form):
#    class Meta():
#        model = User
#        fields = ('first_name','email')

class PersonalInfoForm(forms.ModelForm):
    age = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Age'}),
                 )
    whatsapp = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'WhatsApp Number'}),
                 )
    contact_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Contact Number'}),
                 )
    any_other_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Any Other Number'}),
                 )
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Address'}),
                 )
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'STATE'}),
                 )
    #country_of_residence = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country of Residence'}),
    #             )
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nationality'}),
                 )
    #city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City'}),
    #             )


    #country_of_residence = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name" ,)
    #city = forms.ModelChoiceField(queryset= CityList.objects.all().order_by('city_name'), to_field_name="city_name")


    class Meta():
        model = StdPersonalInfo
        #exclude = ('user',)
        fields = ('gender', 'age','city','country_of_residence','whatsapp','contact_number','any_other_number','address','state','nationality')

class StdQualificationForm(forms.ModelForm):
    #highest_qualification = forms.ModelChoiceField(queryset= HighestQualification.objects.all().order_by('qualification'), to_field_name="qualification")
    #subject = forms.ModelChoiceField(queryset= SubjectList.objects.all().order_by('subject'), to_field_name="subject")
    #program_duration = forms.ModelChoiceField(queryset= ProgramDuration.objects.all().order_by('duration'), to_field_name="duration")
    #from_country = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name")
    #percentage = forms.ModelChoiceField(queryset= Percentage.objects.all().order_by('Percent'), to_field_name="Percent")
    #passing_year = forms.ModelChoiceField(queryset= PassingYear.objects.all().order_by('year'), to_field_name="year")

    class Meta():


        model = StudentQualifications
        fields = ('highest_qualification', 'subject', 'program_duration', 'Insititution','from_country', 'percentage', 'passing_year', 'study_gap1','study_gap2', 'study_gap2','study_gap3','study_gap4','experience1','experience','experience3','experience4','experience4','achievements')

class StudentLanguageForm(forms.ModelForm):


    class Meta():
        model = StudentLanguage
        fields= ('english_language', 'english_language_score', 'other_Language','Other_Language_score')


class StudentFutureForm(forms.ModelForm):

    desired_degree = forms.ModelChoiceField(queryset= HighestQualification.objects.all().order_by('qualification'), to_field_name="qualification")
    desired_subject = forms.ModelChoiceField(queryset= SubjectList.objects.all().order_by('subject'), to_field_name="subject")
    program_duration = forms.ModelChoiceField(queryset= ProgramDuration.objects.all().order_by('duration'), to_field_name="duration")
    desired_country = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name")
    #budget = forms.ModelChoiceField(queryset= Budget.objects.all().order_by('aff_budget'), to_field_name="aff_budget")
    class Meta():
        model = StudentFuture
        fields = ('desired_degree','desired_subject','desired_country','scholarships','budget')


class StudentImageForm():

    class Meta():
        model = StudentImage
        fields = ('profile_pic')

class AgentMobileForm():
    class Meta():
        model = AgentMobileNumber
        fields = ('agent_contact_number')

class AgentCompanyInfoForm(forms.ModelForm):
    comp_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Company Name'}),
                 )
    company_owner = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Company Owner Name'}),
                 )
    agent_whatsapp = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'WhatsApp Number'}),
                 )
    alternative_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Alternative Email'}),
                 )
    agent_website = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Website URL'}),
                 )
    facebook_link = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Facebook Page URL'}),
                 )
    service_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Service Types'}),
                 )
    linked_In = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'LinkedIn URL'}),
                 )
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Address'}),
                 )
    office_contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Office Contact Number'}),
                 )
    office_contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Office Contact Number'}),
                 )
    agent_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'STATE'}),
                 )
    #country_of_residence = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country of Residence'}),
    #             )
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nationality'}),
                 )
    agent_city =    forms.ModelChoiceField(queryset= CityList.objects.all().order_by('city_name'), to_field_name="city_name")
    agent_country = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name")
    agent_state = forms.ModelChoiceField(queryset= StateList.objects.all().order_by('state_name'), to_field_name="state_name")

    class Meta():
        model = AgentCompanyInfo
        fields = ('comp_name','service_type','company_owner','agent_whatsapp','address','alternative_email','agent_website','facebook_link','linked_In','office_contact','agent_city','agent_state','agent_country')


class AgentCompanyRegisterationInfoForm(forms.ModelForm):
    pak_registeration_body1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'1.Registration Body'}),
                 )
    pak_registeration_body2= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'2.Registration Body'}),
                 )
    pak_registeration_body3= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'3.Registration Body'}),
                 )
    pak_registeration_body4= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'4.Registration Body'}),
                 )
    pak_registeration_body5= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'5.Registration Body'}),
                 )
    pak_registeration_body6= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'6.Registration Body'}),
                 )
    Internatiol_registeration_body1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'1.Registration Body'}),
                 )
    Internatiol_registeration_body2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'2.Registration Body'}),
                 )
    Internatiol_registeration_body3=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'3.Registration Body'}),
                 )
    Internatiol_registeration_body4=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'4.Registration Body'}),
                 )
    Internatiol_registeration_body5= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'5.Registration Body'}),
                 )

    Internatiol_registeration_body6= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'6.Registration Body'}),
                 )
    class Meta():
        model = AgentCompanyRegisterationInfo
        fields=('pak_registeration_body1','pak_registeration_body2','pak_registeration_body3','pak_registeration_body4','pak_registeration_body5','pak_registeration_body6','Internatiol_registeration_body1','Internatiol_registeration_body2','Internatiol_registeration_body3',
            'Internatiol_registeration_body4','Internatiol_registeration_body5','Internatiol_registeration_body6')

class AgentServicesOfferedForm(forms.ModelForm):
    countries_Dealing = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Countries Dealing'}),
                 )
    #Services_offered= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Services Offered'}),

    #             )
    service_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Services Type'}),
                 )
    language_classes = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Language Classes'}),
                 )

    program_specialist = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Program Specialist'}),
                 )
    refusal_appeals = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Refusal Appeals'}),
                 )
    scholarships_offered = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Scholaships Offered'}),
                 )
    interview_preparation = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Interview Preparation'}),
                 )
    travel_and_health = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Travel and Health Insurance'}),
                 )
    travel_arrangements = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Travel Arrangements'}),
                 )
    class Meta():
        model = AgentServicesOffered
        fields = ('countries_Dealing','service_type','language_classes','program_specialist','refusal_appeals','scholarships_offered','interview_preparation','travel_and_health','travel_arrangements')


class AgentExpertiseForm(forms.ModelForm):

    visa_ratio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Visa Ratio'}),
                 )
    experience = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Experience (Years)'}),
                 )
    regional_office = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Regional Offices'}),
                 )
    branches = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Branches'}),
                 )
    number_of_counselors = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number of Counselors'}),
                 )
    class Meta():
        model = AgentExpertise
        fields = ('visa_ratio','experience','regional_office','branches','number_of_counselors')


class AgentFeesForm(forms.ModelForm):

    class Meta():
        model = AgentFees
        fields = ('processing_fee','language_fee','refusal_fee','Interview_fee')


class AgentLogoForm(forms.ModelForm):

    class Meta():
        model = AgentLogo
        fields = ('__all__')
