/* jshint esversion: 11, jquery: true */

document.onreadystatechange = function () {
  let lastScrollPosition = 0;
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', function (e) {
    lastScrollPosition = window.scrollY;
      
    if (lastScrollPosition > 50)
      navbar.classList.add('navbar-dark');
    else
      navbar.classList.remove('navbar-dark');
  });
};