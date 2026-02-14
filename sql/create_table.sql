CREATE TABLE IF NOT EXISTS sales (
    transactionno VARCHAR(20),
    date DATE,
    productno VARCHAR(20),
    productname TEXT,
    price NUMERIC,
    quantity INTEGER,
    customerno BIGINT,
    country VARCHAR(100)
);