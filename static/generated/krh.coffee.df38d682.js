(function() {

  console.log('Coffee in the browser!!!');

  $(document).ready(function() {
    return $('.carousel').carousel({
      interval: 2500,
      pause: 'hover'
    });
  });

}).call(this);
