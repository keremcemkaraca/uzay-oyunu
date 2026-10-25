KOMUTLAR = {}

def komut(ad, aciklama=""):
    def decorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"{ad} komutu zaten kayıtlı!")
        KOMUTLAR[ad] = (func, aciklama)
        return func
    return decorator

@komut("yardim", "komutları listeler")
def yardim(durum):
    for k_ad, (_, k_aciklama) in KOMUTLAR.items():
        print(f"{k_ad}\t{k_aciklama}")

@komut("envanter", "envanter eşyalarını gösterir")
def envanter(durum):
    esyalar = durum.get("envanter", [])
    print(", ".join(esyalar) if esyalar else "Envanter boş.")

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum):
    baglantilar = durum.get("baglantilar", [])
    print(", ".join(baglantilar) if baglantilar else "Bağlantı yok.")