// create hyperlinks to all images in posts

$(document).ready(function() {

  $('.blog-text img').each(function(index) {
    var img = $(this)
    img.wrap( "<a href='" + img.attr("src") + "'></a>" );
  });

});
