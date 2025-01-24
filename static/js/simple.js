const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('hidden');
});

const carouselItems = document.querySelectorAll('.carousel-item');
let currentIndex = 0;
        
function updateCarousel() {
    carouselItems.forEach((item, index) => {
    item.classList.toggle('opacity-100', index === currentIndex);
    item.classList.toggle('opacity-0', index !== currentIndex);
    });
}
// Automatic slide every 3 seconds

setInterval(() => {
    currentIndex = (currentIndex + 1) % carouselItems.length;
    updateCarousel();
}, 5000);

// Initialize
updateCarousel();