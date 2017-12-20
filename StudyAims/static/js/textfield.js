<script type="text/javascript">

function yesnoCheck() {
    if (document.getElementById('f-option').checked) {
        document.getElementById('ifYes').style.display = 'block';
        document.getElementById('ifNo').style.display = 'none';
        document.getElementById('University').style.display = 'none';
    }
    else if (document.getElementById('s-option').checked){
    	  document.getElementById('ifNo').style.display = 'block';
        document.getElementById('ifYes').style.display = 'none';
         document.getElementById('University').style.display = 'none';
    }
     else if (document.getElementById('t-option').checked){
    		 document.getElementById('University').style.display = 'block';
        document.getElementById('ifYes').style.display = 'none';
        document.getElementById('ifNo').style.display = 'none';
     
     }
    else document.getElementById('ifNo').style.display = 'none';

}

</script>