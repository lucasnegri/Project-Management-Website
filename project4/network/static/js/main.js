const buttons = document.querySelectorAll(".nav_link.button_header");

buttons.forEach(button => {
  button.addEventListener("click", function() {
    buttons.forEach(b => b.classList.remove("active"));
    this.classList.add("active");
  });
});