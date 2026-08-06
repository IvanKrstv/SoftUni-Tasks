document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const buttonEl = document.getElementById('convert')
    const ouputFieldEl = document.getElementById('outputDistance')

    const values = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    };

    buttonEl.addEventListener('click', (e)=>{
        const inputValue = document.getElementById('inputDistance').value

        if (inputValue === '' || Number(inputValue) < 0) return

        const inputUnitsEl = document.getElementById('inputUnits');
        const outputUnitsEl = document.getElementById('outputUnits');

        const fromUnit = inputUnitsEl.value;
        const toUnit = outputUnitsEl.value;

        ouputFieldEl.value = (Number(inputValue * values[fromUnit] / values[toUnit])).toFixed(2)
    })
}