# Odev9
1)city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.
SELECT city, country FROM city INNER JOIN country ON city.city_id = country.country_id

2)customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.
SELECT payment.payment_id, customer.first_name, customer.last_name FROM customer INNER JOIN payment on customer.customer_id = payment.customer_id

3)customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.
SELECT * FROM customer INNER JOIN rental ON customer.customer_id = rental.customer_id

# Odev10
1)city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz LEFT JOIN sorgusunu yazınız.
SELECT city, country from city LEFT JOIN country ON country.country_id = city.country_id

2)customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz RIGHT JOIN sorgusunu yazınız.
SELECT first_name, last_name, payment_id FROM customer RIGHT JOIN payment ON customer.customer_id = payment.customer_id

3)customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz FULL JOIN sorgusunu yazınız.
SELECT * FROM customer FULL JOIN rental ON customer.customer_id = rental.customer_id

# Odev11
1)actor ve customer tablolarında bulunan first_name sütunları için tüm verileri sıralayalım.
(SELECT first_name FROM actor) UNION (SELECT first_name FROM customer)

2)actor ve customer tablolarında bulunan first_name sütunları için kesişen verileri sıralayalım.
(SELECT first_name FROM actor) INTERSECT (SELECT first_name FROM customer)

3)actor ve customer tablolarında bulunan first_name sütunları için ilk tabloda bulunan ancak ikinci tabloda bulunmayan verileri sıralayalım.
(SELECT first_name FROM actor) EXCEPT (SELECT first_name FROM customer)

4)İlk 3 sorguyu tekrar eden veriler için de yapalım.
(SELECT first_name FROM actor) UNION ALL (SELECT first_name FROM customer)
(SELECT first_name FROM actor) INTERSECT ALL (SELECT first_name FROM customer)
(SELECT first_name FROM actor) EXCEPT ALL (SELECT first_name FROM customer)

# Odev12 
1)film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?
SELECT COUNT(title) FROM film WHERE length > (SELECT AVG(length) FROM film)

2)film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?
SELECT title FROM film WHERE rental_rate = ALL ( SELECT MAX(rental_rate) FROM film )

3)film tablosunda en düşük rental_rate ve en düşük replacement_cost değerlerine sahip filmleri sıralayınız.
SELECT title FROM film WHERE rental_rate = ALL (SELECT MIN(rental_rate) FROM film) AND replacement_cost = ALL (SELECT MIN(replacement_cost) FROM film)

4)payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.
SELECT customer FROM payment WHERE ...
