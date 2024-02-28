# Iris Veri Seti PCA Görselleştirme

Bu repo, Iris veri setinin temel bileşen analizi (PCA) kullanılarak 2 boyuta indirgenmiş halinin görselleştirilmesini içerir.



## Veri Seti

Veri seti, ünlü iris veri setidir. Bu veri seti, iris bitkisinin üç farklı türüne (setosa, versicolor ve virginica) ait çeşitli özelliklerin (örneğin, çiçek yapraklarının uzunluğu ve genişliği) ölçümlerini içerir.



## PCA Analizi

PCA, veri setinin boyutunu azaltmak için kullanılan bir tekniktir. Bu betikte, iris veri seti PCA kullanılarak 2 boyuta indirgenir. İndirgenmiş veri seti, bu iki boyutta temsil edilir ve veri setinin varyansının çoğunu korumaya çalışır.



![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/ad368516-740d-417a-8178-c157d4195090)




## Görselleştirme

PCA tarafından elde edilen 2 boyutlu veri seti, scatter plot grafiğinde görselleştirilir. Her bir iris çiçeği türü için farklı renkler kullanılarak veri noktaları gösterilir.



## Sonuçlar

Görselleştirme sonucunda, farklı iris çiçeği türlerinin birbirinden ne kadar ayrıldığı ve 2 boyutlu uzayda nasıl bir dağılım gösterdiği hakkında bilgi elde edilir.



## Notlar

### Dimension Reduction (Öznitelik İndirgeme)

Öznitelik indirgeme (dimension reduction), makine öğrenimi ve veri analizi alanlarında kullanılan bir tekniktir. Bu teknik, veri kümesindeki özniteliklerin (değişkenlerin veya özelliklerin) sayısını azaltırken, mümkün olan en fazla bilgiyi korur. Öznitelik indirgeme, veri analizinde ve modellemede çeşitli avantajlar sağlar ve aşağıdaki nedenlerden dolayı kullanılabilir:

- Veri Görselleştirme: Yüksek boyutlu verilerin görselleştirilmesi ve anlaşılması zor olabilir. Öznitelik indirgeme, veri kümesindeki boyutu azaltarak, verilerin grafiklerle daha kolay anlaşılmasını sağlar.

- İşlemsel Verimlilik: Büyük boyutlu ve yüksek öznitelikli veri kümeleri, bazı makine öğrenimi algoritmaları için işlemci ve bellek açısından maliyetli olabilir. Öznitelik indirgeme, veri boyutunu azaltarak algoritmaların daha hızlı çalışmasını sağlayabilir.

- Gürültü Azaltma: Veri kümesi gereksiz veya tekrarlayan öznitelikler içerebilir, bu da analiz ve modelleme süreçlerini etkileyebilir. Öznitelik indirgeme, bu tür gereksiz öznitelikleri azaltarak analizin kalitesini artırabilir.

- Öznitelik Seçimi: Öznitelik indirgeme, veri kümesindeki en önemli özellikleri belirlemek ve seçmek için kullanılabilir. Bu sayede, model performansı artırılabilir ve gereksiz özniteliklerden kaçınılır.

- Veri Sıkıştırma: Öznitelik indirgeme aynı zamanda veri sıkıştırma için de kullanılabilir. Azaltılmış boyutta veri setleri, depolama ve iletim maliyetlerini azaltabilir.



### Kullanım Şartları

Öznitelik indirgeme yöntemlerinin kullanılması projenin özelliklerine ve ihtiyaçlarına bağlıdır. Aşağıdaki faktörler, öznitelik indirgeme yöntemlerinin ne zaman kullanılacağına karar verirken dikkate alınmalıdır:

- Veri Kümesinin Boyutu: Büyük boyutlu veri kümeleriyle çalışıyorsanız, öznitelik indirgeme işlemi gereksiz öznitelikleri çıkarmak ve işlemci maliyetini azaltmak için faydalı olabilir.

- Modelin Karmaşıklığı: Karmaşık modeller, genellikle daha fazla özniteliği öğrenme yeteneğine sahiptir. Basit modellerde ise, öznitelik sayısının azaltılması daha fazla anlam ifade edebilir.

- Veri Kalitesi: Veri kümesindeki gereksiz veya tekrarlayan öznitelikler, analizi ve modelleme sürecini olumsuz etkileyebilir. Öznitelik indirgeme, verinin temizlenmesine ve analizin kalitesini artırmaya yardımcı olabilir.

- Görselleştirme İhtiyacı: Veriyi görselleştirmek ve trendleri anlamak için düşük boyutlu bir uzayda çalışmak istiyorsanız, öznitelik indirgeme gerekebilir.

Öznitelik indirgeme yöntemlerinin doğru seçimi, veri setinizin özelliklerine ve projenizin gereksinimlerine bağlıdır. Farklı yöntemleri denemek ve sonuçları değerlendirmek, en uygun öznitelik indirgeme yöntemini belirlemede yardımcı olabilir.



## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Principal Component Analysis (PCA)"
```


## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
