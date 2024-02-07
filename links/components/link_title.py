import reflex as rx
import links.styles.styles as styles
from links.styles.styles import Size as Size


def link_title(text: str) -> rx.Component:
    return rx.heading(text, style=styles.link_title_style, size="lg")
