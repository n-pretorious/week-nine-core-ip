function showModal(photoUrl, profilePhoto, profileUserName, imageCaption, likes, comments, commentAuthor) {
    $('#imageheader').attr('src', profilePhoto)
    $('#userName').text(profileUserName)
    $('#userNameCap').text(profileUserName)
    $('#imgCaption').text(imageCaption)
    $('#comments').text(comments)
    $('#author').text(commentAuthor)
    $('#imagepreview').attr('src', photoUrl);
    $('#noOfLikes').text(likes + ' likes');
    $('#mediaModal').modal();
    // $('.imagepreview').attr('src', $(this).find('img').attr('src'));
}