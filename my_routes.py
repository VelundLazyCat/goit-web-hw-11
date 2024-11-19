
from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from my_db import get_db
from shemas import ContactSchema, ContactResponse
from sqlalchemy.orm import Session
import contacts


router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.get('/', response_model=list[ContactResponse])
async def get_contacts(contact_field: str = Query(None), db: Session = Depends(get_db)):
    contacts_ = await contacts.get_contacts(contact_field, db)
    if contacts_ is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='CONTACTS NOT FOUND')
    return contacts_


@router.get('/{contact_id}', response_model=ContactResponse)
async def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='CONTACT NOT FOUND')
    return contact


@router.post('/', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema, db: Session = Depends(get_db)):
    contact = await contacts.create_contact(body, db)
    return contact


@router.put('/{contact_id}', response_model=ContactResponse)
async def update_contact(body: ContactSchema, contact_id: int, db: Session = Depends(get_db)):
    contact = await contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='CONTACT NOT FOUND')
    return contact


@router.delete('/{contact_id}', response_model=ContactResponse)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await contacts.delete_contact(contact_id, db)
    return contact


@router.get('/7', response_model=list[ContactResponse])
async def get_contacts_birthdays(db: Session = Depends(get_db)):
    contacts_ = await contacts.get_contacts_birthdays(db)
    if contacts_ is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='CONTACTS NOT FOUND')
    return contacts_
