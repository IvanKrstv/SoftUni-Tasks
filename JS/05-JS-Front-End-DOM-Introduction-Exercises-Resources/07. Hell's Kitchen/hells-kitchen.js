function solve() {
    const inputEl = document.querySelector('textarea');
    const bestRestaurantSpanEl = document.querySelector('#bestRestaurant span');
    const bestRestaurantParagraphEl = document.querySelector('#bestRestaurant p');
    const workersSpanEl = document.querySelector('#workers span');
    const workersParagraphEl = document.querySelector('#workers p');

    const inputText = inputEl.value.trim();

    if (!inputText) {
        bestRestaurantSpanEl.textContent = '';
        bestRestaurantParagraphEl.textContent = '';
        workersSpanEl.textContent = '';
        workersParagraphEl.textContent = '';
        return;
    }

    const restaurantsInfo = JSON.parse(inputText);
    const restaurants = [];

    for (const restaurantInfo of restaurantsInfo) {
        const [restaurantName, workersPart] = restaurantInfo.split(/\s-\s/);
        const workers = workersPart
            .split(/\s*,\s*/)
            .map(workerInfo => {
                const lastSpaceIndex = workerInfo.lastIndexOf(' ');
                const name = workerInfo.slice(0, lastSpaceIndex);
                const salary = Number(workerInfo.slice(lastSpaceIndex + 1));

                return { name, salary };
            });

        const existingRestaurant = restaurants.find(r => r.name === restaurantName);

        if (existingRestaurant) {
            existingRestaurant.workers.push(...workers);
        } else {
            restaurants.push({ name: restaurantName, workers });
        }
    }

    const restaurantResults = restaurants.map(restaurant => {
        const salaries = restaurant.workers.map(worker => worker.salary);

        return {
            name: restaurant.name,
            workers: restaurant.workers,
            averageSalary: salaries.reduce((sum, salary) => sum + salary, 0) / salaries.length,
            bestSalary: Math.max(...salaries)
        };
    });

    if (!restaurantResults.length) {
        bestRestaurantSpanEl.textContent = '';
        bestRestaurantParagraphEl.textContent = '';
        workersSpanEl.textContent = '';
        workersParagraphEl.textContent = '';
        return;
    }

    let bestRestaurant = restaurantResults[0];

    for (let i = 1; i < restaurantResults.length; i++) {
        const restaurant = restaurantResults[i];

        if (restaurant.averageSalary > bestRestaurant.averageSalary) {
            bestRestaurant = restaurant;
        }
    }

    const summaryText = `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.averageSalary.toFixed(2)} Best Salary: ${bestRestaurant.bestSalary.toFixed(2)}`;
    const workersText = [...bestRestaurant.workers]
        .sort((a, b) => b.salary - a.salary)
        .map(worker => `Name: ${worker.name} With Salary: ${worker.salary}`)
        .join(' ');

    bestRestaurantSpanEl.textContent = summaryText;
    bestRestaurantParagraphEl.textContent = summaryText;
    workersSpanEl.textContent = workersText;
    workersParagraphEl.textContent = workersText;
}
