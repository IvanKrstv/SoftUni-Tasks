document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const inputForm = document.getElementById('input');
    const generateTextarea = inputForm.querySelector('textarea');

    const shopForm = document.getElementById('shop');
    const tbody = shopForm.querySelector('tbody');
    const resultTextarea = shopForm.querySelector('textarea');

    inputForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const furnitureList = JSON.parse(generateTextarea.value);

        furnitureList.forEach(furniture => {
            const row = document.createElement('tr');

            const imgCell = document.createElement('td');
            const img = document.createElement('img');
            img.src = furniture.img;
            imgCell.appendChild(img);

            const nameCell = document.createElement('td');
            const nameP = document.createElement('p');
            nameP.textContent = furniture.name;
            nameCell.appendChild(nameP);

            const priceCell = document.createElement('td');
            const priceP = document.createElement('p');
            priceP.textContent = furniture.price;
            priceCell.appendChild(priceP);

            const decCell = document.createElement('td');
            const decP = document.createElement('p');
            decP.textContent = furniture.decFactor;
            decCell.appendChild(decP);

            const checkboxCell = document.createElement('td');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkboxCell.appendChild(checkbox);

            row.appendChild(imgCell);
            row.appendChild(nameCell);
            row.appendChild(priceCell);
            row.appendChild(decCell);
            row.appendChild(checkboxCell);

            tbody.appendChild(row);
        });
    });

    shopForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const rows = Array.from(tbody.querySelectorAll('tr'));
        const boughtNames = [];
        let totalPrice = 0;
        let totalDecFactor = 0;
        let boughtCount = 0;

        rows.forEach(row => {
            const checkbox = row.querySelector('input[type="checkbox"]');

            if (checkbox && checkbox.checked && !checkbox.disabled) {
                const cells = row.querySelectorAll('td');
                const name = cells[1].textContent;
                const price = Number(cells[2].textContent);
                const decFactor = Number(cells[3].textContent);

                boughtNames.push(name);
                totalPrice += price;
                totalDecFactor += decFactor;
                boughtCount++;
            }
        });

        const avgDecFactor = boughtCount > 0
            ? totalDecFactor / boughtCount
            : 0;

        resultTextarea.value =
            `Bought furniture: ${boughtNames.join(', ')}\n` +
            `Total price: ${totalPrice}\n` +
            `Average decoration factor: ${avgDecFactor}`;
    });
}