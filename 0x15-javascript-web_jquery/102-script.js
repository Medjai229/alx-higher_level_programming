$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').click(function () {
    $('#hello').empty();
    const len = $('#language_code').val();
    $.get(url + len, function (response) {
      $('#hello').append(response.hello);
    });
  });
});
