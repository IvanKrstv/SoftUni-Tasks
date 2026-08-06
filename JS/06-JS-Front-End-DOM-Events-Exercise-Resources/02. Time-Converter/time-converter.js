document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const daysInputEl = document.getElementById('days-input');
    const hoursInputEl = document.getElementById('hours-input');
    const minutesInputEl = document.getElementById('minutes-input');
    const secondsInputEl = document.getElementById('seconds-input');

    const timeChanges = {
        days: 86400,
        hours: 3600,
        minutes: 60,
        seconds: 1
    };

    const formsArr = Array.from(document.querySelectorAll('form'));

    for (const form of formsArr) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const currentInputEl = e.target.querySelector('input[type="number"]');
            const currentValue = Number(currentInputEl.value);

            if (currentValue < 0) return;

            const multiplier = timeChanges[currentInputEl.id.split('-')[0]] ?? 1;

            updateValues(currentValue * multiplier);
        });
    }

    function updateValues(secondsAmount) {
        daysInputEl.value = Number(secondsAmount / timeChanges.days).toFixed(2);
        hoursInputEl.value = Number(secondsAmount / timeChanges.hours).toFixed(2);
        minutesInputEl.value = Number(secondsAmount / timeChanges.minutes).toFixed(2);
        secondsInputEl.value = Number(secondsAmount / timeChanges.seconds).toFixed(2);
    }
}