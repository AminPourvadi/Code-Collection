const header = document.querySelector('header');

    // تغییر شفافیت هدر هنگام اسکرول
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.opacity = '0.9'; // هدر شفاف‌تر می‌شود
        } else {
            header.style.opacity = '1'; // هدر به حالت اولیه باز می‌گردد
        }
    });