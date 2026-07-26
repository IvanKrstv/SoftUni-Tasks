function solve() {
   const inputEl = document.getElementById('searchField').value.toLowerCase()
   const resultEl = document.getElementById('result')
   const listStudents = document.querySelectorAll('.container tbody tr')

   for(const studentEl of listStudents){
      const studentInfo = studentEl.innerText.toLowerCase()

      if (inputEl && studentInfo.includes(inputEl)){
         studentEl.classList.add('select')
      } else {
         studentEl.classList.remove('select')
      }
      
   }
   
}