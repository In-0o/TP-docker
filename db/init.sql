CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value VARCHAR(255) NOT NULL
    );

INSERT INTO items (name, value) VALUES
    ('Item 1', 'Value 1'),
    ('Item 2', 'Value 2'),
    ('Item 3', 'Value 3');