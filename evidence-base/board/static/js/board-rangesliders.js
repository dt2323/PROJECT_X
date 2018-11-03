
var rangeValues =
[
  "0 - Only use Zero if you do not wish to provide a rating",
  "1 - Very Weak",
  "2 - Weak",
  "3 - Moderate",
  "4 - Strong",
  "5 - Very Strong"
];

var valuesList =
[
  0,0,0,0,0,0,0,0,0,0
]

var rangeSlider = function(){
  var slider = $('.range-slider'),
      range = $('.custom-range'),
      value = $('.range-slider__value');

  slider.each(function(){

    value.each(function(){
      var value = $(this).next().attr('value');
 var val = rangeValues[Math.floor(value/10)];
      $(this).html(val);
    });

    range.on('input', function(){
      var val = Math.floor(this.value/10);
      valuesList[this.id] = val;
  $(this).prev(value).html(rangeValues[val]);
    });


  });
};

rangeSlider();
