

// Function to update users on the list when a team radio button is clicked in the "Project Create Page"
// JavaScript code to update the user list based on the selected team
document.querySelectorAll("input[type='radio']").forEach(function(radio) {
    radio.addEventListener("change", function() {
      var teamId = this.value;
      updateUserList(teamId);
    });
  });
  
  function updateUserList(teamId) {
    // Use AJAX to get the user list for the selected team
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_users_by_team/" + teamId, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        // If the request is successful, update the user list
        var users = JSON.parse(xhr.responseText);
        var checkboxContainer = document.querySelector("#user_checkbox");
        checkboxContainer.innerHTML = "";
        users.forEach(function(user) {
          checkboxContainer.innerHTML += `
            <div class="form-check mb-1">
              <input class="form-check-input" id="user_${user.id}" name="user[]" value="${user.username}" type="checkbox">
              <label class="form-check-label" for="user_${user.id}"><span class="fst-italic pl-1">${user.username}</span></label>
            </div>
          `;
        });
      }
    };
    xhr.send();
  }