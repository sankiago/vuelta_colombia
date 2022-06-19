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

    tarjetaCiclista.addEventListener("click", async function () {
      let numeroDeCiclista = this.querySelector(
        ".numeroDeInscripcion"
      ).textContent;
      ciclista = await eel.consultar_ciclista(numeroDeCiclista)();
      renderizar_detalles(ciclista);
    });

    rejillaCilcistas.appendChild(tarjetaCiclista);
  });
};

const renderizar_detalles = ({
  apellido,
  fecha_nacimiento_formateada,
  fotografia,
  nombre,
  num_equipo,
  num_identificacion,
  num_inscripcion,
  pais,
  ranking_UCI,
}) => {
  if (!fotografia) fotografia = "../img/foto_de_perfil.png";
  const fotografiaNodo = document.querySelector(".fotografia");
  const numeroDeInscripcionNodo = document.querySelector(
    ".columna1 .numeroDeInscripcion"
  ).childNodes[1];
  const nombreNodo = document.querySelector(".columna2 .nombre").childNodes[1];
  const numeroDeIdentificacionNodo = document.querySelector(
    "#numeroDeIdentificacion"
  ).childNodes[1];
  const fechaDeNacimientoNodo =
    document.querySelector("#fechaDeNacimiento").childNodes[1];
  const paisNodo = document.querySelector("#pais").childNodes[1];
  const ranking_UICNodo = document.querySelector("#ranking_UIC").childNodes[1];
  fotografiaNodo.textContent = fotografia;
  numeroDeInscripcionNodo.textContent = num_inscripcion;
  nombreNodo.textContent = `${nombre} ${apellido}`;
  numeroDeIdentificacionNodo.textContent = num_identificacion;
  fechaDeNacimientoNodo.textContent = fecha_nacimiento_formateada;
  paisNodo.value = pais;
  ranking_UICNodo.textContent = ranking_UCI;
};

async function main() {
  renderizar_ciclistas(await consultarTodosLosCiclistas());

  let barraDeBusqueda = document.querySelector("input");
  barraDeBusqueda.addEventListener("keyup", async (event) => {
    if (event.key === "Enter") {
      let resultadoDeBusqueda = undefined;
      if (!barraDeBusqueda.value) {
        resultadoDeBusqueda = await eel.consultar_todos_los_ciclistas()();
      } else {
        resultadoDeBusqueda = await eel.barra_de_busqueda_general_ciclistas(
          barraDeBusqueda.value
        )();
      }
      renderizar_ciclistas(resultadoDeBusqueda);
    }
  });
}

main();
