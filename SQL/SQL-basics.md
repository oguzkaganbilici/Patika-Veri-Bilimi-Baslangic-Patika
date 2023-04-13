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

NOT: Bazı SQL dillerinde ~~ LIKE ve ~~ * ILIKE, ! NOT  yerine geçer.
#### SELECT * FROM actor WHERE first_name ~~ 'P%'
#### SELECT * FROM actor WHERE first_name ~~ * 'P%'
#### SELECT * FROM actor WHERE first_name !~~ 'P%'

