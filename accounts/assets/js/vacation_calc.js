$(document).ready(() => {
  $('#fdate').change(() => {
  var d1 = $('#fdate').val();
  var d2 = $('#tdate').val();

  var startDate = new Date($('#fdate').val());
  var endDate = new Date($('#tdate').val());
  var numOfDates = getBusinessDatesCount(startDate,endDate);


  function getBusinessDatesCount(startDate, endDate) {
    let count = 0;
    const curDate = new Date(startDate.getTime());
    while (curDate <= endDate) {
        const dayOfWeek = curDate.getDay();
        if(!(dayOfWeek in [0, 6])) count++;
        curDate.setDate(curDate.getDate() + 1);
    }
    $('#dif').text(count);
    return count;
  }

  });
});

$(document).ready(() => {
  $('#tdate').change(() => {
  var d1 = $('#fdate').val();
  var d2 = $('#tdate').val();

  var startDate = new Date($('#fdate').val());
  var endDate = new Date($('#tdate').val());
  var numOfDates = getBusinessDatesCount(startDate,endDate);


  function getBusinessDatesCount(startDate, endDate) {
    let count = 0;
    const curDate = new Date(startDate.getTime());
    while (curDate <= endDate) {
        const dayOfWeek = curDate.getDay();
        if(!(dayOfWeek in [0, 6])) count++;
        curDate.setDate(curDate.getDate() + 1);
    }
    $('#dif').text(count);
    return count;
  }

  });
});

