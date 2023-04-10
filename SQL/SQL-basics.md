SELECT
SQL komutları arasında sorgu cümleleridir. Tablolardan veri çekmemizi sağlar.

SELECT <sütun_adi>, <sütün_adi2> FROM <tablo_adi>

Eğer tablonun sütunlarındaki bütün verileri çekmek için * karakterinden faydalanırız.

SELECT * FROM <tablo_adi>

SQL komutlarının büyük-küçük harf duyarlılığı yoktur.

SELECT * FROM <tablo_adi> = select * from <tablo_adi>

*WHERE*
SELECT komutu ile yaptığımız çalışmalarda bizler tüm sütunların veya ilgili sütunlarda bulunan verilerin tamanını çekmek isteriz. 
Çoğu durumda ise verilerin tamamını değil belirli koşulları sağlayan verileri görmek isteriz Bunun için WHERE kullanırız.

SELECT <sütun_adi>, <sütun_adi> FROM <tablo_adi> WHERE <kosul>

SELECT title, replacement_cost FROM film WHERE replacement_cost = 14.99;
  
![image](https://user-images.githubusercontent.com/45708619/230840484-a7f5636e-2b9e-46a0-93b6-074ee3dc33ba.png)
