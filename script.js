function toggleMenu() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active');
}

// Check if user is logged in and show or hide the product listing link
document.addEventListener('DOMContentLoaded', () => {
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
    const listProductSection = document.getElementById('list-product');
    const listProductNav = document.getElementById('list-product-nav');

    if (isLoggedIn) {
        listProductSection.style.display = 'block';
        listProductNav.style.display = 'block';
    } else {
        listProductSection.style.display = 'none';
        listProductNav.style.display = 'none';
    }
});

function setLoginStatus(status) {
    localStorage.setItem('isLoggedIn', status);
}
