$(document).ready(function () {
    $("#signup-form input[type = 'radio").change(function (e) {
        e.preventDefault();
        var selectedOne = $("#signup-form input[type='radio']:checked").val();

        // $.post("/register_user/", selectedOne, function (selectedOne, textStatus, jqXHR) {});

        $.ajax({
            type: "POST",
            url: "/register_user",
            data: "selectedOne",
            success: function (response) {
                alert("usertype found");
                $("#extra-fields").html(response);
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log("Error: " + errorThrown);
            },
        });
    });
});