import reflex as rx
import datetime
from links.styles.styles import Size as Size
from links.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="images/Cc.logo.circle.svg.png",
                width="18px",
                heigth="18px",
                alt="Ícono de Licencia Creative Commons",
            ),
            rx.image(
                src="images/Cc.by.png",
                width="18px",
                heigth="18px",
                alt="Ícono de atribución de la Licencia Creative Commons",
            ),
            rx.link(
                rx.text(f"2022-{datetime.date.today().year} @maurokein."),
                href="https://maurokeindeveloper.github.io/online/",
            ),
            rx.text("En la investigación permanente desde Buenos Aires"),
            rx.image(
                src="images/argentina.png",
                width="100px",
                heigth="auto",
                margin_top=Size.ZERO.value,
                alt="Nombre de Argentina con dos cintas azules por debajo",
            ),
            margin_bottom=Size.BIG.value,
            padding_x=Size.SMALL.value,
            color=TextColor.FOOTER.value,
        ),
    )
