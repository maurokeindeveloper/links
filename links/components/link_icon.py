import reflex as rx
import links.styles.styles as styles
from links.styles.colors import Color as Color


def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(rx.image(src=image), href=url, is_external=True)
