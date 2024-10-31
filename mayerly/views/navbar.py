import reflex as rx # type: ignore


def navbar():
    return rx.flex(
        rx.spacer(),
        rx.badge(
            rx.icon(tag="book", size=28),
            rx.heading("Library", size="8"),
            size="2",
            radius="full",
            align="center",
            color_scheme="cyan",
            variant="surface",
            padding="1rem",
            hight_contrast=True
        ),
        rx.spacer(),
        rx.hstack(
            rx.logo(),
            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
    )
