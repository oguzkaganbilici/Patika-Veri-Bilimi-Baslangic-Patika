# JOIN
Veri tabanları çoğunlukla birbiri ile ilişkili olan tablolarlardan oluşur. Bu birbiri ile ilişkili olan tablolarda ki verileri farklı JOIN yapıları kullanarak birleştirip daha anlamlı veriler haline getirebiliriz.

## Inner Join
INNER JOIN yapısı sayesinde birbiriyle ilişkili olan tabloların birbiriyle eşleşen(kesişen) verilerini sıralayabiliriz. Senaryomuzda kitapları gösterdiğimiz book tablosundaki ID sütunu ve yazarları gösterdiğimiz author tablosundaki author_id sütunları sayesinde her iki tablodan daha anlamlı sonuçlar elde edebiliriz.

#### SELECT book.title, author.first_name, author.last_name FROM book INNER JOIN author ON author.id = book.author.id;  

- INNER yazmasak da default olarak INNER JOIN olarak kabul edecektir.

#### SELECT book.title, author.first_name, author.last_name FROM book  JOIN author ON author.id = book.author.id;

- INNER JOIN yapısında FROM'dan sonra yazdığımız tablo adı farketmez. iki tablodan birisini yazabiliriz. 

![image](https://user-images.githubusercontent.com/45708619/234887243-97b6bbc8-5a73-4d6e-ac4f-059917ddaf3c.png)

## LEFT JOIN 
LEFT JOIN yapısındaki tablo birleştirmesinde, birleştirme işlemi tablo 1(sol tablo) üzerinden gerçekleştirilir.  Senaryomuzda şu şekilde düşünelim, eğer tablo 1 book tablosunu aldığımızda öncelikle book tablosundaki ilgili sütundaki tüm verileri alacağız, sonrasında bu verilerin eşleştiği ilgili tablo 2 sütundaki verileri alacağız. 

- Tablo 1 de olup tablo 2'de olmayan verilerin yerine NULL değeri kullanılır.

#### SELECT title, first_name, last_name FROM author LEFT JOIN book ON author.id = book_author_id;

- Bu sorguda 1. tablo ile 2. tablonun yerleri değiştiğinde aynı sonuçlar elde etmeyiz. Bu sebeple LEFT JOIN simetrik değildir.

- Eğer ki sorgumuz sonucunda NULL değerler görmek istemiyorsak sorgumuza WHERE .... IS NOT NULL; gibi sorgular ekleyebiliriz.
![image](https://user-images.githubusercontent.com/45708619/235300555-360be59a-215d-4dad-b516-7b82ebc347c3.png)


## RIGHT JOIN
RIGHT JOIN yapısındaki tablo birleştirmesinde, birleştirme işlemi tablo 2(sağ tablo) üzerinden gerçekleştirilir. Senaryomuzu şu şekilde düşünelim, eğer tablo 2 olarak author tablosunu aldığımızda öncelikle author tablosunun ilgili sütunundaki tüm verileri alacağız, sonrasında bu verilerin eşleştiği tablo 1'in ilgili sütunundaki verileri alacağız. 

- Tablo 2 de olup tablo 1 de olmayan veriler için NULL değeri kullanılır.

#### SELECT author.first_name, author.last_name, book.title FROM book RIGHT JOIN author ON author.id = book.id

![image](https://user-images.githubusercontent.com/45708619/235302776-6e907340-1b32-424e-8fe4-93aa1f1c8ef0.png)