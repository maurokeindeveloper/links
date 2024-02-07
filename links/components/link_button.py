import reflex as rx
import links.styles.styles as styles
from links.styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
                alt=title,
            ),
            rx.vstack(
                rx.text(title, style=styles.button_title_style),
                rx.link(
                    rx.text(body, style=styles.button_body_style),
                    href=url,
                    is_external=True,
                    width="100%",
                ),
                align_items="start",
                spacing=Size.SMALL.value,
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value,
            ),
            gap="6px",
            width="100%",
        ),
        width="100%",
    )
