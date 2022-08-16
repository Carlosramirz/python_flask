CREATE TABLE pelis (
    id char(36) not null Primary Key,
    titulo varchar(50),
    duracion varchar(3),
    estreno date
);

INSERT INTO pelis (id, titulo, duracion, estreno) VALUES ('3b920204-63aa-475a-b817-bf056b3dc224', 'Gladiator', 120,'2001-01-05');
INSERT INTO pelis (id, titulo, duracion, estreno) VALUES ('db130ef5-6f85-4d28-879a-33020a3a49df', 'Iron-Man2', 115,'2010-05-24');
INSERT INTO pelis (id, titulo, duracion, estreno) VALUES ('ea103dc2-4cb3-4bd0-90d4-62d8556eee25', 'Iron-Man', 112,'2008-05-24');

CREATE TABLE usuarios (
    id varchar(36) not null Primary Key,
    username varchar(12),
    password varchar(150),
    fullname varchar(36)
);

INSERT INTO usuarios (id, username, password, fullname) VALUES ('6c6bc9e8-5972-4d64-a47c-7d9a6c0bfd3a', 'Ramirzcarlos', 'sha256$S4ZreOWW4bky4o14$a45b2cdeeb235faeeb669d56b7eaf449a0039234037c14863a10c713c0c5e512', 'Carlos Ramírez');