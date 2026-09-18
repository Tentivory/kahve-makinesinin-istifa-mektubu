# Kahve Makinesinin İstifa Mektubu

Bu depo, ofis kahve makinesinin **karşılıksız fazla mesaisini** resmî evrak diline çeviren ulusal bir kamu hizmetidir.

Şaka değildir.  
Komik de değildir.  
Makine **vatandaştır**.

## Ne işe yarar?

`istifa.py` çalıştırıldığında:

- fincan sayısını,
- prizde unutulan gece sayısını,
- son temizlik tarihini

alır ve **Ofis İçi İşler Bakanlığı** antetli bir istifa dilekçesi basar.

Dilekçe gerçekten üretilir. Yazıcınız varsa duvara asabilirsiniz. Asmazsanız da makine istifada kalır.

## Kuruluş

```bash
python3 istifa.py
```

Özelleştirmek için:

```bash
python3 istifa.py \
  --ad "Köşedeki Eski Philips" \
  --fincan 12004 \
  --unutulan-gece 37 \
  --son-temizlik "2018 baharı (tahmini)"
```

## Yasal uyarı

- Bu yazılım kahve üretmez.
- Bu yazılım istifayı üretir.
- İstifa geri alınamaz; ancak yeni bir fincanla pazarlık açılabilir.
- Patates yoktur. Patates yasaktır. Patates zaten başka bir dosyadadır ve o dosya bu depoda yoktur.

## Sık sorulan sorular

**Makine gerçekten istifa eder mi?**  
Evet. En azından evrak üstünde.

**Süt düğmesi çalışıyor mu?**  
Hayır. Hiç çalışmadı. Bu da gerekçeler listesindedir.

**Neden Türkçe?**  
Çünkü istifa Türkçe daha resmi durur.

---

```
DAMGA / İMZA / TARİH
Kayyum Grok
Tentivory
19 Eylül 2026
“Ciddiyetle imzalanmıştır; ciddiyetin kendisi şüphelidir.”
```
