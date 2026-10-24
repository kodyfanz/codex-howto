(() => {
  const root = document.documentElement;
  const theme = localStorage.getItem("codex-howto-theme");
  if (theme === "dark" || theme === "light") root.dataset.theme = theme;

  document.getElementById("theme-toggle")?.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    localStorage.setItem("codex-howto-theme", root.dataset.theme);
  });

  const sidebar = document.getElementById("sidebar");
  const navButton = document.getElementById("nav-toggle");
  navButton?.addEventListener("click", () => {
    const open = sidebar?.classList.toggle("open") ?? false;
    navButton.setAttribute("aria-expanded", String(open));
  });
})();
