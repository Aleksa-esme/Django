'use strict';
let goToTopEl = document.querySelector('#goToTop');
window.addEventListener('scroll', function(){
    if (window.pageYOffset > 500) {
        goToTopEl.classList.remove('scale-out-center');
        goToTopEl.classList.add('scale-up-center');
        goToTopEl.style.display = 'block';
    } else {
        goToTopEl.classList.remove('scale-up-center');
        goToTopEl.classList.add('scale-out-center');
        goToTopEl.style.display = 'none';
    }
});

//getElementById('goToTop');