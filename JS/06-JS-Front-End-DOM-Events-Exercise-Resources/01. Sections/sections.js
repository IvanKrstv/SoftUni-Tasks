document.addEventListener('DOMContentLoaded', solve);

function solve() {
   const formEl = document.querySelector('#task-input')
   const contentEl = document.getElementById('content')

   formEl.addEventListener('submit', (e)=>{
      e.preventDefault()
      contentEl.innerHTML = ''

      const inputArr = document.querySelector('input[type="text"]').value.split(', ')
      // ["Section 1", "Section 2", ]
      
      for (const el of inputArr){
         const divEl = document.createElement('div')
         const pEl = document.createElement('p')

         divEl.append(pEl)

         pEl.textContent = el
         pEl.style.display = 'none'

         divEl.addEventListener('click', (e)=>{
            e.target.querySelector('p').style.display = 'block'
         })

         contentEl.append(divEl)

      }
   })
   
}