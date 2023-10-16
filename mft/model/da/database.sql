create database rent_db;

create table rent_db.stuff_tbl
(
    code           int primary key auto_increment,
    name           nvarchar(20),
    brand          nvarchar(20),
    description    nvarchar(255),
    price          int,
    image          nvarchar(50),
    rent_db_condition nvarchar(255),
    rent_db_price     int
);

create table rent_db.user_tbl
(
    code     int primary key auto_increment,
    name     nvarchar(20),
    family   nvarchar(20),
    gender   tinyint,
    age      int,
    username nvarchar(20),
    password nvarchar(20),
    email    nvarchar(50),
    role     tinyint,
    state    nvarchar(20),
    city     nvarchar(20),
    address  nvarchar(100),
    phone    nvarchar(15),
    photo    nvarchar(50),
    status   tinyint default 1,
    score    int
);

create table rent_db.rent_tbl
(
    code         int primary key auto_increment,
    sender_code  int,
    renter_code  int,
    stuff_code   int,
    rent_db_date    datetime,
    return_date  datetime,
    stuff_status tinyint default 1,
    rent_db_price   int,
    information  nvarchar(255),
    FOREIGN KEY(sender_code) REFERENCES user_tbl(code),
    FOREIGN KEY(renter_code) REFERENCES user_tbl(code),
    FOREIGN KEY(stuff_code) REFERENCES stuff_tbl(code)
);
