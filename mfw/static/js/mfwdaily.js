/*
 * MFW Scripts
 *
 * http://www.mfwdaily.com
 *
 * Authored by Rob Morris
 * http://www.madebymrmorris.com
 * @remorrisjr
 *
 * Copyright 2014, MFWDaily
 * License: GNU General Public License, version 3 (GPL-3.0)
 * http://www.opensource.org/licenses/gpl-3.0.html
 *
 */

;(function($) {

	$(document).keypress(function(e) {
		if ($('[id^=about]').is(':visible') && e.keyCode==13){
			//if($("[class^=md-close]").is(":focus")) //if enter pressed and closediv is focus
			$("[class^=md-close]").click();
		}
	});

	$(document).keyup(function(e) {
  		if ($('[id^=about]').is(':visible') && e.keyCode==27) {
  			$("[class^=md-close]").click();
   		}
});

})(jQuery);