# Breast Cancer Classification with Support Vector Machine (SVM)

Bu repo, göğüs kanseri teşhisinde Support Vector Machine (SVM) algoritmasının kullanımını içerir.



## Veri Seti

Veri seti "data.csv" adlı bir CSV dosyasından okunmaktadır. Veri seti, göğüs kanseri teşhisi için özellikler içerir. Öznitelikler, tümör hücrelerinin çeşitli özelliklerini tanımlar. Her bir özellik, kanserin iyi huylu (B) veya kötü huylu (M) olduğunu belirlemeye yardımcı olur.



## Veri Ön İşleme

Veri ön işleme adımları şunlardır:

- Veri setinden gereksiz sütunlar (id ve Unnamed: 32) kaldırıldı.
  
- Hedef değişken olan "diagnosis" sütunu, iyi huylu kanserler için 0 ve kötü huylu kanserler için 1 olacak şekilde dönüştürüldü.
  
- Özellikler normalize edildi.



## Model Eğitimi ve Değerlendirme

SVM algoritması kullanılarak bir model eğitildi ve test edildi. Veri seti, eğitim ve test setlerine ayrılarak (70% eğitim, 30% test) model eğitildi ve performansı değerlendirildi.

Modelin doğruluğu şu şekildedir: [Accuracy of SVM Algorithm: 0.95]



![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/54d17253-fc98-43c6-a751-98150ad6b852)




## Nasıl Başlamalı?

Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Support Vector Machine (SVM)"
```


## Katkılar

Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
