from django.contrib.auth.models import User
from StudyAims.models import StdPersonalInfo,AgentCompanyInfo
import django_filters
from django import forms
from django_filters import Filter
from django_filters.fields import Lookup


class UserFilter(django_filters.FilterSet):
    #user__username = django_filters.CharFilter(lookup_expr='icontains')
    #city = django_filters.CharFilter(lookup_expr='icontains')
    #state = django_filters.CharFilter(lookup_expr='exact')


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
        (City,'City'),
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
    thirtyfive = '35%'
    forty = '40%'
    fortyfive = '45%'
    fifty = '50%'
    fiftyfive = '55%'
    sixty = '60%'
    sixtyfive = '65%'
    seventy = '70%'
    seventyfive = '75%'
    eighty = '80%'
    eightyfive = '85%'
    ninty = '90%'
    nintyfive = '95%'
    hundred = '100%'

    Percentage = (
        (Percentage , 'Percentage'),
        (thirtyfive , '35%'),
        (forty , '40%'),
        (fifty , '50%'),
        (fiftyfive , '55%'),
        (sixty , '60%'),
        (sixtyfive , '65%'),
        (seventy , '70%'),
        (seventyfive , '75%'),
        (eighty , '80%'),
        (eightyfive , '85%'),
        (ninty , '90%'),
        (nintyfive , '95%'),
        (hundred , '100%'),
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



    Desired_Subject  =(
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

        (Years_2  , '2 Years'),
        (Years_3  , '3 Years'),
        (Years_4 , '4 Years')
    )


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

    JobExperience = 'Job Experience'
    NoExperience = 'No Experience'
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

    (NoExperience , 'No Experience'),

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

    Gender = 'Gender'
    male = 'male'
    female = 'female'
    Gender = (
        (Gender , 'Gender'),
        (male, 'male'),
        (female, 'female'),
        )



    Budget = 'Budget'
    Lessthan1k = 'Less than $1000'
    OnkTo2kd   = '$1000-$2000'
    twokTo3kd   = '$2000-$4000'
    threekTo4kd   = '$4000-$6000'
    sixkTo8kd   = '$6000-$8000'
    eightkTo10kd  = '$8000-$10000'
    tenkTo12kd = '$10000-$12000'
    forteenkTo16kd = '$14000-$16000'
    sixteenkTo18kd = '$16000-$18000'
    eighteenkTo20kd = '$18000-$20000'
    twentykTo22kd = '$20000-$22000'
    twentytwokTo24kd = '$22000-$24000'
    twen4To26kd = '$24000-$26000'
    twenty6kTo28kd = '$26000-$28000'
    twenty8kTo30kd = '$28000-$30000'
    more = 'More than $30,000'

    Budget = (
    (Budget , 'Budget'),
    (Lessthan1k , 'Less than $1000'),
    (OnkTo2kd   , '$1000-$2000'),
    (twokTo3kd  , '$2000-$4000'),
    (threekTo4kd   , '$4000-$6000'),
    (sixkTo8kd   , '$6000-$8000'),
    (eightkTo10kd  , '$8000-$10000'),
    (tenkTo12kd , '$10000-$12000'),
    (forteenkTo16kd , '$14000-$16000'),
    (sixteenkTo18kd , '$16000-$18000'),
    (eighteenkTo20kd , '$18000-$20000'),
    (twentykTo22kd , '$20000-$22000'),
    (twentytwokTo24kd , '$22000-$24000'),
    (twen4To26kd , '$24000-$26000'),
    (twenty6kTo28kd , '$26000-$28000'),
    (twenty8kTo30kd , '$28000-$30000'),
    (more , 'More than $30,000'),
    )

    State = 'State'
    Punjab = 'Punjab'
    IslamabadICT = 'Islamabad ICT'
    Sindh = 'Sindh'
    KPK = 'KPC'
    Balochistan = 'Balochistan'
    GilgitBaltistan = 'Gilgit Baltistan'
    AzadJamuKashmir = 'Azad Jamui Kashmir'

    State = (
    (State ,'State'),
    (Punjab , 'Punjab'),
    (IslamabadICT , 'Islamabad ICT'),
    (Sindh , 'Sindh'),
    (KPK , 'KPC'),
    (Balochistan , 'Balochistan'),
    (GilgitBaltistan , 'Gilgit Baltistan'),
    (AzadJamuKashmir , 'Azad Jamui Kashmir'),
    )


    country_of_residence = django_filters.ChoiceFilter(lookup_expr='icontains'  )
    highest_qualification = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = Degree ,lookup_expr='icontains'  )
    subject = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = Subject , lookup_expr='icontains'  )
    passing_year =  django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = PassingYear,lookup_expr='icontains'  )
    percentage = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,lookup_expr='exact')
    studyGap = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = StudyGap,lookup_expr='icontains'  )
    experience = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple,choices = JobExperience,lookup_expr='exact')
    english_language = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices = English_Language,lookup_expr='icontains'  )
    other_Language = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple, choices = OtherLanguage,lookup_expr='icontains'  )
    desired_degree = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple,choices = Desired_Degree ,lookup_expr='icontains'  )
    desired_subject = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple,choices = Subject,lookup_expr='icontains'  )
    desired_country = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple,choices = Country,lookup_expr='icontains'  )
    scholarships = django_filters.ChoiceFilter(choices = Scholarships,lookup_expr='icontains')
    budget = django_filters.MultipleChoiceFilter(widget=forms.CheckboxSelectMultiple,choices = Budget, lookup_expr='exact')
    gender = django_filters.ChoiceFilter(choices = Gender,  lookup_expr='exact')
    city = django_filters.ChoiceFilter(choices = City,lookup_expr='icontains')
    state = django_filters.ChoiceFilter(choices = State, lookup_expr='exact')

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




class ListFilter( Filter ):
  def filter( self, qs, value ):
    return super( ListFilter, self ).filter( qs, Lookup( value.split( u"," ), "in") )

class FilterAgents(django_filters.FilterSet):
    #user__username = django_filters.CharFilter(lookup_expr='icontains')
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

    Nationality = (
    (Nationality, 'Nationality'),
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

    RefusalAppeals = 'Refusal Appeals'
    Yes = 'Yes'
    No = 'No'
    ScholarshipsOffered = 'Scholarships Offered'
    InterviewPreparation = 'Interview Preparation'
    TravelAndHealthInsurance = 'Travel and Health Insurance'
    TravelArrangements = 'Travel Arrangements'
    RegionalOffice = 'Regional Office'
    RefusalAppeals = (
    (RefusalAppeals , 'Refusal Appeals'),
    (Yes , 'Yes'),
    (No , 'No'),
    )

    ScholarshipsOffered = (
    (ScholarshipsOffered , 'Scholarships Offered'),
    (Yes , 'Yes'),
    (No , 'No'),
    )

    InterviewPreparation = (
    (InterviewPreparation , 'Interview Preparation'),
    (Yes , 'Yes'),
    (No , 'No'),
    )
    TravelAndHealthInsurance = (
    (TravelAndHealthInsurance , 'Travel and Health Insurance'),
    (Yes , 'Yes'),
    (No , 'No'),
    )
    RegionalOffice = (

    (Yes , 'Yes'),
    (No , 'No'),
    )


    TravelArrangements = (
    (TravelArrangements , 'Travel Arrangements'),
    (Yes , 'Yes'),
    (No , 'No'),
    )


    VisaSuccessRatio = 'Visa Success Ratio'
    thirtyfive = '35%'
    forty = '40%'
    fortyfive = '45%'
    fifty = '50%'
    fiftyfive = '55%'
    sixty = '60%'
    sixtyfive = '65%'
    seventy = '70%'
    seventyfive = '75%'
    eighty = '80%'
    eightyfive = '85%'
    ninty = '90%'
    nintyfive = '95%'
    hundred = '100%'

    VisaSuccessRatio = (
            (VisaSuccessRatio , 'Visa Success Ratio'),
            (thirtyfive , '35%'),
            (forty , '40%'),
            (fifty , '50%'),
            (fiftyfive , '55%'),
            (sixty , '60%'),
            (sixtyfive , '65%'),
            (seventy , '70%'),
            (seventyfive , '75%'),
            (eighty , '80%'),
            (eightyfive , '85%'),
            (ninty , '90%'),
            (nintyfive , '95%'),
            (hundred , '100%'),

        )

    Experience = 'Experience'
    NoExperience = 'No Experience'
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
    more = 'More Than 10 Years'

    Experience = (

    (NoExperience , 'No Experience'),

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
    (more , 'More Than 10 Years'),

    )


    Branches = 'Branches'
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
    Branches =(
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

    City=(

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
    NumberOfCounselors = 'Number of Counselors'
    five = '5'
    ten = '10'
    fifteen = '15'
    twenty = '20'
    twentyfive = '25'
    thirty = '30'
    thirtyfive = '35'
    forty = '40'
    fortyfive = '45'
    fifty = '50'

    NumberOfCounselors = (

    (five , '5'),
    (ten , '10'),
    (fifteen , '15'),
    (twenty ,'20'),
    (twentyfive , '25'),
    (thirty , '30'),
    (thirtyfive , '35'),
    (forty , '40'),
    (fortyfive , '45'),
    (fifty , '50'),
    )
    Provice = 'Province'
    Punjab = 'Punjab'
    IslamabadICT = 'Islamabad ICT'
    Sindh = 'Sindh'
    KPK = 'KPC'
    Balochistan = 'Balochistan'
    GilgitBaltistan = 'Gilgit Baltistan'
    AzadJamuKashmir = 'Azad Jamui Kashmir'

    Province = (

    (Punjab , 'Punjab'),
    (IslamabadICT , 'Islamabad ICT'),
    (Sindh , 'Sindh'),
    (KPK , 'KPC'),
    (Balochistan , 'Balochistan'),
    (GilgitBaltistan , 'Gilgit Baltistan'),
    (AzadJamuKashmir , 'Azad Jamui Kashmir'),
    )

    yes= 'Yes'
    no = 'No'

    Processing = (
    (yes, 'Yes'),
    (no , 'No'),
    )
    RefusalAppeal = (
    (yes, 'Yes'),
    (no , 'No'),

    )
    Scholarship = (
    (yes, 'Yes'),
    (no , 'No'),
    )
    InterviewPreparation=(
    (yes, 'Yes'),
    (no , 'No'),
    )
    TravelArrangements=(
    (yes, 'Yes'),
    (no , 'No'),
    )
    TravelAndHealthInsurance=(
    (yes, 'Yes'),
    (no , 'No'),
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
    OtherRes = 'Other(Res)'

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
        (OtherRes , 'Other(Res)'),
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
    LanguageClass = 'Language Classes'
    ProgramSpecialists = 'Program Specialists'
    RefusalAppeals = 'Refusal Appeals'
    Scholarships = 'Scholarships'
    InterviewPreparation = 'Interview Preparation'
    TravelHealthInsurance = 'Travel & Health Insurance'
    TravelArrangements = 'Travel Arrangements'
    Other = 'Other'

    TypesOfServices = (
    (AdmissionsVisaProcessing , 'Admissions & Visa Processing'),
    (LanguageClasses , 'Language Classes'),
    (ProgramSpecialists , 'Program Specialists'),
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
    Branches =(
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
    agent_state = django_filters.ChoiceFilter(choices=Province, lookup_expr='exact')
    agent_city = django_filters.ChoiceFilter(choices=City, lookup_expr='exact')
    processing = django_filters.MultipleChoiceFilter(choices=TypesOfServices ,lookup_expr='exact',widget=forms.CheckboxSelectMultiple )
    countries_Dealing = django_filters.MultipleChoiceFilter(choices=Country, lookup_expr='in', widget=forms.CheckboxSelectMultiple)

    language_classes = django_filters.MultipleChoiceFilter(choices=LanguageClasses,widget=forms.CheckboxSelectMultiple, lookup_expr='icontains')
    program_specialist = django_filters.MultipleChoiceFilter(choices=ProgramSpecialist ,lookup_expr='icontains', widget=forms.CheckboxSelectMultiple)
    refusal_appeals = django_filters.MultipleChoiceFilter(choices= RefusalAppeal,lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    scholarships_offered = django_filters.MultipleChoiceFilter(choices= Scholarship,lookup_expr='icontains', widget=forms.CheckboxSelectMultiple)
    #interview_preparation = django_filters.ChoiceFilter(choices= InterviewPreparation,lookup_expr='exact')
    travel_and_health = django_filters.MultipleChoiceFilter(choices=TravelAndHealthInsurance ,lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    #travel_arrangements = django_filters.ChoiceFilter(choices=TravelArrangements ,lookup_expr='exact')
    visa_ratio = django_filters.MultipleChoiceFilter(choices=VisaSuccessRatio ,lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    experience = django_filters.MultipleChoiceFilter(choices= Experience ,lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    regional_office = django_filters.MultipleChoiceFilter(choices = RegionalOffice,lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    branches = django_filters.MultipleChoiceFilter(choices=Branches ,lookup_expr='icontains', widget=forms.CheckboxSelectMultiple)
    number_of_counselors = django_filters.ChoiceFilter(choices=NumberOfCounselors  , lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    processing_fee = django_filters.MultipleChoiceFilter(choices= ProcessingFee, lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    language_fee = django_filters.MultipleChoiceFilter(choices= LanguageFee,lookup_expr='exact', widget=forms.CheckboxSelectMultiple )
    refusal_fee = django_filters.MultipleChoiceFilter(choices= RefusalFee,lookup_expr='exact', widget=forms.CheckboxSelectMultiple)
    Interview_fee = django_filters.MultipleChoiceFilter(choices =InterviewFee,widget=forms.CheckboxSelectMultiple ,lookup_expr='exact')
    #scholarshipfee = django_filters.MultipleChoiceFilter(choices =ScholarshipFee, widget=forms.CheckboxSelectMultiple ,lookup_expr='exact')


    class Meta:
        model = AgentCompanyInfo
        fields = ['agent_state', 'agent_city', 'processing',
         'countries_Dealing', 'language_classes',
         'program_specialist', 'refusal_appeals', 'scholarships_offered', #'interview_preparation',
        'travel_and_health', #'travel_arrangements',
        'visa_ratio', 'experience', 'regional_office', 'branches', 'number_of_counselors', 'processing_fee', 'language_fee', 'refusal_fee',
        'Interview_fee',# 'scholarshipfee'
        ]
