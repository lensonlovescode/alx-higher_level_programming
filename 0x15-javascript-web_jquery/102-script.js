document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').on('click', function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(url, function (data) {
      console.log(data);
      $('#hello').text(data.hello);
    });
  });
});
