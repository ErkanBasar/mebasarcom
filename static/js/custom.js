
window.globaldict = {};

(function (window, document, $, globaldict, undefined) {

  $(document).ready(function () {
    var listItems = $('.slides li');
    for (var i = 0; i < listItems.length; i++) {
      var imageUrl = globaldict.static_url_mask.replace(/123/, globaldict.backgroundImagesInfo[i].filePath);
      $(listItems[i]).css('background-image', imageUrl);
    }
  });


})(window, window.document, window.jQuery, window.globaldict);
