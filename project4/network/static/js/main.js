
const buttons = document.querySelectorAll(".button_header");

buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        buttons.forEach(function(b) {
            b.classList.remove("active");
        });
        this.classList.add("active");
    });
});

