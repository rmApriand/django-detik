document.addEventListener("DOMContentLoaded", function() {
    const searchBtn = document.getElementById("search-btn");
    const popup = document.getElementById("popup");
    const overlay = document.getElementById("overlay");
    const closeBtn = document.getElementById("close-btn");

    searchBtn.addEventListener("click", function(event) {
        event.preventDefault();
        popup.style.display = "block";
        overlay.style.display = "block";
    });

    closeBtn.addEventListener("click", function() {
        popup.style.display = "none";
        overlay.style.display = "none";
    });
});
