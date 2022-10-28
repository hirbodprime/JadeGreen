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

    $("#post-form").submit(function(){
        var password = $("#password").val();
        var passwordRepeat = $("#passwordRepeat").val();
        var error = $("#error");

        if (password != passwordRepeat) {
            error.show();
            return false;
        } else {
            error.hide();
            // Ajax
            $.ajax({
                method : 'POST',
                url : '',
                data : {
                    username: $('#username').val(),
                    password: $('#password').val(),
                    passwordRepeat: $('#passwordRepeat').val(),
                    crsfmiddlewaretoken : $('input[username=crsfmiddlewaretoken]').val()
                },
                success : function (result){
                      
                }

            }) 
        }

    });


});






