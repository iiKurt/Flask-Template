var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
var alertTrigger = document.getElementById('liveAlertBtn')

function flash(message, type) {
	var wrapper = document.createElement('div')
	wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'

	alertPlaceholder.append(wrapper)
}

window.onload = function() {
	csrftoken = document.head.querySelector("[name~=csrf-token][content]").content;

	function submitConfig(event) {
		event.preventDefault();

		/*const data = new FormData(event.target);
		var object = {};
		data.forEach(function(value, key, idk){
			console.log(key)
			console.log(value)
			console.log(Boolean(parseInt(value)))
			object[key] = value;
			console.log("==============")
		});
		var json = JSON.stringify(object);
		//const value = JSON.stringify(Object.fromEntries(data));
		*/

		var object = {};
		object.accountCreation = document.getElementById('accountCreationCheck').checked
		object.posting = document.getElementById('postingCheck').checked

		const xhr = new XMLHttpRequest();
		xhr.open("PUT", "/admin/config");
		xhr.setRequestHeader("X-CSRFToken", csrftoken);
		xhr.setRequestHeader("Content-Type", "application/json");
		xhr.onload = function () {
			if (xhr.status == 200) {
				flash("Changes applied.", 'success')
			}
			else {
				flash("Error.", 'danger')	
			}
		}
		xhr.ontimeout = function() {
			flash("Timed out.", 'warning')
		}
		xhr.send(JSON.stringify(object));
	}

	const form = document.getElementById('configForm');
	form.addEventListener('submit', submitConfig);
}
