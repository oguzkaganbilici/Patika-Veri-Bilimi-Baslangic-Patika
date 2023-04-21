# Sayısal Veriler
- smallint, integer, bigint veri tiplerini tam sayıları ifade etmek için kullanılır. 
## SMALLINT 
 - 2 byte'lık yerde saklanır. yani 16 bite eşittir.
 - En fazla 2^16 tane veri aralığı vardır. Yani -32768 ile 32767 arasında değer alır.
 
 ## INTEGER
 - 4 bytle'lık yerde saklanır.  32 bite eşittir.
 - En fazla 2^32 tane veri aralığı vardır. -2147483648 ile 2147483647 arasında değer alır.
 
 ## BIGINT
 - 8 byte'lık yerde saklanır. 65 bite eşittir.
 
 
 -smallserial, serial, bigserial'lerde bir tamsayı veritipidir. Diğer tam sayı veri tiplerinden farkı olarak otomatik olarak birer birer artmasıdır.

------------


- decimal, numeric, real, double precision veri tipleri ondalıklı sayıları ifade etmek için kullanılır. 

- real veri tipinde virgülden sonra 8, double precision'da 16, numeric'te ise 20 adet ondalıklı sayı saklanabilir.

- decimal, float4 ve float8 sırasıyla numeric, real ve double precision'a eşittir. 

- SQL'de veri tipleri arasında dönüşüm yaparken;
#### SELECT (10.444444 ::REAL)
#### SELECT (10.444444 ::DECIMAL)
şeklinde yapabiliriz.

-------

# Karakter Veri Tipleri
Sınırlı sayıda veri tipi için VARCHAR(x) ve CHAR(x) veri tipi kullanılır. 
VARCHAR veri tipi doldurulmayan karakterleri yok sayar, CHAR ise doldurulmayan karakterler için de boşluk ayırır. Sınırsız karakter kullanımı içinse TEXT veri tipi kullanılır. 

#### SELECT ('Lorem'::CHAR(10) )
'Lorem' 5 karakterli olmasına rağmen 10 karakter boş bırakır.
#### SELECT ('Lorem ipsum dolor sit amet'::CHAR(10))
'Lorem ipsum dolor sit amet' 26 karakterli olmasına rağmen 10 karakter boş bırakır
#### SELECT ('Lorem'::VARCHAR(10))
'Lorem' 5 karakterli olduğundan 5 karakter boş bırakır.
#### SELECT ('Lorem ipsum dolor sit amet'::VARCHAR(10))
'Lorem ipsum dolor sit amet' 26 karakterli olmasına rağmen 10 karakter boş bırakır
#### SELECT ('Lorem ipsum dolor sit amet'::TEXT)
'Lorem ipsum dolor sit amet' 26 karakterli olmasından dolayı 26 karakter boş bırakır.
![image](https://user-images.githubusercontent.com/45708619/233741137-5e10e439-a552-4c30-b7d0-952aa22118c3.png)

-----
#  Boolean Veri Tipleri
True, False veya Null değerini alabilirler. 

- True: true, yes, on,1
- False: false, no, off, 0

#### SELECT ('no'::BOOLEAN)
#### SELECT (yes::BOOLEAN)
-----

# Zaman Veri Tipleri
Genellikle yyyy-aa-gg olarak yazılır.

#### SELECT('1996-10-15'::DATE)
#### SELECT('DEC-02-1900'::DATE)
#### SELECT('DEC 03 1900'::DATE)
#### SELECT('1900 December 03'::DATE)

#### SELECT('03:44'::TIME)
#### SELECT('03:44 AM'::TIME)
#### SELECT('02:16'::TIME WITH TIME ZONE)
#### SELECT('1980 December 03 02:16:06'::TIMESTAMP) 

![image](https://user-images.githubusercontent.com/45708619/233741158-e4044e76-2927-43f1-b588-a94f88e395c4.png)
