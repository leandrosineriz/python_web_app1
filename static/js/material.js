$(document).ready(function(){
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        var form = $('#register-form').serialize();
        $.ajax({
            url: "/postregistration",
            method: "POST",
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: "/check-login",
            type: "POST",
            data: form,
            success: function(res){
                if(res == "error"){
                    alert("Could not log in.");
                }else{
                    console.log("Log in as ", res);
                    window.location.href = "/";
                }
            }
        });
    });

    $(document).on("click", "#logout-link", function(e){
        e.preventDefault();
        $.ajax({
            url: "/logout",
            type: "GET",
            success: function(res){
                if(res == "success"){
                    console.log("Logout success");
                    window.location.href = "/login";
                }else{
                    alert("Something went wrong.");
                }
            }
        });
    });

    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: "/post-activity",
            type: "POST",
            data: form,
            success: function(res){
                    console.log(res);
                    window.location.href = "/";
            }
        });
    });

    $(document).on("submit", "#update-profile-form", function(e){
        e.preventDefault();
        var form = $(this).serialize();
        $.ajax({
            url: "/update-profile",
            type: "POST",
            data: form,
            success: function(res){
                    console.log(res);
                    window.location.href = window.location.href;
            }
        });
    });

});
