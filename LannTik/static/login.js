// style login
document.body.style.backgroundColor = "black"
const judul1 = document.getElementById("judul1")
const judul2 = document.getElementById("judul2")
judul1.style.textAlign = "center"
judul2.style.textAlign = "center"
judul1.style.color = "lightblue"
judul2.style.color = "lightblue"
// style login

// logic login
const button = document.querySelector(".Kirim")
button.addEventListener("click",function(event){
    event.preventDefault()
    // const  login = document.querySelectorAll(".form-login")
    // nama
    const Nama = document.querySelector(".username").value
    // email
    const Email = document.querySelector(".gmail").value
    // alamat
    const Alamat = document.querySelector(".address").value
    
    // model utama
    const data = {
        Nama : Nama,
        Email : Email,
        Alamat : Alamat
    }
    fetch("http://127.0.0.1:8000/user/",{
        method : "POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify(data)
    })
    .then(Response => Response.json())
    .then( hasil =>{
        console.log(hasil)
        window.location.href = "main.html"  
})
})
function loadingButton(){
    return`<button class="kirim" type="button" disabled>
    <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
    <span role="status">Loading...</span>
    </button>
    `
}

function peringatan1(){
    return`<div class="alert alert-primary peringatan1" role="alert">
    Tunggu bentar yaa :)
    </div>`
}
function peringatan2(){
    return`<div class="alert alert-primary peringatan1" role="alert">
    Hak Akses Diberikan:)
    </div>`
}
// logic login