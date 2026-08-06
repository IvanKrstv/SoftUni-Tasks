document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const formEl = document.querySelector('form');
    const menuEL = document.getElementById('menu');

    formEl.addEventListener('submit', (e) => {
        e.preventDefault();

        const textField = document.getElementById('newItemText').value;
        const valueField = document.getElementById('newItemValue').value;

        const newEl = document.createElement('option');
        newEl.textContent = textField;
        newEl.value = valueField;

        menuEL.append(newEl);

        document.getElementById('newItemText').value = '';
        document.getElementById('newItemValue').value = '';
    });
}