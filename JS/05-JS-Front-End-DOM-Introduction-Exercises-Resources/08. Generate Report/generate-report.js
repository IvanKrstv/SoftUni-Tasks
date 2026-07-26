function solve() {
    const headers = Array.from(document.querySelectorAll('th'));
    const rows = Array.from(document.querySelectorAll('tbody tr'));
    const output = document.getElementById('output');

    const selectedColumns = headers
        .map((header, index) => {
            const checkbox = header.querySelector('input[type="checkbox"]');

            return checkbox && checkbox.checked
                ? { name: checkbox.name, index }
                : null;
        })
        .filter(Boolean);

    const report = rows.map(row => {
        const cells = Array.from(row.cells);
        const entry = {};

        selectedColumns.forEach(({ name, index }) => {
            const cell = cells[index];
            entry[name] = cell ? cell.textContent.trim() : '';
        });

        return entry;
    });

    output.value = JSON.stringify(report);
}