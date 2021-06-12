$(document).ready(function() {
    $('.show-form').click(function (){
        $.ajax({
            url:'/main/create',
            type: 'get',
            dataType: 'json',
            beforeSend: function (){
                $('#modal-vacation').modal('show')
            },
            success: function (data){
                $('#modal-vacation .modal-content').html(data.html_form);
            }
        })
    })

    $('#modal-vacation').on('submit', '.create-form', function (){
        var form = $(this);
        $.ajax({
            type: "POST",
            url: form.attr('data-url'),
            data: form.serialize(),
            form: form.attr('method'),
            dataType: 'json',
            success: function (data){
                if(data.form_is_valid) {
                    console.log('Data is saved')
                } else {
                    console.log('Data not saved')
                    console.log(data)
                    $('modal-vacation .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    })


    $('.show-form-update').click(function (){
        alert('dasd')
        $.ajax({
            url:'/main/update',
            type: 'get',
            dataType: 'json',
            beforeSend: function (){
                $('#modal-vacation').modal('show')
            },
            success: function (data){
                $('#modal-vacation .modal-content').html(data.html_form);
            }
        })
    })

    $('#modal-vacation').on('submit', '.create-form', function (){
        var form = $(this);
        $.ajax({
            type: "POST",
            url: form.attr('data-url'),
            data: form.serialize(),
            form: form.attr('method'),
            dataType: 'json',
            success: function (data){
                if(data.form_is_valid) {
                    console.log('Data is saved')
                } else {
                    console.log('Data not saved')
                    console.log(data)
                    $('modal-vacation .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    })
})