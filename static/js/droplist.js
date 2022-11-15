let myDropdown = document.getElementsByClassName('dropdown-toggle');
for (let i = 0; i < myDropdown.length; i++) {
    myDropdown[i].addEventListener('click', function () {
        let el = this.nextElementSibling;
        el.style.display = el.style.display === 'block' ? 'none' : 'block';
    });
}