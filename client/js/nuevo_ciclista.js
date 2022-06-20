function mostrarMenuArchivo() {
  const inputArchivo = document.querySelector(".columna1 input");
  inputArchivo.click();
}

const leerURLDesdeArchivo = archivo => {
    return new Promise((responder, rechazar) => {
        const reader = new FileReader();
        reader.onload = e => responder(e.target.result);
        reader.onerror = e => rechazar(e);
        reader.readAsDataURL(archivo);
    });
};


async function renderizarImagen() {
    const URLDeArchivo = await leerURLDesdeArchivo(this.files[0])
    const fotografia = document.querySelector('main img')
    fotografia.setAttribute('src', URLDeArchivo)
}

const main = async () => {
  const botonAgregarFoto = document.querySelector("label");
  botonAgregarFoto.addEventListener("click", mostrarMenuArchivo);

  const inputArchivo = document.querySelector(".columna1 input");
  inputArchivo.addEventListener("change", renderizarImagen);
};

main();
