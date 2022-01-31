
function slide(direction){
  var container = document.getElementById('timeline');
  var scrollCompleted = 0;
  var slideVar = setInterval(function(){
    if(direction == 'left'){
      container.scrollLeft -= 40;
    } else {
      container.scrollLeft += 40;
    }
    scrollCompleted += 10;
    if(scrollCompleted >= 100){
      window.clearInterval(slideVar);
    }
  }, 50);
}
