# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-18 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyAims', '0013_agentcompanyinfo_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='agent_city',
            field=models.CharField(choices=[('City', 'City'), ('Abbottabad', 'Abbottabad'), ('Adezai', 'Adezai'), ('Ahmed Nager Chatha', 'Ahmed Nager Chatha'), ('Ahmedpur East', 'Ahmedpur East'), ('Ali Bandar', 'Ali Bandar'), ('Ali Pur', 'Ali Pur'), ('Arifwala', 'Arifwala'), ('Astor', 'Astor'), ('Attock', 'Attock'), ('Ayubia', 'Ayubia'), ('Baden', 'Baden'), ('Bagh', 'Bagh'), ('Bahawalnagar', 'Bahawalnagar'), ('Bahawalpur', 'Bahawalpur'), ('Bajaur', 'Bajaur'), ('Banda Daud Shah', 'Banda Daud Shah'), ('Bannu', 'Bannu'), ('Baramula', 'Baramula'), ('Basti Malook', 'Basti Malook'), ('Batagram', 'Batagram'), ('Bazdar', 'Bazdar'), ('Bela', 'Bela'), ('Bellpat', 'Bellpat'), ('Bhagalchur', 'Bhagalchur'), ('Bhaipheru', 'Bhaipheru'), ('Bhakkar', 'Bhakkar'), ('Bhalwal', 'Bhalwal'), ('Bhimber', 'Bhimber'), ('Birote', 'Birote'), ('Buner', 'Buner'), ('Burewala', 'Burewala'), ('Burj', 'Burj'), ('Chachro', 'Chachro'), ('Chagai', 'Chagai'), ('Chah Sandan', 'Chah Sandan'), ('Chailianwala', 'Chailianwala'), ('Chakdara', 'Chakdara'), ('Chakku', 'Chakku'), ('Chakwal', 'Chakwal'), ('Chaman', 'Chaman'), ('Charsadda', 'Charsadda'), ('Chhatr', 'Chhatr'), ('Chichawatni', 'Chichawatni'), ('Chiniot', 'Chiniot'), ('Chitral', 'Chitral'), ('Chowk Azam', 'Chowk Azam'), ('Chowk Sarwar Shaheed', 'Chowk Sarwar Shaheed'), ('Dadu', 'Dadu'), ('Dalbandin', 'Dalbandin'), ('Dargai', 'Dargai'), ('Darya Khan', 'Darya Khan'), ('Daska', 'Daska'), ('Dera Bugti', 'Dera Bugti'), ('Dera Ghazi Khan', 'Dera Ghazi Khan'), ('Dera Ismail Khan', 'Dera Ismail Khan'), ('Derawar Fort', 'Derawar Fort'), ('Dhana Sar', 'Dhana Sar'), ('Dhaular', 'Dhaular'), ('Digri', 'Digri'), ('Dina City', 'Dina City'), ('Dinga', 'Dinga'), ('Dipalpur', 'Dipalpur'), ('Diplo', 'Diplo'), ('Diwana', 'Diwana'), ('Dokri', 'Dokri'), ('Drasan', 'Drasan'), ('Drosh', 'Drosh'), ('Duki', 'Duki'), ('Dushi', 'Dushi'), ('Duzab', 'Duzab'), ('Faisalabad', 'Faisalabad'), ('Fateh Jang', 'Fateh Jang'), ('Gadar', 'Gadar'), ('Gajar', 'Gajar'), ('Garhi Khairo', 'Garhi Khairo'), ('Garruck', 'Garruck'), ('Ghakhar Mandi', 'Ghakhar Mandi'), ('Ghanian', 'Ghanian'), ('Ghauspur', 'Ghauspur'), ('Ghazluna', 'Ghazluna'), ('Ghotki', 'Ghotki'), ('Gilgit', 'Gilgit'), ('Girdan', 'Girdan'), ('Gujar Khan', 'Gujar Khan'), ('Gujranwala', 'Gujranwala'), ('Gujrat', 'Gujrat'), ('Gulistan', 'Gulistan'), ('Gwadar', 'Gwadar'), ('Gwash', 'Gwash'), ('Hab Chauki', 'Hab Chauki'), ('Hafizabad', 'Hafizabad'), ('Hala', 'Hala'), ('Hameedabad', 'Hameedabad'), ('Hangu', 'Hangu'), ('Haripur', 'Haripur'), ('Harnai', 'Harnai'), ('Haroonabad', 'Haroonabad'), ('Hasilpur', 'Hasilpur'), ('Haveli Lakha', 'Haveli Lakha'), ('Hinglaj', 'Hinglaj'), ('Hoshab', 'Hoshab'), ('Hunza', 'Hunza'), ('Hyderabad', 'Hyderabad'), ('Islamkot', 'Islamkot'), ('Ispikan', 'Ispikan'), ('Jacobabad', 'Jacobabad'), ('Jahania', 'Jahania'), ('Jalla Araain', 'Jalla Araain'), ('Jamesabad', 'Jamesabad'), ('Jampur', 'Jampur'), ('Jamshoro', 'Jamshoro'), ('Janghar', 'Janghar'), ('Jati (Mughalbhin)', 'Jati (Mughalbhin)'), ('Jauharabad', 'Jauharabad'), ('Jhal Jhao', 'Jhal Jhao'), ('Jhang', 'Jhang'), ('Jhatpat', 'Jhatpat'), ('Jhelum', 'Jhelum'), ('Jhudo', 'Jhudo'), ('Jiwani', 'Jiwani'), ('Jungshahi', 'Jungshahi'), ('Kalabagh', 'Kalabagh'), ('Kalam', 'Kalam'), ('Kalandi', 'Kalandi'), ('Kalat', 'Kalat'), ('Kamalia', 'Kamalia'), ('Kamararod', 'Kamararod'), ('Kamokey', 'Kamokey'), ('Kanak', 'Kanak'), ('Kandi', 'Kandi'), ('Kandiaro', 'Kandiaro'), ('Kanpur', 'Kanpur'), ('Kapip', 'Kapip'), ('Kappar', 'Kappar'), ('Karachi', 'Karachi'), ('Karak', 'Karak'), ('Karodi', 'Karodi'), ('Karor Lal Esan', 'Karor Lal Esan'), ('Kashmor', 'Kashmor'), ('Kasur', 'Kasur'), ('Katuri', 'Katuri'), ('Keti Bandar', 'Keti Bandar'), ('Khairpur', 'Khairpur'), ('Khanaspur', 'Khanaspur'), ('Khanewal', 'Khanewal'), ('Khanpur', 'Khanpur'), ('Kharan', 'Kharan'), ('Kharian', 'Kharian'), ('Khokhropur', 'AKhokhropur'), ('Khora', 'Khora'), ('khuiratta', 'khuiratta'), ('Khushab', 'Khushab'), ('Khuzdar', 'Khuzdar'), ('Khyber', 'Khyber'), ('Kikki', 'Kikki'), ('Klupro', 'Klupro'), ('Kohan', 'Kohan'), ('Kohat', 'Kohat'), ('Kohistan', 'Kohistan'), ('Kohlu', 'Kohlu'), ('Korak', 'Korak'), ('Korangi', 'Korangi'), ('Kot Addu', 'Kot Addu'), ('Kot Sarae', 'Kot Sarae'), ('Kotli', 'Kotli'), ('Kotri', 'Kotri'), ('Kurram', 'Kurram'), ('Laar', 'Laar'), ('Lahore', 'Lahore'), ('Lahri', 'Lahri'), ('Lakki Marwat', 'Lakki Marwat'), ('Lalamusa', 'Lalamusa'), ('Larkana', 'Larkana'), ('Lasbela', 'Lasbela'), ('Latamber', 'Latamber'), ('Layyah', 'Layyah'), ('Liari', 'Liari'), ('Lodhran', 'Lodhran'), ('Loralai', 'Loralai'), ('Lower Dir', 'Lower Dir'), ('Lund', 'Lund'), ('Mach', 'Mach'), ('Madyan', 'Madyan'), ('Mailsi', 'Mailsi'), ('Makhdoom Aali', 'Makhdoom Aali'), ('Malakand', 'Malakand'), ('Mamoori', 'Mamoori'), ('Mand', 'Mand'), ('Mandi Bahauddin', 'Mandi Bahauddin'), ('Mandi Warburton', 'Mandi Warburton'), ('Mangla', 'Mangla'), ('Manguchar', 'Manguchar'), ('Mansehra', 'Mansehra'), ('Mardan', 'Mardan'), ('Mashki Chah', 'Mashki Chah'), ('Maslti', 'Maslti'), ('Mastuj', 'Mastuj'), ('Mastung', 'Mastung'), ('Mathi', 'Mathi'), ('Matiari', 'Matiari'), ('Mehar', 'Mehar'), ('Mekhtar', 'Mekhtar'), ('Merui', 'Merui'), ('Mian Channu', 'Mian Channu'), ('Mianez', 'Mianez'), ('Mianwali', 'Mianwali'), ('Minawala', 'Minawala'), ('Miram Shah', 'Miram Shah'), ('Mirpur', 'Mirpur'), ('Mirpur Batoro', 'Mirpur Batoro'), ('Mirpur Khas', 'Mirpur Khas'), ('Mirpur Sakro', 'Mirpur Sakro'), ('Mithani', 'Mithani'), ('Mithi', 'Mithi'), ('Mohmand', 'Mohmand'), ('Mongora', 'Mongora'), ('Moro', 'Moro'), ('Multan', 'Multan'), ('Murgha Kibzai', 'Murgha Kibzai')], default=(('City', 'City'), ('Abbottabad', 'Abbottabad'), ('Adezai', 'Adezai'), ('Ahmed Nager Chatha', 'Ahmed Nager Chatha'), ('Ahmedpur East', 'Ahmedpur East'), ('Ali Bandar', 'Ali Bandar'), ('Ali Pur', 'Ali Pur'), ('Arifwala', 'Arifwala'), ('Astor', 'Astor'), ('Attock', 'Attock'), ('Ayubia', 'Ayubia'), ('Baden', 'Baden'), ('Bagh', 'Bagh'), ('Bahawalnagar', 'Bahawalnagar'), ('Bahawalpur', 'Bahawalpur'), ('Bajaur', 'Bajaur'), ('Banda Daud Shah', 'Banda Daud Shah'), ('Bannu', 'Bannu'), ('Baramula', 'Baramula'), ('Basti Malook', 'Basti Malook'), ('Batagram', 'Batagram'), ('Bazdar', 'Bazdar'), ('Bela', 'Bela'), ('Bellpat', 'Bellpat'), ('Bhagalchur', 'Bhagalchur'), ('Bhaipheru', 'Bhaipheru'), ('Bhakkar', 'Bhakkar'), ('Bhalwal', 'Bhalwal'), ('Bhimber', 'Bhimber'), ('Birote', 'Birote'), ('Buner', 'Buner'), ('Burewala', 'Burewala'), ('Burj', 'Burj'), ('Chachro', 'Chachro'), ('Chagai', 'Chagai'), ('Chah Sandan', 'Chah Sandan'), ('Chailianwala', 'Chailianwala'), ('Chakdara', 'Chakdara'), ('Chakku', 'Chakku'), ('Chakwal', 'Chakwal'), ('Chaman', 'Chaman'), ('Charsadda', 'Charsadda'), ('Chhatr', 'Chhatr'), ('Chichawatni', 'Chichawatni'), ('Chiniot', 'Chiniot'), ('Chitral', 'Chitral'), ('Chowk Azam', 'Chowk Azam'), ('Chowk Sarwar Shaheed', 'Chowk Sarwar Shaheed'), ('Dadu', 'Dadu'), ('Dalbandin', 'Dalbandin'), ('Dargai', 'Dargai'), ('Darya Khan', 'Darya Khan'), ('Daska', 'Daska'), ('Dera Bugti', 'Dera Bugti'), ('Dera Ghazi Khan', 'Dera Ghazi Khan'), ('Dera Ismail Khan', 'Dera Ismail Khan'), ('Derawar Fort', 'Derawar Fort'), ('Dhana Sar', 'Dhana Sar'), ('Dhaular', 'Dhaular'), ('Digri', 'Digri'), ('Dina City', 'Dina City'), ('Dinga', 'Dinga'), ('Dipalpur', 'Dipalpur'), ('Diplo', 'Diplo'), ('Diwana', 'Diwana'), ('Dokri', 'Dokri'), ('Drasan', 'Drasan'), ('Drosh', 'Drosh'), ('Duki', 'Duki'), ('Dushi', 'Dushi'), ('Duzab', 'Duzab'), ('Faisalabad', 'Faisalabad'), ('Fateh Jang', 'Fateh Jang'), ('Gadar', 'Gadar'), ('Gajar', 'Gajar'), ('Garhi Khairo', 'Garhi Khairo'), ('Garruck', 'Garruck'), ('Ghakhar Mandi', 'Ghakhar Mandi'), ('Ghanian', 'Ghanian'), ('Ghauspur', 'Ghauspur'), ('Ghazluna', 'Ghazluna'), ('Ghotki', 'Ghotki'), ('Gilgit', 'Gilgit'), ('Girdan', 'Girdan'), ('Gujar Khan', 'Gujar Khan'), ('Gujranwala', 'Gujranwala'), ('Gujrat', 'Gujrat'), ('Gulistan', 'Gulistan'), ('Gwadar', 'Gwadar'), ('Gwash', 'Gwash'), ('Hab Chauki', 'Hab Chauki'), ('Hafizabad', 'Hafizabad'), ('Hala', 'Hala'), ('Hameedabad', 'Hameedabad'), ('Hangu', 'Hangu'), ('Haripur', 'Haripur'), ('Harnai', 'Harnai'), ('Haroonabad', 'Haroonabad'), ('Hasilpur', 'Hasilpur'), ('Haveli Lakha', 'Haveli Lakha'), ('Hinglaj', 'Hinglaj'), ('Hoshab', 'Hoshab'), ('Hunza', 'Hunza'), ('Hyderabad', 'Hyderabad'), ('Islamkot', 'Islamkot'), ('Ispikan', 'Ispikan'), ('Jacobabad', 'Jacobabad'), ('Jahania', 'Jahania'), ('Jalla Araain', 'Jalla Araain'), ('Jamesabad', 'Jamesabad'), ('Jampur', 'Jampur'), ('Jamshoro', 'Jamshoro'), ('Janghar', 'Janghar'), ('Jati (Mughalbhin)', 'Jati (Mughalbhin)'), ('Jauharabad', 'Jauharabad'), ('Jhal Jhao', 'Jhal Jhao'), ('Jhang', 'Jhang'), ('Jhatpat', 'Jhatpat'), ('Jhelum', 'Jhelum'), ('Jhudo', 'Jhudo'), ('Jiwani', 'Jiwani'), ('Jungshahi', 'Jungshahi'), ('Kalabagh', 'Kalabagh'), ('Kalam', 'Kalam'), ('Kalandi', 'Kalandi'), ('Kalat', 'Kalat'), ('Kamalia', 'Kamalia'), ('Kamararod', 'Kamararod'), ('Kamokey', 'Kamokey'), ('Kanak', 'Kanak'), ('Kandi', 'Kandi'), ('Kandiaro', 'Kandiaro'), ('Kanpur', 'Kanpur'), ('Kapip', 'Kapip'), ('Kappar', 'Kappar'), ('Karachi', 'Karachi'), ('Karak', 'Karak'), ('Karodi', 'Karodi'), ('Karor Lal Esan', 'Karor Lal Esan'), ('Kashmor', 'Kashmor'), ('Kasur', 'Kasur'), ('Katuri', 'Katuri'), ('Keti Bandar', 'Keti Bandar'), ('Khairpur', 'Khairpur'), ('Khanaspur', 'Khanaspur'), ('Khanewal', 'Khanewal'), ('Khanpur', 'Khanpur'), ('Kharan', 'Kharan'), ('Kharian', 'Kharian'), ('Khokhropur', 'AKhokhropur'), ('Khora', 'Khora'), ('khuiratta', 'khuiratta'), ('Khushab', 'Khushab'), ('Khuzdar', 'Khuzdar'), ('Khyber', 'Khyber'), ('Kikki', 'Kikki'), ('Klupro', 'Klupro'), ('Kohan', 'Kohan'), ('Kohat', 'Kohat'), ('Kohistan', 'Kohistan'), ('Kohlu', 'Kohlu'), ('Korak', 'Korak'), ('Korangi', 'Korangi'), ('Kot Addu', 'Kot Addu'), ('Kot Sarae', 'Kot Sarae'), ('Kotli', 'Kotli'), ('Kotri', 'Kotri'), ('Kurram', 'Kurram'), ('Laar', 'Laar'), ('Lahore', 'Lahore'), ('Lahri', 'Lahri'), ('Lakki Marwat', 'Lakki Marwat'), ('Lalamusa', 'Lalamusa'), ('Larkana', 'Larkana'), ('Lasbela', 'Lasbela'), ('Latamber', 'Latamber'), ('Layyah', 'Layyah'), ('Liari', 'Liari'), ('Lodhran', 'Lodhran'), ('Loralai', 'Loralai'), ('Lower Dir', 'Lower Dir'), ('Lund', 'Lund'), ('Mach', 'Mach'), ('Madyan', 'Madyan'), ('Mailsi', 'Mailsi'), ('Makhdoom Aali', 'Makhdoom Aali'), ('Malakand', 'Malakand'), ('Mamoori', 'Mamoori'), ('Mand', 'Mand'), ('Mandi Bahauddin', 'Mandi Bahauddin'), ('Mandi Warburton', 'Mandi Warburton'), ('Mangla', 'Mangla'), ('Manguchar', 'Manguchar'), ('Mansehra', 'Mansehra'), ('Mardan', 'Mardan'), ('Mashki Chah', 'Mashki Chah'), ('Maslti', 'Maslti'), ('Mastuj', 'Mastuj'), ('Mastung', 'Mastung'), ('Mathi', 'Mathi'), ('Matiari', 'Matiari'), ('Mehar', 'Mehar'), ('Mekhtar', 'Mekhtar'), ('Merui', 'Merui'), ('Mian Channu', 'Mian Channu'), ('Mianez', 'Mianez'), ('Mianwali', 'Mianwali'), ('Minawala', 'Minawala'), ('Miram Shah', 'Miram Shah'), ('Mirpur', 'Mirpur'), ('Mirpur Batoro', 'Mirpur Batoro'), ('Mirpur Khas', 'Mirpur Khas'), ('Mirpur Sakro', 'Mirpur Sakro'), ('Mithani', 'Mithani'), ('Mithi', 'Mithi'), ('Mohmand', 'Mohmand'), ('Mongora', 'Mongora'), ('Moro', 'Moro'), ('Multan', 'Multan'), ('Murgha Kibzai', 'Murgha Kibzai')), max_length=500),
        ),
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='nationality',
            field=models.CharField(choices=[('Nationality', 'Nationality'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default=(('Nationality', 'Nationality'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')), max_length=500, null=True),
        ),
    ]
