import reflex as rx
from links.components.navbar import navbar
from links.views.header.header import header
from links.views.links.links import links
from links.components.footer import footer
from links.views.colleges.colleges import colleges
import links.styles.styles as styles
from links.styles.styles import Size as Size


# class State(rx.State):
#    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                colleges(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )


app = rx.App(stylesheets=styles.STYLESHEETS, style=styles.BASE_STYLE)
app.add_page(
    index,
    title="mauro_kein | Investigación, programación y docencia",
    description="Mi nombre es Mauro Kein. Soy investigador, docente y programador.",
)
