$(function() {
    // Add refresh button after field (this can be done in the template as well)
    $('img.captcha').after(
            $('<a href="#void" class="captcha-refresh">Refresh</a>')
            );

    // Click-handler for the refresh-link
    $('.captcha-refresh').click(function(){
        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":"
                  + location.port + "/sms/refresh/" + $("#id_mobile_phone").val();

        // Make the AJAX-call
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="sms_captcha_0"]').val(json.key);
            //$form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
});
(function ($) {

	new WOW().init();

	jQuery(window).load(function() { 
		jQuery("#preloader").delay(100).fadeOut("slow");
		jQuery("#load").delay(100).fadeOut("slow");
		if(window.location.pathname != '/'){
			$(".navbar-fixed-top").addClass("top-nav-collapse");
			$(".navbar-fixed-top").css("position", "relative");
		}
	});


	//jQuery to collapse the navbar on scroll
	$(window).scroll(function() {
		if(window.location.pathname != '/') {
			$(".navbar-fixed-top").addClass("top-nav-collapse");
		}else if ($(".navbar").offset().top > 50) {
			$(".navbar-fixed-top").addClass("top-nav-collapse");
		} else {
			$(".navbar-fixed-top").removeClass("top-nav-collapse");
		}
	});


	//jQuery for page scrolling feature - requires jQuery Easing plugin
	$(function() {
		$('.navbar-nav li a').bind('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 1500, 'easeInOutExpo');
			event.preventDefault();
		});
		$('.page-scroll a').bind('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 1500, 'easeInOutExpo');
			event.preventDefault();
		});
	});

})(jQuery);
