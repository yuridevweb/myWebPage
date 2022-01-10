// Modal element
let modal = document.getElementById('ProjectInfo');
function modalOpen() {
  modal.style.display = 'block';
}
function modalClose() {
  modal.style.display = 'none';
}
//Listen for outside click
window.addEventListener('click', outsideClick);

function outsideClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";

}
