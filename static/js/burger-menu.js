
const burgerButton = document.getElementById('iconNavbarSidenav')
const mobileMenu = document.getElementById('sidenav-main')
const body = document.getElementsByTagName('body')[0]

burgerButton.addEventListener('click', ()=>{

    if(body.classList.contains('g-sidenav-pinned')){
        body.classList.remove('g-sidenav-pinned')
        mobileMenu.classList.remove('bg-white')
    }else{
        body.classList.add('g-sidenav-pinned')
        mobileMenu.classList.add('bg-white')
    }
})

