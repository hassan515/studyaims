# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-06 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyAims', '0021_auto_20180206_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentcompanyregisterationinfo',
            name='count',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='StudyAims.Country_Deal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='agent_country',
            field=models.CharField(choices=[('Country', 'Country'), ('Pakistan', 'Pakistan'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('------------------------------', '------------------------------'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default=(('Country', 'Country'), ('Pakistan', 'Pakistan'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('------------------------------', '------------------------------'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')), max_length=500),
        ),
        migrations.AlterField(
            model_name='agentcompanyinfo',
            name='nationality',
            field=models.CharField(choices=[('Nationality', 'Nationality'), ('Pakistan', 'Pakistan'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('------------------------------', '---------------------------'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default=(('Nationality', 'Nationality'), ('Pakistan', 'Pakistan'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('------------------------------', '---------------------------'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')), max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='agentcompanyregisterationinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stdpersonalinfo',
            name='country_of_residence',
            field=models.CharField(choices=[('Country of Residence', 'Country of Residence'), ('Pakistan', 'Pakistan'), ('Australia', 'Australia'), ('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'UK'), ('Ireland', 'Ireland'), ('New Zealand', 'NewZealand'), ('Germany', 'Germany'), ('Sweden', 'Sweden'), ('---------------------------', '---------------------------'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antigua & Barbuda', 'Antigua & Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia & Herzegovina', 'Bosnia & Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Myanmar/Burma', 'Myanmar/Burma'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African', 'Central African'), ('Chad Republic', 'Chad Republic'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Great Britain', 'Great Britain'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel and the Occupied Territories', 'Israel and the Occupied Territories'), ('Italy', 'Italy'), ('Ivory Coast (Cote dIvoire)', 'Ivory Coast (Cote dIvoire)'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Korea', 'Korea'), ('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Republic of Macedonia', 'Republic of Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'NewZealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pacific Islands', 'Pacific Islands'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Reunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincents & Grenadines', 'Saint Vincents & Grenadines'), ('Samoa', 'Samoa'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos', 'Turks & Caicos'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (US)', 'Virgin Islands (US)'), ('Virgin Islands (UK)', 'Virgin Islands (UK)'), ('Yemen', 'Yemen'), ('Zambia ', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='Country of Residence', max_length=500),
        ),
    ]