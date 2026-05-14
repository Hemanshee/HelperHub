// 🔥 Navbar scroll effect
window.addEventListener("scroll", function () {
    let navbar = document.querySelector(".navbar");
    navbar.style.background = window.scrollY > 50 
        ? "rgba(0,0,0,0.95)" 
        : "rgba(0,0,0,0.7)";
});

// 🔥 Button click animation
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            btn.style.transform = "scale(0.95)";
            setTimeout(() => {
                btn.style.transform = "scale(1)";
            }, 150);
        });
    });
});

// 🔥 Simple alert (optional)
function showSuccess() {
    alert("Action completed successfully 🎉");
}