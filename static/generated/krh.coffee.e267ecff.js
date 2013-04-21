(function() {

  console.log('Coffee in the browser!!!');

  $(document).ready(function() {
    return $('.carousel').carousel({
      interval: 5000,
      pause: 'hover'
    });
  });

}).call(this);
