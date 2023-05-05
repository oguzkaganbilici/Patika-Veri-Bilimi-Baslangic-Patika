# Subqueires (altsorgular)

Bir sorgu içerisinde, o sorgunun ihtiyaç duyduğu veri veya verileri getiren sorgulardır.

Örneğin bookstore veritabanında "Gülün Adı" isimli bir kitabımızın sayfa sayısı 466 olsun. Bu kitaptan daha fazla sayıda sayfası bulunan kitapları aşağıdaki sorgu yardımıyla sıralayabiliriz.

#### SELECT * FROM book WHERE page_number > 466;
#### SELECT page_number FROM book WHERE title = 'Gülün Adı';
Her iki sorguyu birleştirirsek;

#### SELECT * FROM book WHERE page_number > ( SELECT page_number FROM book WHERE title = 'Gülün Adı'); 

Başka bir örnek:

#### SELECT title, page_number, (SELECT MAX(page_number) FROM book), (( SELECT MAX(page_number) FROM book ) - page_number ) AS differ FROM book WHERE page_number > (SELECT page_number FROM book WHERE title = 'Gülün Adı');
