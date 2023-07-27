function userScroll() {
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('bg-primary');
            navbar.classList.add('navbar-sticky');
            navbar.setAttribute('data-bs-theme', 'dark');
        } else {
            navbar.classList.remove('bg-primary');
            navbar.classList.remove('navbar-sticky');
            navbar.setAttribute('data-bs-theme', 'light');
        }
    });
}

document.addEventListener('DOMContentLoaded', userScroll);

const modal = new bootstrap.Modal(document.getElementById("modal"))

htmx.on("htmx:afterSwap", (e) => {
  // Response targeting #dialog => show the modal
  if (e.detail.target.id == "dialog") {
    modal.show()
  }
})

htmx.on("htmx:beforeSwap", (e) => {
  // Empty response targeting #dialog => hide the modal
  if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
      modal.hide()
      e.detail.shouldSwap = false
  }
})