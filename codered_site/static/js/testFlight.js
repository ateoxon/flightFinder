$(document).ready(()=>{
  $('#submit_btn').click(()=>{
    alert('clicked')
    var departure_country = $('#departureCountry').val();
    var arrival_country = $('#arrivalCountry').val();
    if(departure_country == "" || arrival_country==""){
      alert('field cant be empty');
    }else{
      $.get('/static/index2.html',(r)=>{
        $('#page').empty();
        $('#page').append(r);
        $.get('/search/country/'+departure_country+'/'+arrival_country,(e)=>{
          console.log(e);
          $('#from_location').empty();
          $('#to_location').empty();
          $('#cheapest_price').empty();
          $('#cheapest_price').attr('style','color:green');
          $('#cheapest_price').append('$ '+e.best[0].price);
          $('#cheapest_distance').empty();
          $('#cheapest_duration').empty();
          $('#best-5-results').empty();
          var top5 = e.top5;
          var i=0;
          var flightPlanCoordinates = [];
          top5.forEach((obj)=>{
            if(i==0){
              $('#cheapest_distance').append(obj.distance);
              $('#cheapest_duration').append(obj.fly_duration);
              $('#from_location').append(obj.cityFrom+' '+departure_country);
              $('#to_location').append(obj.cityTo+' '+arrival_country);
              var ar = obj.route;
              var j=0;
              ar.forEach((o)=>{
                var lat_from = o.latFrom;
                var lng_from = o.lngFrom;
                var lat_to = o.latTo;
                var lng_to = o.lngTo;
                var m1 = {lat:lat_from,lng:lng_from};
                var m2 = {lat:lat_to,lng:lng_to};
                flightPlanCoordinates[j]=m1;
                j++;
                flightPlanCoordinates[j]=m2;
                j++;
              });
            }
            i++;
            console.log(obj);
            var html = '<tr>';
            console.log(obj.price);
            console.log(obj.distance);
            html += '<td style="color:green;"> $'+obj.price+'</td>';
            html += '<td>'+obj.distance+' miles</td>';
            html += '<td>'+obj.fly_duration+'</td>';
            html += '</tr>';
            $('#best-5-results').append(html);
          });
          var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 6,
            center: {lat: 31, lng: -96},
            mapTypeId: 'terrain',
            disableDefaultUI:true
          });
          var flightPath = new google.maps.Polyline({
            path: flightPlanCoordinates,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 2
          });

          flightPath.setMap(map);

          var bounds = new google.maps.LatLngBounds();
          for(var i=0;i<flightPlanCoordinates.length;i++){
            bounds.extend({lat:flightPlanCoordinates[i].lat,lng:flightPlanCoordinates[i].lng});
          }
          map.fitBounds(bounds);

        });
      });
    }
  });
});
