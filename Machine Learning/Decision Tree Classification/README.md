# Python Hata Yönetimi

Bu repo, dilin kurallarına uymayan ifadelerin yol açtığı syntax hataları ve çeşitli istisnaları ele almak için örnekler içerir.

## Syntax Hataları

Syntax hataları, dilin kurallarının ihlal edildiği durumları ifade eder. Kod içerisindeki belirli satırları açmak, syntax hatalarına neden olacaktır. 

Örneğin:

```python
# Aşağıdaki satırı açmak, SyntaxError hatasına neden olacaktır
print 9
```

## İstisna Durumları

Kod aynı zamanda çeşitli istisna durumlarını ele almayı gösterir:

1. ZeroDivisionError

```python
# Aşağıdaki satırı açmak, ZeroDivisionError hatasına neden olacaktır
a = k/zero
```

2. IndexError

```python
# Aşağıdaki satırı açmak, IndexError hatasına neden olacaktır
list1[15]
```

3. ModuleNotFoundError

```python
# Aşağıdaki satırı açmak, ModuleNotFoundError hatasına neden olacaktır
import numpyy
```

4. FileNotFoundError

```python
# Aşağıdaki satırı açmak, FileNotFoundError hatasına neden olacaktır
pd.read_csv("asd")
```

5. TypeError

```python
# Aşağıdaki satırı açmak, TypeError hatasına neden olacaktır
"2" + 2
```

6. ValueError

```python
# Aşağıdaki satırı açmak, ValueError hatasına neden olacaktır
int("sad")
```

7. Try-Except Bloğu

Try-except bloğu, istisnaları yakalamak ve bunlarla uygun bir şekilde başa çıkmak için kullanılır.

```python
try:
    1/1
except:
    print("except")
else:
    print("else")
finally:
    print("done")
```

## Nasıl Başlamalı?
Aşağıdaki adımları izleyerek başlayabilirsiniz:

```bash
git clone https://github.com/dagaca/Python-Data-Science-and-Programming.git
cd "Dealing with Programming Errors"
```

## Katkılar
Projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği oluşturun. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.
