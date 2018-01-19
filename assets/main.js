function main() {
  function updateTime() {
    function handleResponse(data) {
      $('#time_field').text(data);
    }

    /*
    var obj = {
      member1: "foo",
      member2: "bar",
      member3: 3,
      member4: function(blah) {
        ...
      }
    };

    obj.member4(...)
    obj['member4'](...)

    var myMember  = 'member4';
    obj[myMember](...)
    */


    // equivalent to $.get('http://192.168.1.10:8000/time', ...
    $.get('/time', handleResponse);
  }

  var isTimerRunning = false;
  var intervalId;
  function toggleTimer() {
    if (isTimerRunning) {
      clearInterval(intervalId);
      isTimerRunning = false;
      $('#time_button').text("Start timer");
    } else {
      intervalId = setInterval(updateTime, 1000);
      isTimerRunning = true;
      $('#time_button').text("Stop timer");
    }
  }

  // on click, send GET to http://.../time
  $('#time_button').on('click', toggleTimer);

  $('#new_session_form').hide();

  $('#new_session_button').on('click', function() {
    $('#new_session_form').show();
  });

  $('#new_session_ok').on('click', function() {
    // ... do other things before hiding
    $('#new_session_form').hide();
  });
}

$(main);
