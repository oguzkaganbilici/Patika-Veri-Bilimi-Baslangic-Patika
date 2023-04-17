# SELECT

SQL komutları arasında sorgu cümleleridir. Tablolardan veri çekmemizi sağlar.

#### SELECT <sütun_adi>,  <sütün_adi2> FROM <tablo_adi>

Eğer tablonun sütunlarındaki bütün verileri çekmek için * karakterinden faydalanırız.

#### SELECT * FROM <tablo_adi>

SQL komutlarının büyük-küçük harf duyarlılığı yoktur.

#### SELECT * FROM <tablo_adi> = select * from <tablo_adi>

# WHERE

SELECT komutu ile yaptığımız çalışmalarda bizler tüm sütunların veya ilgili sütunlarda bulunan verilerin tamanını çekmek isteriz. 
Çoğu durumda ise verilerin tamamını değil belirli koşulları sağlayan verileri görmek isteriz Bunun için WHERE kullanırız.

#### SELECT <sütun_adi>, <sütun_adi> FROM <tablo_adi> WHERE <kosul>

#### SELECT title, replacement_cost FROM film WHERE replacement_cost = 14.99;
  
![image](https://user-images.githubusercontent.com/45708619/230840484-a7f5636e-2b9e-46a0-93b6-074ee3dc33ba.png)

Birden fazla şartımız olduğunda iki sorgu arasına AND veya OR  kullanılır.
#### SELECT * FROM actor WHERE first_name='Penelope' AND last_name='Monroe' AND ...

Belirtilen şartı sağlamayan durumları sorgulamak istediğimizde sorgumuzun başında NOT kullanılır.

#### SELECT * FROM film WHERE NOT rental_rate = 4.99

# BETWEEN & IN
Belirli aralıkta bulunan verileri sıralamak için BETWEEN... AND yapısı da kullanılabilir.  

#### SELECT * FROM film WHERE length BETWEEN 100 AND 140;
Burada dikkat edilmesi gereken nokta 100 ve 140 sınır değerleri aralığa dahildir.
  
#### SELECT title, length FROM film WHERE length NOT BETWEEN 90 AND 120  === length < 90 OR length > 120

Çok uzun OR sorguları yazmak yerine istenilen değerleri liste haline getirilip IN anahtar kelimesi kullanılabilirdi.
#### SELECT <sütun_adi> FROM <tablo_adi> WHERE length IN (100,140,150,160,170...) == length = 100 OR length = 140 OR length = 150 OR length = 160 OR length = 170 
#### SELECT <sütun_adi> FROM <tablo_adi> WHERE length NOT IN (100,140,150,160,170...)
  
# LIKE ve ILIKE

Bazı durumlarda tam eşleşme yerine belirli şablonlara uyan koşulların sağlanmasını isteriz.
Örneğin first_name sütunun 'Penelope' değerine eşit olmasını değil, ilk harfin 'P' olması koşulunu sağlar. Bunun için LIKE operatörü kullanılır.

#### SELECT * FROM actor WHERE first_name LIKE 'P%' 
#### SELECT * FROM actor WHERE first_name LIKE '%P' --> p ile biten
#### SELECT * FROM actor WHERE first_name LIKE 'P%e' --> p ile başlayıp e ile biten

Burada LIKE operatörü büyük küçük harf duyarlıdır. Yani 'A%' ile 'a%' aynı sonuçları vermeyecektir. Bunu önlemek için ILIKE anahtar kelimesi kullanılabilir

#### SELECT * FROM actor WHERE first_name ILIKE 'a%'
#### SELECT * FROM actor WHERE first_name ILIKE '%a'

#### SELECT * FROM actor WHERE first_name NOT LIKE 'P%' --> p ile başlamayan

Burada kullanılan % karakteri sıfır, bir veya daha fazla karakteri temsil eder ve Wildcard olarak isimlendirilir. Bir diğer Wildcard karakteri ise "_" 'tir. 
_sadece bir harfi temsil eder.

#### SELECT * FROM actor WHERE first_name LIKE 'J_an'; --> "Jean, Juan, Jian, Joan olabilir"

NOT: Bazı SQL dillerinde ~~ LIKE ve ~~* ILIKE, ! NOT  yerine geçer.
#### SELECT * FROM actor WHERE first_name ~~ 'P%'
#### SELECT * FROM actor WHERE first_name ~~* 'P%'
#### SELECT * FROM actor WHERE first_name !~~ 'P%'

  # DISTINCT ve COUNT
Bir sütundaki farklı (unique) değerleri döndürmek için Distinct anahtar kelimesi kullanılır

#### SELECT DISTINCT rental_rate FROM film;
rental_rate'teki farklı değerleri döndürür

Bir sorgu sonucunda oluşan veri sayısını Count anahtar kelimesi ile buluruz. 

#### SELECT COUNT(*) FROM  actor WHERE first_name = 'Penelope';
Penelope adındaki aktörlerin sayısını döndürür

#### SELECT COUNT(*) FROM actor WHERE first_name LIKE 'P%'
Adı P ile başlayan aktör sayısını döndürür

#### SELECT COUNT(DISTINCT first_name ) FROM actor
Kaç farklı first_name sayısını döndürür.
  
# ORDER BY
Order By anahtar kelimesi sayesinde bizler verilerimizi herhangi bir sütunda bulunan değerlere göre azalan veya artan bir şekilde sıralayabiliriz.

#### SELECT <sütun_adi> FROM <tablo_adi> ORDER BY <sütun_adi> ASC/DECS;
#### SELECT * FROM film ORDER BY title (ASC);
Varsayılan olarak ASC gelir.
ASC -> Ascending (Artan)
DECS -> Descending (Azalan)

Order by koşuldan sonra yazılır

#### SELECT title, rental_rate, length FROM film WHERE title ILIKE 'a%' ORDER BY rental_rate ASC, length DESC

# LIMIT ve OFFSET
Bazı durumlarda ise koşullarımızı sağlayan verilerin  tamamını değil belirli sayıda olanlarını sıralamak isteriz, bunun için LIMIT anahtar kelimesini kullanırız.

#### SELECT * FROM film WHERE title LIKE 'B%' ORDER BY length DESC LIMIT 10;
 en uzun ilk 10 film
 
Bazı durumlarda sonuç olarak gördüğümüz veri grubu içerisinden bazılarını geçmek isteriz.
Örneğin B ile başlayan filmleri uzunluklarına göre sıralayalım ve en uzun 6 filmi pass geçelim ve sonrasındaki 4 filmi sıralayalım.

#### SELECT * FROM film WHERE title LIKE 'B%' ORDER BY length DESC, OFFSET 6, LIMIT 4

# AGGREGATE FONKSİYONLAR
Aggregate fonksiyonlar yardımıyla bizler veri kümelerimizden sonuçlar çıkarabiliriz. 
-Kaç adet müşterimiz var?
-Elimizde bulunan filmlerin ort uzunluğu nedir? gibi..

## COUNT
Toplam kaç tane veri olduğunu ararken Count anahtar kelimesi kullanılabilir.
#### SELECT COUNT(*) FROM film

## MAX - MIN
Veri setinde maksimum ve minumum değerleri bulmak için Max-Min anahtar kelimesinden yararlanılır
#### SELECT MAX(replacement_cost) FROM film
#### SELECT MIN(replacement_cost) FROM film

## AVG
Bir veri setinin ortalama değerini bulmak için Avg anahtar kelimesi kullanılır
#### SELECT AVG(length) FROM film

## ROUND
Veri setindeki bir sayıyı yuvarlamak için kullanılır.
Round fonksiyonu 2 parametre alır. İlk parametre yuvarlanacak değer, ikinci parametrede ise kaç karaktere yuvarlanacağını belirtilir.
#### SELECT ROUND(AVG(length), 3) FROM film

##SUM
Bir sütundaki tüm verileri toplamak için Sum anahtar kelimesi kullanılır.
#### SELECT SUM(rental_rate) FROM film

Birden fazla aggregate fonksiyonlarını birlikte kullanabiliriz.
#### SELECT MAX(length), MIN(length), SUM(replacement_cost) FROM film;

#### SELECT MAX(length) FROM film WHERE rental_rate IN (0.99, 2.99);

# GROUP BY
Bazı durumlada veri kümesini gruplandırarak veriler elde etmek isteriz. Örneğin veri setinde şehirler ve müşteri isimleri olsun. Burada hangi şehirde kaçar tane müşteri olduğunu bulmak istersek Group By anahtar kelimesini kullanırız.

#### SELECT rental_rate, MAX(length) FROM film GROUP BY rental_rate 
#### SELECT rental_rate, COUNT(*) FROM GROUP_BY rental_rate

Burada önemli nokta SELECT'ten sonra yazacağımız ifade GROUP_BY'ın kapsadığı bir sütun olması gerekir. Aksi takdirde alaksız iki sütunu yazdığımızda hata alırız.

#### SELECT rating, COUNT(*) FROM film GROUP BY rating
#### SELECT replacement_cost, MIN(length) FROM film GROUP BY replacement_cost
#### SELECT replacement_cost, rental_rate,MIN(length) FROM film GROUP BY replacement_cost, rental_rate 
replacement_cost ve rental_rate degerlerini eşleyip o değerlerin en kısa olanını bulur 

#### SELECT replacement_cost, rental_rate, MIN(length) FROM film GROUP BY replacement_cost, rental_rate ORDER BY replacement_cost ASC, rental_rate DESC;

# HAVING
Having anahtar kelimesi sayesinde gruplandırılmış verimize koşullar uygulayabiliriz.
#### SELECT rental_rate, COUNT(*) FROM film GROUP BY rental_rate HAVING COUNT(*) > 325;
Film sayısı 325'ten büyük rental_rate'lere göre gruplanmış veriyi döndürür

#### SELECT staff_id, COUNT(*) FROM payment GROUP BY staff_id HAVING COUNT(*) > 7300
Toplam satışı 7300'den büyük olan çalışan ID'lerini gruplandırır.

# ALIAS (AS)
AS anahtar kelimesi sayesinde sorgular sonucu oluşturduğumuz sanal tablolar, sütunlara geçiçi isimler verebiliriz.

#### SELECT <sütun_adı> AS <geçici_ad> FROM <tablo_adı>;
Burada AS optinional olarak kullanılır yani AS yazmayıp;
#### SELECT first_name isim, last_name soyisim FROM actor 
olarak da kullanabiliriz.
#### SELECT first_name "isim test", last_name "soyisim test" FROM actor 

#CONCAT
İki sütunu geçiçi olarak birleştirmek istediğimizde Concat fonksiyonu kullanılır.

#### SELECT CONCAT(first_name,' ', last_name) AS 'isim soyisim' FROM actor







