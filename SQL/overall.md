1) isminde en az 4 tane e veya E bulunan kaç film vardır?
SELECT COUNT(title) FROM film WHERE title ILIKE '%e%e%e%e%" 

2) Kategori isimlerini ve kategori başına düşen film sayısını yazınız.
SELECT COUNT(*), category.name FROM category JOIN film ON film_category.category_id=category.category_id JOIN film ON film.film_id = film_category.film_id GROUP BY category.name

3)en çok film bulunan rating kategorisi hangisidir.
SELECT COUNT(*), rating FROM film GROUP BY rating ORDER BY COUNT(*) DESC LIMIT 1

4)Film tablosunda 'K' karakteri ile başlayan ve en uzun ve replacement_cost'u en az olan 3 filmi sıralayınız.
SELECT * FROM film WHERE title LIKE 'K%', ORDER BY length DESC, MIN(replacement_cost) LIMIT 3 

5)En çok alışveriş yapan müşterinin adı nedir?
SELECT first_name.customer, last_name.customer, SUM(amount)  FROM customer JOIN payment ON customer.customer_id=payment.customer_id GROUP BY customer_id ORDER BY SUM(amount) ASC LIMIT 1


