drop table if exists user_db;
create table user_db (
  id integer primary key autoincrement,
  email string not null,
  password string not null
);