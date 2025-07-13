from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import models
from models import (
    Cliente, Indirizzo, MetodoPagamento, Ordine, Spedizione,
    Marca, Tipologia, Prodotto, Fornitore, Fornisce,
    DettaglioOrdine, Recensione
)
import sys

def connessione_database():
    try:
        # Connessione a MySQL (localhost:3306, utente root, nessuna password, DB ecommerce)
        engine = create_engine("mysql+pymysql://root@localhost:3306/ecommerce", echo=True)
        print("✅ Connessione a MySQL riuscita.")

        # Verifica database attivo
        try:
            with engine.connect() as conn:
                result = conn.execute("SELECT DATABASE();")
                print("📌 SQLAlchemy si sta connettendo al database:", result.scalar())
        except Exception as e1:
             print("❌ Errore durante il controllo del database attivo:", e1)
        return engine
        
    except Exception as e:
        print(f"❌ Errore nella connessione al database: {e}")
        sys.exit(1)

def crea_tabelle(engine):
    try:
        print("⚙️  Creazione delle tabelle...")
        models.Base.metadata.create_all(engine)
        print("✅ Tabelle create correttamente.")
    except Exception as e:
        print(f"❌ Errore nella creazione delle tabelle: {e}")

def stampa_tabelle_presenti(engine):
    try:
        insp = inspect(engine)
        print("🔍 Tabelle presenti nel database dopo create_all():")
        for nome in insp.get_table_names():
            print(f" - {nome}")
    except Exception as e:
        print(f"❌ Errore nel recupero delle tabelle: {e}")

if __name__ == "__main__":
    engine = connessione_database()
    crea_tabelle(engine)
    stampa_tabelle_presenti(engine)
