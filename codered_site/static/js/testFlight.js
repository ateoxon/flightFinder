(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  }); // end scroll-trigger

  // Scroll to top button appear
  $(document).scroll(function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  }); // end scroll

  $('#submit_btn').click( () => {
    let departure_country = $('#departureCountry').val();
    let departure_city = $('#departureCity').val();

    let arrival_country = $('#arrivalCountry').val();
    let arrival_city = $('#arrivalCity').val();

    if(!departure_country || !departure_city ||
        !arrival_country || !arrival_city) {
      alert("Fields can't be empty.");
      return;
    }

    $.get('./static/index2.html', (r) => {
      $('#page-top').empty();
      $('#page-top').append(r);
    });

  }); // end submit_btn.click()

})(jQuery); // End of use strict
