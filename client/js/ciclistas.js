const consultarTodosLosCiclistas = eel.consultar_todos_los_ciclistas();
const hacerBusquedaGeneralDeCiclistas = eel.barra_de_busqueda_general_ciclistas;

const renderizar_ciclistas = (ciclistas) => {
  let rejillaCilcistas = document.querySelector(".rejillaCiclistas");
  rejillaCilcistas.textContent = "";
  ciclistas.map((ciclistaActual) => {
    if (!ciclistaActual.fotografia)
      ciclistaActual.fotografia = "../img/foto_de_perfil.png";

    let tarjetaCiclista = document.createElement("div");
    tarjetaCiclista.classList.add("tarjetaCiclista");

    let cajaSuperior = document.createElement("div");
    cajaSuperior.classList.add("cajaSuperior");
    let nombreYApellido = document.createElement("p");
    nombreYApellido.textContent = `${ciclistaActual.nombre} ${ciclistaActual.apellido}`;
    let fotoDelCiclista = document.createElement("img");
    fotoDelCiclista.setAttribute("src", ciclistaActual.fotografia);
    cajaSuperior.appendChild(fotoDelCiclista);
    cajaSuperior.appendChild(nombreYApellido);

    let cajaInferior = document.createElement("div");
    cajaInferior.classList.add("cajaInferior");
    let numeroDeInscripcion = document.createElement("div");
    numeroDeInscripcion.classList.add("numeroDeInscripcion");
    numeroDeInscripcion.textContent = ciclistaActual.num_inscripcion;
    cajaInferior.appendChild(numeroDeInscripcion);

    tarjetaCiclista.appendChild(cajaSuperior);
    tarjetaCiclista.appendChild(cajaInferior);

    tarjetaCiclista.addEventListener('click', function(event){
        console.log(event)
        console.log(this)
    })

    rejillaCilcistas.appendChild(tarjetaCiclista);
  });
};

async function main() {
  renderizar_ciclistas(await consultarTodosLosCiclistas());

  let barraDeBusqueda = document.querySelector("input");
  barraDeBusqueda.addEventListener("keyup", async (event) => {
    if (event.key === "Enter") {
        let resultadoDeBusqueda = undefined
      if (!barraDeBusqueda.value) {
        resultadoDeBusqueda = await eel.consultar_todos_los_ciclistas()();

      } else {
        resultadoDeBusqueda =
          await eel.barra_de_busqueda_general_ciclistas(
            barraDeBusqueda.value
          )();
      }
      renderizar_ciclistas(resultadoDeBusqueda);
    }
  });
}

main();
