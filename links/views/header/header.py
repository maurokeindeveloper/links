import reflex as rx
from links.components.title import title
from links.components.link_icon import link_icon
from links.components.info_text import info_text
from links.styles.styles import Size as Size
from links.styles.colors import TextColor as TextColor, Color as Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Mauro Kein",
                size="xl",
                src="images/profile_2.jpg",
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading(
                    "Mauro Kein",
                    size="lg",
                ),
                rx.text("@maurokein", margin_top=Size.ZERO.value),
                align_items="start",
                spacing=Size.DEFAULT.value,
            ),
            align_items="start",
        ),
        rx.flex(
            info_text("+10", "años de investigación en literatura y humanidades"),
            rx.spacer(),
            info_text("+6", "años de experiencia docente"),
            rx.spacer(),
            info_text("+4", "años estudiando desarrollo de software"),
            font_size=Size.DEFAULT_PLUS.value,
            gap="8px",
        ),
        rx.vstack(
            title("Presentación"),
            rx.text(
                "Soy docente, investigador y desarrollador de software. Investigo las nuevas materialidades y sus efectos en la era digital. Escribo sobre los cruces posibles entre las ciencias humanas y las nuevas tecnologías en el mundo contemporáneo.",
                color=TextColor.BODY.value,
                font_size=Size.DEFAULT.value,
            ),
            align_items="start",
            spacing=Size.SMALL.value,
        ),
        title("Estudios y certificaciones"),
    )
