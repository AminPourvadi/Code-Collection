const accordionButtons = document.querySelectorAll('button');
            
accordionButtons.forEach(button => {
    button.addEventListener('click', function () {
        const targetId = button.getAttribute('data-target');
        const content = document.getElementById(`accordion-collapse-body-${targetId}`);
        const isExpanded = button.getAttribute('aria-expanded') === 'true';
            
        // Toggle visibility with animation
        content.classList.toggle('hidden', isExpanded);
        content.classList.toggle('max-h-0', isExpanded);
        content.classList.toggle('max-h-96', !isExpanded); // Adjust the max height as needed
            
        // Toggle aria-expanded
        button.setAttribute('aria-expanded', !isExpanded);
    });
});
