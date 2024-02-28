# Model Selection with KNN and LR

Bu repo, makine öğrenimi algoritmalarının iris veri seti üzerinde uygulandığı bir Python betiğini içermektedir.



## Veri Seti

Veri seti, ünlü iris veri setidir. Bu veri seti, iris bitkisinin üç farklı türüne (setosa, versicolor ve virginica) ait çeşitli özelliklerin (örneğin, çiçek yapraklarının uzunluğu ve genişliği) ölçümlerini içerir.



## Veri Ön İşleme

Veriler, normalize edilmiş ve eğitim-test ayrımına tabi tutulmuştur. Ayrıca, K-Fold Cross Validation için veri seti hazırlanmıştır.



## K-Nearest Neighbour (KNN) Algoritması

K-Nearest Neighbour algoritması kullanılarak model eğitilmiştir. Modelin performansı, K-Fold Cross Validation yöntemiyle değerlendirilmiş ve test veri seti üzerinde doğruluk oranı hesaplanmıştır. Ayrıca, hiperparametre K için en iyi değer Grid Search Cross Validation kullanılarak bulunmuştur.



## K-Fold Cross Validation 

![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/ed30b146-e6bb-4df4-aacd-9ed208304a30)



## Logistic Regression Algoritması

Ayrıca, Logistic Regression algoritması kullanılarak da model eğitimi yapılmıştır. Logistic Regression modelinin hiperparametrelerini (C ve penalty) belirlemek için Grid Search Cross Validation kullanılmıştır. Modelin performansı, en iyi hiperparametrelerle eğitilmiş modelin test veri seti üzerindeki doğruluğu ile değerlendirilmiştir.



## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Model Selection"
```


## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
