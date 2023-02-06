

window.addEventListener("load", function() {
    const firstTeam = document.querySelector("#selected_team option:first-child").value;
    fetch(`get_team_users/${firstTeam}`)
    .then(response => response.json())
    .then(data => {
        const usersCheckbox = document.getElementById("user_checkbox");
        usersCheckbox.innerHTML = "";
        data.users.forEach(user => {
        usersCheckbox.innerHTML += `
        <div class="form-check mb-1"> 
            <input class="form-check-input" id="flexCheck1" name="user[]" value="${user.username}" type="checkbox"> 
            <label class="form-check-label" for="flexCheck1"><span class="fst-italic pl-1">${user.username}</span></label> 
        </div> `;
    });
});
});


document.getElementById("selected_team").addEventListener("change", function() {
  const teamId = this.value;
  fetch(`/get_team_users/${teamId}`)
      .then(response => response.json())
      .then(data => {
          const usersCheckbox = document.getElementById("user_checkbox");
          usersCheckbox.innerHTML = "";
          data.users.forEach(user => {
              usersCheckbox.innerHTML += `
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="checkbox1" name="user[]" value="{{ user.username }}">
                    <label class="form-check-label" for="checkbox1">{{ user.username }}</label>
                </div>
              `;
          });
      });
});
