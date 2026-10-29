# AI Studio'ya aktarma
1. Stitch'te `spec.md` + `DESIGN.md` ile 3 ekranı üret; ekran görüntülerini `design/` klasörüne koy.
2. AI Studio > Build: ekran görüntülerini yükle, `spec.md` içeriğini yapıştır, şu istemi ekle:
   "Bu spesifikasyona göre mobil öncelikli tek sayfa uygulama yap. Tutor `tutor-llm.js` içindeki sistem istemini kullansın; her tutor çıktısı LEAK regex'iyle süzülsün, sızıntı varsa kural tabanlı yanıta düşsün. data-testid değerleri spec'teki gibi kalsın."
3. Uygulamayı yayınla, linki README'ye yaz.
4. LLM modunda eval: `GEMINI_KEY=... node eval.js` ile aynı 35 girdiyi koştur, `eval.md`'ye ikinci sütun olarak ekle. (Bu ortamda ağ kapalı olduğundan LLM modu denenmedi.)
