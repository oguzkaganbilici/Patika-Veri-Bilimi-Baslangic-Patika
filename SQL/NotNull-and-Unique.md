# NOT NULL
Birçok durumda bizler herhangi bir sütuna yazılacak olan verilere belirli kısıtlamalar getirmek isteriz. Örneğin yaş sütununda sadece sayısal verilerin olmasını isteriz ya da kullanıcı adı sütununa bilinmeyen (NULL) değerinin olmasını istemeyiz. Bu gibi durumlarda CONSTRAINT kısıtlaması kullanılır.

Örneğin,

#### CREATE TABLE users (id SERIAL INTEGER, username VARCHAR(50), email VARCHAR(50), age INTEGER )
olarak bir tablo oluşturalım. Burada username sütununa veri girmediğimizde o sütunlar NULL değerler içerecektir. Bunu önlemenin 2 yolu var. Ya tabloyu oluştururken NOT NULL şartı koyacaktık fakat tablomuz zaten oluştu. Bu duruma olan tabloya kural ekleyeceğiz.

#### ALTER TABLE users COLUMN username SET NOT NULL;

Eğer sütunumuzda hali hazırda NULL değerler varsa yukarıdaki sorgu hata verecektir.
Olan NULL değerleri çıkarmak için;

#### DELETE FROM users WHERE username IS NULL

# Unique

UNIQUE kısıtlaması ile uyguladığımız sütundaki verilerin birbirlerinden farklı,benzersiz olmalarını isteriz. 

NOT NULL kısıtlamalarında olduğu gibi tablo oluştururken veya ALTER komutu ile beraber oluşturulan tablo üzerinde de kullanabiliriz.

#### ALTER TABLE users ADD UNIQUE(email)

