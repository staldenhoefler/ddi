SELECT
    k.vorname,
    k.nachname,
    b.customerID,
    b.orderID,
    SUM(p.preis * op.menge) AS gesamtwert
FROM
    bestellungen b
JOIN
    bestelldetails op ON b.orderID = op.orderID
JOIN
    produkte p ON op.productID = p.productID
JOIN
    kunden k ON b.customerID = k.customerID
GROUP BY
    b.customerID, b.orderID, k.vorname, k.nachname
ORDER BY
    gesamtwert DESC;