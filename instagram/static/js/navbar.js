let Icons = document.querySelectorAll('.fas')
let current = 0;

function selectIcon(index) {
    Icons[current].classList.remove('active');
    current = index;
    Icons[current].classList.add('active');
}