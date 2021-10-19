const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)
const alertBox = document.getElementById('alert-box')
Dropzone.autoDiscover = false
const myDropzone = new Dropzone('#my-dropzone', {
    url: 'reports/upload/',
    init: function(){
        this.on('sending', function(file, xhr, formData){
            console.log('sending...')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function(file, response){
            console.log(response)
            const ex = response.ex
            if(ex){
                alertBox.innerHTML = `
                    <div role="alert" class="alert alert-danger">
                        File already exists.
                    </div>
                `
            }else{
                 alertBox.innerHTML = `
                    <div role="alert" class="alert alert-success">
                        Your file has been uploaded.
                    </div>
                `
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.csv'
})