function solve() {
  const textEl = document.getElementById('text').value.toLowerCase().split(' ')
  const conventionEl = document.getElementById('naming-convention').value
  const resultEl = document.getElementById('result')

  switch (conventionEl) {
    case "Pascal Case":
      resultEl.textContent = textEl.map(word => word[0].toUpperCase() + word.slice(1)).join('')
      break;

    case "Camel Case":
      resultEl.textContent = textEl[0] + textEl.slice(1).map(word => word[0].toUpperCase() + word.slice(1)).join('')
      break;

    default:
      resultEl.textContent = 'Error!'
      break;
  }
  
}