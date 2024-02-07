import reflex as rx
from links.styles.colors import Color as Color
from links.styles.styles import Size as Size


def watch_button(url: str) -> rx.Component:
    return rx.link(
        rx.button(
            "Certificado",
            background_color=Color.WATCH_BUTTON.value,
            font_size=Size.MEDIUM.value,
            white_space="normal",
        ),
        href=url,
        is_external=True,
        height="1.8em",
        width="100%",
    )


def watch_button_deactivate(url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.text("Certificado en trámite", font_size=Size.MEDIUM.value),
            background_color=Color.WATCH_BUTTON.value,
            white_space="normal",
            height="1.8em",
            deactivate=True,
        ),
        href=url,
        is_external=True,
        width="100%",
    )
