-- Database: db_final_orm

DROP DATABASE IF EXISTS db_final_orm;

CREATE DATABASE db_final_orm
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Chile.1252'
    LC_CTYPE = 'Spanish_Chile.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create user userdjango with password 'userdjango'