# CREATE
SQL ile yeni bir tablo oluşturmak için CREATE anahtar kelimesi kullanılır. 

#### CREATE TABLE <tablo_adi> (<sütun_adi1> <veri_tipi> <contraint>, <sütun_adi2> <veri_tipi2> <contraint2> );

#### CREATE TABLE author( id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, email VARCHAR(100), birthday DATE);

Burada tanımladığımız SERIAL veri tipi otomatik olarak artan bir veri tipidir. Kullanıcıdan istenmez.

Aynı tablodan aynı şekilde bir tane daha oluşturmak istediğimiz zaman LIKE kullanılır.
#### CREATE TABLE author2 (LIKE author)

Bir tabloyu içindeki verilerle birlikte kopyalamak istersek AS anahtar kelimesi kullanılır.

#### CREATE TABLE author3 AS SELECT * FROM author;

# INSERT INTO
Tabloya veri eklemek için INSERT INTO anahtar kelimesi kullanılır

#### INSERT INTO author (first_name, last_name, email, birthday) VALUES ('Haruki', 'Murakami', 'hm@gmail.com', '1948-11-07'), ('Sabahattin', 'Ali', 'sa@gmail.com', '1914-07-11');
id otomatik olarak arttığı için veri girişi yapmadık.

Farklı bir tablodan veri kopyalarken yine INSERT INTO kullanılır.
#### INSERT INTO author2 SELECT * FROM author WHERE first_name = 'Sabahattin Ali';

# DROP
Bir tablo silmek istediğimiz zaman DROP kullanılır.

#### DROP TABLE <tablo_adi>

Eğer ki olmayan bir tablo adi girdiğimizde hata almamak için IF EXIST yapısı kullanılır.

#### DROP TABLE IF EXIST author4;
