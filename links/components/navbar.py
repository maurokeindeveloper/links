import reflex as rx
from links.styles.styles import Size as Size
from links.styles.colors import Color as Color
from links.styles import styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("mauro", color=Color.BACKGROUND_OPTIONAL.value),
            rx.span("_kein", color=Color.BACKGROUND.value),
            style=styles.navbar_title_style,
        ),
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        bg=Color.PRIMARY.value,
        position="sticky",
        top="0",
        z_indez="999",
    )
