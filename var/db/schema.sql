DROP TABLE if EXISTS users;

CREATE TABLE users {
	userId INTEGER PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	email VARCHAR(30) NOT NULL,
	password VARCHAR(20) NOT NULL;
};
