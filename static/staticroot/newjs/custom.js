// Animate the element's value from x to y:

$({ someValue: 0 }).animate({ someValue: Math.floor( 5223 ) }, {
    duration: 3500,
    easing: 'swing', // can be anything
    step: function () { // called on every step
        // Update the element's text with rounded-up value:
        $('.count').text(commaSeparateNumber(Math.round(this.someValue)));
    }
});

function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
    }
    return val;
}


$({ someValue: 0 }).animate({ someValue: Math.floor(145) }, {
    duration: 4000,
    easing: 'swing', // can be anything
    step: function () { // called on every step
        // Update the element's text with rounded-up value:
        $('.count1').text(commaSeparateNumber(Math.round(this.someValue)));
    }
});

function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
    }
    return val;
}


$({ someValue: 0 }).animate({ someValue: Math.floor(3700) }, {
    duration: 4000,
    easing: 'swing', // can be anything
    step: function () { // called on every step
        // Update the element's text with rounded-up value:
        $('.count2').text(commaSeparateNumber(Math.round(this.someValue)));
    }
});

function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
    }
    return val;
}

$({ someValue: 0 }).animate({ someValue: Math.floor(90732) }, {
    duration: 4000,
    easing: 'swing', // can be anything
    step: function () { // called on every step
        // Update the element's text with rounded-up value:
        $('.count3').text(commaSeparateNumber(Math.round(this.someValue)));
    }
});

function commaSeparateNumber(val) {
    while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
    }
    return val;
}


window.document.onkeydown = function(e) {
  if (!e) {
    e = event;
  }
  if (e.keyCode == 27) {
    lightbox_close();
  }
}


window.document.onkeydown = function(e) {
  if (!e) {
    e = event;
  }
  if (e.keyCode == 27) {
    lightbox_close3();
  }
}


function lightbox_open() {
  var lightBoxVideo = document.getElementById("VisaChipCardVideo");
  window.scrollTo(0, 0);
  document.getElementById('light').style.display = 'block';
  document.getElementById('fade').style.display = 'block';
  lightBoxVideo.play();
}

function lightbox_close() {
  var lightBoxVideo = document.getElementById("VisaChipCardVideo");
  document.getElementById('light').style.display = 'none';
  document.getElementById('fade').style.display = 'none';
  lightBoxVideo.pause();
}


 window.document.onkeydown = function(e) {
  if (!e) {
    e = event;
  }
  if (e.keyCode == 27) {
    lightbox_close2();
  }
}

function lightbox_open2() {
  var lightBoxVideo = document.getElementById("VisaChipCardVideo2");
  window.scrollTo(0, 0);
  document.getElementById('light2').style.display = 'block';
  document.getElementById('fade2').style.display = 'block';
  lightBoxVideo.play();
}

function lightbox_close2() {
  var lightBoxVideo = document.getElementById("VisaChipCardVideo2");
  document.getElementById('light2').style.display = 'none';
  document.getElementById('fade2').style.display = 'none';
  lightBoxVideo.pause();
}

function lightbox_open3() {
  var lightBoxVideo = document.getElementById("VisaChipCardVideo3");
  window.scrollTo(0, 0);
  document.getElementById('light3').style.display = 'block';
  document.getElementById('fade3').style.display = 'block';
  lightBoxVideo.play();
}

function lightbox_close3() {
  var lightBoxVideo = document.getElementById("VisaChipCardVideo3");
  document.getElementById('light3').style.display = 'none';
  document.getElementById('fade3').style.display = 'none';
  lightBoxVideo.pause();
}

