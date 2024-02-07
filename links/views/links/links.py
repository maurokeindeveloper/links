import reflex as rx
from links.components.link_button import link_button
from links.components.watch_button import watch_button, watch_button_deactivate
from links.components.title import title
from links.components.link_title import link_title
from links.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        link_title("Ponencias"),
        rx.responsive_grid(
            rx.box(
                rx.vstack(
                    rx.vstack(
                        link_button(
                            "'Continuidad y cambio en ediciones impresas y digitales'",
                            "13° Jornadas Internas del Centro de Estudios de Teoría y Crítica Literaria, UNLP",
                            "icons/book-solid.svg",
                            "https://idihcs.fahce.unlp.edu.ar/ctcl/jornada-interna/",
                        ),
                        watch_button_deactivate("#"),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "'Repensar la edición de literatura en tiempos digitales'",
                            "IX Jornadas de Graduadxs y Jóvenes Investigadores en Formación de la FaHCE",
                            "icons/book-open-solid.svg",
                            "https://www.fahce.unlp.edu.ar/facultad/noticias/en-octubre-seran-las-ix-jornadas-de-graduades-e-investigadorxs-en-formacion-de-la-fahce",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1zGk4l_TcXljaCYJxHcZVhTU-gMY1Kiv7/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "'Investigación en el grado: avances y desafíos'",
                            "V Foro Académico de Letras y Lenguas Modernas, UdelaR",
                            "icons/magnifying-glass-plus-solid.svg",
                            "https://sites.google.com/view/falejelu2023",
                        ),
                        watch_button("https://www.youtube.com/watch?v=_DW4k_mUU7s"),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "'Nuevas formas de escribir, editar y leer en la era del Big Data'",
                            "V Foro Académico de Letras y Lenguas Modernas, UdelaR",
                            "icons/keyboard-solid.svg",
                            "https://sites.google.com/view/falejelu2023",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1gPAgGogMjMd7sFty6d9mFUpWIDCrZUBE/view?usp=sharing",
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "'‘Wakefield’: entre la ficción paranoica y el género policial'",
                            "53a Jornadas de Estudios Americanos, UNSaM y AAEA - Comisión 10 Aula 402",
                            "icons/eye-solid.svg",
                            "https://noticias.unsam.edu.ar/2023/07/20/53a-jornadas-de-estudios-americanos-nuevas-iluminaciones-perspectivas-de-la-critica-y-el-arte-en-el-sxxi/",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/108FvYLGy-X47gep2PkT-nUBW-vqa1YW6/view?usp=sharing",
                        ),
                        width="100%",
                    ),
                    gap=Size.DEFAULT_LESS.value,
                ),
            ),
            width="100%",
        ),
        link_title("Cursos y talleres"),
        rx.responsive_grid(
            rx.box(
                rx.vstack(
                    rx.vstack(
                        link_button(
                            "IA, Wikipedia y Cultura Digital",
                            "Curso virtual 'Puentes entre las culturas escolares, digitales y libres'",
                            "icons/wikipedia-w.svg",
                            "https://wikimedia.org.ar/2023/09/27/wikipuentes-2023-ia-wikipedia-y-cultura-digital/",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1S3O4_L_DYD3Nueb11jRTMwgXhj_jCdLL/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Uso de bibliografía con Zotero",
                            "Taller de gestión de referencias bibliográficas con Zotero",
                            "icons/zotero.svg",
                            "https://www.fahce.unlp.edu.ar/facultad/biblioteca/agenda-bibhuma/taller-de-gestion-de-referencias-bibliograficas-con-zotero",
                        ),
                        watch_button_deactivate("#"),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Lectura y escritura en investigación",
                            "Taller 'Lectoescritura en la investigación, y su rol en la formación de grado'",
                            "research.png",
                            "https://drive.google.com/file/d/1JtwoEa6xK8I1UJm9z9FAtPfYzuhEEexv/view",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1AM0-0M9DMtLmDGWifq-mdNZGuvSBew1j/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Bibliotecas Populares y Universidad",
                            "Primer Encuentro entre Bibliotecas Populares y Universidad",
                            "public-library.png",
                            # <a href="https://www.flaticon.com/free-icons/institute" link_="institute icons">Institute icons created by VectorPortal - Flaticon</a>
                            "https://www.fahce.unlp.edu.ar/facultad/secretarias-y-prosecretarias/academica/deptos/bibliotecologia/agenda/1er-encuentro-de-bibliotecas-populares-y-universidad",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/15oMbIOJddFrzCxMwq2FSMk7_Lrq3OnGX/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "VI Jornadas de Jóvenes Lingüistas",
                            "Exploración de la construcción colectiva de nuevos lenguajes digitales",
                            "linguistica.png",
                            # <a href="https://www.flaticon.es/iconos-gratis/linguistica" title="lingüística iconos">Lingüística iconos creados por wanicon - Flaticon</a>
                            "http://investigacion.filo.uba.ar/novedades/vi-jornadas-de-j%C3%B3venes-ling%C3%BCistas",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1ihhAUKMKnAExIYecKGJO-Ee_8ja2ZMHT/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Búsqueda bibliográfica",
                            "Taller de búsquedas bibliográficas: BECYT y recursos de acceso abierto",
                            "libros.png",
                            # <a href="https://www.flaticon.es/iconos-gratis/bibliografia" title="bibliografía iconos">Bibliografía iconos creados por Ylivdesign - Flaticon</a>
                            "https://www.fahce.unlp.edu.ar/facultad/biblioteca/agenda-bibhuma/taller-de-busquedas-becyt-y-recursos-de-acceso-abierto",
                        ),
                        watch_button_deactivate("#"),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Wikimedia, Educación y Culturas Digitales",
                            "Congreso Internacional sobre Wikimedia, Educación y Culturas Digitales",
                            "icons/wikipedia-w.svg",
                            "http://wecudi.fahce.unlp.edu.ar/wecudi",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1eJfUqte3MT7OEuLYUmiIxi4REK1Ugi4k/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "V Jornadas Internas de Literatura Comparada del CELyC",
                            "Cuarto Centenario de la publicación del Primer Folio de la obra de Shakespeare",
                            "icons/open-book-literature.svg",
                            "https://idihcs.fahce.unlp.edu.ar/celyc/v-jornadas-internas/",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/19sqRwpGHQJdrg1JPQbehLksUne01aPtv/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Jornadas 'Las memorias en sus políticas'",
                            "El giro archivístico y sus derivas",
                            "icons/folder-open-regular.svg",
                            "https://www.fahce.unlp.edu.ar/facultad/secretarias-y-prosecretarias/posgrado/maestria/maestria-en-historia-y-memoria/agenda/jornadas-las-memorias-en-sus-politicas-201cel-giro-archivistico-y-sus-derivas201d",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1cSfkQp11vFAPQ-1npI_ShGZUdEOYvJ9b/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    gap=Size.DEFAULT_LESS.value,
                ),
            ),
            width="100%",
        ),
        link_title("Programación"),
        rx.responsive_grid(
            rx.box(
                rx.vstack(
                    rx.vstack(
                        link_button(
                            "Desarrollo con C# Nivel 1",
                            "Curso dictado por el Prof. de la UNGS Maximiliano Sar Fernández",
                            "icons/c.svg",
                            "https://drive.google.com/file/d/1O0LQTA7g-f9ZKo7U7alLqfJNK1cTEc71/view",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1R83bptrkdST2Zc32Nb5n1_y8AJUV83YV/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Desarrallador con orientación en aplicaciones móviles",
                            "Tramo 2: Profundizando en Programación - Desarrollo Mobile",
                            "icons/android-alt.svg",
                            "https://www.argentina.gob.ar/sites/default/files/24._ticmas_-_desarrollador_con_orientacion_en_aplicaciones_moviles_0.pdf",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1lO68zDtJvHECSNKzXohpi0KwhnhZ-Jdv/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Desarrollador con orientación en aplicaciones móviles",
                            "Tramo 1: Introducción - Primeros pasos en Front-End",
                            "icons/code-solid.svg",
                            "https://www.argentina.gob.ar/sites/default/files/24._ticmas_-_desarrollador_con_orientacion_en_aplicaciones_moviles_0.pdf",
                        ),
                        watch_button_deactivate(""),
                        width="100%",
                    ),
                    rx.vstack(
                        link_button(
                            "Fundamentos de Programación",
                            "Curso #SeProgramar del Plan Argentina Programa",
                            "icons/python.svg",
                            "https://www.argentina.gob.ar/economia/conocimiento/argentina-programa",
                        ),
                        watch_button(
                            "https://drive.google.com/file/d/1x-PzZhZ-zcfFIRURbiBJJjfoLbOwxeV5/view?usp=sharing"
                        ),
                        width="100%",
                    ),
                    gap=Size.DEFAULT_LESS.value,
                )
            ),
            width="100%",
        ),
        link_title("Idiomas"),
        rx.responsive_grid(
            rx.box(
                rx.vstack(
                    link_button(
                        "Nivel 8 de Inglés General para Desarrolladores",
                        "B1.2 del Marco Común Europeo de Referencia para las Lenguas - CUI",
                        "icons/language-solid.svg",
                        "https://cui.edu.ar/index.php",
                    ),
                    watch_button(
                        "https://drive.google.com/file/d/1SSd3ywNXqL9aF5J0JVOCw9CPI4tO-Qbd/view?usp=sharing"
                    ),
                    width="100%",
                ),
                gap=Size.DEFAULT_LESS.value,
            ),
            width="100%",
        ),
    )
