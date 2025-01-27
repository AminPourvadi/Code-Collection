const header = document.querySelector('header');
let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
    if (window.scrollY > lastScrollY) {
        header.classList.add('bg-opacity-80'); // هنگام اسکرول به پایین
    } else {
        header.classList.remove('bg-opacity-80'); // هنگام اسکرول به بالا
    }
    lastScrollY = window.scrollY;
});
