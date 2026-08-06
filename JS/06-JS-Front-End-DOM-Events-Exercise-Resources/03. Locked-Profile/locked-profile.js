document.addEventListener('DOMContentLoaded', solve);

function solve() {
    document.querySelector('main').addEventListener('click', (e)=>{
        if(e.target.nodeName === "BUTTON"){
            const currentProfile = e.target.closest('.profile')
            const state = currentProfile.querySelector('input[name*="Locked"]:checked').getAttribute('id').slice(5).toLowerCase()
            
            if (state === 'unlock'){
                const hiddenFieldsEl = currentProfile.querySelector('.hidden-fields')

                if (hiddenFieldsEl.classList.contains('active')){
                    hiddenFieldsEl.classList.remove('active')
                    e.target.textContent = 'Show less'
                } else {
                    hiddenFieldsEl.classList.add('active')
                    e.target.textContent = 'Show more'
                }
            }

        }

    })
}