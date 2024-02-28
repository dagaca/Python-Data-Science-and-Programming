# Breast Cancer Classification with Logistic Regression

Bu repo, bir göğüs kanseri teşhisi veri seti üzerinde Logistic Regression modeli kullanarak sınıflandırma analizi gerçekleştiren bir Python betiği içermektedir.


## Veri Seti

Veri seti "data.csv" adlı bir CSV dosyasından okunmaktadır. 



## Veri Ön İşleme

Veri seti, "id" ve "Unnamed: 32" sütunları gibi gereksiz sütunlar çıkarılarak temizlenmiştir. Teşhis sonuçları "M"alignant için 1, "B"enign için 0 olarak kodlanmıştır. Özellikler normalize edilmiştir.



## Eğitim ve Test

Veri seti, eğitim ve test veri kümelerine ayrılmıştır (%80 eğitim, %20 test).



## Logistic Regression Modeli

Python kodu ile Logistic Regression modeli oluşturulmuştur. Ayrıca, Scikit-learn kütüphanesinde bulunan LogisticRegression modeli de kullanılmıştır. Modelin eğitimi için, ağırlıkların ve bias'ın güncellenmesi (öğrenme) için ileri ve geri yayılım (propagation) işlemleri yapılmıştır.



## Sonuçlar

Modelin performansı, test veri kümesi üzerinde doğruluk (accuracy) oranı kullanılarak değerlendirilmiştir. Ayrıca, Scikit-learn modeliyle elde edilen doğruluk oranıyla karşılaştırma yapılmıştır.




![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/a347f946-78c1-4125-a677-fb25c74ffe32)




## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Logistic Regression Classification"
```


## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
