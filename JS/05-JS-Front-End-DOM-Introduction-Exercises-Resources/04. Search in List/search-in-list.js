function solve() {
   const listTownsEl = document.querySelectorAll('#towns li')
   const inputEl = document.getElementById('searchText').value
   const resultEl = document.getElementById('result')

   let matches = 0

   for (const townEl of listTownsEl){
      let town = townEl.textContent.toLowerCase()

      if (town.includes(inputEl.toLowerCase())){
         matches++
         townEl.style.fontWeight = 'bold'
         townEl.style.textDecoration = 'underline'
      } else {
         townEl.style.fontWeight = ''
         townEl.style.textDecoration = ''
      }
   }

   resultEl.textContent = `${matches} matches found`
}  