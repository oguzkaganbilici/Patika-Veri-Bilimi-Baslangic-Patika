1)city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.
SELECT city, country FROM city INNER JOIN country ON city.id = country.id

2)customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.
SELECT payment_id, payment.first_name, payment.last_name FROM customer INNER JOIN payment ON customer.payment_id = payment.payment_id;

3)customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.
SELECT customer.first_name, customer.last_name, rental.rental_id FROM customer INNER JOIN rental ON customer.id = rental.rental_id;

