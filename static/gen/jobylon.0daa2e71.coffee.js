(function() {

  console.log('Coffee in the browser!!!');

  $(document).ready(function() {
    return $('.carousel').carousel({
      interval: 2000
    });
  });

}).call(this);
