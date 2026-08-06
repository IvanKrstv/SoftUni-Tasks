document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const formEl = document.getElementById('solutionCheck');
    const tableEl = formEl.querySelector('table');
    const tbodyEl = tableEl.querySelector('tbody');
    const sizeSelectEl = document.getElementById('size');
    const messageEl = document.getElementById('check');

    function buildGrid(size) {
        tbodyEl.innerHTML = '';

        for (let row = 0; row < size; row += 1) {
            const trEl = document.createElement('tr');

            for (let col = 0; col < size; col += 1) {
                const tdEl = document.createElement('td');
                const inputEl = document.createElement('input');

                inputEl.type = 'number';
                inputEl.step = '1';
                inputEl.min = '1';
                inputEl.max = size;
                inputEl.required = true;

                tdEl.appendChild(inputEl);
                trEl.appendChild(tdEl);
            }

            tbodyEl.appendChild(trEl);
        }

        messageEl.textContent = '';
        tableEl.style.border = '1px solid #234465';
    }

    function isValidSudoku(size) {
        const inputs = Array.from(tbodyEl.querySelectorAll('input'));
        const values = inputs.map((input) => input.value.trim());

        if (values.some((value) => value === '')) {
            return false;
        }

        const numbers = values.map((value) => Number(value));

        for (let row = 0; row < size; row += 1) {
            const rowValues = [];
            for (let col = 0; col < size; col += 1) {
                const value = numbers[row * size + col];
                if (value < 1 || value > size || rowValues.includes(value)) {
                    return false;
                }
                rowValues.push(value);
            }
        }

        for (let col = 0; col < size; col += 1) {
            const colValues = [];
            for (let row = 0; row < size; row += 1) {
                const value = numbers[row * size + col];
                if (value < 1 || value > size || colValues.includes(value)) {
                    return false;
                }
                colValues.push(value);
            }
        }

        if (Number.isInteger(Math.sqrt(size))) {
            const blockSize = Math.sqrt(size);
            for (let blockRow = 0; blockRow < blockSize; blockRow += 1) {
                for (let blockCol = 0; blockCol < blockSize; blockCol += 1) {
                    const blockValues = [];
                    for (let row = blockRow * blockSize; row < (blockRow + 1) * blockSize; row += 1) {
                        for (let col = blockCol * blockSize; col < (blockCol + 1) * blockSize; col += 1) {
                            const value = numbers[row * size + col];
                            if (value < 1 || value > size || blockValues.includes(value)) {
                                return false;
                            }
                            blockValues.push(value);
                        }
                    }
                }
            }
        }

        return true;
    }

    sizeSelectEl.addEventListener('change', () => {
        buildGrid(Number(sizeSelectEl.value));
    });

    formEl.addEventListener('submit', (e) => {
        e.preventDefault();

        if (isValidSudoku(Number(sizeSelectEl.value))) {
            tableEl.style.border = '2px solid green';
            messageEl.textContent = 'Success!';
        } else {
            tableEl.style.border = '2px solid red';
            messageEl.textContent = 'Keep trying...';
        }
    });

    formEl.addEventListener('reset', () => {
        messageEl.textContent = '';
        tableEl.style.border = '1px solid #234465';
    });

    buildGrid(Number(sizeSelectEl.value));
}