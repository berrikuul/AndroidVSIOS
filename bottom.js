const goTopBtn = document.querySelector(".go-top");

goTopBtn.addEventListener('click', goTop);
window.addEventListener('scroll', trackScroll);

function trackScroll() {
  const offset = window.pageYOffset;
  const coords = document.documentElement.clientHeight/2;
  if (offset > coords) {
    goTopBtn.classList.add('go-top--show');
  } else {
    goTopBtn.classList.remove('go-top--show');
  }

}


function goTop() {
  if(window.pageYOffset > 0) {
    window.scrollBy(0, -75);
    setTimeout(goTop, 0);
  }
}

