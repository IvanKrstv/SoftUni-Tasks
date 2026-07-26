function solve() {
    const inputEl = document.getElementById('input');
    const selectToEl = document.getElementById('selectMenuTo');
    const resultEl = document.getElementById('result');

    const decimalNumber = Number(inputEl.value);
    const target = selectToEl.value;

    if (target === 'binary') {
        resultEl.value = decimalNumber.toString(2);
    } else if (target === 'hexadecimal') {
        resultEl.value = decimalNumber.toString(16).toUpperCase();
    } else {
        resultEl.value = '';
    }
}