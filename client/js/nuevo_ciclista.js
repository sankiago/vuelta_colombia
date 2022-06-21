function mostrarMenuArchivo() {
  const inputArchivo = document.querySelector(".columna1 input");
  inputArchivo.click();
}

const leerURLDesdeArchivo = (archivo) => {
  return new Promise((responder, rechazar) => {
    const reader = new FileReader();
    reader.onload = (e) => responder(e.target.result);
    reader.onerror = (e) => rechazar(e);
    reader.readAsDataURL(archivo);
  });
};

async function renderizarImagen() {
  const URLDeArchivo = await leerURLDesdeArchivo(this.files[0]);
  const fotografia = document.querySelector("main img");
  fotografia.setAttribute("src", URLDeArchivo);
}

async function crearCiclista() {
  const inputArchivoNodo = document.querySelector(".columna1 input");
  const nombre = document.querySelector(".text_field#nombre").value;
  const apellido = document.querySelector(".text_field#apellido").value;
  const archivosSubidosPorElUsuario = inputArchivoNodo.files;
  if(archivosSubidosPorElUsuario.length == 0){
    alert('La foto del ciclista es obligatoria 😳🙏')
    return undefined
  }
  const link_imagen = await leerURLDesdeArchivo(archivosSubidosPorElUsuario[0]);
  const id = document.querySelector(".text_field#id").value;
  const pais = document.querySelector(".text_field#pais").value;
  const fechaDeNacimiento = document.querySelector(
    ".text_field#fechaDeNacimiento"
  ).value;
  const equipo = document.querySelector(".text_field#equipo").value;
  const rankingUCI = document.querySelector(".text_field#rankingUCI").value;
  const respuesta = await eel.crear_ciclista(
    nombre,
    apellido,
    link_imagen,
    id,
    pais,
    fechaDeNacimiento,
    equipo,
    rankingUCI,
  )();
    console.log(respuesta);
    debugger
    if(respuesta){
        alert(respuesta)
    }else{
        location.replace('./ciclistas.html')
    }

}

const main = async () => {
  const botonAgregarFoto = document.querySelector("label");
  botonAgregarFoto.addEventListener("click", mostrarMenuArchivo);

  const inputArchivo = document.querySelector(".columna1 input");
  inputArchivo.addEventListener("change", renderizarImagen);

  const botonCrearCiclista = document.querySelector(".boton");
  botonCrearCiclista.addEventListener("click", crearCiclista);
};

main();
