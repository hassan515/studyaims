
/* optional dropdown */

var expanded = false;

function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("checkboxes");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });


$(document).ready(function () {
  $('#other').change(function() {
    if ($(this).is(':checked')) {
      $('#other-exp').show();
    } else {
      $('#other-exp').hide();
    }
  });
  });


$('.checkboxes input[type="checkbox"]').on('click', function() {

  var title = $(this).closest('.checkboxes').find('input[type="checkbox"]').val(),
    title = $(this).val() + ",";

  if ($(this).is(':checked')) {
    document.getElementsByName('Select_degree')[0].options[0].innerHTML = "Water";
  /*  var html = $("label[for='"+$(this).attr("id")+"']");
    $('.multiSel').append(html); */
    $(".hida").hide();
  } else {
    $('option[title="' + title + '"]').remove();
    var ret = $(".hida");
      $(".hida").show();
  /*  $('.dropdown dt a').append(ret); */

  }
});

var expanded = false;

function major_subject() {
  var maj_sub = document.getElementById("major_subjects");
  if (!expanded) {
    maj_sub.style.display = "block";
    expanded = true;
  } else {
    maj_sub.style.display = "none";
    expanded = false;
  }
}

$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("major_subjects");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });
var expanded = false;

function test() {
  var maj_sub = document.getElementById("tests");
  if (!expanded) {
    maj_sub.style.display = "block";
    expanded = true;
  } else {
    maj_sub.style.display = "none";
    expanded = false;
  }
}

var expanded = false;

function passing_Year() {
  var checkboxes = document.getElementById("pas_yr");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("pas_yr");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });
var expanded = false;

function percentage() {
  var checkboxes = document.getElementById("percent");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("percent");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });
/* Dropdown for province and cities */



var cities = new Array();
cities['Pakistan'] = new Array('Popular Cities','Islamabad','Lahore','Karachi','Rawalpindi','Peshawar','Quetta','Multan','Gujranwala','Sialkot','Faisalabad','-------------------------','Abbottabad','Adezai','Ahmed Nager Chatha','Ahmedpur East','Ali Bandar','Ali Pur','Arifwala','Astor','Attock','Ayubia',
'Baden','Bagh','Bahawalnagar','Bahawalpur','Bajaur','Banda Daud Shah','Bannu','Baramula','Basti Malook','Batagram','Bazdar','Bela','Bellpat','Bhagalchur','Bhaipheru','Bhakkar','Bhalwal','Bhimber','Birote','Buner',
'Burewala','Burj','Chachro','Chagai','Chah Sandan','Chailianwala','Chakdara','Chakku','Chakwal','Chaman','Charsadda','Chhatr','Chichawatni','Chiniot','Chitral','Chowk Azam','Chowk Sarwar Shaheed','Dadu','Dalbandin','Dargai','Darya Khan','Daska','Dera Bugti','Dera Ghazi Khan','Dera Ismail Khan',
'Derawar Fort','Dhana Sar','Dhaular','Digri','Dina City','Dinga','Dipalpur','Diplo','Diwana','Dokri','Drasan','Drosh','Duki','Dushi','Duzab','Faisalabad','Fateh Jang',
'Gadar','Gadra','Gajar','Gandava','Garhi Khairo','Garruck','Ghakhar Mandi','Ghanian','Ghauspur','Ghazluna','Ghotki','Gilgit','Girdan','Gujar Khan','Gujranwala','Gujrat',
'Gulistan','Gwadar','Gwash','Hab Chauki','Hafizabad','Hala','Hameedabad','Hangu','Haripur','Harnai','Haroonabad','Hasilpur','Haveli Lakha','Hinglaj',
'Hoshab','Hunza','Hyderabad','Islamkot','Ispikan','Jacobabad','Jahania','Jalla Araain','Jamesabad','Jampur','Jamshoro','Janghar','Jati (Mughalbhin)','Jauharabad',
'Jhal Jhao','Jhang','Jhatpat','Jhelum','Jhudo','Jiwani','Jungshahi','Kalabagh','Kalam','Kalandi','Kalat','Kamalia','Kamararod','Kamokey','Kanak','Kandi','Kandiaro',
'Kanpur','Kapip','Kappar','Karachi','Karak','Karodi','Karor Lal Esan','Kashmor','Kasur','Katuri','Keti Bandar','Khairpur','Khanaspur',
'Khanewal','Khanpur','Kharan','Kharian','Khokhropur','Khora','khuiratta','Khushab','Khuzdar','Khyber','Kikki','Klupro','Kohan','Kohat','Kohistan','Kohlu','Korak',
'Korangi','Kot Addu','Kot Sarae','Kotli','Kotri','Kurram','Laar','Lahore','Lahri','Lakki Marwat','Lalamusa','Larkana','Lasbela','Latamber','Layyah','Liari','Lodhran','Loralai',
'Lower Dir','Lund','Mach','Madyan','Mailsi','Makhdoom Aali','Malakand','Mamoori','Mand','Mandi Bahauddin','Mandi Warburton','Mangla','Manguchar','Mansehra',
'Mardan','Mashki Chah','Maslti','Mastuj','Mastung','Mathi','Matiari','Mehar','Mekhtar','Merui','Mian Channu','Mianez','Mianwali','Minawala','Miram Shah','Mirpur',
'Mirpur Batoro','Mirpur Khas','Mirpur Sakro','Mithani','Mithi','Mohmand','Mongora','Moro','Multan','Murgha Kibzai','Muridke','Murree','Musa Khel Bazar','Muzaffarabad',
'Nagar','Nagar Parkar','Nagha Kalat','Nal','Naokot','Narowal','Naseerabad','Naudero','Nauroz Kalat','Naushara','Nawabshah','Nazimabad','North Waziristan','Noushero Feroz',
'Nowshera','Nur Gamma','Nushki','Nuttal','Okara','Ormara','Paharpur','Pak Pattan','Palantuk','Panjgur','Pasni','Pattoki','Pendoo','Peshawar','Piharak','Pirmahal',
'Pishin','Plandri','Pokran','Punch','Qambar','Qamruddin Karez','Qazi Ahmad','Qila Abdullah','Qila Didar Singh','Qila Ladgasht','Qila Safed','Qila Saifullah','Quetta',
'Rabwah','Rahim Yar Khan','Raiwind','Rajan Pur','Rakhni','Ranipur','Ratodero','Rawalakot','Rawalpindi','Renala Khurd','Robat Thana','Rodkhan','Rohri','Sadiqabad',
'Safdar Abad – (Dhaban Singh)','Sahiwal','Saidu Sharif','Saidu Sharif','Saindak','Sakesar','Samberial','Sanghar','Sangla Hill','Sanjawi','Sarai Alamgir',
'Sargodha','Saruna','Shabaz Kalat','Shadadkhot','Shafqat Shaheed Chowk','Shahbandar','Shahdadpur','Shahpur','Shahpur Chakar','Shakargarh','Shandur','Shangla','Shangrila','Sharam Jogizai','Sheikhupura','Shikarpur',
'Shingar','Shorap','Sialkot','Sibi','Skardu', 'Sohawa','Sonmiani','Sooianwala','South Waziristan','Spezand','Spintangi','Sui','Sujawal','Sukkur','Sundar (city)',
'Suntsar','Surab','Swabi','Swat','Takhtbai','Talagang','Tando Adam','Tando Allahyar','Tando Bago','Tangi','Tank',
'Tar Ahamd Rind','Tarbela','Taxila','Thall','Thalo','Thatta','Toba Tek Singh','Tordher','Tujal','Tump','Turbat','Umarao','Umarkot',
'Upper Dir','Uthal','Vehari','Veirwaro','Vitakri','Wadh','Wah Cantonment','Wana','Warah','Washap','Wasjuk','Wazirabad',
'Yakmach','Zhob');
cities['Province'] = new Array('City');
cities['Islamabad'] = new Array('Islamabad');
cities['Punjab'] = new Array('Ahmadpur East','Ahmed Nager Chatha','Alipur','Arifwala','Attock','Bhalwal','Bahawalnagar','Bahawalpur','Bhakkar','Burewala','Chillianwala','Chakwal','Chichawatni','Chiniot','Daska','Darya Khan','Dera Ghazi Khan','Dhaular','Dina','Dinga','Dipalpur','Faisalabad',
'Fateh Jang', 'Ghakhar Mandi','Gujranwala','Gujrat','Gujar Khan','Hafizabad','Haroonabad','Hasilpur','Haveli Lakha','Jampur','Jhang','Jhelum','Kalabagh','Karor Lal Esan','Kasur','Kamalia','Kāmoke','Khanewal','Khanpur','Kharian','Khushab',' Kot Adu','Jauharabad','Lahore','Lalamusa',
'Liaquat Pur','Lodhran','Mamoori','Mandi Bahauddin','Mailsi','Mian Channu','Mianwali','Multan','Murree','Muridke','Muzaffargarh','Narowal','Okara','Renala Khurd','Pakpattan','Pattoki','Pir Mahal','Qila Didar Singh',
'Rabwah','Raiwind','Rajanpur','Rahim Yar Khan','Rawalpindi','Sadiqabad','Safdarabad','Sahiwal','Sangla Hill','Sarai Alamgir','Sargodha','Shakargarh','Sheikhupura','Sialkot','Sohawa','Soianwala','Talagang','Taxila','Toba Tek Singh','Vehari','Wah Cantonment','Wazirabad');
cities['Sindh'] = new Array('Badin','Bhirkan','Bhiria City','Bhiria Road','Rajo Khanani','Chak','Dadu','Digri','Diplo','Dokri','Ghotki','Haala','Hyderabad','Islamkot','Jacobabad','Jamshoro','Jungshahi','Kandhkot','Kandiaro','Karachi','Kashmore','Keti Bandar',
'Khadro','Khairpur','Khipro','Kotri','Larkana','Matiari','Mehar','Mirpur Khas','Mithani','Mithi','Mehrabpur','Moro','Nagarparkar','Naudero','Naushahro Feroze','Naushara','Nawabshah','Qambar','Qasimabad','Ranipur','Ratodero','Rohri','Sakrand','Sanghar',
'Shahbandar','Shahdadkot','Shahdadpur','Shahpur Chakar','Shikarpaur','Sinjhoro','Sukkur','Tangwani','Tando Adam Khan','Tando Allahyar','Tando Muhammad Khan','Thatta','Thari Mirwah','Umerkot','Warah');
cities['KPK'] = new Array('Abbottabad','Adezai','Alpuri','Ayubia','Banda Daud Shah','Bannu','Batkhela','Battagram','Birote','Chakdara','Charsadda','Chitral','Daggar','Dargai','Darya Khan','Dera Ismail Khan','Dir','Drosh','Hangu','Haripur',
'Karak','Kohat','Lakki Marwat','Latamber','Madyan','Mansehra','Mardan','Mastuj','Mingora','Nowshera','Paharpur','Peshawar','Saidu Sharif','Swabi','Swat','Tangi','Tank','Thall','Timergara','Tordher​');
cities['Balochistan'] = new Array('Chaman','Dera Allah Yar','Dera Murad Jamali','Gwadar','Hub','Kharan','Khuzdar','Kalat','Loralai','Mastung','Nushki','Pasni','Quetta','	Sibi','Turbat','Zhob');
cities['Gilgit'] = new Array('Askole','Astore','Bunji','Chilas','Chillinji','Chiran','Gakuch','Ghangche','Ghizer','Gilgit','Dayore – Gilgit','Sultanabad – Gilgit','Oshikhanda Gilgit','Jalalabad Gilgit','Jutial Gilgit','Alyabad Hunza','Gorikot','Gulmit','Jaglot','Chalt (Nagar)','Thole (Nagar)','Nasir Abad',
'Mayoon','Khana Abad','Hussain Abad','Qasimabad Masoot (Nagar)','Nagar Proper','Ghulmat (Nagar)','Karimabad (Hunza)','Ishkoman','Khaplu','Minimerg','Misgar','Passu','Shimshal','Skardu','Sust','Taghafari','Thorar');
cities['AJK'] = new Array('Abbaspur','Ath Muqam','Bagh','Barnala','Bhimber','Baloch','Charoi','Chikar','Dheerkot','Dudyal','Dulia jattian','Fateh Pur Thakiala (Nakial)','Hari Gehal','Hattian Bala','Hajeera','Khurshid Abad','Kotli','Khui Rtta','Lipa','Mirpur','Muzaffarabad','Mumtazabad',
'Mang','Patehka (Nasirabad)','Pallandari','Rawalakot','Sharda','Samahni','Sehnsa','Tarar Khal','Thorar');

function setCities() {

  stateSel = document.getElementById('state');
  cityList = cities[stateSel.value];
  changeSelect('city', cityList, cityList);
}

function changeSelect(fieldID, newOptions, newValues) {
  selectField = document.getElementById(fieldID);
  selectField.options.length = 0;
  for (i=0; i<newOptions.length; i++) {
    selectField.options[selectField.length] = new Option(newOptions[i], newValues[i]);
  }
}


function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (oldonload) {
        oldonload();
      }
      func();
    }
  }
}

addLoadEvent(function() {
  setCities();
});


/* Ticker */
$(function (){
  createMarquee();
});

// City lists


// Language Skill

function CheckEnglish(val){
 var element=document.getElementById('english-skills');
 if(val=='Ielts'||val=='toefl'||val=='pte')
   element.style.display='block';
 else
   element.style.display='none';
}

function CheckOther(val){
 var element=document.getElementById('other-lang-skills');
 if(val=='german'||val=='french'||val=='italian'||val=='turkish'||val=='portoguese'||val=='chinese'||val=='japan'||val=='Korian')
   element.style.display='block';
 else
   element.style.display='none';
}

/*--------------------END-------------------- */


var expanded = false;

function english() {
  var check = document.getElementById("eng");

  if (!expanded) {
    check.style.display = "block";
    expanded = true;
  } else {
    check.style.display = "none";
    expanded = false;
  }
}
$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("eng");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });

var expanded = false;

function other() {
  var checkboxes = document.getElementById("oth");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("oth");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });

var expanded = false;

function studyGap() {
  var checkboxes = document.getElementById("st_gap");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("st_gap");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });




var expanded = false;

function serv_types() {
  var checkboxes = document.getElementById("serv_type");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
$(document).mouseup(function (e) {
           var container = new Array();
           container.push($('#msel'));
           $.each(container, function (key, value) {
               if (!$(value).is(e.target) && $(value).has(e.target).length === 0) {
                   ///--need to have better code from yourside..
                   var checkboxes = document.getElementById("serv_type");
                   checkboxes.style.display = "none";
                   ///--need to have better code from yourside..
               }
           });
       });


var expanded = false;

function lang_class_serv() {
  var checkboxes = document.getElementById("lang-serv");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

var expanded = false;

function prg_spc() {
  var checkboxes = document.getElementById("prg");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}


















$(document).ready(function () {
  $('#qual-check').change(function() {
    if ($(this).is(':checked')) {
      $('#degree').show();
    } else {
      $('#degree').hide();
    }
  });
  });

  $(document).ready(function () {
    $('#sub-check').change(function() {
      if ($(this).is(':checked')) {
        $('#subjects').show();
      } else {
        $('#subjects').hide();
      }
    });
    });

    $(document).ready(function () {
      $('#year-check').change(function() {
        if ($(this).is(':checked')) {
          $('#years').show();
        } else {
          $('#years').hide();
        }
      });
      });

      $(document).ready(function () {
        $('#percent-check').change(function() {
          if ($(this).is(':checked')) {
            $('#percent').show();
          } else {
            $('#percent').hide();
          }
        });
        });

        $(document).ready(function () {
          $('#eng_lang-check').change(function() {
            if ($(this).is(':checked')) {
              $('#eng_lang').show();
            } else {
              $('#eng_lang').hide();
            }
          });
          });

          $(document).ready(function () {
            $('#other_lan-check').change(function() {
              if ($(this).is(':checked')) {
                $('#other_lang').show();
              } else {
                $('#other_lang').hide();
              }
            });
            });

            $(document).ready(function () {
              $('#st-gap-check').change(function() {
                if ($(this).is(':checked')) {
                  $('#st-gap').show();
                } else {
                  $('#st-gap').hide();
                }
              });
              });

              $(document).ready(function () {
                $('#st-gap-check').change(function() {
                  if ($(this).is(':checked')) {
                    $('#st-gap').show();
                  } else {
                    $('#st-gap').hide();
                  }
                });
                });

/* New Multi selects */
$(function () {
var degree = [
    { Name: "Matriculation (SSE)" },
    { Name: "O-Level" },
    { Name: "Intermediate (HSSE)" },
      { Name: "Associate Degree" },
      { Name: "A-Level" },
  { Name: "Bachelor(2-Years)" },
  { Name: "Bachelor(3-Years)" },
  { Name: "Bachelor(4-Years)" },
  { Name: "Bachelor(5-Years)" },
{ Name: "Bachelor(6-Years)" },
{ Name: "Master(6-Months)"  },
{ Name: "Master(1-Year)"    },
  { Name: "Master(1.5 Year)"  },
  { Name: "Master(2-Year)"    },
{ Name: "Master(2.5Year)"   },
{ Name: "MPhil / Master(Res)"},
{ Name: "Phd / Doctor(Res)"},
{ Name: "Other(Res)"},
        ];

        $(function () {




            $("#degreeSelectCombo").igCombo({

                dataSource: degree,
                placeholder: "Degree",
                textKey: "Name",
                valueKey: "Name",
                multiSelection: {
                    enabled: true,

                },
                dropDownOrientation: "bottom"
            });

        });
});

$(function () {
var degree = [
  { Name: "Applied Arts" },
  { Name: "Applied Mathematics" },
  { Name: "Applied Sciences & Professions" },
  { Name: "Aquaculture & Fisheries)" },
  { Name: "Arabic" },
  { Name: "Archaeology" },
  { Name: "Architecture" },
  { Name: "Area & Cultural Studies" },
  { Name: "Art History" },
{ Name: "Arts" },
{ Name: "Arts &, Design"  },
{ Name: "Astronomy"    },
  { Name: "Audio)"  },
  { Name: "Auditing"    },
{ Name: "Automotive"   },
{ Name: "Automotive Engineering"},
{ Name: "Aviation"},
{ Name: "Banking"},
{ Name: "Basic Medical Sciences"},
{ Name: "Beauty"},
{ Name: "Bio & Biomedical Engineering"},
{ Name: "Biodiversity & Conservation"},
{ Name: "Biology"},
{ Name: "Biomedicine"},
{ Name: "Biotechnology"},
{ Name: "Business & Management"},
{ Name: "Business Administration"},
{ Name: "Business Information Systems"},
{ Name: "Business Intelligence & Analytics"},
{ Name: "Business Law"},
{ Name: "Business Math"},
{ Name: "Chemical Engineering"},
{ Name: "Chemistry"},
{ Name: "Child Development And Family Life"},
{ Name: "Christian Studies"},
{ Name: "Civics"},
{ Name: "Civics For Non Muslim"},
{ Name: "Civil & Private Law"},
{ Name: "Civil Engineering & Construction"},
{ Name: "Climate Studies & Meteorology"},
{ Name: "Clinical Pathology & Serology"},
{ Name: "Clothing & Textile"},
{ Name: "Coaching"},
{ Name: "Cognitive Sciences"},
{ Name: "Commerce"},
{ Name: "Commercial Geography"},
{ Name: "Commercial Practice"},
{ Name: "Communication Sciences"},
{ Name: "Communications"},
{ Name: "Complementary & Alternative Medicine"},
{ Name: "Computer Science"},
{ Name: "Computer Science & IT"},
{ Name: "Computing"},
{ Name: "Cookery"},
{ Name: "Corporate Communication"},
{ Name: "Corporate Social Responsibility"},
{ Name: "Cosmetics"},
{ Name: "Counselling"},
{ Name: "Creative Writing"},
{ Name: "Criminal Law"},
{ Name: "Criminology"},
{ Name: "Culinary Arts"},
{ Name: "Data Science & Big Data"},
{ Name: "Dental Hygiene"},
{ Name: "Dentistry"},
{ Name: "Design"},
{ Name: "Digital"},
{ Name: "Earth"},
{ Name: "Earth Sciences"},
{ Name: "Ecology"},
{ Name: "Econometrics"},
{ Name: "Economics of War"},
{ Name: "Economics"},
{ Name: "Education"},
{ Name: "Education & Training"},
{ Name: "Educational Psychology"},
{ Name: "Educational Research"},
{ Name: "Electrical Engineering"},
{ Name: "Electronics"},
{ Name: "Electronics & Embedded Technology"},
{ Name: "Elementary Anatomy & Microtech"},
{ Name: "Elementary Chemistry & Chemical"},
{ Name: "Emergency & Disaster Management"},
{ Name: "Energy & Power Engineering"},
{ Name: "Engineering"},
{ Name: "English"},
{ Name: "English Elective"},
{ Name: "Entrepreneurship"},
{ Name: "Environmental Sciences"},
{ Name: "Environmental Economics & Policy"},
{ Name: "Environmental Engineering"},
{ Name: "Environmental Management"},
{ Name: "Ethnic Studies"},
{ Name: "European Law"},
{ Name: "European Studies"},
{ Name: "Event Management"},
{ Name: "Executive MBA"},
{ Name: "Family & Consumer Science"},
{ Name: "Fashion"},
{ Name: "Fashion, Textiles And Luxury Goods"},
{ Name: "Film, Photography & Media"},
{ Name: "Finance"},
{ Name: "Financial Mathematics"},
{ Name: "Fine Art"},
{ Name: "Food & Nutrition"},
{ Name: "Food Sciences"},
{ Name: "Forensic Accounting"},
{ Name: "Forensic Science"},
{ Name: "Forestry"},
{ Name: "French"},
{ Name: "General Engineering & Technology"},
{ Name: "General Studies & Classics"},
{ Name: "Geographical Information Systems"},
{ Name: "Geography"},
{ Name: "Geology"},
{ Name: "German"},
{ Name: "Graphic Design"},
{ Name: "Hairdressing"},
{ Name: "Health & Physical Education"},
{ Name: "Health Informatics"},
{ Name: "Health Management"},
{ Name: "Health Sciences"},
{ Name: "Hematology & Blood Banking"},
{ Name: "History"},
{ Name: "History Of Modern World"},
{ Name: "Home Management"},
{ Name: "Horticulture"},
{ Name: "Hospitality Management"},
{ Name: "Hospitality, Leisure & Sports"},
{ Name: "Hotel Management"},
{ Name: "Human Medicine"},
{ Name: "Human Resource Management"},
{ Name: "Humanities"},
{ Name: "Hydrology & Water Management"},
{ Name: "Industrial & Systems Engineering"},
{ Name: "Industrial Design"},
{ Name: "Informatics & Information Sciences"},
{ Name: "Information Technology"},
{ Name: "Innovation Management"},
{ Name: "Interior"},
{ Name: "Interior Design"},
{ Name: "International Business"},
{ Name: "International Development"},
{ Name: "International Law"},
{ Name: "International Relations"},
{ Name: "Interpreting"},
{ Name: "Islamic Education"},
{ Name: "Islamic History & Culture"},
{ Name: "Islamic Studies"},
{ Name: "IT Security"},
{ Name: "Journalism & Media"},
{ Name: "Landscape Architecture"},
{ Name: "Language Studies"},
{ Name: "Law"},
{ Name: "Legal Studies"},
{ Name: "Liberal Arts"},
{ Name: "Library Science"},
{ Name: "Literature"},
{ Name: "Management, Organisation & Leadership"},
{ Name: "Manufacturing"},
{ Name: "Marine Engineering"},
{ Name: "Maritime"},
{ Name: "Marketing"},
{ Name: "Materials Science & Engineering"},
{ Name: "Mathematics"},
{ Name: "Mechanical Engineering"},
{ Name: "Mechatronics"},
{ Name: "Media Studies & Mass Media"},
{ Name: "Medical"},
{ Name: "Medicine & Health"},
{ Name: "Microbiology"},
{ Name: "Midwifery"},
{ Name: "Military Geography"},
{ Name: "Military Science"},
{ Name: "Mining"},
{ Name: "Modern History"},
{ Name: "Molecular Sciences"},
{ Name: "Museum Studies"},
{ Name: "Music"},
{ Name: "Music History"},
{ Name: "Molecular Sciences"},
{ Name: "Museum Studies"},
{ Name: "Music"},
{ Name: "Music History"},
{ Name: "Natural Resource Management"},
{ Name: "Natural Sciences & Mathematics"},
{ Name: "Natural Sciences"},
{ Name: "Neuroscience"},
{ Name: "Nursing"},
{ Name: "Nutrition"},
{ Name: "Nutrition & Dietetics"},
{ Name: "Oil & Gas"},
{ Name: "Organisational Behaviour"},
{ Name: "Pakistan Studies"},
{ Name: "Pakistani Culture"},
{ Name: "Patent & Intellectual Property Law"},
{ Name: "Pedagogy"},
{ Name: "Performing"},
{ Name: "Persian"},
{ Name: "Pharmaceutical"},
{ Name: "Pharmacy"},
{ Name: "Philosophy"},
{ Name: "Philosophy & Ethics"},
{ Name: "Photography"},
{ Name: "Psychology"},
{ Name: "Physics"},
{ Name: "Physiotherapy"},
{ Name: "Plant & Crop Sciences"},
{ Name: "Political Science"},
{ Name: "Project Management"},
{ Name: "Public Administration"},
{ Name: "Public Health"},
{ Name: "Public Law"},
{ Name: "Public Policy"},
{ Name: "Public Relations"},
{ Name: "Real Estate & Property Management"},
{ Name: "Recreation"},
{ Name: "Religious Studies & Theology"},
{ Name: "Retail Management"},
{ Name: "Risk Management"},
{ Name: "Robotics"},
{ Name: "Social Sciences"},
{ Name: "Social Welfare"},
{ Name: "Sociology"},
{ Name: "Soil Science"},
{ Name: "Space"},
{ Name: "Special Education"},
{ Name: "Special Military Studies"},
{ Name: "Sport & Recreation Statistics"},
{ Name: "Supply Chain Management & Logistics"},
{ Name: "Sustainable Development"},
{ Name: "Sustainable Energy"},
{ Name: "Taxation"},
{ Name: "Teaching"},
{ Name: "Technology Management"},
{ Name: "Television"},
{ Name: "Terrorism & Security"},
{ Name: "Textiles"},
{ Name: "Theatre & Dance"},
{ Name: "Theology"},
{ Name: "Tourism"},
{ Name: "Tourism & Leisure"},
{ Name: "English"},
{ Name: "Toxicology"},
{ Name: "Training"},
{ Name: "Translation"},
{ Name: "Translation & Interpreting"},
{ Name: "Transport Management"},
{ Name: "Transportation Engineering"},
{ Name: "Typing"},
{ Name: "Veterinary"},
{ Name: "Veterinary Medicine"},
{ Name: "Video Games & Multimedia"},
{ Name: "Visual Arts"},
{ Name: "War"},
{ Name: "Web Technologies & Cloud Computing"},
{ Name: "Zoology"},
{ Name: "English"},
{ Name: "English"},
{ Name: "English"},
        ];

        $(function () {




            $("#checkboxSelectCombo").igCombo({

                dataSource: degree,
                placeholder: "Degree",
                textKey: "Name",
                valueKey: "Name",
                multiSelection: {
                    enabled: true,

                },
                dropDownOrientation: "bottom"
            });

        });
});

/* Registration*/
function reg_details() {
    if (document.getElementById('reg-option').checked) {
        document.getElementById('reg_pak').style.display = 'block';
    }
    else document.getElementById('reg_pak').style.display = 'none';
}
function consult_details() {
    if (document.getElementById('ach_Y-option').checked) {
        document.getElementById('consultant').style.display = 'block';
    }
    else document.getElementById('consultant').style.display = 'none';
}
/* End */
var expanded = false;

function consultancy() {
  var checkboxes = document.getElementById("consult");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
/* End */
$(".dropdown dt a").on('click', function() {
  $(".dropdown dd ul").slideToggle('fast');
});

$(".dropdown dd ul li a").on('click', function() {
  $(".dropdown dd ul").hide();
});

function getSelectedValue(id) {
  return $("#" + id).find("dt a span.value").html();
}

$(document).bind('click', function(e) {
  var $clicked = $(e.target);
  if (!$clicked.parents().hasClass("dropdown")) $(".dropdown dd ul").hide();
});





(function ($) {
    "use strict";
    var $wn =  $(window);
    $wn.load(function () {

            /***************
             *  Preloader  *
             ***************/
            var $element = $("#loading");
            $element.fadeOut(1000);

            /****************************
             * Responsive Equal Height  *
             ****************************/
            var $element = $('.equal-hight');
            if ($element.length > 0) {
                var $viewportWidth = $wn.width();
                if ($viewportWidth > 767) {
                    $element.matchHeight();
                }
                $wn.on('resize', function () {
                        if ($viewportWidth > 767) {
                            $element.matchHeight();
                        }
                    });
            }

            /******************************
             *  Language Select dropdown  *
             ******************************/
             $(document).ready(function () {
               $('#ielts-lang').change(function() {
                 if ($(this).is(':checked')) {
                   $('#ielts_score').show();
                 } else {
                   $('#ielts_score').hide();
                 }
               });
               });
               $(document).ready(function () {
                 $('#pte-lang').change(function() {
                   if ($(this).is(':checked')) {
                     $('#pte_score').show();
                   } else {
                     $('#pte_score').hide();
                   }
                 });
                 });

                 $(document).ready(function () {
                   $('#toefl-lang').change(function() {
                     if ($(this).is(':checked')) {
                       $('#toefl_score').show();
                     } else {
                       $('#toefl_score').hide();
                     }
                   });
                   });
                   $(document).ready(function () {
                     $('#other-lang').change(function() {
                       if ($(this).is(':checked')) {
                         $('#other_name').show();
                         $('#other_score').show();
                       } else {
                         $('#other_score').hide();
                         $('#other_name').hide();
                       }
                     });
                     });

                     $(document).ready(function () {
                       $('#german').change(function() {
                         if ($(this).is(':checked')) {
                           $('#german_score').show();

                         } else {
                           $('#german_score').hide();

                         }
                       });
                       });
                       $(document).ready(function () {
                         $('#chinese').change(function() {
                           if ($(this).is(':checked')) {
                             $('#china_level').show();

                           } else {
                             $('#china_level').hide();

                           }
                         });
                         });
                       $(document).ready(function () {
                         $('#russian').change(function() {
                           if ($(this).is(':checked')) {

                             $('#russian_score').show();
                           } else {
                             $('#russian_score').hide();

                           }
                         });
                         });

                         $(document).ready(function () {
                           $('#others').change(function() {
                             if ($(this).is(':checked')) {

                               $('#others_name').show();
                               $('#others_score').show();
                             } else {
                               $('#others_name').hide();
                               $('#others_score').hide();

                             }
                           });
                           });

                           $(document).ready(function () {
                             $('#other_gap').change(function() {
                               if ($(this).is(':checked')) {

                                 $('#oth-gap').show();

                               } else {
                                 $('#oth-gap').hide();

                               }
                             });
                             });

                             $(document).ready(function () {
                               $('#other-degree').change(function() {
                                 if ($(this).is(':checked')) {

                                   $('#oth-degree').show();

                                 } else {
                                   $('#oth-degree').hide();

                                 }
                               });
                               });

                               $(document).ready(function () {
                                 $('#other-desired').change(function() {
                                   if ($(this).is(':checked')) {

                                     $('#oth-des').show();

                                   } else {
                                     $('#oth-des').hide();

                                   }
                                 });
                                 });

                                 $(document).ready(function () {
                                   $('#other-budget').change(function() {
                                     if ($(this).is(':checked')) {

                                       $('#oth-bud').show();

                                     } else {
                                       $('#oth-bud').hide();

                                     }
                                   });
                                   });















/***************
Signup Text fields
*****************/




            function formatState(state) {
                var $state = $('<span><img src="images/' + $.trim(state.text.toLowerCase()) + '.png" class="img-flag" /> ' + state.text + '</span>');
                return $state;
            };

            /****************************
             *  Custom Select dropdown  *
             ****************************/












            var $element = $('#currency_select');
            $element.select2({
                templateResult: formatState,
                templateSelection: formatState,
                minimumResultsForSearch: Infinity
            });
            var $elements = $(".custom_select");
            $elements.select2({

                minimumResultsForSearch: Infinity
            });

            $('.mySelect option').hover(function() {
  	           $(this).toggleClass('hover');
             });



            var current_fs, next_fs, previous_fs; //fieldsets
  var left, opacity, scale; //fieldset properties which we will animate
  var animating; //flag to prevent quick multi-click glitches

  $(".next").click(function(){
  	if(animating) return false;
  	animating = true;

  	current_fs = $(this).parent();
  	next_fs = $(this).parent().next();

  	//activate next step on progressbar using the index of next_fs
  	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

  	//show the next fieldset
  	next_fs.show();
  	//hide the current fieldset with style
  	current_fs.animate({opacity: 0}, {
  		step: function(now, mx) {
  			//as the opacity of current_fs reduces to 0 - stored in "now"
  			//1. scale current_fs down to 80%
  			scale = 1 - (1 - now) * 0.2;
  			//2. bring next_fs from the right(50%)
  			left = (now * 50)+"%";
  			//3. increase opacity of next_fs to 1 as it moves in
  			opacity = 1 - now;
  			current_fs.css({
          'transform': 'scale('+scale+')',
          'position': 'absolute'
        });
  			next_fs.css({'left': left, 'opacity': opacity});
  		},
  		duration: 800,
  		complete: function(){
  			current_fs.hide();
  			animating = false;
  		},
  		//this comes from the custom easing plugin
  		easing: 'easeInOutBack'
  	});
  });

  $(".previous").click(function(){
  	if(animating) return false;
  	animating = true;

  	current_fs = $(this).parent();
  	previous_fs = $(this).parent().prev();

  	//de-activate current step on progressbar
  	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

  	//show the previous fieldset
  	previous_fs.show();
  	//hide the current fieldset with style
  	current_fs.animate({opacity: 0}, {
  		step: function(now, mx) {
  			//as the opacity of current_fs reduces to 0 - stored in "now"
  			//1. scale previous_fs from 80% to 100%
  			scale = 0.8 + (1 - now) * 0.2;
  			//2. take current_fs to the right(50%) - from 0%
  			left = ((1-now) * 50)+"%";
  			//3. increase opacity of previous_fs to 1 as it moves in
  			opacity = 1 - now;
  			current_fs.css({'left': left});
  			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
  		},
  		duration: 800,
  		complete: function(){
  			current_fs.hide();
  			animating = false;
  		},
  		//this comes from the custom easing plugin
  		easing: 'easeInOutBack'
  	});
  });

  $(".submit").click(function(){
  	return false;
  })


            /*************************************
             * Bootstrap Dropdown Menu on hover  *
             *************************************/
            function dropdown() {
                var $viewportWidth = $wn.width();
                var $element = $('ul.nav li.dropdown');
                if ($viewportWidth > 767) {
                    $element.hover(function () {
                        $(this)
                            .find('.dropdown-menu')
                            .stop(true, true)
                            .delay(200)
                            .slideDown(300);
                    }, function () {
                        $(this)
                            .find('.dropdown-menu')
                            .stop(true, true)
                            .delay(200)
                            .slideUp(300);
                    });
                }
            }
            $wn.on('resize', dropdown);
            dropdown();

            /*********************
             *  Banner Carousel  *
             *********************/
            var $element = $('.banner-slider');
            if ($element.length > 0) {
                $element.bxSlider({
                    controls: false,
                    auto: true,
                    mode: 'fade'
                });
            }

            /***********************
             *   Cources Carousel  *
             ***********************/
            var $element = $('.our-cources .owl-carousel');
            if ($element.length > 0) {
                $element.owlCarousel({
                    loop: true,
                    margin: 30,
                    navText: ['', ''],
                    nav: true,
                    autoplay: true,
                    smartSpeed: 1000,
                    autoplayHoverPause: true,
                    responsive: {
                        0: {
                            items: 1
                        },

                        480: {
                            items: 2,
                            margin: 20
                        },

                        768: {
                            items: 3,
                            margin: 20
                        },

                        1024: {
                            items: 4,
                            margin: 0
                        },
                    }
                });
            }

            /****************
             *   Couter up  *
             ****************/
            var $element = $('.counter');
            if ($element.length > 0) {
                $element.counterUp({
                    delay: 10,
                    time: 1000
                });
            }

            /*********************
             *   magnific-popup  *
             *********************/
            var $groups = {};
            var $gallery = $('.galleryItem');
            $gallery.each(function () {
                var id = parseInt($(this)
                    .attr('data-group'), 10);
                if (!$groups[id]) {
                    $groups[id] = [];
                }
                $groups[id].push(this);
            });
            $.each($groups, function () {
                $(this)
                    .magnificPopup({
                        type: 'image',
                        closeOnContentClick: true,
                        gallery: {
                            enabled: true
                        }
                    })
            });

            /***************************
             *   Testimonial Carousel  *
             ***************************/
            var $element = $('.testimonial-slide');
            if ($element.length > 0) {
                $element.bxSlider({
                    controls: false,
                    auto: true,
                    pagerCustom: '#bx-pager'
                });
            }

            /**********************
             *   Brands Carousel  *
             **********************/
            var $element = $('.logos .owl-carousel');
            if ($element.length > 0) {
                $element.owlCarousel({
                    loop: true,
                    margin: 30,
                    navText: ['', ''],
                    nav: true,
                    autoplay: true,
                    smartSpeed: 1000,
                    autoplayHoverPause: true,
                    responsive: {
                        0: {
                            items: 2
                        },

                        480: {
                            items: 3,
                            margin: 20
                        },

                        768: {
                            items: 4,
                            margin: 20
                        },

                        1024: {
                            items: 5,
                            margin: 30
                        },

                        1200: {
                            items: 6,
                            margin: 30
                        },
                    }
                });
            }

            /***************************************
             * footer menu accordian (@media 767)  *
             ***************************************/

            function footerAcc() {
                var $allFooterAcco = $(".foot-nav > ul");
                var $allFooterAccoItems = $(".foot-nav h3");
                if ($wn.width() < 768) {
                    $allFooterAcco.css('display', 'none');
                    $allFooterAccoItems.on("click", function () {
                        if ($(this)
                            .hasClass('open')) {
                            $(this)
                                .removeClass('open');
                            $(this)
                                .next()
                                .stop(true, false)
                                .slideUp(300);
                        } else {
                            $allFooterAcco.slideUp(300);
                            $allFooterAccoItems.removeClass('open');
                            $(this)
                                .addClass('open');
                            $(this)
                                .next()
                                .stop(true, false)
                                .slideDown(300);
                            return false;
                        }
                    });
                } else {
                    $allFooterAcco.css('display', 'block');
                    $allFooterAccoItems.off();
                }
            }
            $wn.on('resize', function () {
                    footerAcc();
                });
            footerAcc();

            /**********************
             *   Gallery Isotope  *
             **********************/
            var $isotopeContainer = $('.isotopeContainer');
            if ($isotopeContainer.length > 0) {
                $isotopeContainer.isotope({
                    itemSelector: '.isotopeSelector'

                });
                $('.isotopeFilters')
                    .on('click', 'a', function (e) {
                        $('.isotopeFilters')
                            .find('.active')
                            .removeClass('active');
                        $(this)
                            .parent()
                            .addClass('active');
                        var $filterValue = $(this)
                            .attr('data-filter');
                        $isotopeContainer.isotope({
                            filter: $filterValue
                        });
                        e.preventDefault();
                        return false;
                    });
            }

            /**************************
             *   Testimonial Masonry  *
             **************************/
            var $element = $('.testimonials');
            if ($element.length > 0) {
                $element.masonry({
                    itemSelector: '.grid-item',
                    percentPosition: true
                });
            }

            /****************************
             *   News & Events Masonry  *
             ****************************/
            var $element = $('.news-listing');
            if ($element.length > 0) {
                $element.masonry({
                    itemSelector: '.grid-item',
                    percentPosition: true
                });
            }

            /*****************
             *   Datepicker  *
             *****************/
            var $element = $('.datepicker');
            if ($element.length > 0) {
                $element.datepicker()
            }

            /****************************
             *   Validate Contact Form  *
             ****************************/
            var $form = $("#ContactForm");
            if ($form.length > 0) {
                $form.validate({
                    rules: {
                        first_name: {
                            required: true,
                            minlength: 3
                        },
                        last_name: {
                            required: true
                        },
                        company: {
                            required: true
                        },
                        business_email: {
                            required: true,
                            email: true
                        },
                        phone_number: {
                            required: true,
                            number: true,
                            minlength: 10
                        },
                        job_title: {
                            required: true
                        }
                    },
                    messages: {
                        first_name: {
                            required: "Please Enter Name",
                            minlength: "Name must consist of at least 3 characters"
                        },
                        business_email: {
                            required: "Please provide an Email",
                            email: "Please enter a valid Email"
                        },
                        phone_number: {
                            required: "Please provide Phone Number",
                            number: "Please enter only digits",
                            minlength: "Phone Number must be atleast 10 Numbers"
                        },
                        job_title: {
                            required: "Please Enter Job Tittle"
                        },
                        last_name: {
                            required: "Please Enter Last Name"
                        }
                    },

                    submitHandler: function ($form) {
                        //Send Booking Mail AJAX
                        var formdata = jQuery("#ContactForm")
                            .serialize();
                        jQuery.ajax({
                            type: "POST",
                            url: "contact_form/ajax-contact.php",
                            data: formdata,
                            dataType: 'json',
                            async: false,
                            success: function (data) {
                                if (data.success) {
                                    jQuery('.msg')
                                        .removeClass('msg-error');
                                    jQuery('.msg')
                                        .addClass('msg-success');
                                    jQuery('.msg')
                                        .text('Thank You, Your Message Has been Sent');
                                } else {
                                    jQuery('.msg')
                                        .removeClass('msg-success');
                                    jQuery('.msg')
                                        .addClass('msg-error');
                                    jQuery('.msg')
                                        .text('Error on Sending Message, Please Try Again');
                                }

                            },
                            error: function (error) {
                                jQuery('.msg')
                                    .removeClass('msg-success');
                                jQuery('.msg')
                                    .addClass('msg-error');
                                jQuery('.msg')
                                    .text('Something Went Wrong');
                            }

                        });
                    }
                });
            }
        });

    /************************
     *   Custom Google map  *
     ************************/
    var mapId = $('#map');
    if (mapId.length > 0) {
        // When the window has finished loading create our google map below
        google.maps.event.addDomListener(window, 'load', init);

        function init() {

            // Basic options for a simple Google Map
            // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
            var mapOptions = {
                // How zoomed in you want the map to start at (always required)
                zoom: 11,
                scrollwheel: false,

                // The latitude and longitude to center the map (always required)
                center: new google.maps.LatLng(40.6700, -73.9400), // New York

                // How you would like to style the map.
                // This is where you would paste any style found on Snazzy Maps.
                styles: [{
                    "featureType": "road",
                    "elementType": "labels",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }, {
                    "featureType": "poi",
                    "elementType": "labels",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }, {
                    "featureType": "transit",
                    "elementType": "labels.text",
                    "stylers": [{
                        "visibility": "off"
                    }]
                }]
            };

            // Get the HTML DOM element that will contain your map
            // We are using a div with id="map" seen below in the <body>
            var mapElement = document.getElementById('map');

            // Create the Google Map using our element and options defined above
            var map = new google.maps.Map(mapElement, mapOptions);

            // Let's also add a marker while we're at it
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(40.6700, -73.9400),
                map: map,
                icon: "images/map-ico.png",
                title: 'Snazzy!'
            });
        }
    }

    /***************************
     *   Scroll to top action  *
     ***************************/
    var $element = $('.scroll-top');

    $wn.on("scroll", function () {
            if ($(this)
                .scrollTop() > 100) {
                $element.fadeIn();
            } else {
                $element.fadeOut();
            }
        });

    $element.on("click", function () {
        var $scrollElement = $("html, body");
        $scrollElement.animate({
            scrollTop: 0
        }, 600);
        return false;
    });

})(jQuery);
