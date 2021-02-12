$(function() {
  $('#btn_translate').click(function () {
    let lan = $('#language_code').val();
    console.log(lan);
    let link = 'https://fourtonfish.com/hellosalut/?lang' + lan;
    console.log(link);
    $.ajax({
      url: link,
      success: function ( jqXHR, data) {
        $('#hello').text(data.hello);
        console.log(data.hello);
      }
    })
  });

});