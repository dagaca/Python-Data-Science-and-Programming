# US Police Shootings - Keşifsel Veri Analizi
Bu repo, Amerika'da polis müdahaleleri üzerine Python kullanarak Keşifsel Veri Analizi (EDA) yapmak için kod içermektedir. Analiz, veri kümesinin çeşitli yönlerini görselleştirmeyi içerir; örneğin yoksulluk oranları, lise mezuniyet oranları, ırk dağılımı ve polis tarafından öldürülen bireylerin özellikleri.


## Veri Seti
Bu projede kullanılan Fatal Police Shootings in the US veri setine [bu bağlantıdan](https://www.kaggle.com/datasets/kwullum/fatal-police-shootings-in-the-us) ulaşabilirsiniz. 

Analiz, Amerika'nın demografik ve polis müdahaleleriyle ilgili çeşitli veri kümelerini kullanır. Aşağıdaki veri kümeleri kullanılmıştır:

- `MedianHouseholdIncome2015.csv`
- `PercentOver25CompletedHighSchool.csv`
- `PercentagePeopleBelowPovertyLevel.csv`
- `PoliceKillingsUS.csv`
- `ShareRaceByCity.csv


## Veri Keşfi ve Görselleştirme
Analiz, veri içindeki ilişkileri keşfetmek ve anlamak için çeşitli görselleştirmeler içerir. Bazı görselleştirmeler şunları içerir:

- Her bir eyaletteki yoksulluk oranını gösteren çubuk grafikleri.
- Lise mezuniyet oranları ile yoksulluk oranları arasındaki ilişkiyi görselleştiren dağılım grafikleri.
- Polis tarafından öldürülenler arasındaki ırk dağılımını gösteren pasta grafikleri.
- Öldürülenler arasındaki yaş ve cinsiyet dağılımını görselleştirmek için kutu grafikleri ve yay grafikleri.


## Kod Açıklaması
Kod, analizin belirli bir yönüne odaklanan bölümlere ayrılmıştır. Bazı bölümler şunları içerir:

- Veri kümelerini yükleme ve inceleme
- Veri ön işleme ve temizleme
- Yoksulluk oranları, lise mezuniyet oranları ve ırk dağılımının görselleştirilmesi
- Öldürülenler arasında en yaygın ad ve soyadların analizi


## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Data Visualization"
cd "seaborn-tutorial-for-beginners"
```

Projenin çalışması için "requirements.txt" içerisinde bulunan Python kütüphanelerini yükleyin:

```bash
pip install -r requirements.txt
```

## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
