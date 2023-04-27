# JOIN
Veri tabanları çoğunlukla birbiri ile ilişkili olan tablolarlardan oluşur. Bu birbiri ile ilişkili olan tablolarda ki verileri farklı JOIN yapıları kullanarak birleştirip daha anlamlı veriler haline getirebiliriz.

## Inner Join
INNER JOIN yapısı sayesinde birbiriyle ilişkili olan tabloların birbiriyle eşleşen(kesişen) verilerini sıralayabiliriz. Senaryomuzda kitapları gösterdiğimiz book tablosundaki ID sütunu ve yazarları gösterdiğimiz author tablosundaki author_id sütunları sayesinde her iki tablodan daha anlamlı sonuçlar elde edebiliriz.

#### SELECT book.title, author.first_name, author.last_name FROM book INNER JOIN author ON author.id = book.author.id;  

- INNER yazmasak da default olarak INNER JOIN olarak kabul edecektir.

#### SELECT book.title, author.first_name, author.last_name FROM book  JOIN author ON author.id = book.author.id;

- INNER JOIN yapısında FROM'dan sonra yazdığımız tablo adı farketmez. iki tablodan birisini yazabiliriz. 

![image](https://user-images.githubusercontent.com/45708619/234887243-97b6bbc8-5a73-4d6e-ac4f-059917ddaf3c.png)
