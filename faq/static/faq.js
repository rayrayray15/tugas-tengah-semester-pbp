const accordionItemHeaders = document.querySelectorAll(".accordion-item-header");

accordionItemHeaders.forEach(accordionItemHeader =>{
    accordionItemHeader.addEventListener("click", event => {
        const currentlyActiveAccordionItemHeader = document.querySelector(".accordion-item-header.active");
        if (currentlyActiveAccordionItemHeader && currentlyActiveAccordionItemHeader !== accordionItemHeader) {
            currentlyActiveAccordionItemHeader.classList.toggle("active");
            currentlyActiveAccordionItemHeader.nextElementSibling.style.maxHeight = 0;
        }

        accordionItemHeader.classList.toggle("active");
        const accordionItemBody = accordionItemHeader.nextElementSibling;
        if (accordionItemHeader.classList.contains("active")){
            accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
        }
        else {
            accordionItemBody.style.maxHeight = 0;
        }
    });
});

const alertBox = document.getElementById('alert-box')
const faqForm = document.getElementById('faq-form')
const qs = document.getElementById('qs')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

const url = "qs"

const handleAlerts = (type, text) =>{
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                            ${text}
                            </div>`
}

faqForm.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('qs', qs.value)

    $.ajax({
        type: 'POST',
        url: url,
        data: fd,
        success: function(response){
            console.log(response)
            handleAlerts('success','Pertanyaan Anda Berhasil Dikirim!')
            setTimeout(()=>{
                alertBox.innerHTML=""
                qs.value =""
            }, 3000)
        },
        error: function(error){
            console.log(error)
            handleAlerts('danger', 'Ulangi lagi..')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})