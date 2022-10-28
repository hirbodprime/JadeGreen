$(document).ready(function(){

    $(document).on('input', '.text-input', function(){
        var usernme = $('#username');
        var password = $('#password');
        var btnElement = $('#btn');
        var passwordRepeat = $('#passwordRepeat');
    
        if(usernme.val() && password.val() && passwordRepeat.val()) {
            $('#btn').prop("disabled",false);
            btnElement.css('background', '#799350');
            btnElement.css('cursor', 'pointer');
        }else{
            $('#btn').prop("disabled",true);
            btnElement.css('background', '#AFB1AF');
            btnElement.css('cursor', 'default');
        }
    })

        $("#post-form").submit(function(e){
            e.preventDefault();
            var _this = $(this)
            $('.err-msg').remove();
            var el = $('<div>')
            el.addClass("alert alert-danger err-msg")
            el.hide()
            if (_this[0].checkValidity() == false) {
                _this[0].reportValidity();
                return false;
            }
            $.ajax({
                headers: {
                    "X-CSRFToken": '{{csrf_token}}'
                },
                url: "http://127.0.0.1:8000/users/APIregister/",
                data: new FormData($(this)[0]),
                cache: false,
                contentType: false,
                processData: false,
                method: 'POST',
                type: 'POST',
                dataType: 'json',
                error: err => {
                    console.log(err)
                    alert_toast("An error occured", 'error');
                },
                success: function(resp) {
                    console.log("here1")
                    if (resp.status == 'success') {
                        el.removeClass("alert alert-danger err-msg")
                        console.log("here")
                        location.href = "http://127.0.0.1:8000/"
                    } else if (resp.status == 'failed' && !!resp.msg) {
                        el.text(resp.msg)
                    } else {
                        el.text("An error occured", 'error');
                        console.err(resp)
                    }
                    _this.prepend(el)
                    el.show('slow')
                }
            })
            
        });
        // var password = $("#password").val();
        // var passwordRepeat = $("#passwordRepeat").val();
        // var error = $("#error");

        // if (password != passwordRepeat) {
        //     error.show();
        //     return false;
        // } else {
        //     error.hide();
        //     // Ajax
        //     $.ajax({
        //         method : 'POST',
        //         url : '',
        //         data : {
        //             username: $('#username').val(),
        //             password: $('#password').val(),
        //             passwordRepeat: $('#passwordRepeat').val(),
        //             crsfmiddlewaretoken : $('input[username=crsfmiddlewaretoken]').val()
        //         },
        //         success : function (result){
                      
        //         }

        //     }) 
        // }

    });






