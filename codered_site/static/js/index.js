$(document).ready(()=>{
  $('#submit_btn').click(()=>{
    var from_country = $('#from_country').val();
    var to_country = $('#to_country').val();
    var from_state = $('#from_state').val();
    var to_state = $('#to_state').val();
    var from_city = $('#from_city').val();
    var to_city = $('#to_city').val();
    if((from_country == "" && to_country=="") || (from_country!="" && to_country=="")
    || (from_country=="" && to_country!="")){
      alert("country can't be empty");
    }else{
      if((from_state=="" && to_state=="") || (to_state=="" && from_state!="")
      || (to_state!="" && from_state=="")){
        $.get('/search/country/'+from_country+'/'+to_country,(result)=>{
          console.log('country result');
        });
      }else{
        if((from_city=="" && to_city=="") || (from_city!="" && to_city=="")
        || (from_city=="" && to_city!="")){
          $.get('/search/provincestate/'+from_country+'/'+from_state+'/'+to_country+'/'+to_state,(result)=>{
            console.log('state result');
          });
        }else{
          $.get('/search/provincestate/'+from_country+'/'+from_state+'/'+from_city+'/'+to_country+
          '/'+to_state+'/'+to_city,(result)=>{
            console.log('city result');
          });
        }
      }

    }
  });

});
