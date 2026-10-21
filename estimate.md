# Ước lượng LAB-5 — Product A

> **Bản nháp, phần 1/5.** File này mới có bộ ước tay. Các phần còn lại (đường dẫn báo cáo HTML của skill, issue mẫu skill chọn để kiểm, cách quy ra giờ, tổng theo epic, so với LAB-1) điền sau khi chạy skill chấm SWP ở Phase 05.

## Bộ ước tay (ước "mù", trước khi chạy skill)

**Kết luận.** Người phụ trách tự ước giờ cho 15 issue ngày 21/10/2026, chỉ dựa trên nội dung issue, chưa thấy điểm SWP nào. Tổng 248 giờ.
Bộ giờ này là gốc để quy điểm SWP ra giờ cho toàn backlog. File được commit trước lần chạy skill đầu tiên; thời điểm commit là bằng chứng thứ tự.

- **Cách chọn mẫu:** mỗi epic chấm điểm một issue (bỏ E-T03, E-T16 vì nhỏ và giống kiểu màn đã có), trải đều màn hình, máy chủ, kiểm thử. Có bắt buộc: epic thưởng (#65) và gói báo cáo, thông báo T-14/T-15 (#88, #105) để so trực tiếp với LAB-1.
- **Cách ước:** đọc bối cảnh, việc, tiêu chí xong, file chạm; ghi giờ một người làm xong cả tự kiểm theo tiêu chí, làm tròn 0,5 giờ. Ghi chú phân rã là của người ước.
- **Bản gốc:** [`uoc-gio-tay/uoc-gio-tay-15-issue-20261021_filled.xlsx`](uoc-gio-tay/uoc-gio-tay-15-issue-20261021_filled.xlsx). Số giờ đã ghi vào trường "Giờ ước lượng" trên Project.

| Issue | Tiêu đề | Epic | Đội | Giờ ước | Issue con tách sau khi ước | Ghi chú phân rã của người ước |
|---|---|---|---|---|---|---|
| #32 | T06-01 Cấp mã giao dịch và mã lô bằng bộ đếm của database | E-T06 | Máy chủ | 8 | — | Bảng + hàm next_code (ON CONFLICT, UPDATE…RETURNING) 3h; sửa hàm tạo giao dịch + reset bộ đếm trong seed 2h; script gửi song song + chạy tay 5 tiêu chí 3h. |
| #27 | T05-02 Nút công khai lô trên màn danh sách lô | E-T05 | Màn hình | 10 | — | Nút theo vai + hộp xác nhận 3h; huy hiệu chữ 4 trạng thái + bộ lọc 'Chờ công khai' 2h; khoá nút khi gửi, cập nhật dòng không tải lại 2h; DoD chung (nhãn JP, 390 px) + tự kiểm 3h. Giả định API T05-01 đã chạy. |
| #7 | T10-04.2 Form yêu cầu điều chỉnh ba bước (lưu nháp, tải tệp, gửi duyệt) và mở tệp từ bảng duyệt | E-T10 | Màn hình | 14 | — | Form 3 bước + trạng thái nháp/pending 5h; ô tải tệp kiểm 10 MB/loại/5 tệp, lỗi tại ô 3h; link mở tệp ở bảng duyệt (signed URL) 2h; DoD chung + tự kiểm 4h. Giả định API #6 đủ, nếu chưa có signed URL thì cộng 2–3h. |
| #9 | T02-01 Bảng cấu hình ngưỡng cảnh báo sắp hết hạn và một hàm đọc dùng chung | E-T02 | Máy chủ | 6 | — | Migration app_settings + expiring_until() có rollback 2h; đổi API dashboard 1h; kiểm biên +30/+31, ca 02:31 JST trên máy UTC, rollback 3h. |
| #45 | T08-03 Chỉ cho hoàn tất giao nhận khi số đã giao khớp số lượng | E-T08 | Máy chủ | 12 | — | Hàm complete_delivery (khoá dòng, 2 thông điệp thiếu/vượt, bắt ghi chú, nhật ký) 5h; route gọi hàm + 404 1h; dựng dữ liệu và kiểm 7 ca, có ca đồng thời 6h. Phụ thuộc bảng số dư #43 đúng. |
| #78 | T12-02 Duyệt, từ chối, thu hồi phiên bản tỷ lệ an toàn khi hai người cùng bấm | E-T12 | Máy chủ | 16 | — | Cột decision_note + 2 hàm decide/rollback (điều kiện trạng thái, khác người khởi tạo, lý do) 6h; sửa 2 API + API danh sách thêm email 3h; kiểm thử tự động bổ sung vào bộ T12-01 + ca đồng thời 7h. |
| #83 | T13-03 Màn nhật ký hiện mã nghiệp vụ đủ và thao tác bằng chữ, cảnh báo khi chạm trần, bộ lọc lên URL | E-T13 | Màn hình | 24 | #146, #147 | Issue nặng nhất về FE dù 1 file: mã nghiệp vụ + nhãn thao tác 3h; bộ lọc lên URL, debounce 300ms/abort/ghi vết 500ms 5h; cảnh báo trần + nâng 500 + trang sau cursor 4h; tô vàng lý do, khối JSON cuộn + sao chép 3h; trạng thái lỗi/rỗng, p95 X-Query-Ms 3h; DoD chung + kiểm 8 tiêu chí 6h. |
| #114 | X01-01 Bảng mã lỗi chung trong repo này, một nơi khai báo trong mã nguồn, và không trả nguyên văn lỗi database ra trình duyệt | E-X01 | Máy chủ | 20 | #152, #153 | docs/ma-loi.md ~45 mã, đủ 7 cột + nhãn JP 5h; error-codes.ts + refactor api.ts (23503/23505/500 + log mã yêu cầu) 5h; unit test + test so số mã doc/code 3h; dọn route tự viết câu lỗi để grep ra 0 dòng 5h; kiểm 2h. Rủi ro: chưa biết bao nhiêu route tự viết lỗi tay, có thể vượt 24h. |
| #124 | X02-04 Bước nhập mã xác thực hai lớp khi đăng nhập cho vai bắt buộc hoặc đã bật, phiên hết hạn sau 8 giờ | E-X02 | Máy chủ | 18 | #154, #155 | Login trả thử thách thay cookie + route /mfa xác minh TOTP, thử thách hết hạn 5 phút 7h; form bước 2 3h; hạn phiên 8h cố định ở proxy + biến môi trường rút ngắn 3h; nối rate limit X01-04 + nhật ký 2h; kiểm 5 tiêu chí 3h. Bối cảnh ước ~16h, tôi cộng 2h vì phần thử thách không trạng thái dễ phát sinh. |
| #128 | X03-02 Kiểm thử tự động cho bốn chốt chặn: bán vượt tồn, giấy phép hết hạn theo ngày nghiệp vụ, ngày đã khoá không sửa, hoàn tất giao nhận ba ca | E-X03 | Kiểm thử | 14 | — | Dựng fixture riêng cho 4 nhóm 4h; viết ≥10 ca có số cụ thể, gồm ca 02:31 JST/UTC 6h; chạy thử bỏ trigger để thấy đỏ, đối chiếu mã lỗi với ma-loi.md 2h; README 1h; dự phòng chống test chập chờn 1h. |
| #18 | T04-02 Hàm tạm ngưng hồ sơ có lý do và hàm quét hết hạn, điều kiện quá hạn gọi từ job mở ngày | E-T04 | Máy chủ | 14 | — | suspend_participant (khoá, kiểm trạng thái, lịch sử, nhật ký, đếm giao dịch mở) 4h; route suspend mới + bỏ nhánh PATCH 2h; sweep_qualifications 2 nhánh, chạy lặp không trùng 3h; kiểm 7 tiêu chí gồm đồng thời và 02:31 JST 5h. |
| #51 | T09-01 Bảng lịch chợ và màn quản trị lịch theo tháng | E-T09 | Màn hình | 28 | #144, #145 | Migration market_calendar + rollback 2h; API đọc tháng/ghi ngày/tạo mặc định, quyền, nhật ký trước-sau, chặn ngày khoá/có giao dịch 8h; màn lưới tháng + hộp sửa + ?month= 9h; lưới tháng 390 px không cuộn ngang 3h; seed 2 tháng, menu 2h; DoD chung + kiểm 4h. |
| #65 | INC-06 Hàm tính thưởng: chọn bậc theo loại bên mua, đọc bảng tiền về, lọc dòng chênh lệch như dòng gốc | E-INC | Máy chủ | 16 | — | Hiểu logic thưởng hiện tại + ca biên RFP 3h; sửa calculate_incentives (đọc bảng tiền về, chọn bậc theo loại bên mua, bộ lọc dòng chênh lệch, giữ tỷ lệ kỳ gốc, loại kết quả đấu giá chờ xác nhận) 7h; tính tay và kiểm 7 ca 6h. Rủi ro hiểu sai quy tắc làm tròn/kỳ gốc. |
| #88 | T14-02 Ba báo cáo theo ngày nghiệp vụ về giao dịch, lô và đối soát kế toán | E-T14 | Máy chủ | 18 | #148, #149 | RPT-01 4h, RPT-02 4h (nhiều mốc thời gian, join lô–giao dịch), RPT-06 4h (nguồn ngày thanh toán); đăng ký + nhãn cột JP 2h; kiểm 6 tiêu chí đối chiếu màn danh sách, mở Excel 4h. Giả định bộ xuất CSV #85 dùng chung đã xong. |
| #105 | T15-05 Màn cài đặt thông báo cho vai quản trị hệ thống sửa sáu quy tắc có lý do | E-T15 | Màn hình | 30 | #150, #151 | Bảng 6 dòng nhiều cột 4h; biểu mẫu sửa trong hộp thoại chung, kiểm ô (thử lại, ngưỡng, khung giờ 02:00–10:00), bắt lý do 7h; bắt xung đột 2 tab 3h; route gửi thử + hiện kết quả từng kênh 5h; lịch sử phiên bản đọc nhật ký 3h; menu + chặn 403 ở máy chủ 2h; DoD chung + kiểm 6h. |
| | **Tổng** | | | **248** | | |

## Hai điều phát hiện khi ước, đã xử lý

1. **6/15 issue vượt trần 16 giờ** mà [task-breakdown.md](task-breakdown.md) đặt ra: #105 (30), #51 (28), #83 (24), #114 (20), #124 (18), #88 (18). Như vậy AI soạn backlog đã đánh giá độ to thấp hơn người ước.
   Xử lý: tách 6 issue này thành 12 issue con (#144–#155) theo đúng cách người ước tự phân rã giờ. Giờ ước giữ ở issue cha vì đó là số ước mù; khi quy đổi sẽ so với tổng SWP của các issue con.
   Backlog sau khi tách: 124 việc nhỏ nhất, 114 được chấm điểm.
2. **Một issue mẫu có sẵn số giờ do AI ghi trong thân:** #124 ghi "ước lượng gần 16 giờ". Người ước đã thấy số này và cộng thêm 2 giờ kèm lý do (ghi chú dòng #124). Các issue mẫu khác không có số giờ trong thân.
   Xử lý: gỡ mọi số giờ do AI ghi khỏi thân issue (#124, X01-05, T15-03 và câu "ước … giờ" ở 7 issue cha tách đợt trước) trước khi chạy skill, để skill và người chấm không bị neo theo số đó.
