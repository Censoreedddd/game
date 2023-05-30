var buttonsPlus = Array.from(document.getElementsByClassName("add"));

for (let btnPlus of buttonsPlus) {
  btnPlus.addEventListener("click", function () {
    btnPlus.nextElementSibling.innerHTML++;
  });
  totalPrice();
}

var buttonsMinus = Array.from(document.getElementsByClassName("minus"));

for (let i = 0; i < buttonsMinus.length; i++) {
  buttonsMinus[i].addEventListener("click", function () {
    if (buttonsMinus[i].previousElementSibling.innerText > 0) {
      buttonsMinus[i].previousElementSibling.innerText--;
      totalPrice();
    }
  });
}

let trash = Array.from(document.getElementsByClassName("fa-trash-alt"));

for (let trsh of trash) {
  trsh.addEventListener("click", function () {
    trsh.parentNode.remove();
  });
}

let hearts = Array.from(document.getElementsByClassName("fa-heart"));

for (let heart of hearts) {
  heart.addEventListener("click", function () {
    if (heart.style.color === "grey") {
      heart.style.color = "red";
    } else {
      heart.style.color = "grey";
    }
  });
}
// Calculate the total price
function totalPrice() {
  // Get the product price
  let productPrice = document.getElementsByClassName('price');
  // Get the product quantity
  let productQuantity = document.getElementsByClassName('qte');
  // Initilize the sum
  let sum = 0;
  for (let i = 0; i < productPrice.length; i++) {
    sum += productPrice[i].innerText * productQuantity[i].innerText;
  }
  document.getElementById('totalp').innerText = sum;
}