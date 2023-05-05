# Subqueires (altsorgular)

Bir sorgu içerisinde, o sorgunun ihtiyaç duyduğu veri veya verileri getiren sorgulardır.

Örneğin bookstore veritabanında "Gülün Adı" isimli bir kitabımızın sayfa sayısı 466 olsun. Bu kitaptan daha fazla sayıda sayfası bulunan kitapları aşağıdaki sorgu yardımıyla sıralayabiliriz.

#### SELECT * FROM book WHERE page_number > 466;
#### SELECT page_number FROM book WHERE title = 'Gülün Adı';
Her iki sorguyu birleştirirsek;

#### SELECT * FROM book WHERE page_number > ( SELECT page_number FROM book WHERE title = 'Gülün Adı'); 

Başka bir örnek:

#### SELECT title, page_number, (SELECT MAX(page_number) FROM book), (( SELECT MAX(page_number) FROM book ) - page_number ) AS differ FROM book WHERE page_number > (SELECT page_number FROM book WHERE title = 'Gülün Adı');

## ANY ve ALL
Any ve operatorleri alt sorgularda sık sık kullanılır ve tek bir sütunda bulunan bir değerle bir değer dizisinin karşılaştırılmasını sağlar.

### ANY
Alt sorgudan gelen herhangi bir değer koşulu sağlanması durumunda TRUE olarak ilgili değerin koşul sağlanmasını sağlar. bookstore veritabanında yapmış olduğumuz aşağıdaki sorguyu inceleyelim.

#### SELECT first_name, last_name FROM author WHERE id = ANY ( SELECT id FROM book WHERE title = 'Abe Lincoln in Illinois' OR title = 'Saving Shiloh' ) ;

Yukarıda görmüş olduğunuz gibi alt sorgudan id gelecektir. Bu id değerinin her ikisi de birbirinden bağımsız olarak ana sorgudaki id sütununda bulunan değerler ile eşleştiği için sorgu sonucunda oluşan sanal tabloda id değeri 4 ve 5 olan yazarlara ait first_name ve last_name değerlerini göreceğiz.

### ALL 
Alt sorgudan gelen tüm değerlerin koşulu sağlaması durumunda TRUE olarak döner. 
bookstore veritabanındaki yine aynı sorguyu inceleyelim.

#### SELECT first_name, last_name FROM author WHERE id = ALL ( SELECT id FROM book WHERE title ='Abe Lincoln in Illinois' OR title = 'Saving Shiloh' )

Alt sorgu tarafından 4 ve 5 id leri gelecektir. Aynı anda 4 ve 5 'in bu koşulu sağlaması olanaksız olduğu için herhangi bir değer dönmeyecektir. 
