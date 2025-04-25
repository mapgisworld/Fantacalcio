document.addEventListener("DOMContentLoaded", function () {
  const homeLink = document.querySelector('a[href="index.html"]');
  const fairPlayLink = document.querySelector('a[href="page/fair_play.html"]');

  const basePath = "/Fantacalcio"; // Percorso corretto per GitHub Pages

  if (homeLink) {
    homeLink.addEventListener("click", function (e) {
      e.preventDefault();
      window.location.href = basePath + "/index.html";
    });
  }

  if (fairPlayLink) {
    fairPlayLink.addEventListener("click", function (e) {
      e.preventDefault();
      window.location.href = basePath + "/page/fair_play.html";
    });
  }
});
