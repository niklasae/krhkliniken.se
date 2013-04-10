console.log 'Coffee in the browser!!!'

$(document).ready ->

  $('.carousel').carousel({
    interval: 2500,
    pause: 'hover'
  })
