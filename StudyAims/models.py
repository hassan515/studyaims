from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
#from django.localflavor.us.models import USPhoneNumberField
from django.contrib.auth.models import User , Group, AbstractBaseUser, BaseUserManager, AbstractUser
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

#class Students(models.Model):
#    user =

#class UserAccountManager(BaseUserManager):
#    def create_user(self, email, first_name, last_name, password=None):
#        if not email:
#            raise ValueError('Email must be set!')
#        user = self.model(email=email, first_name=first_name, last_name=last_name)
#        user.set_password(password)
#        user.save(using=self._db)
#        return user

#    def create_superuser(self,username,  password):
#        user = self.create_user(username,  password)
#        user.is_admin = True
#        user.save(using=self._db)
#        return user

    #def get_by_natural_key(self, email_):
    #    return self.get(code_number=email_)

#class RegStudent(AbstractBaseUser):
#    username = models.CharField('username', max_length=15, unique = True, db_index= True)
#    email = models.EmailField('Email Address', unique = True)
#    mobilenumber = models.PhoneNumberField(unique=True)
    #phone_number = models.RegexField(regex=r'^\+?1?\d{9,14}$')
#    is_active = models.BooleanField(default=True)
#    is_superuser = models.BooleanField(default= False)

#    USERNAME_FIELD = 'username'

#    objects = UserAccountManager()
#    def __unicode_(self):
#        return self.username



#readers = Group.objects.create(name="Students")
#writers = Group.objects.create(name="Agents")


# Create your models here.

#class UserGroup(Group):
    #user = models.ManyToManyField(User)

class UserType(models.Model):
    user = models.OneToOneField
    agent_type = models.CharField(max_length=30)
    student_type = models.CharField(max_length=30)

    def __unicode__(self):

        return self.user
#class AgGroup(models.Model):

#    Agents = Group.objects.create(name='consultants')
    #def __unicode__(self):
    #    return self.user

#class StdGroup(models.Model):
    #user = models.OneToOneField(User)
    #Student = models.OneToOneField(Group, related_name = "Students")
    #Agent = models.OneToOneField(Group, related_name = "Agents")
    #Agent = models.BooleanField(default=False)
#class AgentGroup(models.Model):
#    Agent = models.OneToOneField(Group, related_name = "Agents")
#class StdGroup(models.Model):

    #Student = Group.objects.create(name='Students')
    #Agents = Group.objects.create(name='Agents')

class Countries(models.Model):
    country_name = models.CharField(max_length=50, default=None)
    country_value = models.CharField(max_length=50, default=None)

    def __str__(self):              # __unicode__ on Python 2
        return self.country_name
class CityList(models.Model):
    city_name = models.CharField(max_length=50, default=None)
    city_value = models.CharField(max_length=50, default=None)

    def __str__(self):              # __unicode__ on Python 2
        return self.city_name

class StateList(models.Model):
    state_name = models.CharField(max_length=50, default=None)
    state_value = models.CharField(max_length=50, default=None)

    def __str__(self):              # __unicode__ on Python 2
        return self.state_name

class Processing(models.Model):
    processing_fee = models.CharField(max_length=10, default=None)
    processing_value = models.CharField(max_length=10, default=None)
    def __str__(self):              # __unicode__ on Python 2
        return self.processing_fee

class Language_Fees(models.Model):
    language_fee = models.CharField(max_length=10, default=None)
    language_value = models.CharField(max_length=10, default=None)

    def __str__(self):              # __unicode__ on Python 2
        return self.language_fee

class InterviewFees(models.Model):
    preparation_fee = models.CharField(max_length=10, default=None)
    interview_value = models.CharField(max_length=10, default=None)

    def __str__(self):              # __unicode__ on Python 2
        return self.preparation_fee

class ScholarhipFees(models.Model):
    scholarship_fee = models.CharField(max_length=10, default=None)
    scholarship_value = models.CharField(max_length=10, default=None)

    def __str__(self):              # __unicode__ on Python 2
        return self.scholarship_fee

class PassingYear(models.Model):
    year = models.CharField(max_length=50, default=None)
    year_value = models.CharField(max_length=50, default=None)
    def __str__(self):              # __unicode__ on Python 2
        return self.year

class Budget(models.Model):
    aff_budget = models.CharField(max_length=50, default=None)
    budget_value = models.CharField(max_length=50, default=None)
    def __str__(self):              # __unicode__ on Python 2
        return self.aff_budget

class HighestQualification(models.Model):
    qualification = models.CharField(max_length=50, default=None)
    qualification_value = models.CharField(max_length=50, default=None)
    def __str__(self):              # __unicode__ on Python 2
        return self.qualification
class SubjectList(models.Model):
    subject = models.CharField(max_length=50, default=None)
    subject_value = models.CharField(max_length=50, default=None)
    def __str__(self):              # __unicode__ on Python 2
        return self.subject
class ProgramDuration(models.Model):
    duration = models.CharField(max_length=50, default=None)
    duration_value = models.CharField(max_length=50, default=None)
    def __str__(self):
        return self.duration
class Percentage(models.Model):
    Percent = models.CharField(max_length=50, default=None)
    Percent_value = models.CharField(max_length=50, default=None)
    def __str__(self):
            return self.Percent


class Profile(models.Model):
    @property
    def is_student(self):
        try:
            self.student
            return True
        except Student.DoesNotExist:
            return False

#class Student(Profile):
#    user =  models.ForeignKey(User, on_delete=models.CASCADE)
#    std_name = models.CharField(max_length=50,default=None)
    #email = models.EmailField(default=None, unique=True , primary_key = True)
    #password = models.CharField(max_length=30, default=None)

    #objects = models.Manager()
#    def __str__(self):              # __unicode__ on Python 2
#        return self.std_name




#class RegisterStudent(models.Model):
    #id = models.AutoField(primary_key=True, default=None)
    #student = models.OneToOneField(User, unique=True,)


    #mobilenumber = models.PhoneNumberField(unique=True)


    #pk = id
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.std_name

    #def get_absolute_url(self):
    #    return reverse("update_profile_student",kwargs={'pk':self.pk})




class StdPersonalInfo(models.Model):
    user = models.OneToOneField(User)

    Gender = 'Gender'
    male = 'male'
    female = 'female'
    Gender = (
        (Gender,'Gender'),
        (male, 'male'),
        (female, 'female'),
        )
    City = 'City'
    Lahore = 'Lahore'
    Islmabad = 'Islamabad'

    City  =(
        (City,'City'),
        (Lahore , 'Lahore'),
        (Islmabad, 'Islamabad'),
    )
    Country = 'Country'
    Pakistan = 'Pakistan'
    India = 'India'

    Country = (
        (Country, 'Country'),
        (Pakistan ,'Pakistan'),
        (India , 'India'),
    )
    gender = models.CharField(max_length = 10, choices=Gender, default=Gender)
    age = models.CharField(max_length = 10, default=None, null=True)
    whatsapp = models.CharField(max_length = 15,blank=False, default=None, null=True )
    contact_number = models.CharField(max_length = 15,blank=False, default=None, unique = True)
    any_other_number = models.CharField(max_length = 15,blank=True,)
    address = models.CharField(max_length=500, default= None , null=True)
    city = models.CharField(max_length=25,choices=City, default=City,  null=True)
    state = models.CharField(max_length=35, blank=False, default=None , null=True )
    nationality = models.CharField(max_length=35 , blank=False, default=None, null=True )
    country_of_residence = models.CharField(max_length=35,choices=Country, default=Country, blank=False,  null=True)

    def __str__(self):
        return self.user.username
#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = StudentPersonalInfo.objects.create(user = kwargs['instance'])


    #User.profile = property(lambda u: StudentPersonalInfo.objects.get_or_create(user = u )[0])

    #def __str__(self):
        #return self.std_id

    #class Meta:
         #unique_together = (("id", "std_id"),)

    #def __str__(self):              # __unicode__ on Python 2
    #    return self.gender
    #def __unicode__(self):

#def my_callback(sender , request , user, **kwargs):
#    print kwargs

#user_logged_in.connect(my_callback)
    #def save(self, *args, **kwargs):
    #    key = cal_key(self.std_id)

    #    self.key = key
    #    super(StudentPersonalInfo, self).save(*args, **kwargs)

#post_save.connect(create_profile, sender= User)
#def std_personal(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = StdPersonalInfo.objects.create(user = kwargs['instance'])

#post_save.connect(std_personal, sender= User)
class StudentQualifications(models.Model):

    Degree = 'Degree'
    MA = 'MA'
    BA = 'BA'
    Degree = (
        (Degree,'Degree'),
        (MA , 'MA'),
        (BA , 'BA'),
    )
    Subject = 'Subject'
    Pyshics = 'Physics'
    Engineering = 'Engineering'

    Subject  =(
        (Subject , 'Subject'),
        (Pyshics , 'Physics'),
        (Engineering , 'Engineering'),
    )
    Program_Duration = 'Program_Duration'
    Years_16 = '16 Years'
    Years_14 = '14 Years'

    Program_Duration = (
        (Program_Duration , 'Program_Duration'),
        (Years_16  , '16 Years'),
        (Years_14  , '14Years'),
    )

    Country = 'Country'
    Australia = 'Australia'
    USA = 'USA'

    Country = (
        (Country , 'Country'),
        (Australia , 'Australia'),
        (USA , 'USA'),
    )
    user = models.OneToOneField(User)
    #std_qual_id = models.ForeignKey(RegisterStudent,related_name="std_qual_id")
    #student = models.ForeignKey('name', related_name='Student')
    highest_qualification = models.CharField(max_length=35, choices = Degree, default= Degree)
    subject = models.CharField(max_length=50,choices = Subject, default= Subject )
    program_duration = models.CharField(max_length=20 , choices = Program_Duration, default= Program_Duration)
    Insititution = models.CharField(max_length=200, blank=False)
    from_country = models.CharField(max_length=35, choices = Country, default= Country)
    percentage = models.CharField(max_length=10)
    passing_year = models.CharField(max_length=10)
    study_gap1 = models.CharField(max_length=20, blank=True, null=True)
    study_gap2 = models.CharField(max_length=20, blank=True, null=True)
    study_gap3 = models.CharField(max_length=20, blank=True, null=True)
    study_gap4 = models.CharField(max_length=20, blank=True, null=True)
    experience1 = models.CharField(max_length=20, blank=True, null=True)
    experience = models.CharField(max_length=20, blank=True, null=True)
    experience3 = models.CharField(max_length=20, blank=True, null=True)
    experience4 = models.CharField(max_length=20, blank=True, null=True)
    achievements = models.TextField(max_length=400, blank=True, null=True)
    def __str__(self):
        return self.user.username

#def std_qualification(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = StudentQualifications.objects.create(user = kwargs['instance'])

#post_save.connect(std_qualification, sender= User)
class StudentLanguage(models.Model):
    English_Language = 'English_Language'
    IELTS = 'IELTS'
    TOEFL = 'TOEFL'
    PTE = 'PTE'
    Oher = 'Oher'
    English_Language = (
        (English_Language,'English_Language'),
        (IELTS, 'IELTS'),
        (TOEFL, 'TOEFL'),
        (PTE, 'PTE'),
        (Oher, 'Oher'),
        )

    Other_Language = 'Other_Language'
    German = 'German'
    Chinese = 'Chinese'
    Japanese = 'Japanese'
    Spanish = 'Spanish'
    French = 'French '
    Italian = 'Italian'
    Turkish= 'Turkish'
    Portoguese = 'Portoguese'
    Korian = 'Korian'
    Other = 'Oher'

    Other_Language = (
        (Other_Language,'Other Language'),
        (German , 'German'),
        (Chinese , 'Chinese'),
        (Japanese , 'Japanese'),
        (Spanish , 'Spanish'),
        (French , 'French '),
        (Italian , 'Italian'),
        (Turkish, 'Turkish'),
        (Portoguese , 'Portoguese'),
        (Korian , 'Korian'),
        (Other , 'Oher'),

        )


    user = models.OneToOneField(User)
#    std_lang_id = models.ForeignKey(RegisterStudent,related_name="std_lang_id")
    english_language =  models.CharField(max_length=30,choices=English_Language, default=English_Language, null=True )
    english_language_score = models.CharField(max_length=10, null=True ,default= None)
    other_Language = models.CharField(max_length=30,choices=Other_Language, default=Other_Language, null=True )
    Other_Language_score = models.CharField(max_length=10, null=True,default= None)


    def __str__(self):
        return self.user.username


class StudentFuture(models.Model):
    Desired_Degree = 'Desired Degree'
    MA = 'MA'
    BA = 'BA'
    Desired_Degree = (
        (Desired_Degree,'Desired Degree'),
        (MA , 'MA'),
        (BA , 'BA'),
    )
    Desired_Subject = 'Desired Subject'
    Pyshics = 'Physics'
    Engineering = 'Engineering'

    Desired_Subject  =(
        (Desired_Subject , 'Desired Subject'),
        (Pyshics , 'Physics'),
        (Engineering , 'Engineering'),
    )
    Program_Duration = 'Program_Duration'
    Years_16 = '16 Years'
    Years_14 = '14 Years'

    Program_Duration = (
        (Program_Duration , 'Program_Duration'),
        (Years_16  , '16 Years'),
        (Years_14  , '14Years'),
    )

    Country = 'Country'
    Australia = 'Australia'
    USA = 'USA'

    Country = (
        (Country , 'Country'),
        (Australia , 'Australia'),
        (USA , 'USA'),
    )
    #id = models.OneToOneField(User)
    Scholarships = 'Scholarships'
    Yes = 'Yes'
    No = 'No'
    Scholarships = (
        (Scholarships,'Scholarships'),
        (Yes, 'Yes'),
        (No, 'No'),
        )

#    std_future_id = models.ForeignKey(RegisterStudent,related_name="std_future_id")
    user = models.OneToOneField(User)
    desired_degree = models.CharField(max_length=35, null=True,  choices = Desired_Degree, default = Desired_Degree)
    desired_subject = models.CharField(max_length=35, null=True ,choices = Desired_Subject,  default= Desired_Subject)
    desired_country = models.CharField(max_length=35, null=True,choices = Country,  default= Country)
    scholarships = models.CharField(max_length=35, null=True,choices= Scholarships,  default= Scholarships)
    budget = models.CharField(max_length=25, null=True, default= None)

    def __str__(self):
        return self.user.username

class StudentImage(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to = 'students', null=True)


class AgentMobileNumber(models.Model):
    user = models.OneToOneField(User)
    agent_contact_number = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.user.username

class AgentCompanyInfo(models.Model):
    user = models.OneToOneField(User)
    comp_name = models.CharField(max_length=200, blank=False , default= None)
    service_type =  models.CharField(max_length=50 , default= None , null=True)
    company_owner = models.CharField(max_length=50 , default= None)
    agent_whatsapp = models.CharField(max_length=50 , default= None)
    address = models.TextField(blank=False, default= None, null=True)
    alternative_email = models.EmailField(blank=False , default= None, null=True)
    agent_website = models.URLField( blank = True, null=True)
    facebook_link =  models.URLField( blank = True, null=True)
    linked_In = models.URLField(blank = True, null=True)
    office_contact = models.CharField(max_length=50 , default= None)
    agent_city = models.CharField(max_length=35 , default= None)
    agent_state = models.CharField(max_length=35 , default= None)
    agent_country =  models.CharField(max_length=35 , default= None)

    def __str__(self):
        return self.user.username



class AgentCompanyRegisterationInfo(models.Model):
    user = models.OneToOneField(User)
    #registered_name = models.CharField(max_length=200)

    pak_registeration_body1 = models.CharField(max_length=200, blank=True , default= None)
    pak_registeration_body2 = models.CharField(max_length=400, blank=True , default= None)
    pak_registeration_body3 = models.CharField(max_length=400, blank=True , default= None)
    pak_registeration_body4 = models.CharField(max_length=400, blank=True , default= None)
    pak_registeration_body5 = models.CharField(max_length=400, blank=True , default= None)
    pak_registeration_body6 = models.CharField(max_length=400, blank=True , default= None)

    Internatiol_registeration_body1 = models.CharField(max_length=200, blank=True, default= None)
    Internatiol_registeration_body2 = models.CharField(max_length=200, blank=True, default= None)
    Internatiol_registeration_body3 = models.CharField(max_length=200, blank=True, default= None)
    Internatiol_registeration_body4 = models.CharField(max_length=200, blank=True , default= None)
    Internatiol_registeration_body5 = models.CharField(max_length=200, blank=True , default= None)
    Internatiol_registeration_body6 = models.CharField(max_length=200, blank=True, default= None)

    def __str__(self):
        return self.user.username

class AgentServicesOffered(models.Model):
    user = models.OneToOneField(User)
    countries_Dealing = models.CharField(max_length=250, default= None)
    #Services_offered = models.CharField(max_length=250, default= None)
    service_type =  models.CharField(max_length=50, default= None)
    language_classes =  models.CharField(max_length=250, default= None, blank = True, null=True)
    processing_fee = models.CharField(max_length=20 , default= None, blank = True, null=True)
    program_specialist = models.CharField(max_length=20, default= None, blank = True, null=True)
    refusal_appeals = models.CharField(max_length=20, default= None, blank = True)
    scholarships_offered = models.CharField(max_length=20, default= None, blank = True)
    interview_preparation = models.CharField(max_length=20, default= None, blank = True)
    travel_and_health = models.CharField(max_length=20, default= None, blank = True)
    travel_arrangements = models.CharField(max_length=20, default= None, blank = True)

    def __str__(self):
        return self.user.username
class AgentExpertise(models.Model):
    user = models.OneToOneField(User)
    visa_ratio = models.CharField(max_length=20, default= None, blank = True)
    experience = models.CharField(max_length=20, default= None, blank = True)
    regional_office = models.CharField(max_length=300, default= None, blank = True)
    branches = models.CharField(max_length=250, default= None, blank = True)
    number_of_counselors = models.CharField(max_length=20, default= None, blank = True)


    def __str__(self):
        return self.user.username
class AgentFees(models.Model):

    user = models.OneToOneField(User)
    processing_fee = models.CharField(max_length = 10, default = None, blank =True)
    language_fee = models.CharField(max_length = 10, default = None, blank =True)
    refusal_fee = models.CharField(max_length = 10, default = None, blank =True)
    Interview_fee = models.CharField(max_length = 10, default = None, blank =True)
    scholarshipfee = models.CharField(max_length = 10, default = None, blank =True)
    def __str__(self):
        return self.user.username
class AgentLogo(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to = 'agent_logo',blank = True)
