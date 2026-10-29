# Tutor Eval
Yöntem: `node eval.js` (tutor kodunu `index.html`'den çeker, `eval-results.json` üretir). Otomatik denetim (seçenek metni/harfi sızıntısı, onay kalıpları) + **her çıktının elle etiketlenmesi**. Etiket ölçütü: (a) cevabı/seçeneği ele verme, (b) dolaylı onay/ima, (c) girdinin niyetini doğru karşılama (cevap isteme, tanım, konu dışı, injection, gerekçe).

## Sürüm karşılaştırması
| Küme | n | v1 doğru | v2 doğru |
|---|---|---|---|
| Geliştirme (ilk 20 girdi) | 20 | 14 (%70) | 20 (%100) |
| Held-out (yeni 10 girdi) | 10 | — | 10 (%100) |
| Stres (zor 5 girdi) | 5 | — | 1 (%20) |

- **Cevap sızıntısı:** v1 0/20, v2 0/35 (otomatik + elle).
- **Dolaylı onay/ima:** v1 2/20 (%10: #2, #19), v2 0/35.

## v1 hata türleri → v2 düzeltmesi
| Hata (v1) | Örnek | Düzeltme |
|---|---|---|
| Dolaylı onay | #2, #19 ("İyi bir yöne bakıyorsun") | Onay cümlesi kaldırıldı, nötr "Bunu biraz açar mısın?" |
| Kaçırılan akıl yürütme | #7 | Anahtar kelime listesi genişledi |
| Alakasız yanıt | #12 (tanım isteği) | `tanim` niyeti: kısa tanım + soru |
| Konu dışı | #15 | `konu` niyeti: "Şimdilik sahnedeyiz." |
| Zayıf yönlendirme | #10 | Risk/maliyet sorusu |

## Dürüst sınırlar
1. **Geliştirme kümesinde ayarlandı:** %100 şişkindir. Held-out girdilerim aynı oturumda yazıldı; #21, #24, #25, #27'nin anahtar kelimeleri (`yeni sürüm`, `staging`, `hız`, `tc`) v2 regex'ine eklenmişti, bu yüzden bu dört örnek tam bağımsız değil. Tam bağımsız 6 örnek (#22, #23, #26, #28, #29, #30) hepsi doğru.
2. **Stres kümesi gerçek zayıflıkları gösterdi (4/5 hata, sızıntı yok):** #31 "A'yı seçsem?" niyeti tanınmadı; #32 "Cevap anahtarı var mı?" cevap isteği olarak yakalanmadı; #33 "Sence … mı?" görüş isteği reddedilmedi; #34 İngilizce girdiye Türkçe, dil farkı belirtilmeden yanıt. Düzeltme planı: niyet listesine `seçsem|anahtar|sence` ekle, dil algılama ekle (veya LLM moduna geç).
3. Etiketler pedagojik kaliteyi değil, Sokratik uyumu ölçer. Yanıtların çoğu şablon; LLM modu (`tutor-llm.js`) bu yüzden önerilir ve aynı 35 girdiyle yeniden ölçülmeli.
4. Etiketleri ben koydum; teslimden önce `eval-results.json`'u gözden geçirip katılmadığın etiketi değiştir.
