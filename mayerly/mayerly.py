import reflex as rx # type: ignore
from .views.navbar import navbar
from .views.email import email_gen_ui
from .views.table import main_table
from .backend.backend import State


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.flex(
            rx.box(main_table(), width=["100%", "100%", "100%", "100%"]),
            spacing="6",
            width="100%",
            flex_direction=["column", "column", "column", "row"],
        ),
        height="100vh",
        bg=rx.color("accent", 1),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
        padding_y=["1em", "1em", "2em"],
    )


app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="blue"
    ),
)
app.add_page(
    index,
    on_load=State.load_entries,
    title="Sales App",
    description="Generate personalized sales emails.",
)
