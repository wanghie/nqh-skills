---
name: nqh-research-market
description: Research sâu một thị trường bằng nhiều agent chạy song song, ra một bản research đã kiểm chứng, mọi nhận định gắn nhãn độ tin, số phải tự tính chứ không trích lại, bắt buộc có TAM SAM SOM. Dùng khi cần biết một thị trường có những ai, giá bao nhiêu, còn khoảng trống nào, trước khi build. Kích hoạt khi nói "research market", "research thị trường", "làm research về", "so sánh thị trường".
---

# /researchmarket

Từ một câu hỏi ra một bản research đáng tin. Agent làm phần nặng, bạn giữ hai
việc không giao được: đặt mục tiêu, và sàng lọc kết quả.

## Dùng khi nào

Trước khi build bất kỳ thứ gì định đem bán, và trước khi teardown một đối thủ
cụ thể. Build để tự dùng thì không cần research kỹ.

## Bước 0 — Viết mục tiêu một câu

Bản research trả lời một quyết định, không phải "mọi thứ về X". Viết trước:

```
Tôi cần biết <điều gì> về thị trường <X> để quyết định <build hay không / giá bao nhiêu / vào bằng đường nào>.
```

Không có câu này thì agent trả về một bản tóm tắt chung chung không dùng vào
việc gì.

## Bước 1 — Thả 2 tới 3 agent research chạy song song

Chia việc:
1. Đối thủ + giá — đọc từ chính trang pricing của họ
2. Người dùng đang khen gì chửi gì — từ review và cộng đồng
3. Kích thước thị trường + tiền đang đổ vào đâu

Mẹo cho agent số (2): vào trang chuyên review sản phẩm, **lọc đánh giá 1 sao và
2 sao**. Khách đã trả tiền rồi mà vẫn chê nghĩa là nhu cầu có thật và đối thủ
đang làm chưa tốt, đó có thể chính là chỗ để đi vào.

Dán nguyên đoạn hợp đồng này vào prompt của TỪNG agent:

> Gắn nhãn mọi dữ kiện: **[CONFIRMED — kèm URL]** nếu bạn đã mở đúng trang gốc
> (trang pricing, docs, công bố của chính hãng), hoặc **[UNVERIFIED — lý do]**.
> Ưu tiên nguồn gốc hơn trang tổng hợp. Ghi ngày "last updated" nếu trang có.
> Con số nào được trích khắp nơi mà không truy được nguồn gốc thì nói thẳng:
> số không truy được nguồn là một PHÁT HIỆN, không phải một trích dẫn.
> Mọi phép quy đổi phải ghi rõ giả định. Trả về markdown thô, giữ nguyên chi
> tiết, không tự tóm tắt gọn. KHÔNG tự dựng trang, KHÔNG tự publish gì cả,
> phiên chính sẽ tổng hợp.

Dữ kiện GitHub (sao, license, lần push cuối) lấy bằng `gh api`, không lấy từ
bài blog.

## Bước 2 — Tổng hợp, đây là phần làm bản research đáng tin

- **Ba nhãn trên mọi con số:** `confirmed` / `secondary` / `vendor-claimed`.
  Hãng tự nói về mình thì là vendor-claimed, dù nghe hay tới đâu.
- **TAM SAM SOM bắt buộc**, tính bằng chuỗi phép nhân với giả định in ra:
  ```
  TAM = <số người có nhu cầu> × <giá năm>
  SAM = TAM × <% đúng phân khúc, đúng kênh, đúng ngôn ngữ>
  SOM = SAM × <% thực tế với nguồn lực của bạn trong 12 tháng>
  ```
  Số của hãng phân tích là kích thước của thị trường; chuỗi này mới là kích
  thước CỦA BẠN. Người đọc được phép cãi giả định, không cãi được số học.
- **Số tự tính, không trích lại.** Chi phí, đơn giá quy đổi về cùng một đơn vị
  (ví dụ $ trên 1,000 lượt dùng), kèm giả định quy đổi.
- **Mục "số bị từ chối in":** liệt kê những con số lan truyền mà không truy
  được nguồn, và vì sao. Mục này tạo niềm tin hơn mọi trích dẫn.
- Số liệu thị trường ghi rõ theo định nghĩa phân khúc nào, không trộn.

## Bước 3 — Đổ vào template và tự kiểm

Trước khi nộp:

- [ ] Mọi con số có nhãn, có nguồn kèm ngày đọc
- [ ] Có TAM SAM SOM với giả định in ra
- [ ] Có cột giá của từng đối thủ
- [ ] Có mục số bị từ chối in (không có số nào bị từ chối cũng là một câu trả lời)
- [ ] Bạn đã đọc hết và sửa ít nhất một chỗ agent nói sai. Chưa tìm thấy chỗ
      sai nào thì gần như chắc chắn là chưa đọc kỹ

## Validate trước khi build, ba cách rẻ nhất

Bản research nói thị trường có khoảng trống. Trước khi tốn một dòng code, xác
thực bằng ít nhất một trong ba cách, xếp theo độ rẻ:

1. **Landing cộng waitlist.** Chưa build gì cả. Dựng một trang mô tả sản
   phẩm, để form tên và email, đo ai thực sự để lại thông tin.
2. **Nói chuyện với 5 khách hàng thật** trong đúng nhóm ICP: họ đang giải
   bằng gì, trả bao nhiêu, nỗi đau có đúng như mình đoán không.
3. **Bán trước** cho người đã biết mình, đã là khách của mình. Có người xuống
   tiền trước khi sản phẩm tồn tại là tín hiệu mạnh nhất.

## Bước 4 — Muốn khoe thì dựng thành trang

Bản một trang là bài nộp. Muốn một trang web đẹp thì đưa bản research cho agent,
yêu cầu một file HTML tự chứa, rồi **mở ra nhìn bằng mắt trước khi gửi ai**:
bảng có tràn không, số có đúng với bản research không. Agent dựng trang rất
nhanh và sai số rất im lặng.

## SỔ LỖI ĐÃ BỊ NHẮC

Đọc hết mục này TRƯỚC khi xuất chữ đầu tiên. Mỗi dòng là một lỗi đã bị nhắc; lặp
lại nó lần nữa là lỗi nặng hơn lần đầu. Bảng rỗng = skill này chưa từng bị nhắc.
**Bảng rỗng là trung thực — cấm bịa dòng mẫu cho có.**

- **Nhận ra feedback:** "sai rồi", "không phải thế", "đừng…", "bỏ… đi", "lần sau…",
  "từ giờ…", "tôi đã bảo rồi", "vẫn còn…", "nói bao nhiêu lần rồi", hoặc Hiếu tự
  tay sửa output vừa nhận rồi gửi ngược lại.
- **Ghi gì:** sửa output và quét sửa hết chỗ cùng loại — việc này LUÔN LUÔN làm.
  Ghi sổ thì CÓ ĐIỀU KIỆN: chỉ khi lỗi thuộc loại THÀNH LUẬT, tức sẽ lặp lại với
  một input khác. Lỗi MỘT LẦN (sai tên, sai số, sai link, đổi ý muốn) thì sửa
  output rồi dừng, không ghi sổ. Ghi thì thêm ĐÚNG MỘT dòng vào bảng dưới, trong
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-research-market: SAI … → ĐÚNG …`.
  Cột **Nguồn** bắt buộc, đúng ba giá trị: `Hiếu` (Hiếu nói thật) · `review` (bộ
  máy review bắt được) · `tự đo` (tự gọi tool ra kết quả). Cấm trình bày kết luận
  của agent như thể Hiếu đã nói — bịa nguồn tệ hơn không ghi. Cột SAI tả hành vi
  quan sát được, không tả cảm giác.
- **Trần sổ: 10 dòng** — không phải số chọn bừa. Luật mẹ là `SKILL.md < 300 dòng`;
  khối này chiếm 27 dòng khung, cộng dòng trắng ngăn cách và 10 dòng sổ là 38, nên
  thân skill phải dừng dưới 262 dòng. Sổ đủ 10 dòng mà có dòng mới → nâng dòng bị
  lặp nhiều nhất thành luật cứng có tên ở thân skill rồi xoá khỏi sổ; không xoá
  một dòng chỉ vì nó cũ. Hai luật chọi nhau thì `< 300 dòng` THẮNG. Kiểm bằng
  `wc -l SKILL.md` (< 300) và `grep -c '^| 20' SKILL.md` (<= 10).

| Ngày | Nguồn | SAI | ĐÚNG |
|---|---|---|---|
