from django import forms
from django.contrib.auth.models import User
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit, Field
#from crispy_forms.bootstrap import FormActions

#from django.localflavor.us.forms import PhoneNumberField
from StudyAims.models import StdPersonalInfo,  AgentCompanyInfo, AgentCompanyRegisterationInfo
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
    #user_perm = forms.ChoiceField(widget=forms.RadioSelect(),choices=User_CHOICES , label='')
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
        fields = ('first_name','username', 'email', 'password')
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
    #state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'STATE'}),
    #             )
    #country_of_residence = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country of Residence'}),
    #             )
    #nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nationality'}),
    #             )

    #city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City'}),
    #             )
    Insititution = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From Institute'}),
                 )
    #percentage = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Percentage'}),
    #             )

#    budget = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Budget'}),
#                 )
    english_language_score =  forms.CharField(widget=forms.TextInput(attrs={'placeholder':'English Language Score'}),
                 )
    Other_Language_score =    forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Language Score'}),
                 )
    #country_of_residence = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name" ,)
    #city = forms.ModelChoiceField(queryset= CityList.objects.all().order_by('city_name'), to_field_name="city_name")


    class Meta():
        model = StdPersonalInfo
        #exclude = ('user',)
        fields = ('gender', 'age','city','country_of_residence','whatsapp','contact_number','any_other_number','address','state','nationality', 'highest_qualification', 'subject', 'Insititution','from_country', 'percentage', 'passing_year','studyGap' ,'experience','achievements','english_language', 'english_language_score', 'other_Language','Other_Language_score',
        'desired_degree','desired_subject','desired_country','scholarships','budget')

#class StdQualificationForm(forms.ModelForm):
    #highest_qualification = forms.ModelChoiceField(queryset= HighestQualification.objects.all().order_by('qualification'), to_field_name="qualification")
    #subject = forms.ModelChoiceField(queryset= SubjectList.objects.all().order_by('subject'), to_field_name="subject")
    #program_duration = forms.ModelChoiceField(queryset= ProgramDuration.objects.all().order_by('duration'), to_field_name="duration")
    #from_country = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name")
    #percentage = forms.ModelChoiceField(queryset= Percentage.objects.all().order_by('Percent'), to_field_name="Percent")
    #passing_year = forms.ModelChoiceField(queryset= PassingYear.objects.all().order_by('year'), to_field_name="year")

#    class Meta():


#        model = StudentQualifications
#        fields = ()





class AgentCompanyInfoForm(forms.ModelForm):

    #Country = 'Country'
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

    ProgramSpecialist = 'Program Specialist'
    Certificate = 'Certificate'
    Diploma = 'Diploma'
    OLevel = 'O-Level'
    IntBaccalaureate = 'Int. Baccalaureate'
    Foundation = 'Foundation'
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
    OtherRes = 'Others'

    ProgramSpecialist = (
        (Certificate , 'Certificate'),
        (Diploma , 'Diploma'),
        (OLevel , 'O-Level'),
        (ALevel , 'A-Level'),
        (Foundation , 'Foundation'),
        (IntBaccalaureate , 'Int. Baccalaureate'),
        (AssociateDegree , 'Associate Degree'),
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
        (OtherRes , 'Others'),
    )

    LanguageClasses = 'Language Classes'

    IELTS = 'IELTS'
    TOEFL = 'TOEFL'
    PTE = 'PTE'
    German = 'German'
    Chinese = 'Chinese'
    Japanese = 'Japanese'
    Spanish = 'Spanish'
    French = 'French '
    Italian = 'Italian'
    Turkish= 'Turkish'
    Portuguese = 'Portuguese'
    Korian = 'Korian'
    Other = 'Other'
    LanguageClasses = (


        (IELTS, 'IELTS'),
        (TOEFL, 'TOEFL'),
        (PTE, 'PTE'),
        (German , 'German'),
        (Chinese , 'Chinese'),
        (Japanese , 'Japanese'),
        (Spanish , 'Spanish'),
        (French , 'French '),
        (Italian , 'Italian'),
        (Turkish, 'Turkish'),
        (Portuguese , 'Portuguese'),
        (Korian , 'Korian'),
        (Other, 'Other'),
        )

    TypesOfServices = 'Types of Services'
    AdmissionsVisaProcessing = 'Admissions & Visa Processing'


    LanguageClas = 'Language Classes'
    ProgramSpecial = 'Program Specialists'
    RefusalAppeals = 'Refusal Appeals'
    Scholarships = 'Scholarships'
    InterviewPreparation = 'Interview Preparation'
    TravelHealthInsurance = 'Travel & Health Insurance'
    TravelArrangements = 'Travel Arrangements'
    Other = 'Other'

    TypesOfServices = (
    (AdmissionsVisaProcessing , 'Admissions & Visa Processing'),
    (LanguageClas , 'Language Classes'),
    (ProgramSpecial , 'Program Specialists'),
    (RefusalAppeals , 'Refusal Appeals'),
    (Scholarships , 'Scholarships'),
    (InterviewPreparation , 'Interview Preparation'),
    (TravelHealthInsurance , 'Travel & Health Insurance'),
    (TravelArrangements , 'Travel Arrangements'),
    (Other , 'Other'),
    )

    Branches = 'Branches'
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
    Islamabad = 'Islamabad'
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
    Sialkot = 'Sialkot'
    Rawalpindi = 'Rawalpindi'
    Branches =(
            (Lahore, 'Lahore'),
            (Islamabad, 'Islamabad'),
            (Karachi, 'Karachi'),
            (Gujranwala, 'Gujranwala'),
            (Multan, 'Multan'),
            (Rawalpindi, 'Rawalpindi'),
            (Sialkot, 'Sialkot'),
            (Gujrat, 'Gujrat'),

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
    Nationality = 'Nationality'
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






    Countries = (

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
    #service_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Service Types'}),
    #             )
    linked_In = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'LinkedIn URL'}),
                 )
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Address'}),
                 )
    office_contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Office Contact Number'}),
                 )
    office_contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Office Contact Number'}),
                 )
#    agent_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'STATE'}),
#                 )
    #country_of_residence = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country of Residence'}),
    #             )
    #nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nationality'}),
    #             )
    #agent_city =    forms.CharField(widget=forms.TextInput(attrs={'placeholder':'CITY'}),
    #             )
    #agent_country = forms.ModelChoiceField(queryset= Countries.objects.all().order_by('country_name'), to_field_name="country_name")
    #agent_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Province'}),
    #             )

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
#    countries_Dealing = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Countries Dealing'}),
                 #)
    #Services_offered= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Services Offered'}),

    #             )




    #refusal_appeals = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Refusal Appeals'}),
    #             )
    #scholarships_offered = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Scholaships Offered'}),
    #             )
    #interview_preparation = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Interview Preparation'}),
    #             )
    #travel_and_health = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Travel and Health Insurance'}),
                 #)
    #travel_arrangements = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Travel Arrangements'}),
    #             )

    #visa_ratio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Visa Ratio'}),
#                 )
#    experience = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Experience (Years)'}),
#                 )
#    regional_office = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Regional Offices'}),
#                 )
    branches = forms.MultipleChoiceField(
            choices=Branches,
            initial='Branches',
            widget=forms.CheckboxSelectMultiple,
            required=True,

        )
    #number_of_counselors = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number of Counselors'}),)

    service_type = forms.MultipleChoiceField(
            choices=TypesOfServices,
            initial='Types Of Services',
            widget=forms.CheckboxSelectMultiple,
            required=True,

        )

    countries_Dealing = forms.MultipleChoiceField(
            choices = Countries,
            widget=forms.CheckboxSelectMultiple,
            required=True,

        )
    program_specialist = forms.MultipleChoiceField(
            choices=ProgramSpecialist,
            initial='Program Specialist',
            widget=forms.CheckboxSelectMultiple,
            required=True,
                 )

    language_classes = forms.MultipleChoiceField(
            choices=LanguageClasses,
            initial='Language Classes',
            widget=forms.CheckboxSelectMultiple,
            required=True,
                 )

    class Meta():
        model = AgentCompanyInfo
        fields = ('comp_name','service_type','company_owner','agent_whatsapp','address','alternative_email','agent_website','facebook_link','linked_In','office_contact','agent_city','agent_state','agent_country','nationality',
        'pak_registeration_body1','pak_registeration_body2','pak_registeration_body3','pak_registeration_body4','pak_registeration_body5','pak_registeration_body6','Internatiol_registeration_body1','Internatiol_registeration_body2','Internatiol_registeration_body3',
            'Internatiol_registeration_body4','Internatiol_registeration_body5','Internatiol_registeration_body6','countries_Dealing','language_classes','program_specialist','refusal_appeals','scholarships_offered','interview_preparation','travel_and_health','travel_arrangements',
            'visa_ratio','experience','regional_office','branches','number_of_counselors','processing_fee','language_fee','refusal_fee','Interview_fee','scholarshipfee')


class AgentCompanyRegisterationInfoForm(forms.ModelForm):
    Country = 'Country'
    Nationality = 'Nationality'
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






    Countries = (

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
    #country = forms.MultipleChoiceField(
    #        choices=Countries,
    #        initial='Countries',
    #        widget=forms.CheckboxSelectMultiple,
    #        required=True,
    #             )
    class Meta():
        model = AgentCompanyRegisterationInfo

        fields = ('country',)
