$(document).ready(function() {
    $(document).on('submit', '#feedbackForm', function(e) {
        e.preventDefault();
        var email = $('input[name="email"]').val();
        var nama = $('input[name="nama"]').val();
        var komentar = $('input[name="komentar"]').val();
    })
})