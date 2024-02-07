import reflex as rx
from links.styles.styles import Size as Size


def link_college(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(height="100px", width="175px", src=imagen, alt=f"Logo de {alt}"),
        href=url,
        is_external=True,
    )
