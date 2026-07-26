function toggle() {
    const buttonEl = document.querySelector('.button')
    const extraTextEl = document.querySelector('#extra')

    switch (buttonEl.textContent) {
        case "More":
            buttonEl.textContent = 'Less';
            extraTextEl.style.display = 'block';
            break;

        case "Less":
            buttonEl.textContent = 'More';
            extraTextEl.style.display = 'none';
            break;

        default:
            break;
    }


}