/* ------------------------------------------------
# All scripts here it will extends to all the page
------------------------------------------------ */

// 1) If no patient, show the message
$(document).ready(function() {
    let verify = $("#chk_td").length;
        if (verify == 0) {
            $("#no-data").text("No patient found")
        }
});

// 2) Time running at realtime 
setInterval(function() {
    let date = new Date();
    $("#clock").html(
        `${(date.getHours() < 10 ? '0' : '')}${date.getHours()}:${(date.getMinutes() < 10 ? '0' : '')}${date.getMinutes()}:${(date.getSeconds() < 10 ? '0' : '')}${date.getSeconds()}`
    )
}, 500)

// 3) Validate all input tags
function validateEmail(email) {
    let regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9])+\.)+([a-zA-Z0-9]{2,4})+$/; //regex for email
    return regex.test(email);
}

function validateAll() {
    let name = $("#name").val(),
        phone = $("#phone").val(),
        email = $("#email").val(),
        age = $("#age").val(),
        gender = $("#gender").val();
    // Statement for name input
    if (name == '') {
        swal("Ops!", "Name field cannot be empty.", "error")
        return false;
    }
    else if (name == name.toUpperCase()) {
        swal("Ops!", "Name cannot be in upper case.", "error")
        $("#name").val("")
        return false;
    }
    else if (name.split(" ").length < 2) {
        swal("Ops!", "Name field require the last name.", "info")
        return false;
    }
    // Statement for phone input
    else if (phone == '') {
        swal("Ops!", "Phone field cannot be empty.", "error")
        return false;
    }
    // Statement for email input
    else if (email == '') {
        swal("Ops!", "Email field cannot be empty.", "error")
        return false;
    }
    else if (!(validateEmail(email))) {
        swal("Ops!", "Enter a valid email.", "error")
        $("#email").val("");
        return false;
    }
    // Statement for age input
    else if (age == '') {
        swal("Ops!", "Age field cannot be empty.", "error")
        return false;
    }
    // Method ONE to limit the age value 
    // else if (age > 120) {
    //     swal("Denied!", "The maximum age value is 120 years.", "error")
    //     $("#age").val("");
    //     return false;
    // }
    // Conditional statement for gender
    else if (gender == ''){
        swal("Ops!", "Gender field cannot be empty.", "error")
        return false;
    }
    else {
        return true;
    }

}
// Call the function validateAll 
$("#btn-add").bind("click", validateAll);

// 4) Script - Only letters is allowed 
$(document).ready(function(){
    jQuery('input[name="name"]').keyup(function(){
        let letter = jQuery(this).val(),
        allow = letter.replace(/[^a-zA-Z _]/g, ''); // Allow only alphabets
        jQuery(this).val(allow);
    });
    // To prevent space in the input
    $("input").on("keypress", function(e){
        if (e.which === 32 && !this.value.length)
            e.preventDefault();
        
    })

    // Only the first and the last name required
    $("#name").keyup(function(){
        let name = $("#name").val();
        if (name.split(" ").length === 3){
            swal("Ops!", "Only first and last names required.", "info");
            $("#name").val("");
            return false;
        }
    })
});

// 6) Capitalize the first letter of each word in name 
$("#name").keyup(function(){
    let txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1) {
        return $1.toUpperCase();
    }))
})

// 7) Phone number mask 
$(document).ready(function() {
    $("#phone").inputmask("(999) 99999-99999", {"onincomplete": function() {
        swal("Ops!", "Incomplete phone number. Please review", "info");
        $("#phone").val("");
        return false;
    }})
})

// 8) Script to LOWERCASE <input> email
$(document).ready(function() {
    $("#email").keyup(function() {
        this.value = this.value.toLowerCase();
    });
    
    // Method TWO for limiting the value of age 
    $("#age").keyup(function() {
        let age = $("#age").val();
        if (age > 120) {
            swal("Denied!", "The maximum age value is 120 years.", "error")
            $("#age").val("");
            return false;
        }
    });
});

// 9) Script to allow only digits in AGE
$("#age").keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
});

// 10) Script to prevent age to start with 0
$("#age").on("input", function() {
    if (/^0/.test(this.value)) {
        this.value = this.value.replace(/^0/, "")
    }
});