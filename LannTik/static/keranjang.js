document.body.style.backgroundColor = "black"
const judul1 = document.getElementById("judul1")
const judul2 = document.getElementById("judul2")
judul1.style.textAlign = "center"
judul2.style.textAlign = "center"
judul1.style.color = "lightblue"
judul2.style.color = "lightblue"

fetch("http://127.0.0.1:8000/Pesanan", {
    method : "GET",
    headers:{
      "Content-Type":"application/json",
    },
    mode:"cors"
  })
  .then(Response => Response.json())
  .then( m => {
    
    const tampil = document.querySelector(".keranjang")
    tampil.innerHTML = m.map(item => accordion(item)).join("")
  })

function accordion(m){
    return `
        <li class="list-group-item" > NAMA BARANG : ${m.Nama} <br> HARGA BARANG : ${m.Harga}</li>
    `
}

// ketika tombol pesan email di klik
document.addEventListener("click",function(e){
  if(e.target.classList.contains("buttoon")){
    fetch("http://127.0.0.1:8000/user", {
      method : "GET",
      headers:{
        "Content-Type":"application/json",
      },
      mode : "cors"
    })
    .then(Response => Response.json())
    .then( u => { 
      fetch("http://127.0.0.1:8000/Pesanan", {
        method : "GET",
        headers:{
          "Content-Type":"application/json",
        },
        mode:"cors"
      })
      .then(Response => Response.json())
      .then( m => {
        const nbarang = m[0].Nama
        const hbarang = m[0].Harga
      // response berisi  semua pesanan
        const nama = u[0].Nama
        const email = u[0].Email
        const Alamat = u[0].Alamat
        const data = {
        email : email,
        subject : nama,
        content : `ALAMAT : ${Alamat}\n
        PESANAN : ${nbarang}\n
        HARGA : ${hbarang}
        `
        }
        fetch("http://127.0.0.1:8000/Pesanan/send-email/", {
          method : "POST",
          headers:{
            "Content-Type":"application/json",
          },
        body : JSON.stringify(data)
        })
        .then(Response => Response.json())
        .then( p => {
          console.log("owatta")
        })
      
    })//ini tutup kurung response get
    
  })
  }
})

