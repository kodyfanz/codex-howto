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

  const copyText = async (text) => {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    area.remove();
  };

  const copyIcon = '<svg viewBox="0 0 24 24" focusable="false"><path d="M9 8V5.5A1.5 1.5 0 0 1 10.5 4h8A1.5 1.5 0 0 1 20 5.5v8a1.5 1.5 0 0 1-1.5 1.5H16M5.5 8h8A1.5 1.5 0 0 1 15 9.5v9A1.5 1.5 0 0 1 13.5 20h-8A1.5 1.5 0 0 1 4 18.5v-9A1.5 1.5 0 0 1 5.5 8Z"/></svg>';
  const copiedIcon = '<svg viewBox="0 0 24 24" focusable="false"><path d="m5 12 4.5 4.5L19 7"/></svg>';

  document.addEventListener("click", async (event) => {
    const button = event.target.closest(".copy-code");
    if (!button) return;
    const code = button.closest("pre")?.querySelector("code");
    if (!code) return;
    const icon = button.querySelector(".copy-icon");
    const label = button.querySelector(".sr-only");
    try {
      await copyText(code.textContent);
      if (icon) icon.innerHTML = copiedIcon;
      if (label) label.textContent = "Code copied";
      button.classList.add("is-copied");
      button.setAttribute("aria-label", "Code copied");
    } catch {
      if (label) label.textContent = "Copy failed";
      button.setAttribute("aria-label", "Copy failed");
    }
    window.setTimeout(() => {
      if (icon) icon.innerHTML = copyIcon;
      if (label) label.textContent = "Copy code";
      button.classList.remove("is-copied");
      button.setAttribute("aria-label", "Copy code");
    }, 1600);
  });
})();
