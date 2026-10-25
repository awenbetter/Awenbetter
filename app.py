if not st.session_state.entries:
    st.info("Belum ada foto yang disimpan.")
else:
    for e in sorted(st.session_state.entries, key=lambda x: (CATEGORIES.index(x['category']), x['rank'])):
        c1, c2, c3, c4 = st.columns([1, 3, 3, 1])
        with c1:
            st.image(e["display_bytes"], width="stretch")
        with c2:
            st.write(f"**{e['category']} — RK {e['rank']}**")
            st.caption(f"Periode: {e['date']} · Artikel: {e['article'] or '—'}")
        with c3:
            st.caption(f"PICT referensi: {e['pict_name'] or 'Belum dipilih'}")
        with c4:
            if st.button("Hapus", key=f"del_{e['category']}_{e['rank']}"):
                st.session_state.entries = [x for x in st.session_state.entries if not (x['category'] == e['category'] and x['rank'] == e['rank'])]
                st.rerun()


def make_photo_bytes(raw):
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    target_ratio = PHOTO_W / PHOTO_H
    w, h = im.size
    if w / h > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))
    out = io.BytesIO()
    im.save(out, format="JPEG", quality=92)
    out.seek(0)
    return out


def clear_status_textboxes(slide, rank):
    slot = rank - 1
    x0, y0 = SLOT_X_BY_RANK[slot], SLOT_Y[slot]
    for shape in slide.shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        if shape.text.strip() not in {"√", "No stock", "NO STOCK", "LP", "LAST PIECES"}:
            continue
        sx, sy = shape.left / 914400, shape.top / 914400
        if abs(sx - (x0 + PHOTO_INSET_X)) < 0.35 and abs(sy - (y0 + PHOTO_INSET_Y)) < 0.35:
            shape.text_frame.clear()


def insert_photo_under_overlays(slide, photo_stream, rank):
    slot = rank - 1
    x0, y0 = SLOT_X_BY_RANK[slot], SLOT_Y[slot]
    pic = slide.shapes.add_picture(photo_stream, Inches(x0 + PHOTO_INSET_X), Inches(y0 + PHOTO_INSET_Y), Inches(PHOTO_W), Inches(PHOTO_H))
    sp_tree = slide.shapes._spTree
    sp_tree.remove(pic._element)
    insert_at = len(sp_tree)
    for i, child in enumerate(sp_tree):
        tag = child.tag.split('}')[-1]
        if tag in ("sp", "graphicFrame", "cxnSp"):
            nv = child.find('.//{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr')
            name = nv.get('name', '') if nv is not None else ''
            if name.startswith("object"):
                try:
                    off = child.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}off')
                    x, y = int(off.get('x')) / 914400, int(off.get('y')) / 914400
                    if abs(x - x0) < 0.18 and abs(y - y0) < 0.18 and tag == 'sp':
                        insert_at = i
                        break
                except Exception:
                    pass
    sp_tree.insert(insert_at, pic._element)


def generate_pptx(entries):
    prs = Presentation(str(TEMPLATE_PATH))
    date_text = entries[0]["date"] if entries else format_period(date(2026, 10, 19), date(2026, 10, 25))
    for slide in prs.slides:
        for sh in slide.shapes:
            if getattr(sh, "has_text_frame", False) and re.search(r"\bOCT\s+2026\b", sh.text, flags=re.I):
                # Keep the existing font/layout; replace only the date text in the existing run.
                p = sh.text_frame.paragraphs[0]
                if p.runs:
                    p.runs[0].text = date_text
                    for run in p.runs[1:]:
                        run.text = ""
                else:
                    sh.text_frame.text = date_text
    for entry in entries:
        slide = prs.slides[DISPLAY_SLIDE_INDEX[entry["category"]]]
        clear_status_textboxes(slide, entry["rank"])
        insert_photo_under_overlays(slide, make_photo_bytes(entry["display_bytes"]), entry["rank"])
    out = io.BytesIO()
    prs.save(out)
    out.seek(0)
    return out

if st.session_state.entries:
    st.divider()
    if st.button("Generate PowerPoint (.pptx)", type="primary", width="stretch"):
        try:
            result = generate_pptx(st.session_state.entries)
            st.download_button("Download PowerPoint", data=result.getvalue(), file_name=f"RANKING_POSITION_LADIES_FESTIVAL_CITYLINK_{date.today():%Y%m%d}.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation", width="stretch")
            st.success("PowerPoint berhasil dibuat. Buka hasilnya untuk memeriksa periode dan penempatan foto.")
        except Exception as ex:
            st.error(f"Belum berhasil membuat PowerPoint: {ex}")
            st.caption("Kirim teks error ini agar bisa diperbaiki dengan tepat.")

with st.expander("Catatan"):
    st.markdown("""
- Template yang digunakan adalah file FESTIVAL CITYLINK asli yang sudah disimpan ulang untuk menormalkan file PowerPoint.
- Periode laporan default: **19–25 OCT 2026** dan bisa diubah melalui tanggal mulai/akhir.
- Gunakan **Mulai minggu baru / kosongkan semua foto** sebelum mengisi laporan minggu berikutnya.
- Jika slot kategori dan ranking sudah terisi, aplikasi menolak foto baru agar tidak menimpa foto yang sudah disimpan; hapus slot secara manual jika ingin menggantinya.
- Foto yang dimasukkan ke slide adalah foto display asli; PICT hanya referensi.
- PICT diunggah dari komputer atau folder Google Drive yang tersinkron. Koneksi Google Drive langsung belum disiapkan.
- Template berisi 26 slide; kategori termasuk DENIM PANTS dan halaman SKIRT kedua.
""")

