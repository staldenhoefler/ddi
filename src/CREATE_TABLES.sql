-- Tabelle für Produkte
CREATE TABLE Produkte (
    productID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Kategorie VARCHAR(100),
    Preis DECIMAL(10, 2)
);

-- Tabelle für Produkteigenschaften
CREATE TABLE Produkteigenschaften (
    eigenschaftID SERIAL PRIMARY KEY,
    productID INT NOT NULL,
    AttributName VARCHAR(100),
    AttributWert VARCHAR(255),
    FOREIGN KEY (productID) REFERENCES Produkte(productID)
);

-- Tabelle für Kunden
CREATE TABLE Kunden (
    customerID SERIAL PRIMARY KEY,
    Vorname VARCHAR(100),
    Nachname VARCHAR(100),
    Geburtsdatum DATE,
    Email VARCHAR(255)
);

-- Tabelle für Bewertungen
CREATE TABLE Bewertungen (
    reviewID VARCHAR(255) PRIMARY KEY,
    productID INT NOT NULL,
    customerID INT NOT NULL,
    Sterne INT CHECK (Sterne BETWEEN 1 AND 5),
    Text TEXT,
    Datum DATE,
    FOREIGN KEY (productID) REFERENCES Produkte(productID),
    FOREIGN KEY (customerID) REFERENCES Kunden(customerID)
);


-- Tabelle für Bestellungen
CREATE TABLE Bestellungen (
    orderID SERIAL PRIMARY KEY,
    customerID INT NOT NULL,
    Datum DATE,
    Gesamtpreis DECIMAL(10, 2),
    FOREIGN KEY (customerID) REFERENCES Kunden(customerID)
);

-- Tabelle für Bestelldetails
CREATE TABLE Bestelldetails (
    detailID SERIAL PRIMARY KEY,
    orderID INT NOT NULL,
    productID INT NOT NULL,
    Name VARCHAR(255),
    Menge INT,
    Preis DECIMAL(10, 2),
    Zwischensumme DECIMAL(10, 2),
    FOREIGN KEY (orderID) REFERENCES Bestellungen(orderID),
    FOREIGN KEY (productID) REFERENCES Produkte(productID)
);
