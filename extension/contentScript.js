function DOMModificationHandler(){
    $(this).unbind('DOMSubtreeModified.event1');
    setTimeout(function(){
        modify();
        $('#timeline').bind('DOMSubtreeModified.event1',DOMModificationHandler);
    },10);
}

$('#timeline').bind('DOMSubtreeModified.event1',DOMModificationHandler);

function modify(){
  //find and modify tall tweets

  /*
  */
  $('.tweet').each(function(index) {
    var k = $(this).find('.tweet-text');
    var t = k.text();
    if(t) {
      var r = $(this).find('.content');
      if(!r.hasClass("used")) {
        r.addClass('used');
        $.ajax({
          url: "https://nameless-fjord-34984.herokuapp.com/",
          type: "POST",
          dataType: 'json',
          data: JSON.stringify({"name":t}),
          contentType: "application/json",
          success: function (response) {
            //alert(t + ' ' + response['name']);
            if(response['name'] == 'wc2018' && !r.hasClass("sqish")) {
              r.addClass("sqish");
              r.html(`<button class="squish-button EdgeButton EdgeButton--primary" data-original-content="${encodeURI(r.html())}">This tweet is about World Cup 2018</button>`);
              chrome.runtime.sendMessage({message: "listeners"}, function(response) {
              });
            }
          }
        });
      }
    }
  })
  
}