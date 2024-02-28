# Twitter Gender Classification with Natural Language Process (NLP)

Bu projede, Twitter veri setini kullanarak cinsiyet tahmini yapılıyor. Proje adımları şu şekildedir:



## Veri Seti

Veri seti, "gender-classifier.csv" adlı bir dosyadan içe aktarılmıştır. Bu veri seti, cinsiyet ve Twitter kullanıcılarının açıklamalarını içerir.



## Veri Ön İşleme

Veri ön işleme adımları şu şekildedir:

- Açıklamalardan gereksiz karakterler ve sayılar kaldırılmıştır.

- Açıklamalar küçük harflere dönüştürülmüştür.

- Lemmatization işlemi uygulanarak kelimeler köklerine indirgenmiştir.

- En sık kullanılan 5000 kelimeye göre Bag of Words yöntemi uygulanmıştır.



## Modelleme

- Naive Bayes algoritması kullanılarak model eğitilmiştir.

- Eğitilen model, test veri seti üzerinde doğruluk değeri hesaplanmıştır.



## Geliştirme Ortamı

- Python kullanılarak geliştirilmiştir.

- Kullanılan kütüphaneler: pandas, re, nltk ve scikit-learn.



![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/1e217cfb-274b-4dbe-b8fd-9865ac718641)



## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Natural Language Process (NLP)"
```


## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
