const toggleButton = document.getElementById("lang-toggle");
    const langMenu = document.getElementById("lang-menu");

    toggleButton.addEventListener("click", () => {
        if (langMenu.classList.contains("hidden")) {
            langMenu.classList.remove("hidden");
            // انیمیشن نمایش
            setTimeout(() => {
                langMenu.classList.remove("opacity-0", "transform", "scale-95");
                langMenu.classList.add("opacity-100", "transform", "scale-100");
            }, 10);
        } else {
            // انیمیشن مخفی‌سازی
            langMenu.classList.add("opacity-0", "transform", "scale-95");
            langMenu.classList.remove("opacity-100", "transform", "scale-100");
            setTimeout(() => {
                langMenu.classList.add("hidden");
            }, 300); // مدت زمان انیمیشن
        }
    });

    // بستن منو اگر خارج از آن کلیک شد
    window.addEventListener("click", (event) => {
        if (!toggleButton.contains(event.target) && !langMenu.contains(event.target)) {
            langMenu.classList.add("opacity-0", "transform", "scale-95");
            langMenu.classList.remove("opacity-100", "transform", "scale-100");
            setTimeout(() => {
                langMenu.classList.add("hidden");
            }, 300);
        }
    });

