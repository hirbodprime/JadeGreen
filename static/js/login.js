$(document).ready(function(){

    $(document).on('input', '.text-input', function(){
        var usernme = $('#username');
        var password = $('#password');
        var btnElement = $('#btn');
    
        if(usernme.val() && password.val()) {
            $('#btn').prop("disabled",false);
            btnElement.css('background', '#799350');
            btnElement.css('cursor', 'pointer');
        }else{
            $('#btn').prop("disabled",true);
            btnElement.css('background', '#AFB1AF');
        }
    })

    $("#loginForm").submit(function(){
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
        
    });


});
