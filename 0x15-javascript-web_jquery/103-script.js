$(document).ready(function () {
  $('#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#hello').empty();
  const len = $('#language_code').val();
  $.get(url + len, function (response) {
    $('#hello').append(response.hello);
  });
}
