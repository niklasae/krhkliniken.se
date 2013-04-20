console.log 'Coffee in the browser!!!'

$(document).ready ->

  $('.carousel').carousel({
    interval: 5000,
    pause: 'hover'
  })
