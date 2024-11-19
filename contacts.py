from sqlalchemy import or_, and_
from models import Contact
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from shemas import ContactSchema
from datetime import datetime


async def get_contacts(contact_field: str, db: Session) -> List[Contact] | Contact:
    if not contact_field:
        contacts = db.query(Contact).all()
        return contacts
    contact = db.query(Contact).filter(or_(
        Contact.first_name == contact_field,
        Contact.last_name == contact_field,
        Contact.email == contact_field)).all()
    if contact:
        return contact


async def get_contact(contact_id: int, db: Session) -> Contact:
    contact = db.query(Contact).filter_by(contact_id=contact_id).first()
    return contact


async def create_contact(body: ContactSchema, db: Session) -> Contact:
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactSchema, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(
        Contact.contact_id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.telephon_number = body.telephon_number
        contact.birthday = body.birthday
        contact.description = body.description
        db.commit()
        db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(
        Contact.contact_id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_contacts_birthdays(db: Session) -> List[Contact]:
    contacts_list = []
    today = datetime.now().date()
    contacts_all = db.query(Contact).all()
    for contact in contacts_all:
        days_ = (datetime(year=today.year,
                          month=contact.birthday.month,
                          day=contact.birthday.day).date() - today).days
        if 0 <= days_ < 7:
            contacts_list.append(contact)
    return contacts_list
