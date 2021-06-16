const text = document.getElementById("text");

console.log(text.scrollLeft, text.scrollTop, text.scrollWidth);
text.scrollTop = 500;
text.style.transform = `translateX(${text.scrollTop})`;
console.log(text.scrollLeft, text.scrollTop, text.scrollWidth);


$.fn.moveIt = function(){
    var $window = $(window);
    var instances = [];
    
    $(this).each(function(){
      instances.push(new moveItItem($(this)));
    });
    
    window.addEventListener('scroll', function(){
      var scrollTop = $window.scrollTop();
      instances.forEach(function(inst){
        inst.update(scrollTop);
      });
    }, {passive: true});
  }
  
  var moveItItem = function(el){
    this.el = $(el);
    this.speed = parseInt(this.el.attr('data-scroll-speed'));

  };
  
  moveItItem.prototype.update = function(scrollTop){
    this.el.css('transform', 'translateY(' + -(scrollTop / this.speed) + 'px)');
    // console.log(scrollTop);

  };

  // Fade in

  $.fn.fadeIt = function(){
    var $window = $(window);
    var instance = [];

    $(this).each(function(){
      instance.push(new fadeItItem($(this)));
    });

    window.addEventListener('scroll', function(){
      var scrollTop = $window.scrollTop();
      instance.forEach(function(inst){
        inst.update(scrollTop);
      });
    }, {passive: true});
  }

  var fadeItItem = function(el){
    this.el = $(el);
    this.fadeDistance = parseInt(this.el.attr('data-fade'));
  };

  fadeItItem.prototype.update = function(scrollTop){
    let opa = this.fadeDistance / scrollTop;
    this.el.css('opacity', opa);
    
  }


  $(window).on("load",function() {
    $(window).scroll(function() {
      var windowBottom = $(this).scrollTop() + $(this).innerHeight();
      $(".fade").each(function() {
        /* Check the location of each desired element */
        var objectBottom = $(this).offset().top + $(this).outerHeight();
        
        /* If the element is completely within bounds of the window, fade it in */
        if (objectBottom < windowBottom) { //object comes into view (scrolling down)
          if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
        } else { //object goes out of view (scrolling up)
          if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
        }
      });
    }).scroll(); //invoke scroll-handler on page-load
  });
  
  // Initialization
  $(function(){
    $('[data-scroll-speed]').moveIt();
    $('[data-fade]').fadeIt();
  });
