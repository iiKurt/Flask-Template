window.onload = function() {
	csrftoken = document.head.querySelector("[name~=csrf-token][content]").content;

	var elements = document.querySelectorAll('.btn-delete-user');
	for (var i = 0; i < elements.length; i++) {
		elements[i].onclick = function() {
			const xhr = new XMLHttpRequest()
			xhr.open("DELETE", "/user/" + this.dataset['user-username'])
			xhr.setRequestHeader("X-CSRFToken", csrftoken)
			xhr.onload = function () {
				const response = xhr.responseText
			}
			xhr.send();
		}
	}
}
