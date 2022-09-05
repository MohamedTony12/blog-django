const search_btn = document.querySelector('.search');
const search_input = document.querySelector('#search-input')
const overlay = document.querySelector('.overlay')


search_btn.addEventListener('click',()=>{
    console.log('work');
    search_input.classList.add('show-in')
    overlay.classList.add('show')
})
overlay.addEventListener('click',()=>{
    console.log('work');
    search_input.classList.remove('show-in')
    overlay.classList.remove('show')
})

