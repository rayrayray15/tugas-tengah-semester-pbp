// CODE FOR POP UP BELOW

const openModalButtons = document.querySelectorAll('[data-modal-target')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.popup.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.popup')
        closeModal(modal)
    })
})

function openModal(modal) {
    if (modal == null) {
        return
    }
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal) {
    if (modal == null) {
        return
    }
    modal.classList.remove('active')
    overlay.classList.remove('active')
    var parent = document.getElementById('body');
    var child = parent.getElementsByTagName('ul')[0];
    parent.removeChild(child);
}

// CODE FOR AJAX BELOW

var vaksinContainer = document.getElementById("popup")

var sinovacBtn = document.getElementById("sinovac");
var astrazenecaBtn = document.getElementById("astrazeneca");
var SinopharmBtn = document.getElementById("sinopharm");
var modernaBtn = document.getElementById("moderna");
var pfizerBtn = document.getElementById("pfizer");
var NovavaxBtn = document.getElementById("novavax");

sinovacBtn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/infovaksin/show_json');
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData["datas"], 0);
        console.log(ourData[0])
    };
    ourRequest.send();
})

astrazenecaBtn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/infovaksin/show_json');
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData["datas"], 1);
        // console.log(ourData[0])
    };
    ourRequest.send();
})

SinopharmBtn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/infovaksin/show_json');
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData["datas"], 2);
        // console.log(ourData[0])
    };
    ourRequest.send();
})

modernaBtn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/infovaksin/show_json');
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData["datas"], 3);
        // console.log(ourData[0])
    };
    ourRequest.send();
})

pfizerBtn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/infovaksin/show_json');
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData["datas"], 4);
        // console.log(ourData[0])
    };
    ourRequest.send();
})

NovavaxBtn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/infovaksin/show_json');
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData["datas"], 5);
        // console.log(ourData[0])
    };
    ourRequest.send();
})

let main = document.querySelector('.popup');
let mainTitle = document.querySelector('.title')
let mainHeader = document.querySelector('.popup-header');
let mainBody = document.querySelector('.popup-body');

function renderHTML(data, index) {
    
    // CODE FOR HEADER
    mainTitle.innerHTML = data[index].name;
    let closeButton = mainHeader.querySelector('button')
    closeButton.innerHTML = '&times;'
    
    // CODE FOR BODY

    let mainUl = document.createElement('ul');
    mainBody.appendChild(mainUl);
    
    // Syarat
    let syarat = document.createElement('h3');
    syarat.innerHTML = ('Syarat :');
    mainUl.appendChild(syarat);
    
    let syaratUl = document.createElement('ul');
    mainUl.appendChild(syaratUl);
    
    data[index].syarat.forEach(function(item){
        let syaratLi = document.createElement('li');
        let syaratlist =  document.createTextNode(item);
        syaratLi.appendChild(syaratlist);
        syaratUl.appendChild(syaratLi);
    });
    
    // Dosis dan Jadwal Pemberian
    
    let dosis = document.createElement('h3');
    dosis.innerHTML = ('Dosis dan Jadwal Pemberian :');
    mainUl.appendChild(dosis);
    
    let dosisUl = document.createElement('ul');
    mainUl.appendChild(dosisUl);
    
    let dosisLi = document.createElement('li');
    dosisLi.innerHTML = (data[index].dosis);
    dosisUl.appendChild(dosisLi);
    
    // Efek samping
    
    let efek = document.createElement('h3');
    efek.innerHTML = ('Efek Samping :');
    mainUl.appendChild(efek);
    
    let efekUl = document.createElement('ul');
    mainUl.appendChild(efekUl);
    
    data[index].efek.forEach(function(item) {
        let efekLi = document.createElement('li');
        let efeklist = document.createTextNode(item);
        efekLi.appendChild(efeklist);
        efekUl.appendChild(efekLi);
    })
    
}