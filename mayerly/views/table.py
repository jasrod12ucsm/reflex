import reflex as rx
from ..backend.backend import State, Book
from ..components.form_field import form_field
from ..components.gender_badges import gender_badge


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def _show_Book(book: Book):
    """Show a Book in a table row."""
    return rx.table.row(
        rx.table.row_header_cell(book.name),
        rx.table.cell(book.autor),
        rx.table.cell(book.categoria),
        rx.table.cell(
            book.locacion
        ),
        rx.table.cell(book.idioma),
        rx.table.cell(book.cantidad),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    (State.current_user.id == book.id),
                    rx.button(
                        rx.icon("shopping-basket", size=22),
                        rx.text("Buy Product", size="3"),
                        color_scheme="blue",
                        on_click=State.buy_product(getattr(book,"id")),
                        loading=State.gen_response,
                    ),
                    rx.button(
                        rx.icon("shopping-basket", size=22),
                        rx.text("Buy Product", size="3"),
                        color_scheme="blue",
                        on_click=State.buy_product(getattr(book,"id")),
                        disabled=State.gen_response,
                    ),
                ),
                _update_Book_dialog(book),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_Book(getattr(book, "id")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
                min_width="max-content",
            )
        ),
        style={"_hover": {"bg": rx.color("accent", 2)}},
        align="center",
    )


def _add_Book_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Book", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="book", size=34),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Book Onboarding",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Fill the form with the Book's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        rx.hstack(
                            # Name
                            form_field(
                                "Name",
                                "Book Name",
                                "text",
                                "name",
                                "book-a",
                            ),
                            # Location
                            form_field(
                                "Locacion",
                                "Book Location",
                                "text",
                                "locacion",
                                "map-pinned",
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        rx.hstack(
                            # Email
                            form_field(
                                "Autor", "mayerly aranibar", "text", "autor", "users"
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        # Gender
                        rx.vstack(
                            rx.hstack(
                                rx.icon("user-round", size=16, stroke_width=1.5),
                                rx.text("Idioma"),
                                align="center",
                                spacing="2",
                            ),
                            rx.select(
                                ["Ingles","Español","Portuguez"],
                                placeholder="Select Idioma",
                                name="idioma",
                                direction="row",
                                as_child=True,
                                required=True,
                                width="100%",
                            ),
                            width="100%",
                        ),
                        rx.hstack(
                            # Age
                            form_field(
                                "Cantidad",
                                "Book Cantidad",
                                "int",
                                "cantidad",
                                "arrow-up-0-1",
                            ),
                            # Salary
                            form_field(
                                "Categoria",
                                "Book categoria",
                                "text",
                                "categoria",
                                "circle",
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        width="100%",
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit Book"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_Book_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            width="100%",
            max_width="450px",
            justify=["end", "end", "start"],
            padding="1.5em",
            border=f"2.5px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def _update_Book_dialog(user):
    print(user)
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.icon_button(
                rx.icon("square-pen", size=22),
                color_scheme="green",
                size="2",
                variant="solid",
                on_click=lambda: State.get_user(user),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Edit Book",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Edit the Book's info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        rx.hstack(
                            # Name
                            form_field(
                                "Name",
                                "name",
                                "text",
                                "name",
                                "user",
                                user.name,
                            ),
                            # Location
                            form_field(
                                "Locacion",
                                "locacion",
                                "text",
                                "location",
                                "map-pinned",
                                user.locacion,
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        rx.hstack(
                            # Email
                            form_field(
                                "Autor",
                                "autor",
                                "text",
                                "autor",
                                "users",
                                user.autor,
                            ),
                            # Job
                            form_field(
                                "idioma",
                                "idioma",
                                "text",
                                "idioma",
                                "briefcase",
                                user.idioma,
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        rx.hstack(
                            # Email
                            form_field(
                                "Categoria",
                                "categoria",
                                "text",
                                "categoria",
                                "users",
                                user.categoria,
                            ),
                            # Job
                            form_field(
                                "cantidad",
                                "123",
                                "nint",
                                "cantidad",
                                "briefcase",
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    rx.form.submit(
                        rx.dialog.close(
                            rx.button("Update Book"),
                        ),
                        as_child=True,
                    ),
                    on_submit=lambda form_data: State.update_book_to_db(form_data),
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def main_table():
    return rx.fragment(
        rx.flex(
            _add_Book_button(),
            rx.spacer(),
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                [
                    "book name",
                    "categoria",
                    "autor",
                    "location",
                    "idioma",
                ],
                placeholder="Sort By: Name",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Name", "square-user-round"),
                    _header_cell("Autor", "mail"),
                    _header_cell("Categoria", "person-standing"),
                    _header_cell("Locacion", "user-round"),
                    _header_cell("Idioma", "dollar-sign"),
                ),
            ),
            rx.table.body(rx.foreach(State.users, _show_Book)),
            variant="surface",
            size="3",
            width="100%",
        ),
    )
