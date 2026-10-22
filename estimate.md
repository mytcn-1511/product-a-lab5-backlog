# Ước lượng LAB-5 — Product A

**Báo cáo HTML của skill:** [`swp-report/estimate-swp-mytcn-1511-project-1-20261022-1031.html`](swp-report/estimate-swp-mytcn-1511-project-1-20261022-1031.html) — chạy `tkm:estimate-swp` ngày 22/10/2026, mức `high`, không đẩy lên KPI. File đã đóng băng, không chạy lại sau khi giả lập sprint.

## Tóm tắt 10 dòng

1. Skill chấm 114 việc nhỏ nhất trên Project: tổng **622 SWP** (điểm khối lượng chuẩn), khoảng bất định 594–659 SWP.
2. 88 việc có độ tin cậy cao, 26 trung bình, không việc nào thấp; không việc nào bị đề xuất tách.
3. 10 câu hỏi gửi khách (epic E-X04) không chấm điểm, theo quyết định từ đầu.
4. Skill chọn 5 issue mẫu; người duyệt giữ nguyên cả 5 (lý do ở phần 1).
5. Đổi điểm ra giờ bằng hệ số **k = 2,51 giờ/SWP**, lấy từ 15 issue người phụ trách tự ước trước khi chạy skill (248 giờ ÷ 99 SWP).
6. Issue ước tay giữ số tay; issue còn lại = SWP × k, làm tròn 0,5 giờ; issue cha bằng tổng con.
7. Tổng giờ toàn backlog: **1.555,5 giờ ≈ 222 ngày công** (1 ngày công = 7 giờ), chưa gồm QA chạy kiểm thử riêng.
8. So với LAB-1, phần chức năng tăng từ 1.092 giờ lên 1.384 giờ. Tỷ trọng tăng mạnh nhất ở thông báo, thưởng và xác thực; giảm nhiều nhất ở giao nhận, giao dịch và phiên bản tỷ lệ, nơi prototype đã làm sẵn.
9. Số SWP và giờ đã ghi lên Project bằng script; đọc lại từ Project khớp 100% với báo cáo HTML.
10. Rủi ro chính: một mẫu (#7) có số giờ trên điểm cao gần gấp đôi trung bình, cho thấy skill có thể chấm nhẹ issue màn hình nhiều trạng thái.

| Mã | Nghĩa |
|---|---|
| SWP | Standard Work Point, điểm khối lượng chuẩn = phạm vi (Scope) × độ khó (Complexity) tra bảng cố định của skill |
| Mức khó | rất dễ 1–2 · dễ 3–5 · vừa 6–12 · khó 13–25 · rất khó 26+ SWP |
| k | Số giờ cho một SWP, tính từ bộ ước tay |
| D-xx, Q-x | Dòng trong [PREMISE.md](PREMISE.md) |
| FEAT-xx | Nhóm chức năng trong estimate LAB-1 |

## 1. Issue mẫu skill chọn để kiểm

Skill chọn 5 issue theo quy tắc cố định (điểm thấp nhất, điểm giữa, điểm cao nhất, ngoại lệ, độ tin cậy thấp nhất). Người duyệt xem từng issue, chọn mức khó rồi chọn điểm.

| Issue | Vì sao được chọn | Skill chấm (Scope × Complexity → SWP) | Người duyệt chốt | Lý do |
|---|---|---|---|---|
| #60 INC-01 Đặc tả file CSV ngày thanh toán | Điểm thấp nhất | 1 × 0 → 1 | 1 (giữ) | Chỉ là một tài liệu đặc tả, không có mã; mức rất dễ đúng với việc |
| #74 INC-12 Ngày hiệu lực tỷ lệ theo kỳ | Điểm giữa | 3 × 2 → 5 | 5 (giữ) | Ba chỗ sửa (API, hàm database, ô chọn tháng) và một quy tắc chặn kỳ đã chốt; mức dễ là hợp lý |
| #123 X02-03 Đăng ký xác thực hai lớp | Điểm cao nhất | 5 × 3 → 10 | 10 (giữ) | Chạm database, API, hai màn và dịch vụ xác thực bên ngoài; 10 SWP là đầu trên của mức vừa |
| #3 T10-02 Duyệt và mở lại yêu cầu điều chỉnh | Ngoại lệ | 5 × 3 → 10 | 10 (giữ) | Duyệt đồng thời, khoá lô, làm tròn tiền, nhật ký cùng giao dịch; độ khó đúng mức |
| #7 T10-04.2 Form ba bước điều chỉnh | Độ tin cậy thấp nhất | 2 × 2 → 3 | 3 (giữ) | Hai file màn hình, gọi API của issue anh em; giữ theo khuyến nghị. Lưu ý: giờ ước tay cho issue này là 14 giờ, tức 4,7 giờ/SWP, cao gần gấp đôi k (xem phần 2) |

Không sửa mẫu nào nên không có điểm lan sang issue tương tự; trạng thái hiệu chỉnh của báo cáo là "accepted".

## 2. Cách quy ra giờ

**Cách chọn:** quy ước đổi SWP ra giờ bằng một hệ số k chung, không ước giờ trực tiếp từng issue.
**Vì sao:** skill không tự đổi điểm ra giờ; ước tay 114 issue thì tốn và không nhất quán. Một hệ số lấy từ bộ ước tay độc lập giữ được thang đo của skill và vẫn bám kinh nghiệm thật.

**Quy tắc áp dụng nhất quán:**
1. k = tổng giờ ước tay ÷ tổng SWP của cùng 15 issue = 248 ÷ 99 = **2,51 giờ/SWP**. Issue cha ước tay lấy SWP bằng tổng issue con.
2. Issue lá ước tay giữ số tay. Issue cha ước tay chia giờ tay cho issue con theo tỷ lệ SWP.
3. Issue lá còn lại: giờ = SWP × k, làm tròn 0,5 giờ.
4. Issue cha và epic: giờ = tổng con. Script [`skills/ghi-swp-len-project.py`](skills/ghi-swp-len-project.py) làm cả 4 bước và ghi lên Project.

**Độ tin cậy của k:**

| Nhóm | Số mẫu | Giờ | SWP | Giờ/SWP |
|---|---|---|---|---|
| Cả bộ | 15 | 248 | 99 | 2,51 |
| Issue không tách | 9 | 110 | 50 | 2,20 |
| Issue đã tách con sau khi ước | 6 | 138 | 49 | 2,82 |
| Thấp nhất / cao nhất | — | — | — | 1,4 (#18) / 4,7 (#7) |

- Issue người ước thấy to (vượt 16 giờ) có số giờ trên điểm cao hơn: skill chấm nhẹ hơn cảm nhận của người làm ở việc lớn.
- Chỉ có 1 mẫu QA (#128, 2,8 giờ/SWP) nên không đủ để tính k riêng cho QA; dùng chung k.
- Giờ ước tay gồm cả tự kiểm theo tiêu chí xong, chưa gồm QA viết testcase và chạy kiểm thử riêng.

### Bộ ước tay (ước "mù", trước khi chạy skill)

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

### Hai điều phát hiện khi ước, đã xử lý

1. **6/15 issue vượt trần 16 giờ** mà [task-breakdown.md](task-breakdown.md) đặt ra: #105 (30), #51 (28), #83 (24), #114 (20), #124 (18), #88 (18). Như vậy AI soạn backlog đã đánh giá độ to thấp hơn người ước.
   Xử lý: tách 6 issue này thành 12 issue con (#144–#155) theo đúng cách người ước tự phân rã giờ. Giờ ước giữ ở issue cha vì đó là số ước mù; khi quy đổi sẽ so với tổng SWP của các issue con.
   Backlog sau khi tách: 124 việc nhỏ nhất, 114 được chấm điểm.
2. **Một issue mẫu có sẵn số giờ do AI ghi trong thân:** #124 ghi "ước lượng gần 16 giờ". Người ước đã thấy số này và cộng thêm 2 giờ kèm lý do (ghi chú dòng #124). Các issue mẫu khác không có số giờ trong thân.
   Xử lý: gỡ mọi số giờ do AI ghi khỏi thân issue (#124, X01-05, T15-03 và câu "ước … giờ" ở 7 issue cha tách đợt trước) trước khi chạy skill, để skill và người chấm không bị neo theo số đó.

## 3. Tổng theo epic

| Epic | Số issue lá | Tổng SWP | Tổng giờ | Ghi chú |
|---|---|---|---|---|
| E-T02 Bảng điều khiển đầu ca | 4 | 18 | 41 |  |
| E-T03 Quản trị tài khoản | 3 | 17 | 42.5 |  |
| E-T04 Tư cách tham gia thị trường | 8 | 48 | 109 |  |
| E-T05 Lô hàng: nhận, thẩm định, công khai | 5 | 40 | 100 |  |
| E-T06 Giao dịch: bán thoả thuận và đấu giá | 9 | 56 | 138 |  |
| E-T08 Giao nhận nhiều đợt | 7 | 31 | 77 |  |
| E-T09 Đối soát, khoá ngày, lịch chợ | 9 | 45 | 118 | Có #51 ước tay, đã tách 2 con |
| E-T10 Điều chỉnh sau khoá sổ | 5 | 31 | 84 | Có #7 ước tay |
| E-INC 完納奨励金 (thưởng thanh toán đủ hạn) | 16 | 64 | 163.5 | Có 1 issue ước tay (#65) |
| E-T12 Phiên bản tỷ lệ thưởng | 3 | 25 | 53.5 |  |
| E-T13 Nhật ký thao tác | 4 | 23 | 64 |  |
| E-T14 Báo cáo và xuất dữ liệu | 10 | 50 | 125.5 | Có #88 ước tay, đã tách 2 con |
| E-T15 Quy tắc và gửi thông báo | 10 | 60 | 155 | Có #105 ước tay, đã tách 2 con |
| E-T16 Hộp thư thông báo | 3 | 14 | 35 |  |
| E-X01 Nền tảng vận hành | 7 | 38 | 90 |  |
| E-X02 Bảo mật và phân quyền | 5 | 30 | 78 |  |
| E-X03 Kiểm thử và triển khai | 6 | 32 | 81.5 | Đội QA; chỉ 1 mẫu ước tay (#128) nên dùng chung k |
| **Tổng** | **114** | **622** | **1.555,5** | Không gồm 10 câu hỏi khách E-X04 |

## 4. So với estimate LAB-1

LAB-1 ước theo vai (FE, BE, QA) cho 13 nhóm chức năng: FE + BE 156 ngày công, QA 45 ngày công. Giờ LAB-5 đã gồm tự kiểm nhưng không gồm QA chạy kiểm thử riêng, nên bảng chỉ so với phần FE + BE của LAB-1. Hai epic dùng chung (E-X01, E-X03: 171,5 giờ) không có nhóm chức năng tương ứng ở LAB-1 nên để ngoài bảng. LAB-1 còn các khoản design, BrSE, PM, hạ tầng, sửa lỗi và dự phòng; LAB-5 không chia thành issue nên cũng để ngoài.

**So theo tỷ trọng %** (phần trăm trong tổng của cùng bảng):

| Phần | Epic LAB-5 | LAB-1 FE + BE, giờ (%) | LAB-5, giờ (%) | Chênh tỷ trọng | Vì sao |
|---|---|---|---|---|---|
| FEAT-01 Xác thực, tài khoản | E-T03 + E-X02 | 56 (5.1%) | 120.5 (8.7%) | +3.6 điểm % | Tăng: LAB-1 bỏ sót ràng buộc bảo mật (xác thực hai lớp bắt buộc theo vai, giới hạn đăng nhập sai, chặn vai theo ma trận menu D-11) |
| FEAT-02 Tư cách tham gia | E-T04 | 63 (5.8%) | 109 (7.9%) | +2.1 điểm % | Tăng: LAB-1 bỏ sót ràng buộc (bốn trạng thái tư cách, ba đường gỡ tạm ngưng, xét lại); thêm lịch sử tư cách theo PREMISE Bảng 1 dòng D-45 |
| FEAT-03 Nhận và thẩm định lô | E-T05 | 98 (9.0%) | 100 (7.2%) | -1.7 điểm % | Giảm: prototype đã làm màn nhận lô và thẩm định; thêm bước công khai theo PREMISE Bảng 3 dòng Q5 · D-29 |
| FEAT-04 + 05 Giao dịch, đấu giá | E-T06 | 147 (13.5%) | 138 (10.0%) | -3.5 điểm % | Giảm: prototype đã làm luồng giao dịch; tăng lại phần nhỏ theo PREMISE Bảng 1 dòng D-41 (mã giao dịch) và D-42 (chờ xác nhận kết quả đấu giá) |
| FEAT-06 Điều chỉnh sau khoá sổ | E-T10 | 63 (5.8%) | 84 (6.1%) | +0.3 điểm % | Tăng: LAB-1 bỏ sót ràng buộc chứng cứ đính kèm thật (luồng nháp, kho tệp riêng) |
| FEAT-07 Giao nhận | E-T08 | 112 (10.3%) | 77 (5.6%) | -4.7 điểm % | Giảm: prototype đã làm giao nhận nhiều đợt; chỉ sửa theo PREMISE Bảng 1 dòng Q3 · D-14 và D-40 |
| FEAT-08 Đối soát, khoá ngày | E-T09 + E-T02 | 112 (10.3%) | 159 (11.5%) | +1.2 điểm % | Tăng: PREMISE Bảng 1 dòng D-43 (lịch chợ, job mở và đóng ngày) và Q4 · D-10 (khoá ngày chặn mềm) |
| FEAT-09 完納奨励金 | E-INC | 84 (7.7%) | 163.5 (11.8%) | +4.1 điểm % | Tăng: PREMISE Bảng 2 dòng Q2 · D-08 (bảng tiền về, nhập CSV), Q6 · D-39 (cột loại bên mua) và Bảng 1 dòng D-44 (đẩy chênh lệch sang kỳ mở) |
| FEAT-10 Báo cáo | E-T14 | 126 (11.5%) | 125.5 (9.1%) | -2.5 điểm % | Gần bằng: prototype có 2 báo cáo, phần còn lại khớp phạm vi LAB-1 |
| FEAT-11 Nhật ký thao tác | E-T13 | 63 (5.8%) | 64 (4.6%) | -1.1 điểm % | Gần bằng |
| FEAT-12 Thông báo | E-T15 + E-T16 | 91 (8.3%) | 190 (13.7%) | +5.4 điểm % | Tăng gấp đôi: LAB-1 bỏ sót ràng buộc vận hành (gửi email thật, thử lại tối đa 3 lần, hàng đợi cảnh báo, quy tắc có phiên bản) |
| FEAT-13 Phiên bản tỷ lệ | E-T12 | 77 (7.1%) | 53.5 (3.9%) | -3.2 điểm % | Giảm: prototype đã có màn quản trị tỷ lệ; LAB-5 chỉ sửa chỗ lệch |
| **Tổng** | | **1092** | **1384** | | |

**So giờ trực tiếp** (chỉ hai gói đã chốt so trực tiếp):

| Gói | LAB-1 FE + BE | LAB-1 có QA | LAB-5 | Nhận xét |
|---|---|---|---|---|
| T-14 Báo cáo (FEAT-10) | 126 giờ | 154 giờ | 125,5 giờ | Gần như bằng nhau |
| T-15 Thông báo (FEAT-12) | 91 giờ | 119 giờ | 155 giờ (190 giờ nếu gộp hộp thư E-T16) | Tăng khoảng 70–110%: LAB-1 chưa tính gửi email thật, thử lại và hàng đợi cảnh báo |

## Câu chờ quyết

- **#7 có nên chấm lại không?** Giờ trên điểm của #7 cao gần gấp đôi k. Nếu người duyệt nâng #7 lên mức 4–5 SWP thì skill sẽ lan sang các issue màn hình cùng nhóm. Hiện giữ nguyên theo khuyến nghị; đổi sau phải chạy lại skill và ghi lý do (khuyến nghị: giữ, vì k đã hấp thụ chênh lệch qua bộ ước tay).
