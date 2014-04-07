Create table IF NOT EXISTS books( id integer primary key, title text);
Create table IF NOT EXISTS authors(id integer primary key, name text);
Create table IF NOT EXISTS literature(  authors_id integer,
										books_id integer, 
										foreign key (authors_id) References authors(id),
										foreign key (books_id) References books(id));