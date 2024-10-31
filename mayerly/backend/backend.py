import os
import openai

import reflex as rx
from sqlmodel import select, asc, desc, or_, func

from .models import Book

_client = None

def get_openai_client():
    global _client
    if _client is None:
        _client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    return _client


class State(rx.State):
    """The app state."""

    current_user: Book = Book()
    users: list[Book] = []
    products: dict[str, str] = {}
    email_content_data: str = "Click 'Generate Email' to generate a personalized sales email."
    gen_response = False
    tone: str = "😊 Formal"
    length: str = "1000"
    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    def buy_product(self, product_name: str):
        print(product_name)
        with rx.session() as session:
            product = session.exec(
                select(Book).where(Book.id == product_name)
            ).first()

            if not product:
                return rx.window_alert("Product not found in database")

            if product.cantidad < 1:
                return rx.window_alert("Not enough stock available")

            product.cantidad -= 1
            session.add(product)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Purchased {1}", position="bottom-right")
    

    def load_entries(self) -> list[Book]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Book)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Book, field).ilike(search_value)
                            for field in Book.get_fields()
                        ],
                    )
                )

            if self.sort_value:
                sort_column = getattr(Book, self.sort_value)
                if self.sort_value == "salary":
                    order = desc(sort_column) if self.sort_reverse else asc(
                        sort_column)
                else:
                    order = desc(func.lower(sort_column)) if self.sort_reverse else asc(
                        func.lower(sort_column))
                query = query.order_by(order)

            self.users = session.exec(query).all()

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_user(self, user: Book):
        self.current_user = user

    def add_Book_to_db(self, form_data: dict):
        self.current_user = form_data
        print(self.current_user)
        with rx.session() as session:
            if session.exec(
                select(Book).where(
                    Book.name == self.current_user["name"])
            ).first():
                return rx.window_alert("User with this name already exists")
            session.add(Book(**self.current_user))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {self.current_user['autor']} has been added.", position="bottom-right")

    def update_book_to_db(self, form_data: dict):
        print(form_data)
        self.current_user.update(form_data)
        with rx.session() as session:
            book = session.exec(
                select(Book).where(Book.name == self.current_user["name"])
            ).first()
            for field in Book.get_fields():
                print(field)
                if field != "id":
                    setattr(book, field, self.current_user[field])
            session.add(book)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"Book {self.current_user['name']} has been modified.", position="bottom-right")

    def delete_Book(self, id: int):
        """Delete a Book from the database."""
        print(id)
        with rx.session() as session:
            book= session.exec(
                select(Book).where(Book.id == id)).first()
            session.delete(book)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {Book.name} has been deleted.", position="bottom-right")

   

