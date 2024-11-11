import { useEffect, useState } from "react"
import Carrusel from "../components/Carrusel"
import Cover from "../components/Cover"
import NavbarBody from "../components/NavbarBody"

import style from "../styles/home.module.css"
import InicioSesion from "../components/InicioSesion"
// import InstallButton from "../components/InstallButton"
import { useGlobal } from "../components/GlobalContext"


function Home() {
    const [generos, setGeneros] = useState([]);
    const [mediasDescubrir, setMediasDescubrir] = useState([]);

    const {urlBackend,urlFront} = useGlobal()

    const [sesion, setSesion] = useState(true)

    useEffect(() => {
        setSesion(true) // Cambiar por la funsión en el inicio de sesión hermano
        const fetchGeneros = async () => {
            try {
                const response = await fetch(`${urlBackend}/popview/v1/generos/`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                console.log(data);
                setGeneros(data);
            } catch (error) {
                console.error('Error fetching generos:', error);
            }
        };
        const fetchMediasDescubrir = async () => {
            try {
                const response = await fetch(`${urlBackend}/popview/v1/medias/random/`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                // console.log(data)
                setMediasDescubrir(data);
            } catch (error) {
                console.error('Error fetching generos:', error);
            }
        };

        fetchGeneros();
        fetchMediasDescubrir();
    }, [urlBackend]);



    return <>
        {sesion ?

            <NavbarBody>
                <div className={style.featureMovie_Content}>
                    <div className={style.featureMovie_text}>
                        <h2>Titulo</h2>
                        <div>Descripcion</div>
                        <div>generos</div>
                    </div>
                    <div className={style.featureMovie_Video}>
                        Pelicula
                    </div>
                </div>

                {/* <InstallButton></InstallButton> */}

                <div className={style.content}>
                    
                    <div className="divisor">Generos</div>
                    <div className={style.generoContainer}>
                        <div className={style.generos} onClick={() => window.location = urlFront+'/aleatorio'}>
                            <div>
                                <img src={"./icon/dados.png"} alt={"Aleatorio"} />
                            </div>
                            <div>
                                Aleatorio
                            </div>
                        </div>
                        {generos.map((genero, index) => (
                            <div key={index} className={style.generos} onClick={() => window.location = urlFront+ "/b?g=" + genero.nombre}>
                                <div>
                                    <img src={genero.imagen} alt={genero.nombre} />
                                </div>
                                <div>
                                    {genero.nombre}
                                </div>
                            </div>
                        ))}
                    </div>

                    {/* <div className="divisor">Recomendado</div> */}

                    <div className="divisor">Descubre Peliculas</div>
                    <Carrusel>
                        {mediasDescubrir.map((media, index) => (
                            <Cover key={index} portada={media.poster_url} portada2={media.cover_url} onclick={() => window.location = urlFront+"/p?m=" + media.id} />

                        ))}
                    </Carrusel>


                </div>
            </NavbarBody>
            :
            <InicioSesion></InicioSesion>

        }


    </>
}

export default Home