SELECT
    p.productID,
    p.Name,
    p.Kategorie,
    p.Preis,
    pe.attributname,
    pe.attributwert
FROM
    produkte p
JOIN
    produkteigenschaften pe ON p.productID = pe.productID
WHERE
    pe.AttributName = 'color' AND pe.AttributWert = 'Rot'



