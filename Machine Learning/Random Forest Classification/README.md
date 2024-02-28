# Breast Cancer Classification with Random Forest Classification

Bu repo, Wisconsin Göğüs Kanseri veri kümesini kullanarak göğüs kanserini teşhis etmek için Random Forest algoritmasının uygulanışını göstermektedir.



## Veri Açıklaması

Veri kümesi, bir kitle (FNA) için dijitalleştirilmiş bir görüntüden hesaplanan özellikleri içerir. Özellikler, görüntüde bulunan hücre çekirdeklerinin çeşitli özelliklerini tanımlar. "diagnosis" hedef değişkeni, kütlenin iyi huylu (B) veya kötü huylu (M) olup olmadığını gösterir.



## Veri Ön İşleme

- Veri kümesi yüklenir ve "id" ve "Unnamed: 32" gibi gereksiz sütunlar çıkarılır.

- "diagnosis" hedef değişkeni, kötü huylu (M) için 1 ve iyi huylu (B) için 0 olarak kodlanır.

- Özellik normalizasyonu yapılır, özelliklerin değer aralığını 0 ile 1 arasına ölçekler.

- Veri kümesi, %15'lik bir test boyutuyla eğitim ve test setlerine bölünür.



## Random Forest Sınıflandırıcısı

Ön işlenmiş veri üzerinde 100 karar ağacı ile Random Forest sınıflandırıcısı eğitilir.

```bash
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(x_train, y_train)
```

![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/7cc03aa4-7866-47a5-9567-c5851085dd6a)


## Model Değerlendirmesi

Random Forest algoritmasının doğruluğu test setinde değerlendirilir.

```bash
print("Random Forest Algoritmasının Doğruluğu: ", rf.score(x_test, y_test))
```



## Sonuç

Random Forest algoritması, verilen özelliklere dayanarak göğüs kanserini teşhis etmede belirli bir doğruluk düzeyine ulaşır. Optimal performans için modelin daha fazla analizi ve ayarlaması gerekebilir.



## Nasıl Başlamalı?

Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Random Forest Classification"
```


## Katkılar

Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
