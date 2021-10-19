const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBody = document.getElementById('modal-body')
const reportForm = document.getElementById('report-form')
const alertBox = document.getElementById('alert-box')
console.log(reportBtn)
console.log(img)

const reportName = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
        <div role="alert" class="alert alert-${type}">
            ${msg}
         </div>
    `
}
console.log(reportName)
console.log(reportRemarks)
console.log(csrf)


if (img){
    reportBtn.classList.remove('invisible')
}
console.log(img.src)
reportBtn.addEventListener('click', ()=>{

    console.log('clicked')
    img.setAttribute('class', 'w-100')
    modalBody.prepend(img)
    reportForm.addEventListener('submit', e=>{
        e.preventDefault()
        const formData = new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('name', reportName)
        formData.append('remarks', reportRemarks)
        formData.append('image', img.src)

        $.ajax({
            type: 'POST',
            url: '/reports/save/',
            data: formData,
            success: function(response){
                console.log(response)
                handleAlerts('success', 'Report created successfully.')
            },
            error: function(error){
                console.log(error)
                  handleAlerts('danger', 'Sorry...something went wrong.')
            },
            processData: false,
            contentType: false,
        })
    })
})