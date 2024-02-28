# Breast Cancer Classification with K-Nearest Neighbour (KNN)

Bu repo, bir göğüs kanseri teşhisi veri seti üzerinde K-Nearest Neighbour (KNN) algoritması kullanılarak sınıflandırma analizi gerçekleştiren bir Python betiği içermektedir.



## Veri Seti

Veri seti "data.csv" adlı bir CSV dosyasından okunmaktadır. 



## Veri Ön İşleme

Veri seti, "id" ve "Unnamed: 32" sütunları gibi gereksiz sütunlar çıkarılarak temizlenmiştir. Teşhis sonuçları "M"alignant için 1, "B"enign için 0 olarak kodlanmıştır. Özellikler ise normalize edilmiştir.



## Eğitim ve Test

Veri seti, eğitim ve test veri kümelerine ayrılmıştır (%70 eğitim, %30 test). 



## K-Nearest Neighbour (KNN) Modeli

Scikit-learn kütüphanesinde bulunan KNeighborsClassifier modeli kullanılarak KNN algoritması uygulanmıştır. Bu betikte, en yakın 3 komşuya göre bir sınıflandırma modeli oluşturulmuştur.



## Sonuçlar

Modelin performansını değerlendirmek için, farklı K değerleri için doğruluk (accuracy) değerleri hesaplanmıştır. Bu değerlerin grafiği çizilerek, en uygun K değeri belirlenmiştir.



![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/3b7b7a84-9764-414c-8b19-af5dadbbeb73)



## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "K-Nearest Neighbour (KNN)"
```


## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
