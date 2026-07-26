function solve() {
  const inputEl = document.getElementById('input');
  const outputEl = document.getElementById('output');
  const text = inputEl.value.trim();

  if (!text) {
    outputEl.innerHTML = '';
    return;
  }

  const sentences = text.match(/[^.!?]+[.!?]?/g)?.map(s => s.trim()).filter(Boolean) || [];
  const paragraphs = [];

  for (let i = 0; i < sentences.length; i += 3) {
    paragraphs.push(sentences.slice(i, i + 3).join(' '));
  }

  outputEl.innerHTML = '';

  paragraphs.forEach(paragraphText => {
    const paragraphEl = document.createElement('p');
    paragraphEl.textContent = paragraphText;
    outputEl.appendChild(paragraphEl);
  });
}