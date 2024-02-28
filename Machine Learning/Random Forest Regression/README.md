# Random Forest Regression

Bu repo, bir futbol maçının tribün seviyesine bağlı olarak bilet ücretini tahmin etmek için Random Forest Regression modelini kullanmaktadır.



## Veri Seti

Veri seti Random Forest Regression için "random_forest_regression_dataset.csv" adlı bir CSV dosyasından okunmaktadır. Veri seti, futbol maçı bilet ücretlerini tribün seviyesine göre içeren bir veri kümesidir.



## Model

Random Forest Regression, veri setindeki tribün seviyesi ve bilet ücreti arasındaki ilişkiyi modellemek için kullanılır. Model, 100 ağaçtan oluşan bir orman oluşturur.

```bash
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x, y)
```



![image](https://github.com/dagaca/Python-Data-Science-and-Programming/assets/80363244/d5200f64-5add-468c-8bc3-cfd6dda77aa3)



## Tahmin

Model, belirli bir tribün seviyesi için bilet ücretini tahmin etmek için kullanılabilir. Örneğin, 7.8 tribün seviyesindeki bilet ücreti aşağıdaki gibi tahmin edilir:

```bash
print("7.8 tribün seviyesinde ücretin tahmini: ", rf.predict([[7.8]]))
```



## Görselleştirme

Modelin tahminlerini gerçek verilerle karşılaştırmak için bir görselleştirme yapılır. Tribün seviyesine göre bilet ücreti dağılımını gösteren kırmızı noktalar ve model tarafından tahmin edilen yeşil çizgi görüntülenir.

```bash
plt.scatter(x, y, color="red")
plt.plot(x_, y_head, color="green")
plt.xlabel("Tribün Seviyesi")
plt.ylabel("Ücret")
plt.show()
```

Bu görselleştirme, modelin veri setindeki dağılıma ne kadar iyi uyduğunu gösterir.



## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Machine Learning"
cd "Random Forest Regression"
```


## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
