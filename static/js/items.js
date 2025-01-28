document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', () => {
        const content = document.querySelector(button.getAttribute('data-target'));
        const icon = button.querySelector('svg');

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
            icon.classList.remove('rotate-180');
        } else {
            document.querySelectorAll('.accordion-content').forEach(c => c.style.maxHeight = null);
            document.querySelectorAll('.accordion-button svg').forEach(i => i.classList.remove('rotate-180'));
            content.style.maxHeight = content.scrollHeight + 'px';
            icon.classList.add('rotate-180');
        }
    });
});