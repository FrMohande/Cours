// YOUR NAME HERE

// === constants ===
const MAX_QTY = 9
const productIdKey = 'product';
const orderIdKey = 'order';
const inputIdKey = 'qte';

// === global variables  ===
// the total cost of selected products
var total = 0;

// function called when page is loaded, it performs initializations 
var init = function () {
  createShop()
	
	var filter = document.getElementById('filter')
	filter.addEventListener('keyup', searchProduct)

}
window.addEventListener('load', init)

// usefull functions

/*
* create and add all the div.produit elements to the div#boutique element
* according to the product objects that exist in 'catalog' variable
*/
var createShop = function () {
  var shop = document.getElementById('boutique')
	for (var i = 0; i < catalog.length; i++) {
  		shop.appendChild(createProduct(catalog[i], i))
	}
}

/*
* create the div.produit elment corresponding to the given product
* The created element receives the id "index-product" where index is replaced by param's value
* @param product (product object) = the product for which the element is created
* @param index (int) = the index of the product in catalog, used to set the id of the created element
*/
var createProduct = function (product, index) {
	// build the div element for product
  var block = document.createElement('div')
	block.className = 'produit';
	// set the id for this product
  block.id = index + '-' + productIdKey
	// build the h4 part of 'block'
	block.appendChild(createBlock('h4', product.name))
	
	// /!\ should add the figure of the product... does not work yet... /!\ 
	block.appendChild(createFigureBlock(product))

	// build and add the div.description part of 'block' 
	block.appendChild(createBlock('div', product.description, 'description'))
	// build and add the div.price part of 'block'
	block.appendChild(createBlock('div', product.price, 'prix'))
	// build and add control div block to product element
	block.appendChild(createOrderControlBlock(index))
	return block
}

/* return a new element of tag 'tag' with content 'content' and class 'cssClass'
 * @param tag (string) = the type of the created element (example : "p")
 * @param content (string) = the html wontent of the created element (example : "bla bla")
 * @param cssClass (string) (optional) = the value of the 'class' attribute for the created element
 */
var createBlock = function (tag, content, cssClass) {
  var element = document.createElement(tag)
	if (cssClass != undefined) {
  element.className = cssClass
	}
  element.innerHTML = content
	return element
}

/*
* builds the control element (div.controle) for a product
* @param index = the index of the considered product
*
* TODO : add the event handling,
*   /!\  in this version button and input do nothing  /!\
*/
function createOrderControlBlock (index) {
  var control = document.createElement('div')
	control.className = 'controle';

	// create input quantity element
  var input = document.createElement('input')
	input.id = index + '-' + inputIdKey
	input.type = 'number';
  input.step = '1';
  input.value = '0';
  input.min = '0';
  input.max = MAX_QTY.toString()
	input.addEventListener('keyup', checkInput)

	// add input to control as its child
	control.appendChild(input)
	
	// create order button
	var button = document.createElement('button')
	button.className = 'commander'
	button.id = index + '-' + orderIdKey
	button.addEventListener('click', createAchats)
	// add control to control as its child
	control.appendChild(button)
	

	// the built control div node is returned
	return control
}

/*
* create and return the figure block for this product
* see the static version of the project to know what the <figure> should be
* @param product (product object) = the product for which the figure block is created
*
* TODO : write the correct code
*/
var createFigureBlock = function (product) {
	// this is absolutely not the correct answer !
	// TODO
  var figure = document.createElement('figure')
	var img = document.createElement('img')
	img.alt = product.description
	img.src = product.image

	figure.appendChild(img)

  return figure
}

function searchProduct () {
  var content = this.value 
	var productName 
	var productBlock = document.getElementsByClassName('produit')
	for (var i = 0; i < catalog.length; i++) {
  productName = catalog[i].name
		if (productName.indexOf(content) > -1) {
  productBlock[i].style.display = 'inline-block';
} else {
  productBlock[i].style.display = 'none';
}
}
}

function checkInput () {
  var value = parseInt(this.value)
	var min = parseInt(this.min)
	var max = parseInt(this.max) 
	if (typeof value === 'number') {
  this.value = value 
	} else {
  this.value = '0'
}
  if ((min > value) || (value > max)) {
  this.value = '0';
}
}
function createAchats () {
  var achats = document.getElementById('achats')
	var achatsFils = achats.childNodes
	var temp = this.id 
	var id = temp.replace('-order', '')
	var dejaAjouts = false 

	for (var i = 0; i < achatsFils.length; i++) {
  temp = achatsFils[i].id.substring(0, 1) 
		if (id == temp) {
  dejaAjouts = true 
		}
}
  if (dejaAjouts) {
  modifAchat(id)
	} else {
  achats.appendChild(createAchat(id))
	}
  modifMontant(total) 

}

function createAchat (id) {
  var achat = document.createElement('div') 
	var qte = document.getElementById(id + '-qte')
	if (qte.value > 0) {
  achat.className = 'achat';
  achat.id = id + '-achat';
  achat.appendChild(createFigureBlock(catalog[id])) 
		achat.appendChild(createBlock('h4', catalog[id].name))


		achat.appendChild(createBlock('div', qte.value, 'quantite'))
		achat.appendChild(createBlock('div', catalog[id].price, 'prix'))

		var controle = document.createElement('div')
		controle.className = 'controle';
  var button = document.createElement('button') 
		button.className = 'retirer';
  button.id = id + '-remove';
  controle.appendChild(button) 
		button.addEventListener('click', removeAchat) 

		achat.appendChild(controle) 
		total = total + ((parseInt(qte.value)) * (parseInt(catalog[id].price))) 
		return achat 
	}
}

function modifAchat (id) {
  var achat = document.getElementById(id + '-achat')
	var achatQte = achat.getElementsByClassName('quantite')
	var qte = document.getElementById(id + '-qte')
	var ancienSomme = parseInt(catalog[id].price) * parseInt(achatQte[0].innerHTML) 
	achatQte[0].innerHTML = parseInt(achatQte[0].innerHTML) + parseInt(qte.value) 

	var newSomme = parseInt(catalog[id].price) * parseInt(achatQte[0].innerHTML) 
	total = total + newSomme - ancienSomme 
}
function removeAchat () {
  var achats = document.getElementById('achats')
	var id = this.id.replace('-remove', '') ;
  var achat = document.getElementById(id + '-achat')
	var qte = achat.querySelector('.quantite')
	var prix = achat.querySelector('.prix') 
	var calcul = parseInt(qte.innerHTML) * parseInt(prix.innerHTML) 
	total = Math.abs(total - calcul) 

	modifMontant(total) 
	achats.removeChild(achat) 
}
function modifMontant () {
  var montant = document.getElementById('montant')
	montant.innerHTML = total
}
fmmp;