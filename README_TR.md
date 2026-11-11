# Metin2 Singleplayer - topluluk çevirileri

[English](README.md) | [Polski](README_PL.md) | **Türkçe** | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Bu depo **Metin2 Singleplayer**'ın metinlerini içerir - oyun istemcisi, eşya
ve canavar adları, sunucu mesajları, görevler, botların sohbeti, Windows
başlatıcısı (launcher) ve klasik web paneli - böylece oyuncular oyunu kendi dillerine
çevirebilir. Burada yalnızca çeviriler var, oyun kodu yok.

Her pull request otomatik olarak kontrol edilir; kabul edilen çeviriler
sonraki sürümlerde oyuna eklenir.

## Burada ne var

| klasör | ne |
|---|---|
| `template/` | oyunun tüm metinleri, `translation` sütunu boş. Yeni bir dilin başlangıcı. |
| `de/` `fr/` `pt/` `ro/` `tr/` | oyunda zaten olan diller, mevcut çevirileriyle: düzeltin ve eksikleri tamamlayın (`status` değeri `new` olan satırlar). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | yeni diller, yapay zekâ yardımıyla tamamen çevrildi: anadili bu olanlar, kulağa yanlış gelenleri düzeltin. |
| `en_US/` | Amerikan İngilizcesi: İngilizce kaynak metin (İngiliz yazımı) ABD yazımıyla (color, armor, defense...). |
| `tools/validate.py` | her pull request'in geçtiği kontrol. |

Kaynak dil İngilizcedir; Lehçe yardımcı olarak yanında durur. İkisinin de
kendi klasörü yoktur.

Her dil klasöründe aynı CSV dosyaları vardır; GitHub'ın gösterip
düzenleyebilmesi için parçalara bölünmüştür (dosya başına en fazla 700 satır):

| dosyalar | ne |
|---|---|
| `1_klient_NN.csv` | istemci: pencereler, düğmeler, açıklamalar, beceriler, kurallar |
| `2_przedmioty_potwory_NN.csv` | eşya ve canavar adları, eşya açıklamaları |
| `3_gra_serwer_NN.csv` | sunucunun kendi mesajları (sohbet, sistem satırları) |
| `4_questy_NN.csv` | görev diyalogları |
| `5_boty_czat_NN.csv` | botların sohbeti, canavarların sözleri, sunucunun ifadeleri |
| `6_launcher_NN.csv` | Windows başlatıcısı |
| `7_panel_NN.csv` | klasik web paneli (tarayıcıda, 7788 portundaki yönetici paneli) |

Her dosyanın sütunları:

| sütun | |
|---|---|
| `id` | satırın anahtarı. **Asla değiştirmeyin.** |
| `english` | çevrilecek metin. **Asla değiştirmeyin.** |
| `polski` | aynı metnin Lehçesi, yardımcı olarak (boş olabilir). |
| `translation` | **çeviriniz - düzenlediğiniz tek sütun.** Boş = oyun İngilizcesini gösterir. |
| `notes` | metnin nerede göründüğü, neyin korunması gerektiği, uzunluk sınırı. |
| `status` | `new` (çevrilmemiş), `done` (çevrilmiş), `check` (İngilizcesiyle aynı - kontrol edin). `done` yapabilirsiniz. |

## Nasıl çevrilir

### A. Tarayıcıda (küçük değişiklikler)

1. Dosyayı açın, örneğin [`tr/1_klient_01.csv`](tr/1_klient_01.csv). GitHub
   onu tablo olarak gösterir; üstündeki arama kutusu bir satırı bulur.
2. Kaleme tıklayın (**Edit this file**). GitHub ilk seferde sizin için bir
   kopya (fork) oluşturur.
3. İstediğiniz satırların yalnızca `translation` sütununu değiştirin. Virgül,
   tırnak işareti ya da yeni satır içeren metin çift tırnak içindedir
   (`"böyle, işte"`); içindeki tırnak işareti iki kez yazılır (`""`).
4. **Commit changes...**, ardından **Propose changes** ve **Create pull
   request**'e tıklayın. Neyi çevirdiğinizi bir cümleyle yazın.

### B. Bir tablo programında (çok sayıda satır)

1. Dosyaları indirin (dosyayı açın, **Download raw file**; ya da her şey için
   yeşil **Code** düğmesi, **Download ZIP**).
2. Bir tablo programında açın:
   - **Google E-Tablolar**: Dosya > İçe aktar > Yükle. Ayar gerektirmez.
   - **LibreOffice Calc**: dosyayı açın; karakter kümesi **UTF-8**, ayırıcı
     **virgül** seçin ve sütunları **Metin** yapın.
   - **Excel**: dosyaya çift tıklamayın (Excel harfleri yanlış okur). Veri >
     Metinden/CSV'den, dosya kaynağı **65001: Unicode (UTF-8)**, sınırlayıcı
     **Virgül**. **CSV UTF-8 (virgülle ayrılmış)** olarak kaydedin.
3. `translation` sütununu doldurun. Dosya adlarını değiştirmeyin, sütun
   eklemeyin ya da silmeyin, `id` ve `english`'i değiştirmeyin. Sıralama ve
   filtreleme sorun değildir.
4. Aynı adla CSV (UTF-8, virgülle ayrılmış) olarak kaydedin.
5. GitHub'da dil klasörünü açın, **Add file > Upload files**, dosyalarınızı
   bırakın, ardından **Propose changes** ve **Create pull request**.

Her şeyi bir seferde çevirmeniz gerekmez - elinizde olanı gönderin.

## Kurallar

1. **Yalnızca `translation` sütunu.** `id` ve `english` olduğu gibi kalır;
   kontrol, bunların değiştirildiği dosyayı reddeder.
2. **Her değişkeni ve kodu İngilizcedeki gibi, aynı sırayla koruyun** - onları
   oyun doldurur:
   - printf değişkenleri: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... ve `%%` (yüzde işareti);
   - yer tutucular: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` görev penceresinde yeni satırdır; `[WAIT]`, `[DELAY value;5]`,
     `[COLOR r;1|g;0|b;0]` onun komutlarıdır;
   - renkler `|cffff0000` ... `|r`, bağlantılar `|H` ... `|h`, `|E` ... `|e`.

   Dilinizin gerektirdiği gibi cümle içinde yerlerini değiştirebilirsiniz,
   ama `%` ile başlayan değişkenler aynı sırada kalmalıdır. `[Guild]` ya da
   `[PT]` gibi köşeli parantez içindeki metin sıradan metindir: çevirin.
3. **Harfler.** Oyun her dili tek bir Windows kod sayfasında çizer, bu yüzden
   yalnızca o sayfanın harfleri gösterilebilir - emoji ya da `→`, `✓` gibi
   simgeler yok:

   | kod sayfası | diller | harfler |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (Latin), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (Kiril) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumence: kod sayfasında yalnızca **çengelli ş ţ** vardır, virgüllü ș ț
   yoktur. Başlatıcı (`6_launcher_*`) ayrı bir Windows programıdır ve her
   harfi kabul eder; tarayıcıda açılan bir sayfa olan web paneli
   (`7_panel_*`) de öyle: ikisi de **UTF-8**'dir, her dilin her harfi olur.
4. **Botların sohbeti** (notes sütununda "ASCII letters only" yazan
   satırlar): botlar oyuncular gibi yazar, aksansız düz a-z harfleriyle.
5. **Uzunluk.** notes "max N characters" diyorsa, oyunda daha fazlası için
   yer yoktur.
6. **Yeni satırlar** yalnızca İngilizcede olan yerlerde ya da notes "new
   lines allowed" diyorsa.
7. **Web paneli** (`7_panel_*`): metinleri bir web sayfasına girer, bu yüzden
   İngilizcedeki HTML etiketlerini olduğu gibi koruyun (`<b>`, `</b>`,
   `<a href="...">`, `<br>` ve `<number>` gibi köşeli parantezli yer
   tutucular) ve kendinizden `<`, `>` ya da `javascript:` eklemeyin.
   Değişkenleri `%s`, `%d`, `%(ad)s` ve `{ad}`'dir; adlı `%(ad)s` yer
   değiştirebilir. Ardından boşluk gelen `%` (`25% a character`) yüzde
   işaretidir. En az bir panel metni çevrilmiş bir dil, panelin dil
   seçicisinde görünür; çevrilmemiş olanı panel İngilizce gösterir.

## Yeni bir dil

1. `template/` klasörünün tamamını, dilinizin iki harfli ISO 639-1 koduyla
   adlandırılmış bir klasöre kopyalayın (`hu`, `es`, `cs`... -
   [listeye](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
   bakın). Bunu bir tablo programıyla yapabilirsiniz: `template/`'i indirin,
   çevirin ve dosyaları yeni klasöre yükleyin (**Add file > Upload files**,
   klasörü oluşturmak için adın önüne `xx/` yazın).
2. Çevirin ve bir pull request açın.

Yeni bir dil, oyuncular onu seçebilmeden önce oyunda biraz iş gerektirir
(1250 kod sayfası dışındaki diller yeni bir istemciye de ihtiyaç duyar), bu
yüzden ilk çeviriden birkaç sürüm sonra gelebilir.

## Kontrol

Her pull request `tools/validate.py`'yi çalıştırır (GitHub Actions). Bulduğu
satırda şunları bildirir:

- `template/`'te olmayan ya da iki kez geçen bir `id`;
- değiştirilmiş bir `english` sütunu;
- İngilizcedekinden farklı değişkenler, yer tutucular, komutlar ya da renk
  kodları;
- web panelinin sayfasında İngilizcedekinden farklı HTML etiketleri ya da
  kendinden bir `<`, `>` veya `javascript:`;
- dilin kod sayfası dışında bir harf, sekme, kontrol karakteri, izin
  verilmeyen yerde yeni satır, fazla uzun metin.

Yalnızca pull request'inizin değiştirdiği satırlar değerlendirilir;
dosyalarda zaten olan sorunlar sayılır ama size engel olmaz. Kontrolü kendiniz
çalıştırmak için (Python 3, kurulacak bir şey yok): `python tools/validate.py tr`.

## Lisans

Bir pull request açarak, çevirinizin Metin2 Singleplayer'da kullanılmasını ve
projeyle aynı koşullarda paylaşılmasını kabul etmiş olursunuz:
[CC BY-NC-ND 4.0](LICENSE). Katkıda bulunanlar projede anılır. Metin2'nin
kendisi ve orijinal metinleri Ymir Interactive ve Webzen'e aittir.
