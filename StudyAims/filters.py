from django.contrib.auth.models import User
from StudyAims.models import StdPersonalInfo,  StudentLanguage, UserType , StudentFuture, AgentCompanyInfo
import django_filters
from django import forms

class UserFilter(django_filters.FilterSet):
    #user__username = django_filters.CharFilter(lookup_expr='icontains')
    #city = django_filters.CharFilter(lookup_expr='icontains')
    #state = django_filters.CharFilter(lookup_expr='exact')

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
    Desired_Degree = 'Desired Degree'
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
    Desired_Degree = (

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
    Desired_Subject = 'Desired Subject'
    Pyshics = 'Physics'
    Engineering = 'Engineering'

    Desired_Subject  =(

        (Pyshics , 'Physics'),
        (Engineering , 'Engineering'),
    )
    Program_Duration = 'Program Duration'
    Years_2 = '2 Years'
    Years_3 = '3 Years'
    Years_4 = '4 Years'


    Program_Duration = (

        (Years_2  , '2 Years'),
        (Years_3  , '3 Years'),
        (Years_4 , '4 Years')
    )

    Country = 'Country'
    Pak = 'Pakistan'
    Australia = 'Australia'
    Country = (

        (Pak , 'Pakistan'),
        (Australia , 'Australia'),

    )
    #id = models.OneToOneField(User)
    Scholarships = 'Scholarships'
    Yes = 'Yes'
    No = 'No'
    Scholarships = (

        (Yes, 'Yes'),
        (No, 'No'),
        )

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


    country_of_residence = django_filters.ChoiceFilter(choices = Country,lookup_expr='icontains'  )
    highest_qualification = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = Degree ,lookup_expr='icontains'  )
    subject = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = Subject , lookup_expr='icontains'  )
    passing_year =  django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = PassingYear,lookup_expr='icontains'  )
    percentage = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,lookup_expr='exact')
    studyGap = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = StudyGap,lookup_expr='icontains'  )
    experience = django_filters.CharFilter(lookup_expr='exact')
    english_language = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = English_Language,lookup_expr='icontains'  )
    other_Language = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple, choices = OtherLanguage,lookup_expr='icontains'  )
    desired_degree = django_filters.ChoiceFilter(choices = Desired_Degree ,lookup_expr='icontains'  )
    desired_subject = django_filters.ChoiceFilter(choices = Subject,lookup_expr='icontains'  )
    desired_country = django_filters.ChoiceFilter(choices = Country,lookup_expr='icontains'  )
    scholarships = django_filters.ChoiceFilter(choices = Scholarships,lookup_expr='icontains'  )
    budget = django_filters.CharFilter(lookup_expr='exact')
    gender = django_filters.CharFilter(lookup_expr='exact')
    city = django_filters.ChoiceFilter(choices = City,lookup_expr='icontains'  )
    state = django_filters.CharFilter(lookup_expr='exact')

    #gender = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #year_joined__gt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__gt')
    #year_joined__lt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__lt')
    #gender__stdpersonalinfo__user = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = StdPersonalInfo
        fields = ['gender', 'city', 'state', 'country_of_residence', 'highest_qualification', 'subject','percentage', 'passing_year', 'studyGap', 'experience', 'english_language','other_Language', 'desired_degree',
        'desired_subject', 'desired_country', 'scholarships', 'budget' ]

#class PersonalFilter(django_filters.FilterSet):
#    gender = django_filters.CharFilter(lookup_expr='icontains')
    #gender = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #year_joined__gt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__gt')
    #year_joined__lt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__lt')


#    class Meta:
#        model = StdPersonalInfo
#        fields = ['gender']

class FilterAgents(django_filters.FilterSet):
    #user__username = django_filters.CharFilter(lookup_expr='icontains')
    agent_state = django_filters.CharFilter(lookup_expr='icontains')
    agent_city = django_filters.CharFilter(lookup_expr='icontains')
    processing = django_filters.CharFilter(lookup_expr='exact')
    countries_Dealing = django_filters.CharFilter(lookup_expr='icontains')
    language_classes = django_filters.CharFilter(lookup_expr='icontains')
    program_specialist = django_filters.CharFilter(lookup_expr='icontains')
    refusal_appeals = django_filters.CharFilter(lookup_expr='exact')
    scholarships_offered = django_filters.CharFilter(lookup_expr='icontains')
    interview_preparation = django_filters.CharFilter(lookup_expr='exact')
    travel_and_health = django_filters.CharFilter(lookup_expr='exact')
    travel_arrangements = django_filters.CharFilter(lookup_expr='exact')
    visa_ratio = django_filters.CharFilter(lookup_expr='exact')
    experience = django_filters.CharFilter(lookup_expr='exact')
    regional_office = django_filters.CharFilter(lookup_expr='exact')
    branches = django_filters.CharFilter(lookup_expr='icontains')
    number_of_counselors = django_filters.CharFilter(lookup_expr='exact')
    processing_fee = django_filters.CharFilter(lookup_expr='exact')
    language_fee = django_filters.CharFilter(lookup_expr='exact')
    refusal_fee = django_filters.CharFilter(lookup_expr='exact')
    Interview_fee = django_filters.CharFilter(lookup_expr='exact')
    scholarshipfee = django_filters.CharFilter(lookup_expr='exact')


    class Meta:
        model = AgentCompanyInfo
        fields = ['agent_state', 'agent_city', 'processing', 'countries_Dealing', 'language_classes', 'program_specialist', 'refusal_appeals', 'scholarships_offered', 'interview_preparation',
        'travel_and_health', 'travel_arrangements', 'visa_ratio', 'experience', 'regional_office', 'branches', 'number_of_counselors', 'processing_fee', 'language_fee', 'refusal_fee',
        'Interview_fee', 'scholarshipfee' ]
