document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const encodeFormEl = document.getElementById('encode')
    const decodeFormEl = document.getElementById('decode')

    encodeFormEl.addEventListener('submit', (e) => {
        e.preventDefault()

        const message = encodeFormEl.querySelector('textarea').value;
        
        const encodedMessage = Array.from(message).map(char => String.fromCharCode(char.charCodeAt(0) + 1)).join('');

        encodeFormEl.querySelector('textarea').value = '';
        decodeFormEl.querySelector('textarea').value = encodedMessage;
    });

    decodeFormEl.addEventListener('submit', (e) => {
        e.preventDefault()

        const encodedMessage = decodeFormEl.querySelector('textarea').value;
        const decodedMessage = Array.from(encodedMessage).map(char => String.fromCharCode(char.charCodeAt(0) - 1)).join('');

        decodeFormEl.querySelector('textarea').value = decodedMessage;
    })
}