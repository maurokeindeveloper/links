import reflex as rx
from links.components.link_college import link_college
from links.components.title import title
from links.styles.styles import Size as Size
from links.styles.styles import title_style


def colleges() -> rx.Component:
    return rx.vstack(
        title(
            "Casas de estudio",
        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.responsive_grid(
            link_college(
                "images/fahce-unlp.png",
                "https://www.fahce.unlp.edu.ar/",
                "Facultad de Humanidades y Ciencias de la Educación de la Universidad Nacional de La Plata",
            ),
            link_college(
                "images/filo-uba.jpg",
                "http://www.filo.uba.ar/",
                "Facultad de Filosofía y Letras de la Universidad de Buenos Aires",
            ),
            link_college(
                "images/logo-info-unlp.png",
                "https://www.info.unlp.edu.ar/",
                "Facultad de Informática de la Universidad Nacional de La Plata",
            ),
            link_college(
                "images/argentina-programa.jpg",
                "https://www.argentina.gob.ar/economia/conocimiento/argentina-programa",
                "Plan Argentina Programa de la Secretaría del Conocimiento del Ministerio de Economía de la Nación",
            ),
            columns=[1, 2, 4],
            gap=Size.LARGE.value,
        ),
        width="100%",
        align_items="center",
    )
