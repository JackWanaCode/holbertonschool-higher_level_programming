$(document).ready(function () {
  let url = 'https://fourtonfish.com/hellosalut/?lang=';
  $('#btn_translate').click(function () {
    let language = $('#language_code').val();
    $.get(url + language, function (data) {
      $('#hello > div').remove();
      $('#hello').append('<div>' + data.hello + '</div>');
    });
  });
  $(document).keypress(function (event) {
    let keycode = event.keyCode || event.which;
    if (keycode == '13') {
      let language = $('#language_code').val();
      $.get(url + language, function (data) {
        $('#hello > div').remove();
        $('#hello').append('<div>' + data.hello + '</div>');
      });
    }
  });
});
