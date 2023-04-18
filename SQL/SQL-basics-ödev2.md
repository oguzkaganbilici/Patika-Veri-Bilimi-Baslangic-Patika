# Odev5

1)film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en uzun (length) 5 filmi sıralayınız.
SELECT title,length FROM film WHERE title LIKE '%n' ORDER BY length DESC LIMIT 5

2)film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en kısa (length) ikinci(6,7,8,9,10) 5 filmi(6,7,8,9,10) sıralayınız.
SELECT title,length FROM film WHERE title LIKE '%n' ORDER BY length OFFSET 5 LIMIT 5 

3)customer tablosunda bulunan last_name sütununa göre azalan yapılan sıralamada store_id 1 olmak koşuluyla ilk 4 veriyi sıralayınız.
SELECT * FROM customer WHERE store_id=1 ORDER BY last_name DESC OFFSET 4


# Odev6
1)film tablosunda bulunan rental_rate sütunundaki değerlerin ortalaması nedir?
SELECT AVG(rental_rate) FROM film

2)film tablosunda bulunan filmlerden kaç tanesi 'C' karakteri ile başlar?
SELECT COUNT(title) FROM film WHERE title LIKE 'C%'

3)film tablosunda bulunan filmlerden rental_rate değeri 0.99 a eşit olan en uzun (length) film kaç dakikadır?
SELECT MAX(length) FROM film WHERE rental_rate = 0.99

4)film tablosunda bulunan filmlerin uzunluğu 150 dakikadan büyük olanlarına ait kaç farklı replacement_cost değeri vardır?
SELECT COUNT(DISTINC(replacement_cost)) FROM film WHERE length >=150

# Odev7
1)film tablosunda bulunan filmleri rating değerlerine göre gruplayınız.
SELECT * FROM film GROUP BY rating

2)film tablosunda bulunan filmleri replacement_cost sütununa göre grupladığımızda film sayısı 50 den fazla olan replacement_cost değerini ve karşılık gelen film sayısını sıralayınız.
SELECT replacement_cost, COUNT(*) FROM film GROUP BY replacement_cost HAVING COUNT(*) > 50

3)customer tablosunda bulunan store_id değerlerine karşılık gelen müşteri sayılarını nelerdir? 
SELECT store_id, COUNT(customer_count) FROM customer GROUP BY store_id 

4)city tablosunda bulunan şehir verilerini country_id sütununa göre gruplandırdıktan sonra en fazla şehir sayısı barındıran country_id bilgisini ve şehir sayısını paylaşınız.
SELECT country_id, COUNT(city) FROM city GROUP BY country_id ORDER BY COUNT(city) DESC LIMIT 1

# Odev8
1)test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.
CREATE TABLE employee id INTEGER, name VARCHAR(50), birthday DATE, email VARCHAR(100);

2)Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.
INSERT INTO employee (id, name, birthday, email) values (1, 'Lodovico', '1996-10-15', 'lsimmens0@creativecommons.org');

3)Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.
UPDATE employee SET name = "oguz" WHERE id = 1;
UPDATE employee SET birthday = "1995-10-15" WHERE name = "oguz";
UPDATE employee SET email = "okb@gmail.com" WHERE name = "oguz";

4)Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.
DELETE FROM employee WHERE id = 1;
DELETE FROM employee WHERE name = "oguz";
DELETE FROM employee WHERE email = "okb@gmail.com"






