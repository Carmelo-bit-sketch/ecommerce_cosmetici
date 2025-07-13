-- DDL: creazione tabelle principali (estratto semplificato)
CREATE DATABASE IF NOT EXISTS ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ecommerce;

CREATE TABLE CLIENTE (
    IDCliente INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Cognome VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20),
    DataIscrizione DATE NOT NULL
);

CREATE TABLE INDIRIZZO (
    IDIndirizzo INT AUTO_INCREMENT PRIMARY KEY,
    Via VARCHAR(100) NOT NULL,
    NumeroCivico VARCHAR(10) NOT NULL,
    Città VARCHAR(50) NOT NULL,
    CAP VARCHAR(10) NOT NULL
);

CREATE TABLE CLIENTE_INDIRIZZO (
    IDCliente INT,
    IDIndirizzo INT,
    PRIMARY KEY(IDCliente, IDIndirizzo),
    FOREIGN KEY (IDCliente) REFERENCES CLIENTE(IDCliente),
    FOREIGN KEY (IDIndirizzo) REFERENCES INDIRIZZO(IDIndirizzo)
);

-- Esempio DML: inserimento dati
INSERT INTO CLIENTE (Nome, Cognome, Email, Password, Telefono, DataIscrizione)
VALUES ('Mario', 'Rossi', 'mario.rossi@mail.it', 'password', '3331112222', CURDATE());
