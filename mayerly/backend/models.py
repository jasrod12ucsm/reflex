import reflex as rx


class Book(rx.Model, table=True):  # type: ignore
    """The Book model."""

    name: str
    autor: str
    categoria: str
    locacion: str
    idioma: str
    cantidad:int