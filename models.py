from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


"""
Контакти повинні зберігатися в базі даних та містити в собі наступну інформацію:
-Ім'я
-Прізвище
-Електронна адреса
-Номер телефону
-День народження
-Додаткові дані (необов'язково)
"""


class Contact(Base):
    __tablename__ = 'contacts'
    contact_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20), index=True)
    last_name: Mapped[str] = mapped_column(String(20), index=True)
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    telephon_number: Mapped[str] = mapped_column(String(15), unique=True)
    birthday: Mapped[Date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(String(250))
