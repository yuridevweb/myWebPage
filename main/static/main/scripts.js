// Modal element
let modal = document.getElementById('ProjectInfo');
//Modal open btn
let modalBtn = document.getElementsByClassName('modalBtn');
//Modal close btn
let closeBtn = document.getElementById('closeBtn');
//Listen for outside click
window.addEventListener('click', outsideClick);

modalBtn.addEventListener('click', modalOpen);
closeBtn.addEventListener('click', modalClose);

function modalOpen() {
  modal.style.display = 'block';
}
function modalClose() {
  modal.style.display = 'none';
}

function outsideClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}