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
    Abbottabad = 'Abbottabad'
    Adezai = 'Adezai'
    AhmedNagerChatha = 'Ahmed Nager Chatha'
    AhmedpurEast = 'Ahmedpur East'
    AliBandar = 'Ali Bandar'
    AliPur = 'Ali Pur'
    Arifwala = 'Arifwala'
    Astor = 'Astor'
    Attock = 'Attock'
    Ayubia = 'Ayubia'
    Baden = 'Baden'
    Bagh = 'Bagh'
    Bahawalnagar = 'Bahawalnagar'
    Bahawalpur = 'Bahawalpur'
    Bajaur = 'Bajaur'
    BandaDaudShah = 'Banda Daud Shah'
    Bannu = 'Bannu'
    Baramula = 'Baramula'
    BastiMalook = 'Basti Malook'
    Batagram = 'Batagram'
    Bazdar  = 'Bazdar'
    Bela = 'Bela'
    Bellpat = 'Bellpat'
    Bhagalchur = 'Bhagalchur'
    Bhaipheru = 'Bhaipheru'
    Bhakkar = 'Bhakkar'
    Bhalwal = 'Bhalwal'
    Bhimber = 'Bhimber'
    Buner = 'Buner'
    Birote = 'Birote'
    Burewala = 'Burewala'
    Burj = 'Burj'
    Chachro = 'Chachro'
    Chagai = 'Chagai'
    ChahSandan = 'Chah Sandan'
    Chailianwala = 'Chailianwala'
    Chakdara = 'Chakdara'
    Chakku = 'Chakku'
    Chakwal = 'Chakwal'
    Chaman = 'Chaman'
    Charsadda = 'Charsadda'
    Chhatr = 'Chhatr'
    Chichawatni = 'Chichawatni'
    Chiniot = 'Chiniot'
    Chitral = 'Chitral'
    ChowkAzam = 'Chowk Azam'
    ChowkSarwarShaheed = 'Chowk Sarwar Shaheed'
    Dadu = 'Dadu'
    Dalbandin = 'Dalbandin'
    Dargai = 'Dargai'
    DaryaKhan = 'Darya Khan'
    Daska = 'Daska'
    DeraBugti = 'Dera Bugti'
    DeraGhaziKhan = 'Dera Ghazi Khan'
    DeraIsmailKhan = 'Dera Ismail Khan'
    DerawarFort = 'Derawar Fort'
    DhanaSar = 'Dhana Sar'
    Dhaular = 'Dhaular'
    Digri = 'Digri'
    DinaCity = 'Dina City'
    Dinga = 'Dinga'
    Dipalpur = 'Dipalpur'
    Diplo = 'Diplo'
    Diwana = 'Diwana'
    Dokri = 'Dokri'
    Drasan = 'Drasan'
    Drosh = 'Drosh'
    Duki = 'Duki'
    Dushi = 'Dushi'
    Duzab = 'Duzab'
    Faisalabad = 'Faisalabad'
    FatehJang = 'Fateh Jang'
    Gadar = 'Gadar'
    Gajar = 'Gajar'
    GarhiKhairo = 'Garhi Khairo'
    Garruck = 'Garruck'
    GhakharMandi = 'Ghakhar Mandi'
    Ghanian = 'Ghanian'
    Ghauspur = 'Ghauspur'
    Ghazluna = 'Ghazluna'
    Ghotki = 'Ghotki'
    Gilgit = 'Gilgit'
    Girdan = 'Girdan'
    GujarKhan = 'Gujar Khan'
    Gujranwala = 'Gujranwala'
    Gujrat = 'Gujrat'
    Gulistan = 'Gulistan'
    Gwadar = 'Gwadar'
    Gwash = 'Gwash'
    HabChauki = 'Hab Chauki'
    Hafizabad = 'Hafizabad'
    Hala = 'Hala'
    Hameedabad = 'Hameedabad'
    Hangu = 'Hangu'
    Haripur = 'Haripur'
    Harnai = 'Harnai'
    Haroonabad = 'Haroonabad'
    Hasilpur = 'Hasilpur'
    HaveliLakha = 'Haveli Lakha'
    Hinglaj = 'Hinglaj'
    Hoshab = 'Hoshab'
    Hunza = 'Hunza'
    Hyderabad = 'Hyderabad'
    Islamkot = 'Islamkot'
    Ispikan = 'Ispikan'
    Jacobabad = 'Jacobabad'
    Jahania = 'Jahania'

    JallaAraain = 'Jalla Araain'
    Jamesabad = 'Jamesabad'
    Jampur = 'Jampur'
    Jamshoro = 'Jamshoro'
    Janghar = 'Janghar'
    Jati = 'Jati (Mughalbhin)'
    Jauharabad = 'Jauharabad'
    JhalJhao = 'Jhal Jhao'
    Jhang = 'Jhang'
    Jhatpat = 'Jhatpat'
    Jhelum = 'Jhelum'
    Jhudo = 'Jhudo'
    Jiwani = 'Jiwani'
    Jungshahi = 'Jungshahi'
    Kalabagh = 'Kalabagh'
    Kalam = 'Kalam'
    Kalandi = 'Kalandi'
    Kalat = 'Kalat'
    Kamalia = 'Kamalia'
    Kamararod = 'Kamararod'
    Kamokey = 'Kamokey'
    Kanak = 'Kanak'
    Kandi = 'Kandi'
    Kandiaro = 'Kandiaro'
    Kanpur = 'Kanpur'
    Kapip = 'Kapip'
    Kappar = 'Kappar'
    Karachi = 'Karachi'
    Karak = 'Karak'
    Karodi = 'Karodi'
    KarorLalEsan = 'Karor Lal Esan'
    Kashmor = 'Kashmor'
    Kasur = 'Kasur'
    Katuri = 'Katuri'
    KetiBandar = 'Keti Bandar'
    Khairpur = 'Khairpur'
    Khanaspur = 'Khanaspur'
    Khanewal = 'Khanewal'
    Khanpur = 'Khanpur'
    Kharan = 'Kharan'
    Kharian = 'Kharian'
    Khokhropur = 'Khokhropur'
    Khora = 'Khora'
    khuiratta = 'khuiratta'
    Khushab = 'Khushab'
    Khuzdar = 'Khuzdar'
    Khyber = 'Khyber'
    Kikki = 'Kikki'
    Klupro = 'Klupro'
    Kohan = 'Kohan'
    Kohat = 'Kohat'
    Kohistan = 'Kohistan'
    Kohlu = 'Kohlu'
    Korak = 'Korak'
    Korangi = 'Korangi'
    KotAddu = 'Kot Addu'
    KotSarae = 'Kot Sarae'
    Kotli = 'Kotli'
    Kotri = 'Kotri'
    Kurram = 'Kurram'
    Laar = 'Laar'
    Lahore = 'Lahore'
    Lahri = 'Lahri'
    LakkiMarwat = 'Lakki Marwat'
    Lalamusa = 'Lalamusa'
    Larkana = 'Larkana'
    Lasbela = 'Lasbela'
    Latamber = 'Latamber'
    Layyah = 'Layyah'
    Liari = 'Liari'
    Lodhran = 'Lodhran'
    Loralai = 'Loralai'
    LowerDir = 'Lower Dir'
    Lund = 'Lund'
    Mach = 'Mach'
    Madyan = 'Madyan'
    Mailsi = 'Mailsi'
    MakhdoomAali = 'Makhdoom Aali'
    Malakand = 'Malakand'
    Mamoori = 'Mamoori'
    Mand = 'Mand'
    MandiBahauddin = 'Mandi Bahauddin'
    MandiWarburton = 'Mandi Warburton'
    Mangla = 'Mangla'

    Manguchar = 'Manguchar'
    Mansehra = 'Mansehra'
    Mardan = 'Mardan'
    MashkiChah = 'Mashki Chah'
    Maslti = 'Maslti'
    Mastuj = 'Mastuj'
    Mastung = 'Mastung'
    Mathi = 'Mathi'
    Matiari = 'Matiari'
    Mehar = 'Mehar'
    Mekhtar = 'Mekhtar'
    Merui = 'Merui'
    MianChannu = 'Mian Channu'
    Mianez = 'Mianez'
    Mianwali = 'Mianwali'
    Minawala = 'Minawala'
    MiramShah = 'Miram Shah'
    Mirpur = 'Mirpur'
    MirpurBatoro = 'Mirpur Batoro'
    MirpurKhas = 'Mirpur Khas'
    MirpurSakro = 'Mirpur Sakro'
    Mithani = 'Mithani'
    Mithi = 'Mithi'
    Mohmand = 'Mohmand'
    Mongora = 'Mongora'
    Moro = 'Moro'
    Multan = 'Multan'
    MurghaKibzai = 'Murgha Kibzai'
    City  =(
            (Abbottabad , 'Abbottabad'),
        	(Adezai , 'Adezai'),
        	(AhmedNagerChatha , 'Ahmed Nager Chatha'),
        	(AhmedpurEast , 'Ahmedpur East'),
        	(AliBandar , 'Ali Bandar'),
        	(AliPur , 'Ali Pur'),
        	(Arifwala , 'Arifwala'),
        	(Astor , 'Astor'),
        	(Attock , 'Attock'),
        	(Ayubia , 'Ayubia'),
        	(Baden , 'Baden'),
        	(Bagh , 'Bagh'),
        	(Bahawalnagar , 'Bahawalnagar'),
        	(Bahawalpur , 'Bahawalpur'),
        	(Bajaur , 'Bajaur'),
        	(BandaDaudShah , 'Banda Daud Shah'),
        	(Bannu , 'Bannu'),
        	(Baramula , 'Baramula'),
        	(BastiMalook , 'Basti Malook'),
        	(Batagram , 'Batagram'),
        	(Bazdar , 'Bazdar'),
        	(Bela , 'Bela'),
        	(Bellpat , 'Bellpat'),
        	(Bhagalchur , 'Bhagalchur'),
        	(Bhaipheru , 'Bhaipheru'),
        	(Bhakkar , 'Bhakkar'),
        	(Bhalwal , 'Bhalwal'),
        	(Bhimber , 'Bhimber'),
        	(Birote , 'Birote'),
        	(Buner , 'Buner'),
        	(Burewala , 'Burewala'),
        	(Burj , 'Burj'),
        	(Chachro , 'Chachro'),
        	(Chagai , 'Chagai'),
        	(ChahSandan , 'Chah Sandan'),
        	(Chailianwala , 'Chailianwala'),
        	(Chakdara , 'Chakdara'),
        	(Chakku , 'Chakku'),
        	(Chakwal , 'Chakwal'),
        	(Chaman , 'Chaman'),
        	(Charsadda , 'Charsadda'),
        	(Chhatr , 'Chhatr'),
        	(Chichawatni , 'Chichawatni'),
        	(Chiniot , 'Chiniot'),
        	(Chitral , 'Chitral'),
        	(ChowkAzam , 'Chowk Azam'),
        	(ChowkSarwarShaheed , 'Chowk Sarwar Shaheed'),
        	(Dadu , 'Dadu'),
        	(Dalbandin , 'Dalbandin'),
        	(Dargai , 'Dargai'),
        	(DaryaKhan , 'Darya Khan'),
        	(Daska , 'Daska'),
        	(DeraBugti , 'Dera Bugti'),
        	(DeraGhaziKhan , 'Dera Ghazi Khan'),
        	(DeraIsmailKhan , 'Dera Ismail Khan'),
        	(DerawarFort , 'Derawar Fort'),
        	(DhanaSar , 'Dhana Sar'),
        	(Dhaular , 'Dhaular'),
        	(Digri , 'Digri'),
        	(DinaCity , 'Dina City'),
        	(Dinga , 'Dinga'),
        	(Dipalpur , 'Dipalpur'),
        	(Diplo , 'Diplo'),
        	(Diwana , 'Diwana'),
        	(Dokri , 'Dokri'),
        	(Drasan , 'Drasan'),
        	(Drosh , 'Drosh'),
        	(Duki , 'Duki'),
        	(Dushi , 'Dushi'),
        	(Duzab , 'Duzab'),
        	(Faisalabad , 'Faisalabad'),
        	(FatehJang , 'Fateh Jang'),
        	(Gadar , 'Gadar'),
        	(Gajar , 'Gajar'),
        	(GarhiKhairo , 'Garhi Khairo'),
        	(Garruck , 'Garruck'),
        	(GhakharMandi , 'Ghakhar Mandi'),
        	(Ghanian , 'Ghanian'),
        	(Ghauspur , 'Ghauspur'),
        	(Ghazluna , 'Ghazluna'),
        	(Ghotki , 'Ghotki'),
        	(Gilgit , 'Gilgit'),
        	(Girdan , 'Girdan'),
        	(GujarKhan , 'Gujar Khan'),
        	(Gujranwala , 'Gujranwala'),
        	(Gujrat , 'Gujrat'),
        	(Gulistan , 'Gulistan'),
        	(Gwadar , 'Gwadar'),
        	(Gwash , 'Gwash'),
        	(HabChauki , 'Hab Chauki'),
        	(Hafizabad , 'Hafizabad'),
        	(Hala , 'Hala'),
        	(Hameedabad , 'Hameedabad'),
        	(Hangu , 'Hangu'),
        	(Haripur , 'Haripur'),
        	(Harnai , 'Harnai'),
        	(Haroonabad , 'Haroonabad'),
        	(Hasilpur , 'Hasilpur'),
        	(HaveliLakha , 'Haveli Lakha'),
        	(Hinglaj , 'Hinglaj'),
        	(Hoshab , 'Hoshab'),
        	(Hunza , 'Hunza'),
        	(Hyderabad , 'Hyderabad'),
        	(Islamkot , 'Islamkot'),
        	(Ispikan , 'Ispikan'),
        	(Jacobabad , 'Jacobabad'),
        	(Jahania , 'Jahania'),
        	(JallaAraain , 'Jalla Araain'),
        	(Jamesabad , 'Jamesabad'),
        	(Jampur , 'Jampur'),
        	(Jamshoro , 'Jamshoro'),
        	(Janghar , 'Janghar'),
        	(Jati , 'Jati (Mughalbhin)'),
        	(Jauharabad , 'Jauharabad'),
        	(JhalJhao , 'Jhal Jhao'),
        	(Jhang , 'Jhang'),
        	(Jhatpat , 'Jhatpat'),
        	(Jhelum , 'Jhelum'),
        	(Jhudo , 'Jhudo'),
        	(Jiwani , 'Jiwani'),
        	(Jungshahi , 'Jungshahi'),
        	(Kalabagh , 'Kalabagh'),
        	(Kalam , 'Kalam'),
        	(Kalandi , 'Kalandi'),
        	(Kalat , 'Kalat'),
        	(Kamalia , 'Kamalia'),
        	(Kamararod , 'Kamararod'),
        	(Kamokey , 'Kamokey'),
        	(Kanak , 'Kanak'),
        	(Kandi , 'Kandi'),
        	(Kandiaro , 'Kandiaro'),
        	(Kanpur , 'Kanpur'),
        	(Kapip , 'Kapip'),
        	(Kappar , 'Kappar'),
        	(Karachi , 'Karachi'),
        	(Karak , 'Karak'),
        	(Karodi , 'Karodi'),
        	(KarorLalEsan , 'Karor Lal Esan'),
        	(Kashmor , 'Kashmor'),
        	(Kasur , 'Kasur'),
        	(Katuri , 'Katuri'),
        	(KetiBandar , 'Keti Bandar'),
        	(Khairpur , 'Khairpur'),
        	(Khanaspur , 'Khanaspur'),
        	(Khanewal , 'Khanewal'),
        	(Khanpur , 'Khanpur'),
        	(Kharan , 'Kharan'),
        	(Kharian , 'Kharian'),
        	(Khokhropur , 'AKhokhropur'),
        	(Khora , 'Khora'),
        	(khuiratta , 'khuiratta'),
        	(Khushab , 'Khushab'),
        	(Khuzdar , 'Khuzdar'),
        	(Khyber , 'Khyber'),
        	(Kikki , 'Kikki'),
        	(Klupro , 'Klupro'),
        	(Kohan , 'Kohan'),
        	(Kohat , 'Kohat'),
        	(Kohistan , 'Kohistan'),
        	(Kohlu , 'Kohlu'),
        	(Korak , 'Korak'),
        	(Korangi , 'Korangi'),
        	(KotAddu , 'Kot Addu'),
        	(KotSarae , 'Kot Sarae'),
        	(Kotli , 'Kotli'),
        	(Kotri , 'Kotri'),
        	(Kurram , 'Kurram'),
        	(Laar , 'Laar'),
        	(Lahore , 'Lahore'),
        	(Lahri , 'Lahri'),
        	(LakkiMarwat , 'Lakki Marwat'),
        	(Lalamusa , 'Lalamusa'),
        	(Larkana , 'Larkana'),
        	(Lasbela , 'Lasbela'),
        	(Latamber , 'Latamber'),
        	(Layyah , 'Layyah'),
        	(Liari , 'Liari'),
        	(Lodhran , 'Lodhran'),
        	(Loralai , 'Loralai'),
        	(LowerDir , 'Lower Dir'),
        	(Lund , 'Lund'),
        	(Mach , 'Mach'),
        	(Madyan , 'Madyan'),
        	(Mailsi , 'Mailsi'),
        	(MakhdoomAali , 'Makhdoom Aali'),
        	(Malakand , 'Malakand'),
        	(Mamoori , 'Mamoori'),
        	(Mand , 'Mand'),
        	(MandiBahauddin , 'Mandi Bahauddin'),
        	(MandiWarburton , 'Mandi Warburton'),
        	(Mangla , 'Mangla'),
        	(Manguchar , 'Manguchar'),
        	(Mansehra , 'Mansehra'),
        	(Mardan , 'Mardan'),
        	(MashkiChah , 'Mashki Chah'),
        	(Maslti , 'Maslti'),
        	(Mastuj , 'Mastuj'),
        	(Mastung , 'Mastung'),
        	(Mathi , 'Mathi'),
        	(Matiari , 'Matiari'),
        	(Mehar , 'Mehar'),
        	(Mekhtar , 'Mekhtar'),
        	(Merui , 'Merui'),
        	(MianChannu , 'Mian Channu'),
        	(Mianez , 'Mianez'),
        	(Mianwali , 'Mianwali'),
        	(Minawala , 'Minawala'),
        	(MiramShah , 'Miram Shah'),
        	(Mirpur , 'Mirpur'),
        	(MirpurBatoro , 'Mirpur Batoro'),
        	(MirpurKhas , 'Mirpur Khas'),
        	(MirpurSakro , 'Mirpur Sakro'),
        	(Mithani , 'Mithani'),
        	(Mithi , 'Mithi'),
        	(Mohmand , 'Mohmand'),
        	(Mongora , 'Mongora'),
        	(Moro , 'Moro'),
        	(Multan , 'Multan'),
        	(MurghaKibzai , 'Murgha Kibzai'),

    )
    Country = 'Country'
    Pakistan = 'Pakistan'
    India = 'India'
    Australia = 'Australia'
    UK = 'UK'
    Canada = 'Canada'
    Ireland = 'Ireland'
    NewZealand = 'New Zealand'
    Germany = 'Germany'
    Sweden = 'Sweden'
    Afghanistan = 'Afghanistan'
    Algeria = 'Algeria'
    Albania = 'Albania'
    Andorra = 'Andorra'
    Angola = 'Angola'
    Anguilla = 'Anguilla'
    AntiguaBarbuda = 'Antigua & Barbuda'

    Argentina = 'Argentina'
    Armenia = 'Armenia'
    Austria = 'Austria'
    Azerbaijan = 'Azerbaijan'
    Bahamas = 'Bahamas'
    Bahrain = 'Bahrain'
    Bangladesh = 'Bangladesh'
    Barbados = 'Barbados'
    Belarus = 'Belarus'
    Belgium = 'Belgium'
    Belize = 'Belize'
    Benin = 'Benin'
    Bermuda = 'Bermuda'
    Bhutan = 'Bhutan'
    Bolivia = 'Bolivia'
    BosniaHerzegovina = 'Bosnia & Herzegovina'
    Botswana = 'Botswana'
    Brazil = 'Brazil'
    BruneiDarussalam = 'Brunei Darussalam'
    Bulgaria = 'Bulgaria'
    BurkinaFaso = 'Burkina Faso'
    MyanmarBurma = 'Myanmar/Burma'
    Burundi = 'Burundi'
    Cambodia = 'Cambodia'
    Cameroon = 'Cameroon'
    CapeVerde = 'Cape Verde'
    CaymanIslands = 'Cayman Islands'
    CentralAfrican = 'Central African'
    ChadRepublic = 'Chad Republic'
    Chile = 'Chile'
    China = 'China'
    Colombia = 'Colombia'
    Comoros = 'Comoros'
    Congo = 'Congo'
    CostaRica = 'Costa Rica'
    Croatia = 'Croatia'
    Cuba = 'Cuba'
    Cyprus = 'Cyprus'
    CzechRepublic = 'Czech Republic'
    DemocraticRepublicoftheCongo = 'Democratic Republic of the Congo'
    Denmark = 'Denmark'
    Djibouti = 'Djibouti'
    DominicanRepublic = 'Dominican Republic'
    Dominica = 'Dominica'
    Ecuador = 'Ecuador'
    Egypt = 'Egypt'
    ElSalvador = 'El Salvador'
    EquatorialGuinea = 'Equatorial Guinea'
    Eritrea ='Eritrea'
    Estonia = 'Estonia'
    Ethiopia = 'Ethiopia'
    Fiji = 'Fiji'
    Finland = 'Finland'
    France = 'France'
    FrenchGuiana = 'French Guiana'
    Gabon = 'Gabon'
    Gambia = 'Gambia'
    Georgia = 'Georgia'
    Ghana = 'Ghana'
    GreatBritain = 'Great Britain'
    Greece = 'Greece'
    Grenada = 'Grenada'
    Guadeloupe = 'Guadeloupe'
    Guatemala = 'Guatemala'
    Guinea = 'Guinea'
    GuineaBissau = 'Guinea-Bissau'
    Guyana = 'Guyana'
    Haiti = 'Haiti'
    Honduras = 'Honduras'
    Hungary = 'Hungary'
    Iceland = 'Iceland'
    Indonesia = 'Indonesia'
    Iran = 'Iran'
    Iraq = 'Iraq'
    IsraelandtheOccupiedTerritories = 'Israel and the Occupied Territories'
    Italy = 'Italy'
    IvoryCoast = 'Ivory Coast (Cote dIvoire)'
    Jamaica = 'Jamaica'
    Japan = 'Japan'
    Jordan = 'Jordan'
    Kazakhstan = 'Kazakhstan'
    Kenya = 'Kenya'
    Kosovo = 'Kosovo'
    Kuwait = 'Kuwait'
    Korea = 'Korea'
    KyrgyzRepublic ='Kyrgyz Republic (Kyrgyzstan)'
    Laos = 'Laos'
    Latvia = 'Latvia'
    Lebanon = 'Lebanon'
    Lesotho = 'Lesotho'
    Liberia = 'Liberia'
    Libya = 'Libya'
    Liechtenstein = 'Liechtenstein'
    Lithuania = 'Lithuania'
    Luxembourg = 'Luxembourg'
    RepublicofMacedonia = 'Republic of Macedonia'
    Madagascar = 'Madagascar'
    Malawi = 'Malawi'
    Malaysia = 'Malaysia'
    Maldives = 'Maldives'
    Mali = 'Mali'
    Malta = 'Malta'
    Martinique = 'Martinique'
    Mauritania = 'Mauritania'
    Mauritius = 'Mauritius'
    Mayotte = 'Mayotte'
    Mexico = 'Mexico'
    Moldova = 'Moldova'
    Mongolia = 'Mongolia'
    Montenegro = 'Montenegro'
    Montserrat = 'Montserrat'
    Morocco = 'Morocco'
    Mozambique = 'Mozambique'
    Namibia = 'Namibia'
    Nepal = 'Nepal'
    Netherlands = 'Netherlands'
    NewZealand = 'New Zealand'
    Nicaragua = 'Nicaragua'
    Niger = 'Niger'
    Nigeria = 'Nigeria'
    Oman = 'Oman'
    PacificIslands = 'Pacific Islands'
    Pakistan = 'Pakistan'
    Panama = 'Panama'
    PapuaNewGuinea = 'Papua New Guinea'
    Paraguay = 'Paraguay'
    Peru = 'Peru'
    Philippines = 'Philippines'
    Poland = 'Poland'
    Portugal = 'Portugal'
    PuertoRico = 'Puerto Rico'
    Qatar = 'Qatar'
    Reunion = 'Reunion'
    Romania = 'Romania'
    RussianFederation = 'Russian Federation'
    Rwanda = 'Rwanda'
    SaintKittsandNevis = 'Saint Kitts and Nevis'
    SaintLucia = 'Saint Lucia'
    SaintVincentGrenadines  ='Saint Vincents & Grenadines'
    Samoa = 'Samoa'
    SaoTomeandPrincipe = 'Sao Tome and Principe'
    SaudiArabia = 'Saudi Arabia'
    Senegal = 'Senegal'
    Serbia = 'Serbia'
    Seychelles = 'Seychelles'
    SierraLeone = 'Sierra Leone'
    Singapore = 'Singapore'
    SlovakRepublic = 'Slovak Republic'
    Slovenia = 'Slovenia'
    SolomonIslands = 'Solomon Islands'
    Somalia = 'Somalia'
    SouthAfrica = 'South Africa'
    RepublicofSouthKorea = 'Korea, Republic of (South Korea)'
    SouthSudan = 'South Sudan'
    Spain = 'Spain'
    SriLanka = 'Sri Lanka'
    Sudan = 'Sudan'
    Suriname = 'Suriname'
    Swaziland = 'Swaziland'
    Switzerland = 'Switzerland'
    Syria = 'Syria'
    Tajikistan = 'Tajikistan'
    Tanzania = 'Tanzania'
    Thailand = 'Thailand'
    TimorLeste = 'Timor Leste'
    Togo = 'Togo'
    TrinidadTobago = 'Trinidad & Tobago'
    Turkey = 'Turkey'
    Turkmenistan = 'Turkmenistan'
    TurksCaicos = 'Turks & Caicos'
    Uganda = 'Uganda'
    Ukraine = 'Ukraine'
    UnitedArabEmirates = 'United Arab Emirates'
    Uruguay = 'Uruguay'
    USA = 'USA'
    Uzbekistan = 'Uzbekistan'
    Venezuela = 'Venezuela'
    Vietnam = 'Vietnam'
    VirginIslandsUK = 'Virgin Islands (UK)'
    VirginIslandsUS = 'Virgin Islands (US)'
    Yemen = 'Yemen'
    Zambia  = 'Zambia '
    Zimbabwe = 'Zimbabwe'
    Norway = 'Norway'






    Country = (
        (Country, 'Country'),
    (Australia , 'Australia'),
	(USA , 'USA'),
	(Canada , 'Canada'),
	(UK , 'UK'),
	(Ireland , 'Ireland'),
	(NewZealand , 'NewZealand'),
	(Germany , 'Germany'),
	(Sweden , 'Sweden'),

	(Afghanistan , 'Afghanistan'),
	(Albania , 'Albania'),
	(Algeria , 'Algeria'),
	(Andorra , 'Andorra'),
	(Angola , 'Angola'),
	(Anguilla , 'Anguilla'),
	(AntiguaBarbuda , 'Antigua & Barbuda'),
	(Argentina , 'Argentina'),
	(Armenia , 'Armenia'),
	(Austria , 'Austria'),
	(Azerbaijan , 'Azerbaijan'),
	(Bahamas , 'Bahamas'),
	(Bahrain , 'Bahrain'),
	(Bangladesh , 'Bangladesh'),
	(Barbados , 'Barbados'),
	(Belarus , 'Belarus'),
	(Belgium , 'Belgium'),
	(Belize , 'Belize'),
	(Benin , 'Benin'),
	(Bermuda , 'Bermuda'),
	(Bhutan , 'Bhutan'),
	(Bolivia , 'Bolivia'),
	(BosniaHerzegovina , 'Bosnia & Herzegovina'),
	(Botswana , 'Botswana'),
	(Brazil , 'Brazil'),
	(BruneiDarussalam , 'Brunei Darussalam'),
	(Bulgaria , 'Bulgaria'),
	(BurkinaFaso , 'Burkina Faso'),
	(MyanmarBurma , 'Myanmar/Burma'),
	(Burundi , 'Burundi'),
	(Cambodia , 'Cambodia'),
	(Cameroon , 'Cameroon'),
	(CapeVerde , 'Cape Verde'),
	(CaymanIslands , 'Cayman Islands'),
	(CentralAfrican , 'Central African'),
	(ChadRepublic , 'Chad Republic'),
	(Chile , 'Chile'),
	(China , 'China'),
	(Colombia , 'Colombia'),
	(Comoros , 'Comoros'),
	(Congo , 'Congo'),
	(CostaRica , 'Costa Rica'),
	(Croatia , 'Croatia'),
	(Cuba , 'Cuba'),
	(Cyprus , 'Cyprus'),
	(CzechRepublic , 'Czech Republic'),
	(DemocraticRepublicoftheCongo , 'Democratic Republic of the Congo'),
	(Denmark , 'Denmark'),
	(Djibouti , 'Djibouti'),
	(DominicanRepublic , 'Dominican Republic'),
	(Dominica , 'Dominica'),
	(Ecuador , 'Ecuador'),
	(Egypt , 'Egypt'),
	(ElSalvador , 'El Salvador'),
	(EquatorialGuinea , 'Equatorial Guinea'),
	(Eritrea , 'Eritrea'),
	(Estonia , 'Estonia'),
	(Ethiopia , 'Ethiopia'),
	(Fiji , 'Fiji'),
	(Finland , 'Finland'),
	(France , 'France'),
	(FrenchGuiana , 'French Guiana'),
	(Gabon , 'Gabon'),
	(Gambia , 'Gambia'),
	(Georgia , 'Georgia'),
	(Ghana , 'Ghana'),
	(GreatBritain , 'Great Britain'),
	(Greece , 'Greece'),
	(Grenada , 'Grenada'),
	(Guadeloupe , 'Guadeloupe'),
	(Guatemala , 'Guatemala'),
	(Guinea , 'Guinea'),
	(GuineaBissau , 'Guinea-Bissau'),
	(Guyana , 'Guyana'),
	(Haiti , 'Haiti'),
	(Honduras , 'Honduras'),
	(Hungary , 'Hungary'),
	(Iceland , 'Iceland'),
	(India , 'India'),
	(Indonesia , 'Indonesia'),
	(Iran , 'Iran'),
	(Iraq , 'Iraq'),
	(IsraelandtheOccupiedTerritories , 'Israel and the Occupied Territories'),
	(Italy , 'Italy'),
	(IvoryCoast , 'Ivory Coast (Cote dIvoire)'),
	(Jamaica , 'Jamaica'),
	(Japan , 'Japan'),
	(Jordan , 'Jordan'),
	(Kazakhstan , 'Kazakhstan'),
	(Kenya , 'Kenya'),
	(Kosovo , 'Kosovo'),
	(Kuwait , 'Kuwait'),
	(Korea , 'Korea'),
	(KyrgyzRepublic , 'Kyrgyz Republic (Kyrgyzstan)'),
	(Laos , 'Laos'),
	(Latvia , 'Latvia'),
	(Lebanon , 'Lebanon'),
	(Lesotho , 'Lesotho'),
	(Liberia , 'Liberia'),
	(Libya , 'Libya'),
	(Liechtenstein , 'Liechtenstein'),
	(Lithuania , 'Lithuania'),
	(Luxembourg , 'Luxembourg'),
	(RepublicofMacedonia , 'Republic of Macedonia'),
	(Madagascar , 'Madagascar'),
	(Malawi , 'Malawi'),
	(Malaysia , 'Malaysia'),
	(Maldives , 'Maldives'),
	(Mali , 'Mali'),
	(Malta , 'Malta'),
	(Martinique , 'Martinique'),
	(Mauritania , 'Mauritania'),
	(Mauritius , 'Mauritius'),
	(Mayotte , 'Mayotte'),
	(Mexico , 'Mexico'),
	(Moldova , 'Moldova'),
	(Mongolia , 'Mongolia'),
	(Montenegro , 'Montenegro'),
	(Montserrat , 'Montserrat'),
	(Morocco , 'Morocco'),
	(Mozambique , 'Mozambique'),
	(Namibia , 'Namibia'),
	(Nepal , 'Nepal'),
	(Netherlands , 'Netherlands'),
	(NewZealand , 'NewZealand'),
	(Nicaragua , 'Nicaragua'),
	(Niger , 'Niger'),
	(Nigeria , 'Nigeria'),
	(Norway , 'Norway'),
	(Oman , 'Oman'),
	(PacificIslands , 'Pacific Islands'),
	(Pakistan , 'Pakistan'),
	(Panama , 'Panama'),
	(PapuaNewGuinea , 'Papua New Guinea'),
	(Paraguay , 'Paraguay'),
	(Peru , 'Peru'),
	(Philippines , 'Philippines'),
	(Poland , 'Poland'),
	(Portugal , 'Portugal'),
	(PuertoRico , 'Puerto Rico'),
	(Qatar , 'Qatar'),
	(Reunion , 'Reunion'),
	(Romania , 'Romania'),
	(RussianFederation , 'Russian Federation'),
	(Rwanda , 'Rwanda'),
	(SaintKittsandNevis , 'Saint Kitts and Nevis'),
	(SaintLucia , 'Saint Lucia'),
	(SaintVincentGrenadines , 'Saint Vincents & Grenadines'),
	(Samoa , 'Samoa'),
	(SaoTomeandPrincipe , 'Sao Tome and Principe'),
	(SaudiArabia , 'Saudi Arabia'),
	(Senegal , 'Senegal'),
	(Serbia , 'Serbia'),
	(Seychelles , 'Seychelles'),
	(SierraLeone , 'Sierra Leone'),
	(Singapore , 'Singapore'),
	(SlovakRepublic , 'Slovak Republic'),
	(Slovenia , 'Slovenia'),
	(SolomonIslands , 'Solomon Islands'),
	(Somalia , 'Somalia'),
	(SouthAfrica , 'South Africa'),

	(SouthSudan , 'South Sudan'),
	(Spain , 'Spain'),
	(SriLanka , 'Sri Lanka'),
	(Sudan , 'Sudan'),
	(Suriname , 'Suriname'),
	(Swaziland , 'Swaziland'),
	(Switzerland , 'Switzerland'),
	(Syria , 'Syria'),
	(Tajikistan , 'Tajikistan'),
	(Tanzania , 'Tanzania'),
	(Thailand , 'Thailand'),
	(TimorLeste , 'Timor Leste'),
	(Togo , 'Togo'),
	(TrinidadTobago , 'Trinidad & Tobago'),
	(Turkey , 'Turkey'),
	(Turkmenistan , 'Turkmenistan'),
	(TurksCaicos , 'Turks & Caicos'),
	(Uganda , 'Uganda'),
	(Ukraine , 'Ukraine'),
	(UnitedArabEmirates , 'United Arab Emirates'),
	(Uruguay , 'Uruguay'),
	(Uzbekistan , 'Uzbekistan'),
	(Venezuela , 'Venezuela'),
	(Vietnam , 'Vietnam'),
	(VirginIslandsUS , 'Virgin Islands (US)'),
    (VirginIslandsUK , 'Virgin Islands (UK)'),
	(Yemen , 'Yemen'),
	(Zambia , 'Zambia'),
	(Zimbabwe , 'Zimbabwe'),

    )

    PopularDestinations = 'Popular Destinations'



    Subject = 'subject'
    AppliedArts = 'Applied Arts'
    AppliedMathematics = 'Applied Mathematics'
    AppliedSciencesProfessions = 'Applied Sciences & Professions'
    AquacultureFisheries = 'Aquaculture & Fisheries'
    Arabic = 'Arabic'
    Archaeology = 'Archaeology'
    Architecture = 'Architecture'
    AreaCulturalStudies = 'Area & Cultural Studies'
    ArtHistory = 'Art History'
    Arts = 'Arts'
    ArtsDesign = 'Arts & Design'
    Astronomy = 'Astronomy'
    Audio = 'Audio'
    Auditing = 'Auditing'
    Automotive = 'Automotive'
    AutomotiveEngineering = 'Automotive Engineering'
    Aviation = 'Aviation'
    Banking = 'Banking'
    BasicMedicalSciences = 'Basic Medical Sciences'
    Beauty = 'Beauty'
    BioBiomedicalEngineering = 'Bio & Biomedical Engineering'
    BiodiversityConservation = 'Biodiversity & Conservation'
    Biology = 'Biology'
    Biomedicine = 'Biomedicine'
    Biotechnology = 'Biotechnology'
    BusinessManagement = 'Business & Management'
    BusinessAdministration = 'Business Administration'
    BusinessInformationSystems = 'Business Information Systems'
    BusinessIntelligenceAnalytics = 'Business Intelligence & Analytics'
    BusinessLaw = 'Business Law'
    BusinessMath = 'Business Math'
    ChemicalEngineering = 'Chemical Engineering'
    Chemistry = 'Chemistry'
    ChildDevelopmentAndFamilyLife = 'Child Development And Family Life'
    ChristianStudies = 'Christian Studies'
    Civics = 'Civics'
    CivicsForNonMuslim = 'Civics For Non Muslim'
    CivilPrivateLaw = 'Civil & Private Law'
    CivilEngineeringConstruction = 'Civil Engineering & Construction'
    ClimateStudiesMeteorology = 'Climate Studies & Meteorology'
    ClinicalPathologySerology = 'Clinical Pathology & Serology'
    ClothingTextile = 'Clothing & Textile'
    Coaching = 'Coaching'
    CognitiveSciences = 'Cognitive Sciences'
    Commerce = 'Commerce'
    CommercialGeography = 'Commercial Geography'
    CommercialPractice = 'Commercial Practice'
    CommunicationSciences = 'Communication Sciences'
    Communications = 'Communications'
    ComplementaryAlternativeMedicine = 'Complementary & Alternative Medicine'
    ComputerScience = 'Computer Science'
    ComputerScienceIT = 'Computer Science & IT'
    Computing = 'Computing'
    Cookery = 'Cookery'
    CorporateCommunication = 'Corporate Communication'
    CorporateSocialResponsibility = 'Corporate Social Responsibility'
    Cosmetics = 'Cosmetics'
    Counselling = 'Counselling'
    CreativeWriting = 'Creative Writing'
    CriminalLaw = 'Criminal Law'
    Criminology = 'Criminology'
    CulinaryArts = 'Culinary Arts'
    DataScienceBigData = 'Data Science & Big Data'
    DentalHygiene = 'Dental Hygiene'
    Dentistry = 'Dentistry'
    Design = 'Design'
    Digital = 'Digital'
    Earth = 'Earth'
    EarthSciences = 'Earth Sciences'
    Ecology = 'Ecology'
    Econometrics = 'Econometrics'
    EconomicsofWar = 'Economics of War'
    Economics = 'Economics'
    Education = 'Education'
    EducationTraining = 'Education & Training'
    EducationalPsychology = 'Educational Psychology'
    EducationalResearch = 'Educational Research'
    ElectricalEngineering = 'Electrical Engineering'
    Electronics = 'Electronics'
    ElectronicsEmbeddedTechnology = 'Electronics & Embedded Technology'
    ElementaryAnatomyMicrotech = 'Elementary Anatomy & Microtech'
    ElementaryChemistryChemical = 'Elementary Chemistry & Chemical'
    EmergencyDisasterManagement = 'Emergency & Disaster Management'
    EnergyPowerEngineering = 'Energy & Power Engineering'
    Engineering = 'Engineering'
    English = 'English'
    EnglishElective = 'English Elective'
    Entrepreneurship = 'Entrepreneurship'
    EnvironmentalSciences = 'Environmental Sciences'
    EnvironmentalEconomicsPolicy = 'Environmental Economics & Policy'
    EnvironmentalEngineering = 'Environmental Engineering'
    EnvironmentalManagement = 'Environmental Management'
    EthnicStudies = 'Ethnic Studies'
    EuropeanLaw = 'European Law'
    EuropeanStudies = 'European Studies'
    EventManagement = 'Event Management'
    ExecutiveMBA = 'Executive MBA'
    FamilyConsumerScience = 'Family & Consumer Science'
    Fashion = 'Fashion'
    FashionTextilesAndLuxuryGoods = 'Fashion, Textiles And Luxury Goods'
    FilmPhotographyMedia = 'Film, Photography & Media'
    Finance = 'Finance'
    FinancialMathematics = 'Financial Mathematics'
    FineArt = 'Fine Art'
    FoodNutrition = 'Food & Nutrition'
    FoodSciences = 'Food Sciences'
    ForensicAccounting = 'Forensic Accounting'
    ForensicScience = 'Forensic Science'
    Forestry = 'Forestry'
    French = 'French'
    GeneralEngineeringTechnology = 'General Engineering & Technology'
    GeneralStudiesClassics = 'General Studies & Classics'
    GeographicalInformationSystems = 'Geographical Information Systems'
    Geography = 'Geography'
    Geology = 'Geology'
    German = 'German'
    GraphicDesign = 'Graphic Design'
    Hairdressing = 'Hairdressing'
    HealthPhysicalEducation = 'Health & Physical Education'
    HealthInformatics = 'Health Informatics'
    HealthManagement = 'Health Management'
    HealthSciences = 'Health Sciences'
    History = 'History'
    HematologyBloodBanking = 'Hematology & Blood Banking'
    HistoryOfModernWorld = 'History Of Modern World'
    HomeManagement = 'Home Management'
    Horticulture = 'Horticulture'
    HospitalityManagement = 'Hospitality Management'
    HospitalityLeisureSports = 'Hospitality, Leisure & Sports'
    HotelManagement = 'Hotel Management'
    HumanMedicine = 'Human Medicine'
    HumanResourceManagement = 'Human Resource Management'
    Humanities = 'Humanities'
    HydrologyWaterManagement= 'Hydrology & Water Management'
    IndustrialSystemsEngineering = 'Industrial & Systems Engineering'
    IndustrialDesign = 'Industrial Design'
    InformaticsInformationSciences = 'Informatics & Information Sciences'
    InformationTechnology = 'Information Technology'
    InnovationManagement = 'Innovation Management'
    Interior = 'Interior'
    InteriorDesign = 'Interior Design'
    InternationalBusiness = 'International Business'
    InternationalDevelopment = 'International Development'
    InternationalLaw = 'International Law'
    InternationalRelations = 'International Relations'
    Interpreting = 'Interpreting'
    IslamicEducation = 'Islamic Education'
    IslamicHistoryCulture = 'Islamic History & Culture'
    IslamicStudies = 'Islamic Studies'
    ITSecurity = 'IT Security'
    JournalismMedia = 'Journalism & Media'
    LandscapeArchitecture = 'Landscape Architecture'
    LanguageStudies = 'Language Studies'
    Law = 'Law'
    LegalStudies= 'Legal Studies'
    LiberalArts = 'Liberal Arts'
    LibraryScience = 'Library Science'
    Literature = 'Literature'
    ManagementOrganisationLeadership = 'Management, Organisation & Leadership'
    Manufacturing = 'Manufacturing'
    MarineEngineering = 'Marine Engineering'
    Maritime = 'Maritime'
    Marketing = 'Marketing'
    MaterialsScienceEngineering = 'Materials Science & Engineering'
    Mathematics= 'Mathematics'
    MechanicalEngineering = 'Mechanical Engineering'
    Mechatronics = 'Mechatronics'
    MediaStudiesMassMedia = 'Media Studies & Mass Media'
    Medical = 'Medical'
    MedicineHealth = 'Medicine & Health'
    Microbiology = 'Microbiology'
    Midwifery= 'Midwifery'
    MilitaryGeography = 'Military Geography'
    MilitaryScience = 'Military Science'
    Mining = 'Mining'
    ModernHistory = 'Modern History'
    MolecularSciences = 'Molecular Sciences'
    MuseumStudies = 'Museum Studies'
    Music = 'Music'
    MusicHistory = 'Music History'
    MolecularSciences = 'Molecular Sciences'
    MuseumStudies = 'Museum Studies'
    Music = 'Music'
    MusicHistory = 'Music History'
    NaturalResourceManagement = 'Natural Resource Management'
    NaturalSciencesMathematics= 'Natural Sciences & Mathematics'
    NaturalSciences = 'Natural Sciences'
    Neuroscience = 'Neuroscience'
    Nursing = 'Nursing'
    Nutrition = 'Nutrition'
    NutritionDietetics = 'Nutrition & Dietetics'
    OilGas = 'Oil & Gas'
    OrganisationalBehaviour = 'Organisational Behaviour'
    PakistanStudies = 'Pakistan Studies'
    PakistaniCulture = 'Pakistani Culture'
    PatentIntellectualPropertyLaw = 'Patent & Intellectual Property Law'
    Pedagogy = 'Pedagogy'
    Performing = 'Performing'
    Persian = 'Persian'
    Pharmaceutical = 'Pharmaceutical'
    Pharmacy = 'Pharmacy'
    Philosophy = 'Philosophy'
    PhilosophyEthics = 'Philosophy & Ethics'
    Photography = 'Photography'
    Psychology = 'Psychology'
    Physics = 'Physics'
    Physiotherapy = 'Physiotherapy'
    PlantCropSciences = 'Plant & Crop Sciences'
    PoliticalScience = 'Political Science'
    ProjectManagement = 'Project Management'
    PublicAdministration = 'Public Administration'
    PublicHealth = 'Public Health'
    PublicLaw = 'Public Law'
    PublicPolicy = 'Public Policy'
    PublicRelations = 'Public Relations'
    RealEstatePropertyManagement = 'Real Estate & Property Management'
    Recreation = 'Recreation'
    ReligiousStudiesTheology = 'Religious Studies & Theology'
    RetailManagement = 'Retail Management'
    RiskManagement = 'Risk Management'
    Robotics = 'Robotics'
    SocialSciences = 'Social Sciences'
    SocialWelfare = 'Social Welfare'
    Sociology = 'Sociology'
    SoilScience = 'Soil Science'
    Space = 'Space'
    SpecialEducation = 'Special Education'
    SpecialMilitaryStudies = 'Special Military Studies'
    SportRecreationStatistics = 'Sport & Recreation Statistics'
    SupplyChainManagementLogistics = 'Supply Chain Management & Logistics'
    SustainableDevelopment = 'Sustainable Development'
    SustainableEnergy = 'Sustainable Energy'
    Taxation = 'Taxation'
    Teaching = 'Teaching'
    TechnologyManagement = 'Technology Management'
    Television = 'Television'
    TerrorismSecurity = 'Terrorism & Security'
    Textiles = 'Textiles'
    TheatreDance = 'Theatre & Dance'
    Theology = 'Theology'
    Tourism = 'Tourism'
    TourismLeisure = 'Tourism & Leisure'
    Toxicology = 'Toxicology'
    Training = 'Training'
    Translation = 'Translation'
    TranslationInterpreting = 'Translation & Interpreting'
    TransportManagement = 'Transport Management'
    TransportationEngineering = 'Transportation Engineering'
    Typing = 'Typing'
    Veterinary = 'Veterinary'
    VeterinaryMedicine = 'Veterinary Medicine'
    VideoGamesMultimedia = 'Video Games & Multimedia'
    VisualArts = 'Visual Arts'
    War = 'War'
    WebTechnologiesCloudComputing = 'Web Technologies & Cloud Computing'
    Zoology = 'Zoology'


    Subject = (
    (Subject , 'Subject'),

    (AppliedArts , 'Applied Arts'),
    (AppliedMathematics, 'Applied Mathematics'),
    (AppliedSciencesProfessions , 'Applied Sciences & Professions'),
    (AquacultureFisheries , 'Aquaculture & Fisheries'),
    (Arabic , 'Arabic'),
    (Archaeology , 'Archaeology'),
    (Architecture , 'Architecture'),
    (AreaCulturalStudies , 'Area & Cultural Studies'),
    (ArtHistory , 'Art History'),
    (Arts , 'Arts'),
    (ArtsDesign , 'Arts & Design'),
    (Astronomy , 'Astronomy'),
    (Audio , 'Audio'),
    (Auditing , 'Auditing'),
    (Automotive , 'Automotive'),
    (AutomotiveEngineering , 'Automotive Engineering'),
    (Aviation , 'Aviation'),
    (Banking , 'Banking'),
    (BasicMedicalSciences , 'Basic Medical Sciences'),
    (BioBiomedicalEngineering , 'Bio & Biomedical Engineering'),
    (BiodiversityConservation , 'Biodiversity & Conservation'),
    (Biology , 'Biology'),
    (Biomedicine , 'Biomedicine'),
    (Biotechnology , 'Biotechnology'),
    (BusinessManagement , 'Business & Management'),
    (BusinessAdministration , 'Business Administration'),
    (BusinessInformationSystems , 'Business Information Systems'),
    (BusinessIntelligenceAnalytics , 'Business Intelligence & Analytics'),
    (BusinessLaw , 'Business Law'),
    (BusinessMath , 'Business Math'),
    (ChemicalEngineering , 'Chemical Engineering'),
    (Chemistry , 'Chemistry'),
    (ChildDevelopmentAndFamilyLife , 'Child Development And Family Life'),
    (ChristianStudies , 'Christian Studies'),
    (Civics , 'Civics'),
    (CivicsForNonMuslim , 'Civics For Non Muslim'),
    (CivilPrivateLaw , 'Civil & Private Law'),
    (CivilEngineeringConstruction , 'Civil Engineering & Construction'),
    (ClimateStudiesMeteorology , 'Climate Studies & Meteorology'),
    (ClinicalPathologySerology , 'Clinical Pathology & Serology'),
    (ClothingTextile , 'Clothing & Textile'),
    (Coaching , 'Coaching'),
    (CognitiveSciences , 'Cognitive Sciences'),
    (Commerce , 'Commerce'),
    (CommercialGeography , 'Commercial Geography'),
    (CommercialPractice , 'Commercial Practice'),
    (CommunicationSciences , 'Communication Sciences'),
    (Communications , 'Communications'),
    (ComplementaryAlternativeMedicine , 'Complementary & Alternative Medicine'),
    (ComputerScience , 'Computer Science'),
    (ComputerScienceIT , 'Computer Science & IT'),
    (Computing , 'Computing'),
    (Cookery , 'Cookery'),
    (CorporateCommunication , 'Corporate Communication'),
    (CorporateSocialResponsibility , 'Corporate Social Responsibility'),
    (Cosmetics , 'Cosmetics'),
    (Counselling , 'Counselling'),
    (CreativeWriting , 'Creative Writing'),
    (CriminalLaw , 'Criminal Law'),
    (Criminology , 'Criminology'),
    (CulinaryArts , 'Culinary Arts'),
    (DataScienceBigData , 'Data Science & Big Data'),
    (DentalHygiene , 'Dental Hygiene'),
    (Dentistry , 'Dentistry'),
    (Design , 'Design'),
    (Digital , 'Digital'),
    (Earth , 'Earth'),
    (EarthSciences , 'Earth Sciences'),
    (Ecology , 'Ecology'),
    (Econometrics , 'Econometrics'),
    (EconomicsofWar , 'Economics of War'),
    (Economics , 'Economics'),
    (Education , 'Education'),
    (EducationTraining , 'Education & Training'),
    (EducationalPsychology , 'Educational Psychology'),
    (EducationalResearch , 'Educational Research'),
    (ElectricalEngineering , 'Electrical Engineering'),
    (Electronics , 'Electronics'),
    (ElectronicsEmbeddedTechnology , 'Electronics & Embedded Technology'),
    (ElementaryAnatomyMicrotech , 'Elementary Anatomy & Microtech'),
    (ElementaryChemistryChemical , 'Elementary Chemistry & Chemical'),
    (EmergencyDisasterManagement , 'Emergency & Disaster Management'),
    (EnergyPowerEngineering , 'Energy & Power Engineering'),
    (Engineering , 'Engineering'),
    (English , 'English'),
    (EnglishElective , 'English Elective'),
    (Entrepreneurship , 'Entrepreneurship'),
    (EnvironmentalSciences , 'Environmental Sciences'),
    (EnvironmentalEconomicsPolicy , 'Environmental Economics & Policy'),
    (EnvironmentalEngineering , 'Environmental Engineering'),
    (EnvironmentalManagement , 'Environmental Management'),
    (EthnicStudies , 'Ethnic Studies'),
    (EuropeanLaw , 'European Law'),
    (EuropeanStudies , 'European Studies'),
    (EventManagement , 'Event Management'),
    (ExecutiveMBA , 'Executive MBA'),
    (FamilyConsumerScience , 'Family & Consumer Science'),
    (Fashion , 'Fashion'),
    (FashionTextilesAndLuxuryGoods , 'Fashion, Textiles And Luxury Goods'),
    (FilmPhotographyMedia , 'Film, Photography & Media'),
    (Finance , 'Finance'),
    (FinancialMathematics , 'Financial Mathematics'),
    (FineArt , 'Fine Art'),
    (FoodNutrition , 'Food & Nutrition'),
    (FoodSciences , 'Food Sciences'),
    (ForensicAccounting , 'Forensic Accounting'),
    (ForensicScience , 'Forensic Science'),
    (Forestry , 'Forestry'),
    (French , 'French'),
    (GeneralEngineeringTechnology , 'General Engineering & Technology'),
    (GeneralStudiesClassics , 'General Studies & Classics'),
    (GeographicalInformationSystems , 'Geographical Information Systems'),
    (Geography , 'Geography'),
    (Geology , 'Geology'),
    (German , 'German'),
    (GraphicDesign , 'Graphic Design'),
    (Hairdressing , 'Hairdressing'),
    (HealthPhysicalEducation , 'Health & Physical Education'),
    (HealthInformatics , 'Health Informatics'),
    (HealthManagement , 'Health Management'),
    (HealthSciences , 'Health Sciences'),
    (HematologyBloodBanking , 'Hematology & Blood Banking'),
    (History , 'History'),
    (HistoryOfModernWorld , 'History Of Modern World'),
    (HomeManagement , 'Home Management'),
    (Horticulture , 'Horticulture'),
    (HospitalityManagement , 'Hospitality Management'),
    (HospitalityLeisureSports , 'Hospitality, Leisure & Sports'),
    (HotelManagement , 'Hotel Management'),
    (HumanMedicine , 'Human Medicine'),
    (HumanResourceManagement , 'Human Resource Management'),
    (Humanities , 'Humanities'),
    (HydrologyWaterManagement , 'Hydrology & Water Management'),
    (IndustrialSystemsEngineering , 'Industrial & Systems Engineering'),
    (IndustrialDesign , 'Industrial Design'),
    (InformaticsInformationSciences , 'Informatics & Information Sciences'),
    (InformationTechnology , 'Information Technology'),
    (InnovationManagement , 'Innovation Management'),
    (Interior , 'Interior'),
    (InteriorDesign , 'Interior Design'),
    (InternationalBusiness , 'International Business'),
    (InternationalDevelopment , 'International Development'),
    (InternationalLaw , 'International Law'),
    (InternationalRelations , 'International Relations'),
    (Interpreting , 'Interpreting'),
    (IslamicEducation , 'Islamic Education'),
    (IslamicHistoryCulture , 'Islamic History & Culture'),
    (IslamicStudies , 'Islamic Studies'),
    (ITSecurity , 'IT Security'),
    (JournalismMedia , 'Journalism & Media'),
    (LandscapeArchitecture , 'Landscape Architecture'),
    (LanguageStudies , 'Language Studies'),
    (Law , 'Law'),
    (LegalStudies , 'Legal Studies'),
    (LiberalArts , 'Liberal Arts'),
    (LibraryScience , 'Library Science'),
    (Literature , 'Literature'),
    (ManagementOrganisationLeadership , 'Management, Organisation & Leadership'),
    (Manufacturing , 'Manufacturing'),
    (MarineEngineering , 'Marine Engineering'),
    (Maritime , 'Maritime'),
    (Marketing , 'Marketing'),
    (MaterialsScienceEngineering , 'Materials Science & Engineering'),
    (Mathematics , 'Mathematics'),
    (MechanicalEngineering , 'Mechanical Engineering'),
    (Mechatronics , 'Mechatronics'),
    (MediaStudiesMassMedia , 'Media Studies & Mass Media'),
    (Medical , 'Medical'),
    (MedicineHealth , 'Medicine & Health'),
    (Microbiology , 'Microbiology'),
    (Midwifery , 'Midwifery'),
    (MilitaryGeography , 'Military Geography'),
    (MilitaryScience , 'Military Science'),
    (Mining , 'Mining'),
    (ModernHistory , 'Modern History'),
    (ModernHistory , 'Modern History'),
    (MolecularSciences , 'Molecular Sciences'),
    (MuseumStudies , 'Museum Studies'),
    (Music , 'Music'),
    (MusicHistory , 'Music History'),
    (MolecularSciences , 'Molecular Sciences'),
    (MuseumStudies , 'Museum Studies'),
    (Music , 'Music'),
    (MusicHistory , 'Music History'),
    (NaturalResourceManagement , 'Natural Resource Management'),
    (NaturalSciencesMathematics , 'Natural Sciences & Mathematics'),
    (NaturalSciences , 'Natural Sciences'),
    (Neuroscience , 'Neuroscience'),
    (Nursing , 'Nursing'),
    (Nutrition , 'Nutrition'),
    (NutritionDietetics , 'Nutrition & Dietetics'),
    (OilGas , 'Oil & Gas'),
    (OrganisationalBehaviour , 'Organisational Behaviour'),
    (PakistanStudies , 'Pakistan Studies'),
    (PakistaniCulture , 'Pakistani Culture'),
    (PatentIntellectualPropertyLaw , 'Patent & Intellectual Property Law'),
    (Pedagogy , 'Pedagogy'),
    (Performing , 'Performing'),
    (Persian , 'Persian'),
    (Pharmaceutical , 'Pharmaceutical'),
    (Pharmacy , 'Pharmacy'),
    (Philosophy , 'Philosophy'),
    (PhilosophyEthics , 'Philosophy & Ethics'),
    (Photography , 'Photography'),
    (Psychology , 'Psychology'),
    (Physics , 'Physics'),
    (Physiotherapy , 'Physiotherapy'),
    (PlantCropSciences , 'Plant & Crop Sciences'),
    (PoliticalScience , 'Political Science'),
    (ProjectManagement , 'Project Management'),
    (PublicAdministration , 'Public Administration'),
    (PublicHealth , 'Public Health'),
    (PublicLaw , 'Public Law'),
    (PublicPolicy , 'Public Policy'),
    (PublicRelations , 'Public Relations'),
    (RealEstatePropertyManagement , 'Real Estate & Property Management'),
    (Recreation , 'Recreation'),
    (ReligiousStudiesTheology , 'Religious Studies & Theology'),
    (RetailManagement , 'Retail Management'),
    (RiskManagement , 'Risk Management'),
    (Robotics , 'Robotics'),
    (SocialSciences , 'Social Sciences'),
    (SocialWelfare , 'Social Welfare'),
    (Sociology , 'Sociology'),
    (SoilScience , 'Soil Science'),
    (Space , 'Space'),
    (SpecialEducation , 'Special Education'),
    (SpecialMilitaryStudies , 'Special Military Studies'),
    (SportRecreationStatistics , 'Sport & Recreation Statistics'),
    (SupplyChainManagementLogistics , 'Supply Chain Management & Logistics'),
    (SustainableDevelopment , 'Sustainable Development'),
    (SustainableEnergy , 'Sustainable Energy'),
    (Taxation , 'Taxation'),
    (Teaching , 'Teaching'),
    (TechnologyManagement , 'Technology Management'),
    (Television , 'Television'),
    (TerrorismSecurity , 'Terrorism & Security'),
    (Textiles , 'Textiles'),
    (TheatreDance , 'Theatre & Dance'),
    (Theology , 'Theology'),
    (Tourism , 'Tourism'),
    (TourismLeisure , 'Tourism & Leisure'),
    (Toxicology , 'Toxicology'),
    (Training , 'Training'),
    (Translation , 'Translation'),
    (TranslationInterpreting , 'Translation & Interpreting'),
    (TransportManagement , 'Transport Management'),
    (TransportationEngineering , 'Transportation Engineering'),
    (Typing , 'Typing'),
    (Veterinary , 'Veterinary'),
    (VeterinaryMedicine , 'Veterinary Medicine'),
    (VideoGamesMultimedia , 'Video Games & Multimedia'),
    (VisualArts , 'Visual Arts'),
    (War , 'War'),
    (WebTechnologiesCloudComputing , 'Web Technologies & Cloud Computing'),
    (Zoology , 'Zoology'),
    )



    Degree = 'Degree'
    Matriculation_SSE = 'Matriculation SSE'
    OLevel = 'O-Level'
    IntermediateHSSE = 'Intermediate(HSSE)'
    AssociateDegree = 'Associate Degree'
    ALevel = 'A-Level'
    BachelorYears2 = 'Bachelor(2-Years)'
    BachelorYears3 = 'Bachelor(3-Years)'
    BachelorYears4 = 'Bachelor(4-Years)'
    BachelorYears5 = 'Bachelor(5-Years)'
    BachelorYears6 = 'Bachelor(6-Years)'
    MasterMonths6 = 'Master(6-Months)'
    MasterYear1 = 'Master(1-Year)'
    MasterYear15 = 'Master(1.5 Years)'
    MasterYears2 = 'Master(2-Years)'
    MasterYear25 = 'Master(2.5Years)'
    Phd = 'Phd / Doctor(Res)'
    OtherRes = 'Other(Res)'

    Degree = (
        (Degree , 'Degree'),
        (Matriculation_SSE , 'Matriculation SSE'),
        (OLevel , 'O-Level'),
        (IntermediateHSSE , 'Intermediate HSSE'),
        (AssociateDegree , 'Associate Degree'),
        (ALevel , 'A-Level'),
        (BachelorYears2 , 'Bachelor 2-Years'),
        (BachelorYears3 , 'Bachelor 3-Years'),
        (BachelorYears4 , 'Bachelor 4-Years'),
        (BachelorYears5 , 'Bachelor 5-Years'),
        (BachelorYears6 , 'Bachelor(6-Years)'),
        (MasterMonths6 , 'Master(6-Months)'),
        (MasterYear1 , 'Master(1-Year)'),
        (MasterYear15 , 'Master(1.5 Years)'),
        (MasterYears2 , 'Master(2-Years)'),
        (MasterYear25 , 'Master(2.5Years)'),
        (Phd  , 'Phd / Doctor(Res)'),
        (OtherRes , 'Other(Res)'),
    )

    StudyGap = 'Study Gap'
    Monthto3Months = '1 - Month to 3-Months'
    Monthto6Month = '3- Month to 6-Months'
    Yearto15Year = '1-Year to 1.5-Years'
    Yearto2Years  = '1.5-Year to 2 Years'
    Yearsto25Years = '2-Years to 2.5-Years'
    Yearsto3Years = '2.5-Years to 3-Years'
    Yearsto35Years = '3-Years to 3.5-Years'
    Yearsto4Years = '3.5-Years to 4-Years'
    Yearsto45Years = '4-Years to 4.5-Years'
    Yearsto5Years = '4.5-Years to 5-Years'
    Yearsto55Years = '5-Years to 5.5-Years'
    Yearsto6Years = '5.5-Years to 6-Years'
    Yearsto65Years = '6-Years to 6.5-Years'
    Yearsto7Years = '6.5-Years to 7-Years'
    Yearsto75Years = '7-Years to 7.5-Years'
    Yearsto8Years = '7.5-Years to 8-Years'
    Yearsto85Years = '8-Years to 8.5-Years'
    Yearsto9Years = '8.5-Years to 9-Years'
    Yearsto95Years = '9-Years to 9.5-Years'
    Yearsto10Years = '9.5-Years to 10-Years'
    Other = 'Other'
    StudyGap = (
    (StudyGap , 'Study Gap'),
    (Monthto3Months , '1- Month to 3-Months'),
    (Monthto6Month , '3- Month to 6-Months'),
    (Yearto15Year , '1-Year to 1.5-Yeara'),
    (Yearto2Years , '1.5-Year to 2 Years'),
    (Yearsto25Years , '2-Years to 2.5-Years'),
    (Yearsto3Years  , '2.5-Years to 3-Years'),
    (Yearsto35Years , '3-Years to 3.5-Years'),
    (Yearsto45Years , '4-Years to 4.5-Years'),
    (Yearsto5Years , '4.5-Years to 5-Years'),
    (Yearsto55Years , '5-Years to 5.5-Years'),
    (Yearsto6Years , '5.5-Years to 6-Years'),
    (Yearsto65Years , '6-Years to 6.5-Years'),
    (Yearsto7Years , '6.5-Years to 7-Years'),
    (Yearsto75Years  , '7-Years to 7.5-Years'),
    (Yearsto8Years , '7.5-Years to 8-Years'),
    (Yearsto85Years , '8-Years to 8.5-Years'),
    (Yearsto9Years , '8.5-Years to 9-Years'),
    (Yearsto95Years , '9-Years to 9.5-Years'),
    (Yearsto10Years , '9.5-Years to 10-Years'),
    (Other , 'Other'),

    )

    JobExperience = 'Job Experience'
    Monthto3Months = '1 - Month to 3-Months'
    Monthto6Month = '3- Month to 6-Months'
    Yearto15Year = '1-Year to 1.5-Years'
    Yearto2Years  = '1.5-Year to 2 Years'
    Yearsto25Years = '2-Years to 2.5-Years'
    Yearsto3Years = '2.5-Years to 3-Years'
    Yearsto35Years = '3-Years to 3.5-Years'
    Yearsto4Years = '3.5-Years to 4-Years'
    Yearsto45Years = '4-Years to 4.5-Years'
    Yearsto5Years = '4.5-Years to 5-Years'
    Yearsto55Years = '5-Years to 5.5-Years'
    Yearsto6Years = '5.5-Years to 6-Years'
    Yearsto65Years = '6-Years to 6.5-Years'
    Yearsto7Years = '6.5-Years to 7-Years'
    Yearsto75Years = '7-Years to 7.5-Years'
    Yearsto8Years = '7.5-Years to 8-Years'
    Yearsto85Years = '8-Years to 8.5-Years'
    Yearsto9Years = '8.5-Years to 9-Years'
    Yearsto95Years = '9-Years to 9.5-Years'
    Yearsto10Years = '9.5-Years to 10-Years'
    Other = 'Other'
    JobExperience = (
    (JobExperience , 'Job Experience'),
    (Monthto3Months , '1- Month to 3-Months'),
    (Monthto6Month , '3- Month to 6-Months'),
    (Yearto15Year , '1-Year to 1.5-Yeara'),
    (Yearto2Years , '1.5-Year to 2 Years'),
    (Yearsto25Years , '2-Years to 2.5-Years'),
    (Yearsto3Years  , '2.5-Years to 3-Years'),
    (Yearsto35Years , '3-Years to 3.5-Years'),
    (Yearsto45Years , '4-Years to 4.5-Years'),
    (Yearsto5Years , '4.5-Years to 5-Years'),
    (Yearsto55Years , '5-Years to 5.5-Years'),
    (Yearsto6Years , '5.5-Years to 6-Years'),
    (Yearsto65Years , '6-Years to 6.5-Years'),
    (Yearsto7Years , '6.5-Years to 7-Years'),
    (Yearsto75Years  , '7-Years to 7.5-Years'),
    (Yearsto8Years , '7.5-Years to 8-Years'),
    (Yearsto85Years , '8-Years to 8.5-Years'),
    (Yearsto9Years , '8.5-Years to 9-Years'),
    (Yearsto95Years , '9-Years to 9.5-Years'),
    (Yearsto10Years , '9.5-Years to 10-Years'),
    (Other , 'Other'),

    )

    Percentage = 'Percentage'


    Percentage = (
        (Percentage , 'Percentage'),

    )



    Program_Duration = 'Program_Duration'
    Years_16 = '16 Years'
    Years_14 = '14 Years'

    Program_Duration = (
        (Program_Duration , 'Program_Duration'),
        (Years_16  , '16 Years'),
        (Years_14  , '14Years'),
    )

    PassingYear = 'Passing Year'
    Y1990 = '1990'
    Y1991 = '1991'
    Y1992 = '1992'
    Y1993 = '1993'
    Y1994 = '1994'
    Y1995 = '1995'
    Y1996 = '1996'
    Y1997 = '1997'
    Y1998 = '1998'
    Y1999 = '1999'
    Y2000 = '2000'
    Y2001 = '2001'
    Y2002 = '2002'

    Y2003 = '2003'
    Y2004 = '2004'
    Y2005 = '2005'
    Y2006 = '2006'
    Y2007 = '2007'
    Y2008 = '2008'
    Y2009 = '2009'
    Y2010 = '2010'
    Y2011 = '2011'
    Y2012 = '2012'
    Y2013 = '2013'
    Y2014 = '2014'
    Y2015 = '2015'
    Y2016 = '2016'
    Y2017 = '2017'
    Y2018 = '2018'

    PassingYear = (

            (Y1990 , '1990'),
            (Y1991 , '1991'),
            (Y1992 , '1992'),
            (Y1993 , '1993'),
            (Y1994 , '1994'),
            (Y1995 , '1995'),
            (Y1996 , '1996'),
            (Y1996 , '1996'),
            (Y1996 , '1996'),
            (Y1996 , '1996'),
            (Y2000 , '2000'),
            (Y2001 , '2001'),
            (Y2002 , '2002'),
            (Y2003 , '2003'),
            (Y2004 , '2004'),
            (Y2005 , '2005'),
            (Y2006 , '2006'),
            (Y2007 , '2007'),
            (Y2008 , '2008'),
            (Y2009 , '2009'),
            (Y2010 , '2010'),
            (Y2011 , '2011'),
            (Y2012 , '2012'),
            (Y2013 , '2013'),
            (Y2014 , '2014'),
            (Y2015 , '2015'),
            (Y2016 , '2016'),
            (Y2017 , '2017'),
            (Y2018 , '2018'),
    )


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

    OtherLanguage = 'Other_Language'
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

    OtherLanguage = (
        (OtherLanguage,'Other Language'),
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
    DesiredDegree = 'Desired Degree'
    Matriculation_SSE = 'Matriculation SSE'
    OLevel = 'O-Level'
    IntermediateHSSE = 'Intermediate(HSSE)'
    AssociateDegree = 'Associate Degree'
    ALevel = 'A-Level'
    BachelorYears2 = 'Bachelor(2-Years)'
    BachelorYears3 = 'Bachelor(3-Years)'
    BachelorYears4 = 'Bachelor(4-Years)'
    BachelorYears5 = 'Bachelor(5-Years)'
    BachelorYears6 = 'Bachelor(6-Years)'
    MasterMonths6 = 'Master(6-Months)'
    MasterYear1 = 'Master(1-Year)'
    MasterYear15 = 'Master(1.5 Years)'
    MasterYears2 = 'Master(2-Years)'
    MasterYear25 = 'Master(2.5Years)'
    Phd = 'Phd / Doctor(Res)'
    OtherRes = 'Other(Res)'

    DesiredDegree = (
        (DesiredDegree , ' Desired Degree'),
        (Matriculation_SSE , 'Matriculation SSE'),
        (OLevel , 'O-Level'),
        (IntermediateHSSE , 'Intermediate HSSE'),
        (AssociateDegree , 'Associate Degree'),
        (ALevel , 'A-Level'),
        (BachelorYears2 , 'Bachelor 2-Years'),
        (BachelorYears3 , 'Bachelor 3-Years'),
        (BachelorYears4 , 'Bachelor 4-Years'),
        (BachelorYears5 , 'Bachelor 5-Years'),
        (BachelorYears6 , 'Bachelor(6-Years)'),
        (MasterMonths6 , 'Master(6-Months)'),
        (MasterYear1 , 'Master(1-Year)'),
        (MasterYear15 , 'Master(1.5 Years)'),
        (MasterYears2 , 'Master(2-Years)'),
        (MasterYear25 , 'Master(2.5Years)'),
        (Phd  , 'Phd / Doctor(Res)'),
        (OtherRes , 'Other(Res)'),
    )
    DesireSubject = 'Desired Subject'
    AppliedArts = 'Applied Arts'
    AppliedMathematics = 'Applied Mathematics'
    AppliedSciencesProfessions = 'Applied Sciences & Professions'
    AquacultureFisheries = 'Aquaculture & Fisheries'
    Arabic = 'Arabic'
    Archaeology = 'Archaeology'
    Architecture = 'Architecture'
    AreaCulturalStudies = 'Area & Cultural Studies'
    ArtHistory = 'Art History'
    Arts = 'Arts'
    ArtsDesign = 'Arts & Design'
    Astronomy = 'Astronomy'
    Audio = 'Audio'
    Auditing = 'Auditing'
    Automotive = 'Automotive'
    AutomotiveEngineering = 'Automotive Engineering'
    Aviation = 'Aviation'
    Banking = 'Banking'
    BasicMedicalSciences = 'Basic Medical Sciences'
    Beauty = 'Beauty'
    BioBiomedicalEngineering = 'Bio & Biomedical Engineering'
    BiodiversityConservation = 'Biodiversity & Conservation'
    Biology = 'Biology'
    Biomedicine = 'Biomedicine'
    Biotechnology = 'Biotechnology'
    BusinessManagement = 'Business & Management'
    BusinessAdministration = 'Business Administration'
    BusinessInformationSystems = 'Business Information Systems'
    BusinessIntelligenceAnalytics = 'Business Intelligence & Analytics'
    BusinessLaw = 'Business Law'
    BusinessMath = 'Business Math'
    ChemicalEngineering = 'Chemical Engineering'
    Chemistry = 'Chemistry'
    ChildDevelopmentAndFamilyLife = 'Child Development And Family Life'
    ChristianStudies = 'Christian Studies'
    Civics = 'Civics'
    CivicsForNonMuslim = 'Civics For Non Muslim'
    CivilPrivateLaw = 'Civil & Private Law'
    CivilEngineeringConstruction = 'Civil Engineering & Construction'
    ClimateStudiesMeteorology = 'Climate Studies & Meteorology'
    ClinicalPathologySerology = 'Clinical Pathology & Serology'
    ClothingTextile = 'Clothing & Textile'
    Coaching = 'Coaching'
    CognitiveSciences = 'Cognitive Sciences'
    Commerce = 'Commerce'
    CommercialGeography = 'Commercial Geography'
    CommercialPractice = 'Commercial Practice'
    CommunicationSciences = 'Communication Sciences'
    Communications = 'Communications'
    ComplementaryAlternativeMedicine = 'Complementary & Alternative Medicine'
    ComputerScience = 'Computer Science'
    ComputerScienceIT = 'Computer Science & IT'
    Computing = 'Computing'
    Cookery = 'Cookery'
    CorporateCommunication = 'Corporate Communication'
    CorporateSocialResponsibility = 'Corporate Social Responsibility'
    Cosmetics = 'Cosmetics'
    Counselling = 'Counselling'
    CreativeWriting = 'Creative Writing'
    CriminalLaw = 'Criminal Law'
    Criminology = 'Criminology'
    CulinaryArts = 'Culinary Arts'
    DataScienceBigData = 'Data Science & Big Data'
    DentalHygiene = 'Dental Hygiene'
    Dentistry = 'Dentistry'
    Design = 'Design'
    Digital = 'Digital'
    Earth = 'Earth'
    EarthSciences = 'Earth Sciences'
    Ecology = 'Ecology'
    Econometrics = 'Econometrics'
    EconomicsofWar = 'Economics of War'
    Economics = 'Economics'
    Education = 'Education'
    EducationTraining = 'Education & Training'
    EducationalPsychology = 'Educational Psychology'
    EducationalResearch = 'Educational Research'
    ElectricalEngineering = 'Electrical Engineering'
    Electronics = 'Electronics'
    ElectronicsEmbeddedTechnology = 'Electronics & Embedded Technology'
    ElementaryAnatomyMicrotech = 'Elementary Anatomy & Microtech'
    ElementaryChemistryChemical = 'Elementary Chemistry & Chemical'
    EmergencyDisasterManagement = 'Emergency & Disaster Management'
    EnergyPowerEngineering = 'Energy & Power Engineering'
    Engineering = 'Engineering'
    English = 'English'
    EnglishElective = 'English Elective'
    Entrepreneurship = 'Entrepreneurship'
    EnvironmentalSciences = 'Environmental Sciences'
    EnvironmentalEconomicsPolicy = 'Environmental Economics & Policy'
    EnvironmentalEngineering = 'Environmental Engineering'
    EnvironmentalManagement = 'Environmental Management'
    EthnicStudies = 'Ethnic Studies'
    EuropeanLaw = 'European Law'
    EuropeanStudies = 'European Studies'
    EventManagement = 'Event Management'
    ExecutiveMBA = 'Executive MBA'
    FamilyConsumerScience = 'Family & Consumer Science'
    Fashion = 'Fashion'
    FashionTextilesAndLuxuryGoods = 'Fashion, Textiles And Luxury Goods'
    FilmPhotographyMedia = 'Film, Photography & Media'
    Finance = 'Finance'
    FinancialMathematics = 'Financial Mathematics'
    FineArt = 'Fine Art'
    FoodNutrition = 'Food & Nutrition'
    FoodSciences = 'Food Sciences'
    ForensicAccounting = 'Forensic Accounting'
    ForensicScience = 'Forensic Science'
    Forestry = 'Forestry'
    French = 'French'
    GeneralEngineeringTechnology = 'General Engineering & Technology'
    GeneralStudiesClassics = 'General Studies & Classics'
    GeographicalInformationSystems = 'Geographical Information Systems'
    Geography = 'Geography'
    Geology = 'Geology'
    German = 'German'
    GraphicDesign = 'Graphic Design'
    Hairdressing = 'Hairdressing'
    HealthPhysicalEducation = 'Health & Physical Education'
    HealthInformatics = 'Health Informatics'
    HealthManagement = 'Health Management'
    HealthSciences = 'Health Sciences'
    History = 'History'
    HematologyBloodBanking = 'Hematology & Blood Banking'
    HistoryOfModernWorld = 'History Of Modern World'
    HomeManagement = 'Home Management'
    Horticulture = 'Horticulture'
    HospitalityManagement = 'Hospitality Management'
    HospitalityLeisureSports = 'Hospitality, Leisure & Sports'
    HotelManagement = 'Hotel Management'
    HumanMedicine = 'Human Medicine'
    HumanResourceManagement = 'Human Resource Management'
    Humanities = 'Humanities'
    HydrologyWaterManagement= 'Hydrology & Water Management'
    IndustrialSystemsEngineering = 'Industrial & Systems Engineering'
    IndustrialDesign = 'Industrial Design'
    InformaticsInformationSciences = 'Informatics & Information Sciences'
    InformationTechnology = 'Information Technology'
    InnovationManagement = 'Innovation Management'
    Interior = 'Interior'
    InteriorDesign = 'Interior Design'
    InternationalBusiness = 'International Business'
    InternationalDevelopment = 'International Development'
    InternationalLaw = 'International Law'
    InternationalRelations = 'International Relations'
    Interpreting = 'Interpreting'
    IslamicEducation = 'Islamic Education'
    IslamicHistoryCulture = 'Islamic History & Culture'
    IslamicStudies = 'Islamic Studies'
    ITSecurity = 'IT Security'
    JournalismMedia = 'Journalism & Media'
    LandscapeArchitecture = 'Landscape Architecture'
    LanguageStudies = 'Language Studies'
    Law = 'Law'
    LegalStudies= 'Legal Studies'
    LiberalArts = 'Liberal Arts'
    LibraryScience = 'Library Science'
    Literature = 'Literature'
    ManagementOrganisationLeadership = 'Management, Organisation & Leadership'
    Manufacturing = 'Manufacturing'
    MarineEngineering = 'Marine Engineering'
    Maritime = 'Maritime'
    Marketing = 'Marketing'
    MaterialsScienceEngineering = 'Materials Science & Engineering'
    Mathematics= 'Mathematics'
    MechanicalEngineering = 'Mechanical Engineering'
    Mechatronics = 'Mechatronics'
    MediaStudiesMassMedia = 'Media Studies & Mass Media'
    Medical = 'Medical'
    MedicineHealth = 'Medicine & Health'
    Microbiology = 'Microbiology'
    Midwifery= 'Midwifery'
    MilitaryGeography = 'Military Geography'
    MilitaryScience = 'Military Science'
    Mining = 'Mining'
    ModernHistory = 'Modern History'
    MolecularSciences = 'Molecular Sciences'
    MuseumStudies = 'Museum Studies'
    Music = 'Music'
    MusicHistory = 'Music History'
    MolecularSciences = 'Molecular Sciences'
    MuseumStudies = 'Museum Studies'
    Music = 'Music'
    MusicHistory = 'Music History'
    NaturalResourceManagement = 'Natural Resource Management'
    NaturalSciencesMathematics= 'Natural Sciences & Mathematics'
    NaturalSciences = 'Natural Sciences'
    Neuroscience = 'Neuroscience'
    Nursing = 'Nursing'
    Nutrition = 'Nutrition'
    NutritionDietetics = 'Nutrition & Dietetics'
    OilGas = 'Oil & Gas'
    OrganisationalBehaviour = 'Organisational Behaviour'
    PakistanStudies = 'Pakistan Studies'
    PakistaniCulture = 'Pakistani Culture'
    PatentIntellectualPropertyLaw = 'Patent & Intellectual Property Law'
    Pedagogy = 'Pedagogy'
    Performing = 'Performing'
    Persian = 'Persian'
    Pharmaceutical = 'Pharmaceutical'
    Pharmacy = 'Pharmacy'
    Philosophy = 'Philosophy'
    PhilosophyEthics = 'Philosophy & Ethics'
    Photography = 'Photography'
    Psychology = 'Psychology'
    Physics = 'Physics'
    Physiotherapy = 'Physiotherapy'
    PlantCropSciences = 'Plant & Crop Sciences'
    PoliticalScience = 'Political Science'
    ProjectManagement = 'Project Management'
    PublicAdministration = 'Public Administration'
    PublicHealth = 'Public Health'
    PublicLaw = 'Public Law'
    PublicPolicy = 'Public Policy'
    PublicRelations = 'Public Relations'
    RealEstatePropertyManagement = 'Real Estate & Property Management'
    Recreation = 'Recreation'
    ReligiousStudiesTheology = 'Religious Studies & Theology'
    RetailManagement = 'Retail Management'
    RiskManagement = 'Risk Management'
    Robotics = 'Robotics'
    SocialSciences = 'Social Sciences'
    SocialWelfare = 'Social Welfare'
    Sociology = 'Sociology'
    SoilScience = 'Soil Science'
    Space = 'Space'
    SpecialEducation = 'Special Education'
    SpecialMilitaryStudies = 'Special Military Studies'
    SportRecreationStatistics = 'Sport & Recreation Statistics'
    SupplyChainManagementLogistics = 'Supply Chain Management & Logistics'
    SustainableDevelopment = 'Sustainable Development'
    SustainableEnergy = 'Sustainable Energy'
    Taxation = 'Taxation'
    Teaching = 'Teaching'
    TechnologyManagement = 'Technology Management'
    Television = 'Television'
    TerrorismSecurity = 'Terrorism & Security'
    Textiles = 'Textiles'
    TheatreDance = 'Theatre & Dance'
    Theology = 'Theology'
    Tourism = 'Tourism'
    TourismLeisure = 'Tourism & Leisure'
    Toxicology = 'Toxicology'
    Training = 'Training'
    Translation = 'Translation'
    TranslationInterpreting = 'Translation & Interpreting'
    TransportManagement = 'Transport Management'
    TransportationEngineering = 'Transportation Engineering'
    Typing = 'Typing'
    Veterinary = 'Veterinary'
    VeterinaryMedicine = 'Veterinary Medicine'
    VideoGamesMultimedia = 'Video Games & Multimedia'
    VisualArts = 'Visual Arts'
    War = 'War'
    WebTechnologiesCloudComputing = 'Web Technologies & Cloud Computing'
    Zoology = 'Zoology'


    DesireSubject = (
    (DesireSubject , 'Desire Subject'),

    (AppliedArts , 'Applied Arts'),
    (AppliedMathematics, 'Applied Mathematics'),
    (AppliedSciencesProfessions , 'Applied Sciences & Professions'),
    (AquacultureFisheries , 'Aquaculture & Fisheries'),
    (Arabic , 'Arabic'),
    (Archaeology , 'Archaeology'),
    (Architecture , 'Architecture'),
    (AreaCulturalStudies , 'Area & Cultural Studies'),
    (ArtHistory , 'Art History'),
    (Arts , 'Arts'),
    (ArtsDesign , 'Arts & Design'),
    (Astronomy , 'Astronomy'),
    (Audio , 'Audio'),
    (Auditing , 'Auditing'),
    (Automotive , 'Automotive'),
    (AutomotiveEngineering , 'Automotive Engineering'),
    (Aviation , 'Aviation'),
    (Banking , 'Banking'),
    (BasicMedicalSciences , 'Basic Medical Sciences'),
    (BioBiomedicalEngineering , 'Bio & Biomedical Engineering'),
    (BiodiversityConservation , 'Biodiversity & Conservation'),
    (Biology , 'Biology'),
    (Biomedicine , 'Biomedicine'),
    (Biotechnology , 'Biotechnology'),
    (BusinessManagement , 'Business & Management'),
    (BusinessAdministration , 'Business Administration'),
    (BusinessInformationSystems , 'Business Information Systems'),
    (BusinessIntelligenceAnalytics , 'Business Intelligence & Analytics'),
    (BusinessLaw , 'Business Law'),
    (BusinessMath , 'Business Math'),
    (ChemicalEngineering , 'Chemical Engineering'),
    (Chemistry , 'Chemistry'),
    (ChildDevelopmentAndFamilyLife , 'Child Development And Family Life'),
    (ChristianStudies , 'Christian Studies'),
    (Civics , 'Civics'),
    (CivicsForNonMuslim , 'Civics For Non Muslim'),
    (CivilPrivateLaw , 'Civil & Private Law'),
    (CivilEngineeringConstruction , 'Civil Engineering & Construction'),
    (ClimateStudiesMeteorology , 'Climate Studies & Meteorology'),
    (ClinicalPathologySerology , 'Clinical Pathology & Serology'),
    (ClothingTextile , 'Clothing & Textile'),
    (Coaching , 'Coaching'),
    (CognitiveSciences , 'Cognitive Sciences'),
    (Commerce , 'Commerce'),
    (CommercialGeography , 'Commercial Geography'),
    (CommercialPractice , 'Commercial Practice'),
    (CommunicationSciences , 'Communication Sciences'),
    (Communications , 'Communications'),
    (ComplementaryAlternativeMedicine , 'Complementary & Alternative Medicine'),
    (ComputerScience , 'Computer Science'),
    (ComputerScienceIT , 'Computer Science & IT'),
    (Computing , 'Computing'),
    (Cookery , 'Cookery'),
    (CorporateCommunication , 'Corporate Communication'),
    (CorporateSocialResponsibility , 'Corporate Social Responsibility'),
    (Cosmetics , 'Cosmetics'),
    (Counselling , 'Counselling'),
    (CreativeWriting , 'Creative Writing'),
    (CriminalLaw , 'Criminal Law'),
    (Criminology , 'Criminology'),
    (CulinaryArts , 'Culinary Arts'),
    (DataScienceBigData , 'Data Science & Big Data'),
    (DentalHygiene , 'Dental Hygiene'),
    (Dentistry , 'Dentistry'),
    (Design , 'Design'),
    (Digital , 'Digital'),
    (Earth , 'Earth'),
    (EarthSciences , 'Earth Sciences'),
    (Ecology , 'Ecology'),
    (Econometrics , 'Econometrics'),
    (EconomicsofWar , 'Economics of War'),
    (Economics , 'Economics'),
    (Education , 'Education'),
    (EducationTraining , 'Education & Training'),
    (EducationalPsychology , 'Educational Psychology'),
    (EducationalResearch , 'Educational Research'),
    (ElectricalEngineering , 'Electrical Engineering'),
    (Electronics , 'Electronics'),
    (ElectronicsEmbeddedTechnology , 'Electronics & Embedded Technology'),
    (ElementaryAnatomyMicrotech , 'Elementary Anatomy & Microtech'),
    (ElementaryChemistryChemical , 'Elementary Chemistry & Chemical'),
    (EmergencyDisasterManagement , 'Emergency & Disaster Management'),
    (EnergyPowerEngineering , 'Energy & Power Engineering'),
    (Engineering , 'Engineering'),
    (English , 'English'),
    (EnglishElective , 'English Elective'),
    (Entrepreneurship , 'Entrepreneurship'),
    (EnvironmentalSciences , 'Environmental Sciences'),
    (EnvironmentalEconomicsPolicy , 'Environmental Economics & Policy'),
    (EnvironmentalEngineering , 'Environmental Engineering'),
    (EnvironmentalManagement , 'Environmental Management'),
    (EthnicStudies , 'Ethnic Studies'),
    (EuropeanLaw , 'European Law'),
    (EuropeanStudies , 'European Studies'),
    (EventManagement , 'Event Management'),
    (ExecutiveMBA , 'Executive MBA'),
    (FamilyConsumerScience , 'Family & Consumer Science'),
    (Fashion , 'Fashion'),
    (FashionTextilesAndLuxuryGoods , 'Fashion, Textiles And Luxury Goods'),
    (FilmPhotographyMedia , 'Film, Photography & Media'),
    (Finance , 'Finance'),
    (FinancialMathematics , 'Financial Mathematics'),
    (FineArt , 'Fine Art'),
    (FoodNutrition , 'Food & Nutrition'),
    (FoodSciences , 'Food Sciences'),
    (ForensicAccounting , 'Forensic Accounting'),
    (ForensicScience , 'Forensic Science'),
    (Forestry , 'Forestry'),
    (French , 'French'),
    (GeneralEngineeringTechnology , 'General Engineering & Technology'),
    (GeneralStudiesClassics , 'General Studies & Classics'),
    (GeographicalInformationSystems , 'Geographical Information Systems'),
    (Geography , 'Geography'),
    (Geology , 'Geology'),
    (German , 'German'),
    (GraphicDesign , 'Graphic Design'),
    (Hairdressing , 'Hairdressing'),
    (HealthPhysicalEducation , 'Health & Physical Education'),
    (HealthInformatics , 'Health Informatics'),
    (HealthManagement , 'Health Management'),
    (HealthSciences , 'Health Sciences'),
    (HematologyBloodBanking , 'Hematology & Blood Banking'),
    (History , 'History'),
    (HistoryOfModernWorld , 'History Of Modern World'),
    (HomeManagement , 'Home Management'),
    (Horticulture , 'Horticulture'),
    (HospitalityManagement , 'Hospitality Management'),
    (HospitalityLeisureSports , 'Hospitality, Leisure & Sports'),
    (HotelManagement , 'Hotel Management'),
    (HumanMedicine , 'Human Medicine'),
    (HumanResourceManagement , 'Human Resource Management'),
    (Humanities , 'Humanities'),
    (HydrologyWaterManagement , 'Hydrology & Water Management'),
    (IndustrialSystemsEngineering , 'Industrial & Systems Engineering'),
    (IndustrialDesign , 'Industrial Design'),
    (InformaticsInformationSciences , 'Informatics & Information Sciences'),
    (InformationTechnology , 'Information Technology'),
    (InnovationManagement , 'Innovation Management'),
    (Interior , 'Interior'),
    (InteriorDesign , 'Interior Design'),
    (InternationalBusiness , 'International Business'),
    (InternationalDevelopment , 'International Development'),
    (InternationalLaw , 'International Law'),
    (InternationalRelations , 'International Relations'),
    (Interpreting , 'Interpreting'),
    (IslamicEducation , 'Islamic Education'),
    (IslamicHistoryCulture , 'Islamic History & Culture'),
    (IslamicStudies , 'Islamic Studies'),
    (ITSecurity , 'IT Security'),
    (JournalismMedia , 'Journalism & Media'),
    (LandscapeArchitecture , 'Landscape Architecture'),
    (LanguageStudies , 'Language Studies'),
    (Law , 'Law'),
    (LegalStudies , 'Legal Studies'),
    (LiberalArts , 'Liberal Arts'),
    (LibraryScience , 'Library Science'),
    (Literature , 'Literature'),
    (ManagementOrganisationLeadership , 'Management, Organisation & Leadership'),
    (Manufacturing , 'Manufacturing'),
    (MarineEngineering , 'Marine Engineering'),
    (Maritime , 'Maritime'),
    (Marketing , 'Marketing'),
    (MaterialsScienceEngineering , 'Materials Science & Engineering'),
    (Mathematics , 'Mathematics'),
    (MechanicalEngineering , 'Mechanical Engineering'),
    (Mechatronics , 'Mechatronics'),
    (MediaStudiesMassMedia , 'Media Studies & Mass Media'),
    (Medical , 'Medical'),
    (MedicineHealth , 'Medicine & Health'),
    (Microbiology , 'Microbiology'),
    (Midwifery , 'Midwifery'),
    (MilitaryGeography , 'Military Geography'),
    (MilitaryScience , 'Military Science'),
    (Mining , 'Mining'),
    (ModernHistory , 'Modern History'),
    (ModernHistory , 'Modern History'),
    (MolecularSciences , 'Molecular Sciences'),
    (MuseumStudies , 'Museum Studies'),
    (Music , 'Music'),
    (MusicHistory , 'Music History'),
    (MolecularSciences , 'Molecular Sciences'),
    (MuseumStudies , 'Museum Studies'),
    (Music , 'Music'),
    (MusicHistory , 'Music History'),
    (NaturalResourceManagement , 'Natural Resource Management'),
    (NaturalSciencesMathematics , 'Natural Sciences & Mathematics'),
    (NaturalSciences , 'Natural Sciences'),
    (Neuroscience , 'Neuroscience'),
    (Nursing , 'Nursing'),
    (Nutrition , 'Nutrition'),
    (NutritionDietetics , 'Nutrition & Dietetics'),
    (OilGas , 'Oil & Gas'),
    (OrganisationalBehaviour , 'Organisational Behaviour'),
    (PakistanStudies , 'Pakistan Studies'),
    (PakistaniCulture , 'Pakistani Culture'),
    (PatentIntellectualPropertyLaw , 'Patent & Intellectual Property Law'),
    (Pedagogy , 'Pedagogy'),
    (Performing , 'Performing'),
    (Persian , 'Persian'),
    (Pharmaceutical , 'Pharmaceutical'),
    (Pharmacy , 'Pharmacy'),
    (Philosophy , 'Philosophy'),
    (PhilosophyEthics , 'Philosophy & Ethics'),
    (Photography , 'Photography'),
    (Psychology , 'Psychology'),
    (Physics , 'Physics'),
    (Physiotherapy , 'Physiotherapy'),
    (PlantCropSciences , 'Plant & Crop Sciences'),
    (PoliticalScience , 'Political Science'),
    (ProjectManagement , 'Project Management'),
    (PublicAdministration , 'Public Administration'),
    (PublicHealth , 'Public Health'),
    (PublicLaw , 'Public Law'),
    (PublicPolicy , 'Public Policy'),
    (PublicRelations , 'Public Relations'),
    (RealEstatePropertyManagement , 'Real Estate & Property Management'),
    (Recreation , 'Recreation'),
    (ReligiousStudiesTheology , 'Religious Studies & Theology'),
    (RetailManagement , 'Retail Management'),
    (RiskManagement , 'Risk Management'),
    (Robotics , 'Robotics'),
    (SocialSciences , 'Social Sciences'),
    (SocialWelfare , 'Social Welfare'),
    (Sociology , 'Sociology'),
    (SoilScience , 'Soil Science'),
    (Space , 'Space'),
    (SpecialEducation , 'Special Education'),
    (SpecialMilitaryStudies , 'Special Military Studies'),
    (SportRecreationStatistics , 'Sport & Recreation Statistics'),
    (SupplyChainManagementLogistics , 'Supply Chain Management & Logistics'),
    (SustainableDevelopment , 'Sustainable Development'),
    (SustainableEnergy , 'Sustainable Energy'),
    (Taxation , 'Taxation'),
    (Teaching , 'Teaching'),
    (TechnologyManagement , 'Technology Management'),
    (Television , 'Television'),
    (TerrorismSecurity , 'Terrorism & Security'),
    (Textiles , 'Textiles'),
    (TheatreDance , 'Theatre & Dance'),
    (Theology , 'Theology'),
    (Tourism , 'Tourism'),
    (TourismLeisure , 'Tourism & Leisure'),
    (Toxicology , 'Toxicology'),
    (Training , 'Training'),
    (Translation , 'Translation'),
    (TranslationInterpreting , 'Translation & Interpreting'),
    (TransportManagement , 'Transport Management'),
    (TransportationEngineering , 'Transportation Engineering'),
    (Typing , 'Typing'),
    (Veterinary , 'Veterinary'),
    (VeterinaryMedicine , 'Veterinary Medicine'),
    (VideoGamesMultimedia , 'Video Games & Multimedia'),
    (VisualArts , 'Visual Arts'),
    (War , 'War'),
    (WebTechnologiesCloudComputing , 'Web Technologies & Cloud Computing'),
    (Zoology , 'Zoology'),
    )



    Program_Duration = 'Program Duration'
    Years_2 = '2 Years'
    Years_3 = '3 Years'
    Years_4 = '4 Years'


    Program_Duration = (
        (Program_Duration , 'Program Duration'),
        (Years_2  , '2 Years'),
        (Years_3  , '3 Years'),
        (Years_4 , '4 Years')
    )

    Country = 'Country'
    Pak = 'Pakistan'
    Australia = 'Australia'
    Country = (
        (Country , 'Country'),
        (Pak , 'Pakistan'),
        (Australia , 'Australia'),

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



    #Qualification part

    #user = models.OneToOneField(User)
    #std_qual_id = models.ForeignKey(RegisterStudent,related_name="std_qual_id")
    #student = models.ForeignKey('name', related_name='Student')
    highest_qualification = models.CharField(max_length=35, choices = Degree, default= Degree)
    subject = models.CharField(max_length=50,choices = Subject, default= Subject )
    program_duration = models.CharField(max_length=20 , choices = Program_Duration, default= Program_Duration)
    Insititution = models.CharField(max_length=200, blank=False)
    from_country = models.CharField(max_length=35, choices = Country, default= Country)
    percentage = models.CharField(max_length=10)
    passing_year = models.CharField(max_length=10, choices = PassingYear, default=PassingYear)
    studyGap = models.CharField(max_length=150, choices = StudyGap, default=StudyGap)
    study_gap1 = models.CharField(max_length=20, blank=True, null=True)
    study_gap2 = models.CharField(max_length=20, blank=True, null=True)
    study_gap3 = models.CharField(max_length=20, blank=True, null=True)
    #study_gap4 = models.CharField(max_length=20, blank=True, null=True)
    experience = models.CharField(max_length=150, choices = JobExperience, default=JobExperience)
    experience1 = models.CharField(max_length=20, blank=True, null=True)
    experience2 = models.CharField(max_length=20, blank=True, null=True)
    experience3 = models.CharField(max_length=20, blank=True, null=True)
    #experience4 = models.CharField(max_length=20, blank=True, null=True)
    achievements = models.TextField(max_length=400, blank=True, null=True)


    #Language part
    english_language =  models.CharField(max_length=30,choices=English_Language, default=English_Language, null=True )
    english_language_score = models.CharField(max_length=10, null=True ,default= None)
    other_Language = models.CharField(max_length=30,choices=OtherLanguage, default=OtherLanguage, null=True )
    Other_Language_score = models.CharField(max_length=10, null=True,default= None)

    #Future Plans part
    desired_degree = models.CharField(max_length=35, null=True,  choices = DesiredDegree, default = DesiredDegree)
    desired_subject = models.CharField(max_length=35, null=True ,choices = DesireSubject,  default= DesireSubject)
    desired_country = models.CharField(max_length=35, null=True,choices = Country,  default= Country)
    scholarships = models.CharField(max_length=35, null=True,choices= Scholarships,  default= Scholarships)
    budget = models.CharField(max_length=25, null=True, default= None)

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
#class StudentQualifications(models.Model):




#def std_qualification(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = StudentQualifications.objects.create(user = kwargs['instance'])

#post_save.connect(std_qualification, sender= User)
class StudentLanguage(models.Model):


    user = models.OneToOneField(User)
#    std_lang_id = models.ForeignKey(RegisterStudent,related_name="std_lang_id")



    def __str__(self):
        return self.user.username


class StudentFuture(models.Model):

#    std_future_id = models.ForeignKey(RegisterStudent,related_name="std_future_id")
    user = models.OneToOneField(User)


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

    Country = 'Country'
    Pakistan = 'Pakistan'
    India = 'India'
    Australia = 'Australia'
    UK = 'UK'
    Canada = 'Canada'
    Ireland = 'Ireland'
    NewZealand = 'New Zealand'
    Germany = 'Germany'
    Sweden = 'Sweden'
    Afghanistan = 'Afghanistan'
    Algeria = 'Algeria'
    Albania = 'Albania'
    Andorra = 'Andorra'
    Angola = 'Angola'
    Anguilla = 'Anguilla'
    AntiguaBarbuda = 'Antigua & Barbuda'

    Argentina = 'Argentina'
    Armenia = 'Armenia'
    Austria = 'Austria'
    Azerbaijan = 'Azerbaijan'
    Bahamas = 'Bahamas'
    Bahrain = 'Bahrain'
    Bangladesh = 'Bangladesh'
    Barbados = 'Barbados'
    Belarus = 'Belarus'
    Belgium = 'Belgium'
    Belize = 'Belize'
    Benin = 'Benin'
    Bermuda = 'Bermuda'
    Bhutan = 'Bhutan'
    Bolivia = 'Bolivia'
    BosniaHerzegovina = 'Bosnia & Herzegovina'
    Botswana = 'Botswana'
    Brazil = 'Brazil'
    BruneiDarussalam = 'Brunei Darussalam'
    Bulgaria = 'Bulgaria'
    BurkinaFaso = 'Burkina Faso'
    MyanmarBurma = 'Myanmar/Burma'
    Burundi = 'Burundi'
    Cambodia = 'Cambodia'
    Cameroon = 'Cameroon'
    CapeVerde = 'Cape Verde'
    CaymanIslands = 'Cayman Islands'
    CentralAfrican = 'Central African'
    ChadRepublic = 'Chad Republic'
    Chile = 'Chile'
    China = 'China'
    Colombia = 'Colombia'
    Comoros = 'Comoros'
    Congo = 'Congo'
    CostaRica = 'Costa Rica'
    Croatia = 'Croatia'
    Cuba = 'Cuba'
    Cyprus = 'Cyprus'
    CzechRepublic = 'Czech Republic'
    DemocraticRepublicoftheCongo = 'Democratic Republic of the Congo'
    Denmark = 'Denmark'
    Djibouti = 'Djibouti'
    DominicanRepublic = 'Dominican Republic'
    Dominica = 'Dominica'
    Ecuador = 'Ecuador'
    Egypt = 'Egypt'
    ElSalvador = 'El Salvador'
    EquatorialGuinea = 'Equatorial Guinea'
    Eritrea ='Eritrea'
    Estonia = 'Estonia'
    Ethiopia = 'Ethiopia'
    Fiji = 'Fiji'
    Finland = 'Finland'
    France = 'France'
    FrenchGuiana = 'French Guiana'
    Gabon = 'Gabon'
    Gambia = 'Gambia'
    Georgia = 'Georgia'
    Ghana = 'Ghana'
    GreatBritain = 'Great Britain'
    Greece = 'Greece'
    Grenada = 'Grenada'
    Guadeloupe = 'Guadeloupe'
    Guatemala = 'Guatemala'
    Guinea = 'Guinea'
    GuineaBissau = 'Guinea-Bissau'
    Guyana = 'Guyana'
    Haiti = 'Haiti'
    Honduras = 'Honduras'
    Hungary = 'Hungary'
    Iceland = 'Iceland'
    Indonesia = 'Indonesia'
    Iran = 'Iran'
    Iraq = 'Iraq'
    IsraelandtheOccupiedTerritories = 'Israel and the Occupied Territories'
    Italy = 'Italy'
    IvoryCoast = 'Ivory Coast (Cote dIvoire)'
    Jamaica = 'Jamaica'
    Japan = 'Japan'
    Jordan = 'Jordan'
    Kazakhstan = 'Kazakhstan'
    Kenya = 'Kenya'
    Kosovo = 'Kosovo'
    Kuwait = 'Kuwait'
    Korea = 'Korea'
    KyrgyzRepublic ='Kyrgyz Republic (Kyrgyzstan)'
    Laos = 'Laos'
    Latvia = 'Latvia'
    Lebanon = 'Lebanon'
    Lesotho = 'Lesotho'
    Liberia = 'Liberia'
    Libya = 'Libya'
    Liechtenstein = 'Liechtenstein'
    Lithuania = 'Lithuania'
    Luxembourg = 'Luxembourg'
    RepublicofMacedonia = 'Republic of Macedonia'
    Madagascar = 'Madagascar'
    Malawi = 'Malawi'
    Malaysia = 'Malaysia'
    Maldives = 'Maldives'
    Mali = 'Mali'
    Malta = 'Malta'
    Martinique = 'Martinique'
    Mauritania = 'Mauritania'
    Mauritius = 'Mauritius'
    Mayotte = 'Mayotte'
    Mexico = 'Mexico'
    Moldova = 'Moldova'
    Mongolia = 'Mongolia'
    Montenegro = 'Montenegro'
    Montserrat = 'Montserrat'
    Morocco = 'Morocco'
    Mozambique = 'Mozambique'
    Namibia = 'Namibia'
    Nepal = 'Nepal'
    Netherlands = 'Netherlands'
    NewZealand = 'New Zealand'
    Nicaragua = 'Nicaragua'
    Niger = 'Niger'
    Nigeria = 'Nigeria'
    Oman = 'Oman'
    PacificIslands = 'Pacific Islands'
    Pakistan = 'Pakistan'
    Panama = 'Panama'
    PapuaNewGuinea = 'Papua New Guinea'
    Paraguay = 'Paraguay'
    Peru = 'Peru'
    Philippines = 'Philippines'
    Poland = 'Poland'
    Portugal = 'Portugal'
    PuertoRico = 'Puerto Rico'
    Qatar = 'Qatar'
    Reunion = 'Reunion'
    Romania = 'Romania'
    RussianFederation = 'Russian Federation'
    Rwanda = 'Rwanda'
    SaintKittsandNevis = 'Saint Kitts and Nevis'
    SaintLucia = 'Saint Lucia'
    SaintVincentGrenadines  ='Saint Vincents & Grenadines'
    Samoa = 'Samoa'
    SaoTomeandPrincipe = 'Sao Tome and Principe'
    SaudiArabia = 'Saudi Arabia'
    Senegal = 'Senegal'
    Serbia = 'Serbia'
    Seychelles = 'Seychelles'
    SierraLeone = 'Sierra Leone'
    Singapore = 'Singapore'
    SlovakRepublic = 'Slovak Republic'
    Slovenia = 'Slovenia'
    SolomonIslands = 'Solomon Islands'
    Somalia = 'Somalia'
    SouthAfrica = 'South Africa'
    RepublicofSouthKorea = 'Korea, Republic of (South Korea)'
    SouthSudan = 'South Sudan'
    Spain = 'Spain'
    SriLanka = 'Sri Lanka'
    Sudan = 'Sudan'
    Suriname = 'Suriname'
    Swaziland = 'Swaziland'
    Switzerland = 'Switzerland'
    Syria = 'Syria'
    Tajikistan = 'Tajikistan'
    Tanzania = 'Tanzania'
    Thailand = 'Thailand'
    TimorLeste = 'Timor Leste'
    Togo = 'Togo'
    TrinidadTobago = 'Trinidad & Tobago'
    Turkey = 'Turkey'
    Turkmenistan = 'Turkmenistan'
    TurksCaicos = 'Turks & Caicos'
    Uganda = 'Uganda'
    Ukraine = 'Ukraine'
    UnitedArabEmirates = 'United Arab Emirates'
    Uruguay = 'Uruguay'
    USA = 'USA'
    Uzbekistan = 'Uzbekistan'
    Venezuela = 'Venezuela'
    Vietnam = 'Vietnam'
    VirginIslandsUK = 'Virgin Islands (UK)'
    VirginIslandsUS = 'Virgin Islands (US)'
    Yemen = 'Yemen'
    Zambia  = 'Zambia '
    Zimbabwe = 'Zimbabwe'
    Norway = 'Norway'






    Country = (
        (Country, 'Country'),
    (Australia , 'Australia'),
	(USA , 'USA'),
	(Canada , 'Canada'),
	(UK , 'UK'),
	(Ireland , 'Ireland'),
	(NewZealand , 'NewZealand'),
	(Germany , 'Germany'),
	(Sweden , 'Sweden'),

	(Afghanistan , 'Afghanistan'),
	(Albania , 'Albania'),
	(Algeria , 'Algeria'),
	(Andorra , 'Andorra'),
	(Angola , 'Angola'),
	(Anguilla , 'Anguilla'),
	(AntiguaBarbuda , 'Antigua & Barbuda'),
	(Argentina , 'Argentina'),
	(Armenia , 'Armenia'),
	(Austria , 'Austria'),
	(Azerbaijan , 'Azerbaijan'),
	(Bahamas , 'Bahamas'),
	(Bahrain , 'Bahrain'),
	(Bangladesh , 'Bangladesh'),
	(Barbados , 'Barbados'),
	(Belarus , 'Belarus'),
	(Belgium , 'Belgium'),
	(Belize , 'Belize'),
	(Benin , 'Benin'),
	(Bermuda , 'Bermuda'),
	(Bhutan , 'Bhutan'),
	(Bolivia , 'Bolivia'),
	(BosniaHerzegovina , 'Bosnia & Herzegovina'),
	(Botswana , 'Botswana'),
	(Brazil , 'Brazil'),
	(BruneiDarussalam , 'Brunei Darussalam'),
	(Bulgaria , 'Bulgaria'),
	(BurkinaFaso , 'Burkina Faso'),
	(MyanmarBurma , 'Myanmar/Burma'),
	(Burundi , 'Burundi'),
	(Cambodia , 'Cambodia'),
	(Cameroon , 'Cameroon'),
	(CapeVerde , 'Cape Verde'),
	(CaymanIslands , 'Cayman Islands'),
	(CentralAfrican , 'Central African'),
	(ChadRepublic , 'Chad Republic'),
	(Chile , 'Chile'),
	(China , 'China'),
	(Colombia , 'Colombia'),
	(Comoros , 'Comoros'),
	(Congo , 'Congo'),
	(CostaRica , 'Costa Rica'),
	(Croatia , 'Croatia'),
	(Cuba , 'Cuba'),
	(Cyprus , 'Cyprus'),
	(CzechRepublic , 'Czech Republic'),
	(DemocraticRepublicoftheCongo , 'Democratic Republic of the Congo'),
	(Denmark , 'Denmark'),
	(Djibouti , 'Djibouti'),
	(DominicanRepublic , 'Dominican Republic'),
	(Dominica , 'Dominica'),
	(Ecuador , 'Ecuador'),
	(Egypt , 'Egypt'),
	(ElSalvador , 'El Salvador'),
	(EquatorialGuinea , 'Equatorial Guinea'),
	(Eritrea , 'Eritrea'),
	(Estonia , 'Estonia'),
	(Ethiopia , 'Ethiopia'),
	(Fiji , 'Fiji'),
	(Finland , 'Finland'),
	(France , 'France'),
	(FrenchGuiana , 'French Guiana'),
	(Gabon , 'Gabon'),
	(Gambia , 'Gambia'),
	(Georgia , 'Georgia'),
	(Ghana , 'Ghana'),
	(GreatBritain , 'Great Britain'),
	(Greece , 'Greece'),
	(Grenada , 'Grenada'),
	(Guadeloupe , 'Guadeloupe'),
	(Guatemala , 'Guatemala'),
	(Guinea , 'Guinea'),
	(GuineaBissau , 'Guinea-Bissau'),
	(Guyana , 'Guyana'),
	(Haiti , 'Haiti'),
	(Honduras , 'Honduras'),
	(Hungary , 'Hungary'),
	(Iceland , 'Iceland'),
	(India , 'India'),
	(Indonesia , 'Indonesia'),
	(Iran , 'Iran'),
	(Iraq , 'Iraq'),
	(IsraelandtheOccupiedTerritories , 'Israel and the Occupied Territories'),
	(Italy , 'Italy'),
	(IvoryCoast , 'Ivory Coast (Cote dIvoire)'),
	(Jamaica , 'Jamaica'),
	(Japan , 'Japan'),
	(Jordan , 'Jordan'),
	(Kazakhstan , 'Kazakhstan'),
	(Kenya , 'Kenya'),
	(Kosovo , 'Kosovo'),
	(Kuwait , 'Kuwait'),
	(Korea , 'Korea'),
	(KyrgyzRepublic , 'Kyrgyz Republic (Kyrgyzstan)'),
	(Laos , 'Laos'),
	(Latvia , 'Latvia'),
	(Lebanon , 'Lebanon'),
	(Lesotho , 'Lesotho'),
	(Liberia , 'Liberia'),
	(Libya , 'Libya'),
	(Liechtenstein , 'Liechtenstein'),
	(Lithuania , 'Lithuania'),
	(Luxembourg , 'Luxembourg'),
	(RepublicofMacedonia , 'Republic of Macedonia'),
	(Madagascar , 'Madagascar'),
	(Malawi , 'Malawi'),
	(Malaysia , 'Malaysia'),
	(Maldives , 'Maldives'),
	(Mali , 'Mali'),
	(Malta , 'Malta'),
	(Martinique , 'Martinique'),
	(Mauritania , 'Mauritania'),
	(Mauritius , 'Mauritius'),
	(Mayotte , 'Mayotte'),
	(Mexico , 'Mexico'),
	(Moldova , 'Moldova'),
	(Mongolia , 'Mongolia'),
	(Montenegro , 'Montenegro'),
	(Montserrat , 'Montserrat'),
	(Morocco , 'Morocco'),
	(Mozambique , 'Mozambique'),
	(Namibia , 'Namibia'),
	(Nepal , 'Nepal'),
	(Netherlands , 'Netherlands'),
	(NewZealand , 'NewZealand'),
	(Nicaragua , 'Nicaragua'),
	(Niger , 'Niger'),
	(Nigeria , 'Nigeria'),
	(Norway , 'Norway'),
	(Oman , 'Oman'),
	(PacificIslands , 'Pacific Islands'),
	(Pakistan , 'Pakistan'),
	(Panama , 'Panama'),
	(PapuaNewGuinea , 'Papua New Guinea'),
	(Paraguay , 'Paraguay'),
	(Peru , 'Peru'),
	(Philippines , 'Philippines'),
	(Poland , 'Poland'),
	(Portugal , 'Portugal'),
	(PuertoRico , 'Puerto Rico'),
	(Qatar , 'Qatar'),
	(Reunion , 'Reunion'),
	(Romania , 'Romania'),
	(RussianFederation , 'Russian Federation'),
	(Rwanda , 'Rwanda'),
	(SaintKittsandNevis , 'Saint Kitts and Nevis'),
	(SaintLucia , 'Saint Lucia'),
	(SaintVincentGrenadines , 'Saint Vincents & Grenadines'),
	(Samoa , 'Samoa'),
	(SaoTomeandPrincipe , 'Sao Tome and Principe'),
	(SaudiArabia , 'Saudi Arabia'),
	(Senegal , 'Senegal'),
	(Serbia , 'Serbia'),
	(Seychelles , 'Seychelles'),
	(SierraLeone , 'Sierra Leone'),
	(Singapore , 'Singapore'),
	(SlovakRepublic , 'Slovak Republic'),
	(Slovenia , 'Slovenia'),
	(SolomonIslands , 'Solomon Islands'),
	(Somalia , 'Somalia'),
	(SouthAfrica , 'South Africa'),

	(SouthSudan , 'South Sudan'),
	(Spain , 'Spain'),
	(SriLanka , 'Sri Lanka'),
	(Sudan , 'Sudan'),
	(Suriname , 'Suriname'),
	(Swaziland , 'Swaziland'),
	(Switzerland , 'Switzerland'),
	(Syria , 'Syria'),
	(Tajikistan , 'Tajikistan'),
	(Tanzania , 'Tanzania'),
	(Thailand , 'Thailand'),
	(TimorLeste , 'Timor Leste'),
	(Togo , 'Togo'),
	(TrinidadTobago , 'Trinidad & Tobago'),
	(Turkey , 'Turkey'),
	(Turkmenistan , 'Turkmenistan'),
	(TurksCaicos , 'Turks & Caicos'),
	(Uganda , 'Uganda'),
	(Ukraine , 'Ukraine'),
	(UnitedArabEmirates , 'United Arab Emirates'),
	(Uruguay , 'Uruguay'),
	(Uzbekistan , 'Uzbekistan'),
	(Venezuela , 'Venezuela'),
	(Vietnam , 'Vietnam'),
	(VirginIslandsUS , 'Virgin Islands (US)'),
    (VirginIslandsUK , 'Virgin Islands (UK)'),
	(Yemen , 'Yemen'),
	(Zambia , 'Zambia'),
	(Zimbabwe , 'Zimbabwe'),

    )




    ProcessingFee =  'Processing Fee'
    zerofivek = '0-5000'
    fivektenk = '5000-10,000'
    tenkfifteenk = '10,000-15000'
    fifteenktwentyk = '15000-20,000'
    twentyktwentyfivek = '20,000-25000'
    twentyfivekthiryk = '25000-30,000'
    thirtytofive= '30,000-35000'
    thirtyfivetoforty = '35000-40,000'
    fortytofortyfive= '40,000-45000'
    fortyfivetofifty = '45000-50,000'
    fiftytosixty = '50,000-60,000'
    sixtyto70 = '60,000-70,000'
    seventyto80 = '70,000-80,000'
    eightyto90 = '80,000-90,000'
    nightyto100 = '90,000-100,000'
    hundredto125 = '100,000-125,000'
    onetwofiveto150= '125,000-150,000'
    onefiftyto200 = '150,000-200,000'


    ProcessingFee = (

    	(zerofivek ,'0-5000'),
    	(fivektenk  ,'5000-10,000'),
    	(tenkfifteenk,  '10,000-15000'),
    	(fifteenktwentyk , '15000-20,000'),
    	(twentyktwentyfivek , '20,000-25000'),
    	(twentyfivekthiryk , '25000-30,000'),
    	(thirtytofive ,'30,000-35000'),
    	(thirtyfivetoforty , '35000-40,000'),
    	(fortytofortyfive, '40,000-45000'),
    	(fortyfivetofifty , '45000-50,000'),
    	(fiftytosixty , '50,000-60,000'),
    	(sixtyto70  ,'60,000-70,000'),
    	(seventyto80 , '70,000-80,000'),
    	(eightyto90  ,'80,000-90,000'),
    	(nightyto100 , '90,000-100,000'),
    	(hundredto125 , '100,000-125,000'),
    	(onetwofiveto150 ,'125,000-150,000'),
    	(onefiftyto200 , '150,000-200,000'),
    )

    LanguageFee =  'Language Fees'
    zerofivek = '0-5000'
    fivektenk = '5000-10,000'
    tenkfifteenk = '10,000-15000'
    fifteenktwentyk = '15000-20,000'
    twentyktwentyfivek = '20,000-25000'
    twentyfivekthiryk = '25000-30,000'
    thirtytofive= '30,000-35000'
    thirtyfivetoforty = '35000-40,000'
    fortytofortyfive= '40,000-45000'
    fortyfivetofifty = '45000-50,000'
    fiftytosixty = '50,000-60,000'
    sixtyto70 = '60,000-70,000'
    seventyto80 = '70,000-80,000'
    eightyto90 = '80,000-90,000'
    nightyto100 = '90,000-100,000'
    hundredto125 = '100,000-125,000'
    onetwofiveto150= '125,000-150,000'
    onefiftyto200 = '150,000-200,000'


    LanguageFee = (

    	(zerofivek ,'0-5000'),
    	(fivektenk  ,'5000-10,000'),
    	(tenkfifteenk,  '10,000-15000'),
    	(fifteenktwentyk , '15000-20,000'),
    	(twentyktwentyfivek , '20,000-25000'),
    	(twentyfivekthiryk , '25000-30,000'),
    	(thirtytofive ,'30,000-35000'),
    	(thirtyfivetoforty , '35000-40,000'),
    	(fortytofortyfive, '40,000-45000'),
    	(fortyfivetofifty , '45000-50,000'),
    	(fiftytosixty , '50,000-60,000'),
    	(sixtyto70  ,'60,000-70,000'),
    	(seventyto80 , '70,000-80,000'),
    	(eightyto90  ,'80,000-90,000'),
    	(nightyto100 , '90,000-100,000'),
    	(hundredto125 , '100,000-125,000'),
    	(onetwofiveto150 ,'125,000-150,000'),
    	(onefiftyto200 , '150,000-200,000'),
    )

    RefusalFee =  'Refusal Fee'
    zerofivek = '0-5000'
    fivektenk = '5000-10,000'
    tenkfifteenk = '10,000-15000'
    fifteenktwentyk = '15000-20,000'
    twentyktwentyfivek = '20,000-25000'
    twentyfivekthiryk = '25000-30,000'
    thirtytofive= '30,000-35000'
    thirtyfivetoforty = '35000-40,000'
    fortytofortyfive= '40,000-45000'
    fortyfivetofifty = '45000-50,000'
    fiftytosixty = '50,000-60,000'
    sixtyto70 = '60,000-70,000'
    seventyto80 = '70,000-80,000'
    eightyto90 = '80,000-90,000'
    nightyto100 = '90,000-100,000'
    hundredto125 = '100,000-125,000'
    onetwofiveto150= '125,000-150,000'
    onefiftyto200 = '150,000-200,000'


    RefusalFee = (

    	(zerofivek ,'0-5000'),
    	(fivektenk  ,'5000-10,000'),
    	(tenkfifteenk,  '10,000-15000'),
    	(fifteenktwentyk , '15000-20,000'),
    	(twentyktwentyfivek , '20,000-25000'),
    	(twentyfivekthiryk , '25000-30,000'),
    	(thirtytofive ,'30,000-35000'),
    	(thirtyfivetoforty , '35000-40,000'),
    	(fortytofortyfive, '40,000-45000'),
    	(fortyfivetofifty , '45000-50,000'),
    	(fiftytosixty , '50,000-60,000'),
    	(sixtyto70  ,'60,000-70,000'),
    	(seventyto80 , '70,000-80,000'),
    	(eightyto90  ,'80,000-90,000'),
    	(nightyto100 , '90,000-100,000'),
    	(hundredto125 , '100,000-125,000'),
    	(onetwofiveto150 ,'125,000-150,000'),
    	(onefiftyto200 , '150,000-200,000'),
        )

    InterviewFee =  'Interview Fees'
    zerofivek = '0-5000'
    fivektenk = '5000-10,000'
    tenkfifteenk = '10,000-15000'
    fifteenktwentyk = '15000-20,000'
    twentyktwentyfivek = '20,000-25000'
    twentyfivekthiryk = '25000-30,000'
    thirtytofive= '30,000-35000'
    thirtyfivetoforty = '35000-40,000'
    fortytofortyfive= '40,000-45000'
    fortyfivetofifty = '45000-50,000'
    fiftytosixty = '50,000-60,000'
    sixtyto70 = '60,000-70,000'
    seventyto80 = '70,000-80,000'
    eightyto90 = '80,000-90,000'
    nightyto100 = '90,000-100,000'
    hundredto125 = '100,000-125,000'
    onetwofiveto150= '125,000-150,000'
    onefiftyto200 = '150,000-200,000'


    InterviewFee = (

        	(zerofivek ,'0-5000'),
        	(fivektenk  ,'5000-10,000'),
        	(tenkfifteenk,  '10,000-15000'),
        	(fifteenktwentyk , '15000-20,000'),
        	(twentyktwentyfivek , '20,000-25000'),
        	(twentyfivekthiryk , '25000-30,000'),
        	(thirtytofive ,'30,000-35000'),
        	(thirtyfivetoforty , '35000-40,000'),
        	(fortytofortyfive, '40,000-45000'),
        	(fortyfivetofifty , '45000-50,000'),
        	(fiftytosixty , '50,000-60,000'),
        	(sixtyto70  ,'60,000-70,000'),
        	(seventyto80 , '70,000-80,000'),
        	(eightyto90  ,'80,000-90,000'),
        	(nightyto100 , '90,000-100,000'),
        	(hundredto125 , '100,000-125,000'),
        	(onetwofiveto150 ,'125,000-150,000'),
        	(onefiftyto200 , '150,000-200,000'),
        )


    ScholarshipFee =  'Scholarship Fees'
    zerofivek = '0-5000'
    fivektenk = '5000-10,000'
    tenkfifteenk = '10,000-15000'
    fifteenktwentyk = '15000-20,000'
    twentyktwentyfivek = '20,000-25000'
    twentyfivekthiryk = '25000-30,000'
    thirtytofive= '30,000-35000'
    thirtyfivetoforty = '35000-40,000'
    fortytofortyfive= '40,000-45000'
    fortyfivetofifty = '45000-50,000'
    fiftytosixty = '50,000-60,000'
    sixtyto70 = '60,000-70,000'
    seventyto80 = '70,000-80,000'
    eightyto90 = '80,000-90,000'
    nightyto100 = '90,000-100,000'
    hundredto125 = '100,000-125,000'
    onetwofiveto150= '125,000-150,000'

    onefiftyto200 = '150,000-200,000'

    ScholarshipFee = (

        	(zerofivek ,'0-5000'),
        	(fivektenk  ,'5000-10,000'),
        	(tenkfifteenk,  '10,000-15000'),
        	(fifteenktwentyk , '15000-20,000'),
        	(twentyktwentyfivek , '20,000-25000'),
        	(twentyfivekthiryk , '25000-30,000'),
        	(thirtytofive ,'30,000-35000'),
        	(thirtyfivetoforty , '35000-40,000'),
        	(fortytofortyfive, '40,000-45000'),
        	(fortyfivetofifty , '45000-50,000'),
        	(fiftytosixty , '50,000-60,000'),
        	(sixtyto70  ,'60,000-70,000'),
        	(seventyto80 , '70,000-80,000'),
        	(eightyto90  ,'80,000-90,000'),
        	(nightyto100 , '90,000-100,000'),
        	(hundredto125 , '100,000-125,000'),
        	(onetwofiveto150 ,'125,000-150,000'),
        	(onefiftyto200 , '150,000-200,000'),
        )


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
    agent_country =  models.CharField(max_length=35 , choices = Country, default= Country)

    pak_registeration_body1 = models.CharField(max_length=200, blank=True ,null=True,  default= None)
    pak_registeration_body2 = models.CharField(max_length=400, blank=True ,null=True, default= None)
    pak_registeration_body3 = models.CharField(max_length=400, blank=True ,null=True, default= None)
    pak_registeration_body4 = models.CharField(max_length=400, blank=True ,null=True, default= None)
    pak_registeration_body5 = models.CharField(max_length=400, blank=True ,null=True, default= None)
    pak_registeration_body6 = models.CharField(max_length=400, blank=True ,null=True, default= None)

    Internatiol_registeration_body1 = models.CharField(max_length=200, blank=True,null=True, default= None)
    Internatiol_registeration_body2 = models.CharField(max_length=200, blank=True,null=True, default= None)
    Internatiol_registeration_body3 = models.CharField(max_length=200, blank=True,null=True, default= None)
    Internatiol_registeration_body4 = models.CharField(max_length=200, blank=True ,null=True, default= None)
    Internatiol_registeration_body5 = models.CharField(max_length=200, blank=True ,null=True, default= None)
    Internatiol_registeration_body6 = models.CharField(max_length=200, blank=True,null=True, default= None)


    countries_Dealing = models.CharField(max_length=250, choices = Country,  default= Country)
    #Services_offered = models.CharField(max_length=250, default= None)
    service_type =  models.CharField(max_length=50, default= None)
    language_classes =  models.CharField(max_length=250, default= None, blank = True, null=True)
    processing = models.CharField(max_length=20 , default= None, blank = True, null=True)
    program_specialist = models.CharField(max_length=20, default= None, blank = True, null=True)
    refusal_appeals = models.CharField(max_length=20, default= None, blank = True)
    scholarships_offered = models.CharField(max_length=20, default= None, blank = True)
    interview_preparation = models.CharField(max_length=20, default= None, blank = True)
    travel_and_health = models.CharField(max_length=20, default= None, blank = True)
    travel_arrangements = models.CharField(max_length=20, default= None, blank = True)

    visa_ratio = models.CharField(max_length=20, default= None, blank = True)
    experience = models.CharField(max_length=20, default= None, blank = True)
    regional_office = models.CharField(max_length=300, default= None, blank = True)
    branches = models.CharField(max_length=250, default= None, blank = True)
    number_of_counselors = models.CharField(max_length=20, default= None, blank = True)

    processing_fee = models.CharField(max_length = 30,choices= ProcessingFee ,default = ProcessingFee, blank =True)
    language_fee = models.CharField(max_length = 30,choices=LanguageFee, default = LanguageFee, blank=True,null=True,)
    refusal_fee = models.CharField(max_length = 30,choices=RefusalFee ,default = RefusalFee, blank=True,null=True,)
    Interview_fee = models.CharField(max_length = 30,choices=InterviewFee,  default = InterviewFee, blank=True,null=True,)
    scholarshipfee = models.CharField(max_length = 30,choices=ScholarshipFee, default = ScholarshipFee, blank=True,null=True,)
    def __str__(self):
        return self.user.username



class AgentCompanyRegisterationInfo(models.Model):
    user = models.OneToOneField(User)
    #registered_name = models.CharField(max_length=200)



    def __str__(self):
        return self.user.username

class AgentServicesOffered(models.Model):
    user = models.OneToOneField(User)


    def __str__(self):
        return self.user.username
class AgentExpertise(models.Model):
    user = models.OneToOneField(User)



    def __str__(self):
        return self.user.username
class AgentFees(models.Model):

    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
class AgentLogo(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to = 'agent_logo',blank = True)
