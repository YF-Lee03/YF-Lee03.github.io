// The initial theme is applied by an inline script in _layouts/default.html,
// before first paint. This file only handles user interaction.
const root = document.documentElement;
const themeToggle = document.querySelector(".theme-toggle");
const themeColor = document.querySelector('meta[name="theme-color"]');

themeToggle?.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = nextTheme;
  themeColor?.setAttribute("content", nextTheme === "dark" ? "#181c19" : "#f4f0e7");
  try { localStorage.setItem("theme", nextTheme); } catch (e) {}
});

// Render inline $...$ math with the self-hosted KaTeX loaded before this file.
window.renderMathInElement?.(document.body, {
  delimiters: [{ left: "$", right: "$", display: false }],
  throwOnError: false,
});

const year = document.querySelector("#year");
if (year) year.textContent = new Date().getFullYear();
