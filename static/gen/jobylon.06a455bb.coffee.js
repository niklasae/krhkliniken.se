(function() {

  console.log('Coffee in the browser!!!');

  $(document).ready(function() {
    return $('.carousel').carousel({
      interval: 3000,
      pause: 'hover'
    });
  });

}).call(this);
