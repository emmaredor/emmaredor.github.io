/**
 * Menu
 */
$("a.menu-icon").on("click", function(event) {
  var w = $(".menu");

  w.css({
    display: (w.css("display") === "none")
      ? "block"
      : "none"
  });
});

/**
 * Footer year
 */
$(document).ready(function() {
  $("#year").text(new Date().getFullYear());
});

/**
 * Red Panda GIF Randomizer
 */
$(document).ready(function() {
  const gifElement = $("#red-panda-gif");
  
  if (gifElement.length > 0) {
    console.log("Red panda GIF element found!");
    
    // List of available GIF files
    const availableGifs = [
      'attack.gif',
      'eeping.gif', 
      'eepy.gif',
      'falling.gif',
      'idle.gif',
      'idle2.gif',
      'jump.gif'
    ];
    
    // Select a random GIF
    const randomIndex = Math.floor(Math.random() * availableGifs.length);
    const selectedGif = availableGifs[randomIndex];
    const gifPath = '/assets/img/red_pandas/' + selectedGif;
    
    console.log("Selected GIF:", selectedGif);
    
    // Set the src attribute to load the random GIF
    gifElement.attr('src', gifPath);
    
    // Log when the GIF loads successfully
    gifElement.on('load', function() {
      console.log("GIF loaded successfully:", selectedGif);
    });
    
    gifElement.on('error', function() {
      console.error("Failed to load GIF:", selectedGif);
    });
    
  } else {
    console.log("Red panda GIF element NOT found!");
  }
});

/**
 * Footer email
 */
$(document).ready(function() {
  $(".email-link-cloaked").on("click", function(event) {
    const _link = event.target;

    const _user = reverseString(_link.getAttribute("data-resu"));
    const _domain = reverseString(_link.getAttribute("data-eman-niamod"));
    const _tld = reverseString(_link.getAttribute("data-dlt-niamod"));

    window.location.href = `mailto:${_user}@${_domain}.${_tld}`;
  });
});

/**
 * Reverses a string
 */
function reverseString(str) {
  return str.split("").reverse().join("");
}

/**
 * Moves WeChat widget
 */
function moveWidget(event) {
  var w = $("#wechat-widget");

  w.css({
    left: event.pageX - 25,
    top: event.pageY - w.height() - 60
  });
}

$("a#wechat-link").on("mouseenter", function(event) {
  $("#wechat-widget").css({ display: "block" });

  moveWidget(event);
});

$("a#wechat-link").on("mousemove", function(event) {
  moveWidget(event);
});

$("a#wechat-link").on("mouseleave", function(event) {
  $("#wechat-widget").css({ display: "none" });
});
