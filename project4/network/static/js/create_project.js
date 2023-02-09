
// Function to load the page when a "create_team" is called. When the page first loads, it update the user_list with the team.members
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


// Function to update user_list being passed when the user select a "team" on the selection input
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
                        <input type="checkbox" class="form-check-input" id="checkbox1" name="user[]" value="${ user.username }">
                        <label class="form-check-label" for="checkbox1">${user.username }</label>
                    </div>
                `;
            });
        });
});
