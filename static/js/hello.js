function post_greeting() {
    $.ajax({
        type: 'POST',
        url: '/greeting_post',
        data: '',
        contentType: 'application/json',
        success: function (data) {
            const greeting = JSON.parse(data.ResultSet).greeting
            const greeting_image = JSON.parse(data.ResultSet).image
            document.getElementById('greeting').innerHTML = greeting
            document.getElementById('greeting_image').src = greeting_image

        }
    })
}