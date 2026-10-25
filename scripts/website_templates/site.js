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

  document.addEventListener("click", async (event) => {
    const button = event.target.closest(".copy-code");
    if (!button) return;
    const code = button.closest("pre")?.querySelector("code");
    if (!code) return;
    const original = button.textContent;
    try {
      await copyText(code.textContent);
      button.textContent = "Copied";
      button.setAttribute("aria-label", "Code copied");
    } catch {
      button.textContent = "Copy failed";
      button.setAttribute("aria-label", "Copy failed");
    }
    window.setTimeout(() => {
      button.textContent = original;
      button.setAttribute("aria-label", "Copy code");
    }, 1600);
  });
})();
