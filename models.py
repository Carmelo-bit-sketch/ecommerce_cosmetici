from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Date, ForeignKey, Table, Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

cliente_indirizzo = Table(
    'CLIENTE_INDIRIZZO', Base.metadata,
    Column('IDCliente', Integer, ForeignKey('CLIENTE.IDCliente'), primary_key=True),
    Column('IDIndirizzo', Integer, ForeignKey('INDIRIZZO.IDIndirizzo'), primary_key=True)
)

class Cliente(Base):
    __tablename__ = 'CLIENTE'
    IDCliente = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(50), nullable=False)
    Cognome = Column(String(50), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Password = Column(String(100), nullable=False)
    Telefono = Column(String(20))
    DataIscrizione = Column(Date, nullable=False)
    indirizzi = relationship("Indirizzo", secondary=cliente_indirizzo, back_populates="clienti")
    ordini = relationship("Ordine", back_populates="cliente")
    recensioni = relationship("Recensione", back_populates="cliente")

class Indirizzo(Base):
    __tablename__ = 'INDIRIZZO'
    IDIndirizzo = Column(Integer, primary_key=True, autoincrement=True)
    Via = Column(String(100), nullable=False)
    NumeroCivico = Column(String(10), nullable=False)
    Città = Column(String(50), nullable=False)
    CAP = Column(String(10), nullable=False)
    clienti = relationship("Cliente", secondary=cliente_indirizzo, back_populates="indirizzi")

class MetodoPagamento(Base):
    __tablename__ = 'METODO_PAGAMENTO'
    IDMetodo = Column(Integer, primary_key=True, autoincrement=True)
    Tipo = Column(String(30), nullable=False)
    ordini = relationship("Ordine", back_populates="metodo")

class Ordine(Base):
    __tablename__ = 'ORDINE'
    IDOrdine = Column(Integer, primary_key=True, autoincrement=True)
    IDCliente = Column(Integer, ForeignKey('CLIENTE.IDCliente'), nullable=False)
    IDMetodo = Column(Integer, ForeignKey('METODO_PAGAMENTO.IDMetodo'), nullable=False)
    DataOrdine = Column(Date, nullable=False)
    Totale = Column(Float, nullable=False)
    cliente = relationship("Cliente", back_populates="ordini")
    metodo = relationship("MetodoPagamento", back_populates="ordini")
    dettaglio = relationship("DettaglioOrdine", back_populates="ordine")
    spedizione = relationship("Spedizione", back_populates="ordine", uselist=False)

class Spedizione(Base):
    __tablename__ = 'SPEDIZIONE'
    IDSpedizione = Column(Integer, primary_key=True, autoincrement=True)
    IDOrdine = Column(Integer, ForeignKey('ORDINE.IDOrdine'), unique=True, nullable=False)
    Stato = Column(String(20), nullable=False)
    DataPrevista = Column(Date, nullable=False)
    ordine = relationship("Ordine", back_populates="spedizione")

class Marca(Base):
    __tablename__ = 'MARCA'
    IDMarca = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(50), nullable=False)
    prodotti = relationship("Prodotto", back_populates="marca")

class Tipologia(Base):
    __tablename__ = 'TIPOLOGIA'
    IDTipologia = Column(Integer, primary_key=True, autoincrement=True)
    Categoria = Column(String(50), nullable=False)
    prodotti = relationship("Prodotto", back_populates="tipologia")

class Prodotto(Base):
    __tablename__ = 'PRODOTTO'
    IDProdotto = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(100), nullable=False)
    Descrizione = Column(Text, nullable=False)
    Prezzo = Column(Float, nullable=False)
    QuantitaDisponibile = Column(Integer, nullable=False)
    Sconto = Column(Float, default=0)
    IDMarca = Column(Integer, ForeignKey('MARCA.IDMarca'), nullable=False)
    IDTipologia = Column(Integer, ForeignKey('TIPOLOGIA.IDTipologia'), nullable=False)
    marca = relationship("Marca", back_populates="prodotti")
    tipologia = relationship("Tipologia", back_populates="prodotti")
    dettagli = relationship("DettaglioOrdine", back_populates="prodotto")
    forniture = relationship("Fornisce", back_populates="prodotto")
    recensioni = relationship("Recensione", back_populates="prodotto")

class Fornitore(Base):
    __tablename__ = 'FORNITORE'
    IDFornitore = Column(Integer, primary_key=True, autoincrement=True)
    NomeFornitore = Column(String(100), nullable=False)
    PartitaIVA = Column(String(11), unique=True, nullable=False)
    Recapito = Column(String(100))
    forniture = relationship("Fornisce", back_populates="fornitore")

class Fornisce(Base):
    __tablename__ = 'FORNISCE'
    IDFornitore = Column(Integer, ForeignKey('FORNITORE.IDFornitore'), primary_key=True)
    IDProdotto = Column(Integer, ForeignKey('PRODOTTO.IDProdotto'), primary_key=True)
    PrezzoFornitura = Column(Float, nullable=False)
    fornitore = relationship("Fornitore", back_populates="forniture")
    prodotto = relationship("Prodotto", back_populates="forniture")

class DettaglioOrdine(Base):
    __tablename__ = 'DETTAGLIO_ORDINE'
    IDOrdine = Column(Integer, ForeignKey('ORDINE.IDOrdine'), primary_key=True)
    IDProdotto = Column(Integer, ForeignKey('PRODOTTO.IDProdotto'), primary_key=True)
    Quantita = Column(Integer, nullable=False)
    PrezzoUnitario = Column(Float, nullable=False)
    ordine = relationship("Ordine", back_populates="dettaglio")
    prodotto = relationship("Prodotto", back_populates="dettagli")

class Recensione(Base):
    __tablename__ = 'RECENSIONE'
    IDRecensione = Column(Integer, primary_key=True, autoincrement=True)
    IDCliente = Column(Integer, ForeignKey('CLIENTE.IDCliente'), nullable=False)
    IDProdotto = Column(Integer, ForeignKey('PRODOTTO.IDProdotto'), nullable=False)
    Voto = Column(Integer, nullable=False)
    Commento = Column(Text)
    DataRec = Column(Date, nullable=False)
    cliente = relationship("Cliente", back_populates="recensioni")
    prodotto = relationship("Prodotto", back_populates="recensioni")
