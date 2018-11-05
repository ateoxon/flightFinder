// This example creates a 2-pixel-wide red polyline showing the path of
// the first trans-Pacific flight between Oakland, CA, and Brisbane,
// Australia which was made by Charles Kingsford Smith.
//$(document).ready({
  function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 6,
      center: {lat: 31, lng: -96},
      mapTypeId: 'terrain'
    });

    var flightPlanCoordinates = [
      {lat: 29.989648, lng: -95.336810},
      {lat: 32.900257, lng: -97.040346}//,
      //{lat: -18.142, lng: 178.431},
      //{lat: -27.467, lng: 153.027}
    ];
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });

    flightPath.setMap(map);
  }
//});
