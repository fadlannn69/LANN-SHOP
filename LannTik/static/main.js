document.body.style.backgroundColor = "black"
const judul1 = document.getElementById("judul1")
const judul2 = document.getElementById("judul2")
judul1.style.textAlign = "center"
judul2.style.textAlign = "center"
judul1.style.color = "lightblue"
judul2.style.color = "lightblue"


const drop = document.querySelector(".dropdown-menu")
drop.addEventListener("click",function(e){
  if(e.target.tagName === "A"){
    const Jenis = (e.target.innerText)
    fetch("http://127.0.0.1:8000/Barang/?Jenis=" + Jenis, {
      method : "GET",
      headers:{
        "Content-Type":"application/json",
      },
      mode:"cors"
    })
    .then(Response => Response.json())
    .then(j => {
      
      const tampil = document.querySelector(".card-container")
      tampil.innerHTML = j.map(item => cards(item)).join("")
    })
  }
})

document.addEventListener("click",function(e){
  if(e.target.classList.contains("modalpesanbutton")){
    const nama = e.target.id //ini berisi nama barang yang akan di pesan
    const harga = e.target.name
    const data = {
      Nama : nama,
      Harga : harga,
    }
    fetch("http://127.0.0.1:8000/Pesanan/",{
      method : "POST",
      headers:{
          "Content-Type":"application/json"
      },
      body: JSON.stringify(data)
  })
  .then(Response => Response.json())
  .then( hasil =>{
      console.log("berhasil" , hasil)
    })

  }
})



function cards(j){
  return `<div class="card" style="display:flex; flex-direction:column;width: 18rem;justify-content : center ; align-items:center; text-align : center">
  <img src="/data/${j.Gambar}" class="card-img-top">
    <h5 class="card-title">${j.Nama}</h5>
    <p class="card-text">RP : ${j.Harga}</p>
    <a href="#" class="btn btn-primary modalpesanbutton" id="${j.Nama}" name="${j.Harga}">PESAN</a>
    <br>
    <style>.card-img-top{ width: 200px;height: 150px;object-fit: cover;}</style>
    <style> .card-container{ display: flex;flex-wrap : wrap; gap: 10px;}</style>
  </div>
</div>`
}

