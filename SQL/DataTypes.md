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

![image](https://user-images.githubusercontent.com/45708619/233368034-74b83a39-4b94-46bc-8ee2-0f116d844407.png)
