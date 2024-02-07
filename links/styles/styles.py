import reflex as rx
from enum import Enum
from .colors import Color as Color, TextColor as TextColor
from .fonts import Font as Font, FontWeight as FontWeight

# Constants
MAX_WIDTH = "760px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT_LESS = "0.9em"
    DEFAULT = "1em"
    DEFAULT_PLUS = "1.1em"
    NOT_SO_BIG = "1.2em"
    LARGE = "1.6em"
    BIG = "2em"


# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND_OPTIONAL.value,
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.BODY.value,
        "background_color": Color.BACKGROUND.value,
        "white_space": "normal",
        "text_align": "start",
    },
    rx.Link: {"text_decoration": "none", "_hover": {}},
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.NOT_SO_BIG.value,
)

title_style = dict(
    width="100%", padding_top=Size.DEFAULT.value, color=Color.PRIMARY.value
)

link_title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=Color.PRIMARY.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value, font_weight="bold", color=TextColor.BODY.value
)

button_body_style = dict(font_size=Size.MEDIUM.value, color=TextColor.FOOTER.value)
