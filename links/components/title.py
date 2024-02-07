import reflex as rx
import links.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(text, style=styles.title_style, size="xl")
