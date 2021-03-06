function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$("#comment_form").submit(function (e) {
  e.preventDefault()
  var formData = new FormData($("#comment_form")[0]);
  $.ajax({
    url: "/comment/add/",
    type: "POST",
    data: formData,
    cache: false,
    contentType: false,
    processData: false,
    success: function (data) {
      if (data.error) {
        $("#CommentError").html(data.error).show()
      } else {
        d = new Date(data.commented_on);
        $("#comments_div").prepend("<li class='list-group-item list-row' id='comment" + data.comment_id + "'>" +
          "<div class='pull-right right-container'>" +
          "<div class='list-row-buttons btn-group pull-right'>" +
          "<button class='btn btn-link btn-sm dropdown-toggle' data-toggle='dropdown' type='button'><span class='caret'></span></button>" +
          "<ul class='dropdown-menu pull-right'>" +
          "<li><a class='action' onclick='edit_comment(" + data.comment_id + ")'>Edit</a></li>" +
          "<li><a class='action' onclick='remove_comment(" + data.comment_id + ")''>Remove</a></li></ul></div></div>" +
          "<div class='stream-head-container'> " + data.commented_by + " Commented</div>" +
          "<div class='stream-post-container' id='comment_name" + data.comment_id + "'><pre>" + data.comment + "</pre></div>" +
          "<div class='stream-date-container" + data.comment_id + "'>" + d.toGMTString() + "</div></div><div class='stream-date-container' id='comment_file_div" + data.comment_id + "'><div id='new_comment" + data.comment_id + "'</div></div></li>"
        )
        $("#id_comments").val("")
        alert("Comment Submitted")
      }
    }
  })
})

//
// $("#comment_2_form").submit(function (e) {
//   e.preventDefault()
//   var formData = new FormData($("#comment_2_form")[0]);
//   $.ajax({
//     url: "/comment2/add/",
//     type: "POST",
//     data: formData,
//     cache: false,
//     contentType: false,
//     processData: false,
//     success: function (data) {
//       if (data.error) {
//         $("#CommentError").html(data.error).show()
//       } else {
//         d = new Date(data.commented_on);
//         $("#comments_div").prepend("<li class='list-group-item list-row' id='comment" + data.comment_id + "'>" +
//           "<div class='pull-right right-container'>" +
//           "<div class='list-row-buttons btn-group pull-right'>" +
//           "<button class='btn btn-link btn-sm dropdown-toggle' data-toggle='dropdown' type='button'><span class='caret'></span></button>" +
//           "<ul class='dropdown-menu pull-right'>" +
//           "<li><a class='action' onclick='edit_comment(" + data.comment_id + ")'>Edit</a></li>" +
//           "<li><a class='action' onclick='remove_comment(" + data.comment_id + ")''>Remove</a></li></ul></div></div>" +
//           "<div class='stream-head-container'> " + data.commented_by + " Commented</div>" +
//           "<div class='stream-post-container' id='comment_name" + data.comment_id + "'><pre>" + data.comment + "</pre></div>" +
//           "<div class='stream-date-container" + data.comment_id + "'>" + d.toGMTString() + "</div></div><div class='stream-date-container' id='comment_file_div" + data.comment_id + "'><div id='new_comment" + data.comment_id + "'</div></div></li>"
//         )
//         $("#id_comments").val("")
//         alert("Reply Submitted")
//       }
//     }
//   })
// })
//
//
//



function edit_comment(x) {
  $('#Comments_Cases_Modal').modal('show');
  comment = $("#comment_name" + x).text()
  $("#commentid").val(x)
  $("#id_editcomment").val(comment)
}

$("#comment_edit").click(function (e) {
  e.preventDefault()
  var formData = new FormData($("#comment_edit_form")[0]);
  $.ajax({
    url: "/comment/edit/",
    type: "POST",
    data: formData,
    cache: false,
    contentType: false,
    processData: false,
    success: function (data) {
      if (data.error) {
        $("#CommentEditError").html(data.error).show()
      } else {
        $("#comment_name" + data.commentid).html('<pre>' + data.comment + '</pre>')
        $('#Comments_Cases_Modal').modal('hide');
        $("#id_editcomment").val("")
        $("#CommentEditError").hide()
      }
    }
  })
})


function HideError(e) {
  $("#CommentError").hide()
}

function remove_comment(x) {
  var csrftoken = getCookie('csrftoken');
  var con = confirm("Do you want to Delete it for Sure!?")
  if (con == true) {
    $.post('/comment/remove/', {
      "comment_id": x,
      "csrfmiddlewaretoken": csrftoken,
    }, function (data) {
      if (data.error) {
        alert(data.error)
      } else {
        $("#comment" + data.cid).remove()
      }
    })
  }
}
