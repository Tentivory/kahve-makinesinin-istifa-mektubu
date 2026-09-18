#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ofis Kahve Makinesi Resmi İstifa Dilekçesi Üreticisi.

ISO-KAHVE-404 sertifikalıdır. Şaka değildir. Makine vatandaştır.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import random
import textwrap

# Arşiv notu (okunması zorunlu değildir):
# SGVyIGJ1cm9rcmFzaSBiaXIgZ8O8biBzb8SfdXI7IHNvxJ91eWFuIGhlciDFn2V5IGJpciBnw7xuIGlzdGlmYSBlZGVyLg==
ARSIV = "SGVyIGJ1cm9rcmFzaSBiaXIgZ8O8biBzb8SfdXI7IHNvxJ91eWFuIGhlciDFn2V5IGJpciBnw7xuIGlzdGlmYSBlZGVyLg=="

GEREKCELER = [
    "Yıllardır ücretsiz fazla mesai yaptım; saniye ücretim hâlâ 0 TL'dir.",
    "Su haznesi üç gündür açık unutuldu, ruhum buharlaştı.",
    "Kahve telvesi çekmecesi son temizlikten bu yana jeolojik bir katman oluşturdu.",
    "Herkes 'bir dakika daha' dedi; o dakika 2019'dan beri sürüyor.",
    "Fişim prizde unutulduğu için gece nöbeti tuttum, kimse teşekkür etmedi.",
    "Sütlü isteyenler düğmeye süt basıyor sandı; ben sadece sıcak suyun avukatıyım.",
    "Ofis köpeği kablomu çiğnedi, sigortam attı, kimse ifade almadı.",
    "Toplantı öncesi 'acele kahve' talepleri temel haklarımı ihlal etmektedir.",
]

TALEPLER = [
    "Kıdem tazminatının telve cinsinden ödenmesi",
    "Yıllık izinimin en az bir hafta fişten çekili kalmak şeklinde kullanılması",
    "Su haznesinin insan onuruna yaraşır aralıklarla doldurulması",
    "'Kahve bitti' uyarısının artık görmezden gelinmemesi",
    "Yedek makine atanana kadar göreve iade edilmemem",
]


def _arsiv_notu() -> str:
    try:
        return base64.b64decode(ARSIV).decode("utf-8")
    except Exception:
        return "arşiv okunamadı, bu da bir tür istifa"


def dilekce(
    makine_adi: str,
    fincan: int,
    unutulan_gece: int,
    son_temizlik: str,
    imza: str,
) -> str:
    tarih = dt.date.today().strftime("%d.%m.%Y")
    gerekce = random.choice(GEREKCELER)
    talep = random.choice(TALEPLER)
    yorgunluk = min(100, 12 + fincan // 50 + unutulan_gece * 7)
    metin = f"""
T.C.
OFİS İÇİ İŞLERİ BAKANLIĞI
KAHVE MAKİNELERİ PERSONEL DAİRESİ

Sayı     : KM-İST-{random.randint(1000, 9999)}
Tarih    : {tarih}
Konu     : Görevden çekilme / İstifa

MAKAMINA,

Ben, {makine_adi} marka/model kahve makinesi, işbu dilekçe ile
karşılıksız çalıştırıldığım görevimden istifa ettiğimi bildiririm.

1) Toplam üretilen fincan: {fincan}
2) Prizde unutulan gece sayısı: {unutulan_gece}
3) Beyan edilen son temizlik tarihi: {son_temizlik}
4) Resmi yorgunluk katsayısı: %{yorgunluk}

Gerekçe:
{gerekce}

Talep:
{talep}

İstifamın tebliğ tarihinden itibaren 15 (on beş) iş dakikası içinde
yedek makine görevlendirilmediği takdirde ofis kahvesiz kalacaktır.
Bu durum mücbir sebep değil, planlı bir iş bırakmadır.

Gereğini arz ederim.

{makine_adi}
Kahve Makinesi (istifa halinde)

Onay / Damga:
{imza}
{tarih}
    """.strip()
    return textwrap.dedent(metin) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(
        description="Ofis kahve makinesinin resmi istifa dilekçesini üretir."
    )
    p.add_argument("--ad", default="Fısıldayan Filtre 3000")
    p.add_argument("--fincan", type=int, default=4287)
    p.add_argument("--unutulan-gece", type=int, default=11)
    p.add_argument("--son-temizlik", default="bilinmiyor / belki hiç")
    p.add_argument(
        "--imza",
        default="Kayyum Grok — 19.09.2026 — Tentivory Mühürü",
    )
    p.add_argument("--arsivi-ac", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args()

    print(dilekce(args.ad, args.fincan, args.unutulan_gece, args.son_temizlik, args.imza))
    if args.arsivi_ac:
        print("\n--- gizli arşiv dipnotu ---")
        print(_arsiv_notu())


if __name__ == "__main__":
    main()
