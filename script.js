// The initial theme is applied by an inline script in _layouts/default.html,
// before first paint. This file only handles user interaction.
const root = document.documentElement;
const themeToggle = document.querySelector(".theme-toggle");
const themeColor = document.querySelector('meta[name="theme-color"]');
const menuToggle = document.querySelector(".menu-toggle");
const menu = document.querySelector("#site-nav");

themeToggle?.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = nextTheme;
  themeColor?.setAttribute("content", nextTheme === "dark" ? "#181c19" : "#f4f0e7");
  try { localStorage.setItem("theme", nextTheme); } catch (e) {}
});

menuToggle?.addEventListener("click", () => {
  const isOpen = menu.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

menu?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    menu.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
  });
});

const year = document.querySelector("#year");
if (year) year.textContent = new Date().getFullYear();
