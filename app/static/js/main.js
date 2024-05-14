$(document).on('click','#sidebar li', function(){
    $(this).addClass('active').siblings().removeClass('active')
});

$(document).ready(function(){
    $("#toggleSidebar").click(function(){
        $(".left-menu").toggleClass("hide");
        $(".content-wrapper").toggleClass("hide");
    });

    
});

function myFunction(x) {
    if (x.matches) { // If media query matches
        $(".left-menu").toggleClass("hide");
        $(".content-wrapper").toggleClass("hide");
    } else {
        $(".left-menu").classList.remove("hide");
        $(".content-wrapper").classList.remove("hide")
    }
  }


// Create a MediaQueryList object
var x = window.matchMedia("(width<= 767px)")

// Call listener function at run time
myFunction(x);

// Attach listener function on state changes
x.addEventListener("change", function() {
  myFunction(x);
});