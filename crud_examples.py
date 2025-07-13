from sqlalchemy.orm import Session
from models import Cliente
from datetime import date

def crea_cliente(session: Session, nome, cognome, email, password, telefono):
    cliente = Cliente(
        Nome=nome, Cognome=cognome, Email=email,
        Password=password, Telefono=telefono,
        DataIscrizione=date.today()
    )
    session.add(cliente)
    session.commit()
    return cliente

def leggi_clienti(session: Session):
    return session.query(Cliente).all()

def aggiorna_email(session: Session, id_cliente, nuova_email):
    cliente = session.query(Cliente).filter_by(IDCliente=id_cliente).first()
    if cliente:
        cliente.Email = nuova_email
        session.commit()
        return True
    return False

def elimina_cliente(session: Session, id_cliente):
    cliente = session.query(Cliente).filter_by(IDCliente=id_cliente).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        return True
    return False
