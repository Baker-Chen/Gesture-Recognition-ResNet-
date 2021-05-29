var ft = $('.number img').get()[0];
var fs = $('.number img').get()[1];
var stop = 0;

$.fn.open = function () {
    setTimeout(function () {
        $("#door_left").animate2({
            transform: "translate(-65%, 0%)",
        }, 2000)
        $("#door_right").animate2({
            transform: "translate(65%, 0%)",
        }, 2000)
        $("#door_left").delay(2000).animate2({
            transform: "translate(0%, 0%)",
        }, 2000)
        $("#door_right").delay(2000).animate2({
            transform: "translate(0%, 0%)",
        }, 2000)
    }, 1800);
};
$("#button2").click(function () {
    $("#door_left").stop(true, false).animate2({
        transform: "translate(-65%, 0%)",
    }, 2000)
    $("#door_right").stop(true, false).animate2({
        transform: "translate(65%, 0%)",
    }, 2000)
});
$("#button3").click(function () {
    $("#door_left").stop(true, false).animate2({
        transform: "translate(0%, 0%)",
    }, 2000)
    $("#door_right").stop(true, false).animate2({
        transform: "translate(0%, 0%)",
    }, 2000)
});

// $('#button4').click(function () {
//     setTimeout(function () {
//         ft.id = parseInt(ft.id, 10) + 1
//         fs.id = parseInt(fs.id, 10) + 1
//         $('.number img').attr("src", 'static/images/' + fs.id + '.png');
//     }, 1000);
// });

// $('#button5').click(function () {
//     ft.id = 1;
//     fs.id = 1;
//     $('.number img').attr("src", 'static/images/' + fs.id + '.png');
//     timerInterval = setInterval(() => {
//         ft.id = parseInt(ft.id, 10) + 1;
//         fs.id = parseInt(fs.id, 10) + 1;
//         $('.number img').attr("src", 'static/images/' + fs.id + '.png');
//         if (fs.id == 7) {
//             clearInterval(timerInterval);
//         }
//     }, 1000);
// });

// $('#button6').click(function () {
//     timerInterval = setInterval(() => {
//         $.ajax({
//             type: 'POST',
//             url: '/getdata',
//             success: function (a) {
//                 console.log('喔有東西: ' + a);
//             }
//         });
//     }, 1000);
// });

$('#button6').click(function () {
    timerInterval = setInterval(() => {
        if (stop == 0) {
            $('.sign').css('opacity', '0');
            $.ajax({
                type: 'POST',
                url: '/getdata',
                success: function (a) {
                    console.log('a是: ' + a + 'id是：' + ft.id);
                    if (ft.id > a) {
                        let myPromise = new Promise(function (myResolve) {
                            setTimeout(function () {
                                $('.sign img').attr("src", 'static/images/down.png');
                                myResolve();
                            }, 100);
                        });
                        myPromise.then(function () {
                            $('.sign').css('opacity', '0.8');
                            $().elev(a, -1);
                        });
                    } else if (ft.id < a) {
                        let myPromise = new Promise(function (myResolve) {
                            setTimeout(function () {
                                $('.sign img').attr("src", 'static/images/up.png');
                                myResolve();
                            }, 100);
                        });
                        myPromise.then(function () {
                            $('.sign').css('opacity', '0.8');
                            $().elev(a, 1);
                        });
                    }
                }
            });
        };

    }, 1000);
});

// $('#button7').click(function () {
//     $.ajax({
//         type: 'POST',
//         url: '/change/2/',
//         success: function (a) {
//             console.log('已改變成: ' + a);
//         }
//     });
// });

$.fn.animate2 = function (properties, duration, ease) {
    ease = ease || 'ease';
    var $this = this;
    var cssOrig = { transition: $this.css('transition') };
    return $this.queue(next => {
        properties['transition'] = 'all ' + duration + 'ms ' + ease;
        $this.css(properties);
        setTimeout(function () {
            $this.css(cssOrig);
            next();
        }, duration);
    });
};

$(document).ready(function () {
    $.ajax({
        type: 'POST',
        url: '/getdata',
        success: function (a) {
            ft.id = a;
            fs.id = a;
            $('.number img').attr("src", 'static/images/' + fs.id + '.png');
        }
    });
});

$.fn.elev = function (floor, up) {
    stop = 1;
    timerInterval = setInterval(() => {
        ft.id = parseInt(ft.id, 10) + 1 * up;
        fs.id = parseInt(fs.id, 10) + 1 * up;
        console.log(fs.id)
        $('.number img').attr("src", 'static/images/' + fs.id + '.png');
        if (fs.id == floor) {
            clearInterval(timerInterval);
            stop = 0;
            $().open();
        }
    }, 1000);
};