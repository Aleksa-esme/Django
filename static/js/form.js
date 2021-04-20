//проверка пусто ли в input при отправке формы

'use strict';
let formEl = document.querySelector('form');
let firstInput = document.getElementById('first_input');
let secondInput = document.getElementById('second_input');
let thirdInput = document.getElementById('third_input');

formEl.addEventListener('submit', function(event){
    let firstInputEmpty = firstInput.value === '';
    let secondInputEmpty = secondInput.value === '';
    let thirdInputEmpty = thirdInput.value === '';

    if (firstInputEmpty) {
        firstInput.style.borderColor = 'red';
    }
    if (secondInputEmpty) {
        secondInput.style.borderColor = 'red';
    }
    if (thirdInputEmpty) {
        thirdInput.style.borderColor = 'red';
    }
    if (firstInputEmpty || secondInputEmpty || thirdInputEmpty) {
        event.preventDefault();
    }
});