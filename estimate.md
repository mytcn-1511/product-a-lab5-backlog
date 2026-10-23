# Ước lượng LAB-5 — Product A

**Báo cáo HTML của skill:** [`swp-report/estimate-swp-mytcn-1511-project-1-20261023-1115.html`](swp-report/estimate-swp-mytcn-1511-project-1-20261023-1115.html) — chạy `tkm:estimate-swp` ngày 22/10/2026 (mức `high`, không đẩy lên KPI), hiệu chỉnh lại ngày 23/10/2026 sau khi người duyệt sửa mẫu #7. Không chấm lại điểm ban đầu; chỉ chạy lại bước hiệu chỉnh của skill.
Bản hiệu chỉnh lần đầu (giữ nguyên cả 5 mẫu) vẫn giữ ở [`swp-report/estimate-swp-mytcn-1511-project-1-20261022-1031.html`](swp-report/estimate-swp-mytcn-1511-project-1-20261022-1031.html) để đối chiếu.

## Tóm tắt 10 dòng

1. Skill chấm 114 việc nhỏ nhất trên Project. Sau hiệu chỉnh, tổng là **667 SWP** (điểm khối lượng chuẩn), khoảng bất định 639–704 SWP. Điểm ban đầu của skill là 622 SWP.
2. 88 việc có độ tin cậy cao, 26 trung bình, không việc nào thấp; không việc nào bị đề xuất tách.
3. 10 câu hỏi gửi khách (epic E-X04) không chấm điểm, theo quyết định từ đầu.
4. Skill chọn 5 issue mẫu. Người duyệt giữ 4 mẫu và **nâng #7 từ 3 lên 5 SWP**, vì bộ ước tay cho thấy skill chấm nhẹ issue màn hình nhiều trạng thái. Mức sửa lan sang 16 issue cùng nhóm.
5. Đổi điểm ra giờ bằng hệ số **k = 2,25 giờ/SWP**, lấy từ 15 issue người phụ trách tự ước trước khi chạy skill (248 giờ ÷ 110 SWP).
6. Issue ước tay giữ số tay; issue còn lại = SWP × k, làm tròn 0,5 giờ; issue cha bằng tổng con.
7. Tổng giờ toàn backlog: **1.511 giờ ≈ 216 ngày công** (1 ngày công = 7 giờ), chưa gồm QA chạy kiểm thử riêng.
8. So với LAB-1, phần chức năng và nền tảng chung tăng từ 1.225 giờ lên 1.436 giờ. Tỷ trọng tăng mạnh nhất ở thông báo, thưởng và xác thực; giảm nhiều nhất ở nền tảng chung, giao nhận và giao dịch, nơi prototype đã làm sẵn.
9. Số SWP và giờ đã ghi lên Project bằng script; đọc lại từ Project khớp 100% với báo cáo HTML.
10. Sau khi sửa #7, giờ trên điểm của 15 mẫu nằm trong khoảng 1,4–3,2 (trước là 1,4–4,7). Hệ số k ổn định hơn.

| Mã | Nghĩa |
|---|---|
| SWP | Standard Work Point, điểm khối lượng chuẩn = phạm vi (Scope) × độ khó (Complexity) tra bảng cố định của skill |
| Mức khó | rất dễ 1–2 · dễ 3–5 · vừa 6–12 · khó 13–25 · rất khó 26+ SWP |
| k | Số giờ cho một SWP, tính từ bộ ước tay |
| D-xx, Q-x | Dòng trong [PREMISE.md](PREMISE.md) |
| FEAT-xx | Nhóm chức năng trong estimate LAB-1 |
| Prototype | Bản mẫu chạy được làm ở LAB-3; LAB-5 chỉ chia việc cho phần còn thiếu hoặc lệch thiết kế |
| Epic, issue lá, issue cha | Epic là nhóm việc lớn; issue lá là việc nhỏ nhất được chấm điểm; issue cha có issue con, điểm bằng tổng con |
| QA, testcase | Kiểm thử viên; kịch bản kiểm thử |

## 1. Issue mẫu skill chọn để kiểm

Skill chọn 5 issue theo quy tắc cố định (điểm thấp nhất, điểm giữa, điểm cao nhất, ngoại lệ, độ tin cậy thấp nhất). Người duyệt xem từng issue, chọn mức khó rồi chọn điểm.

| Issue | Vì sao được chọn | Skill chấm (Scope × Complexity → SWP) | Người duyệt chốt | Lý do |
|---|---|---|---|---|
| #60 INC-01 Đặc tả file CSV ngày thanh toán | Điểm thấp nhất | 1 × 0 → 1 | 1 (giữ) | Chỉ là một tài liệu đặc tả, không có mã; mức rất dễ đúng với việc |
| #74 INC-12 Ngày hiệu lực tỷ lệ theo kỳ | Điểm giữa (trung vị dưới) | 3 × 2 → 5 | 5 (giữ) | Ba chỗ sửa (API, hàm database, ô chọn tháng) và một quy tắc chặn kỳ đã chốt; mức dễ là hợp lý |
| #123 X02-03 Đăng ký xác thực hai lớp | Điểm cao nhất | 5 × 3 → 10 | 10 (giữ) | Chạm database, API, hai màn và dịch vụ xác thực bên ngoài; 10 SWP nằm trong mức vừa (6–12) |
| #3 T10-02 Duyệt và mở lại yêu cầu điều chỉnh | Ngoại lệ: cách xa điểm giữa nhất trong các issue chưa được chọn | 5 × 3 → 10 | 10 (giữ) | Nhiều ràng buộc khó trên ít file: duyệt đồng thời, khoá lô, làm tròn tiền, nhật ký cùng giao dịch; độ khó đúng mức |
| #7 T10-04.2 Form ba bước điều chỉnh | Độ tin cậy thấp nhất | 2 × 2 → 3 | **5 (sửa, thành 3 × 2)** | Skill chỉ đếm 2 file màn hình. Thực tế là form 3 bước nhiều trạng thái (nháp, tải tệp, gửi duyệt), lỗi tải tệp hiện tại ô, cộng 7 điều kiện xong chung của màn hình. Giờ ước tay là 14 giờ, tức 4,7 giờ/SWP, gần gấp đôi hệ số chung lúc đó (2,51): bằng chứng skill chấm nhẹ |

Lần duyệt đầu (22/10) giữ nguyên cả 5 mẫu. Ngày 23/10, khi so với bộ ước tay, người duyệt thấy #7 lệch rõ nhất nên sửa lại. Trạng thái hiệu chỉnh của báo cáo thành "calibrated" (đã hiệu chỉnh).

**Mức sửa lan sang đâu.** Skill đổi #7 từ phạm vi bậc 2 lên bậc 3, giữ nguyên độ khó. Mức +1 bậc phạm vi được áp cho mọi issue cùng nhóm: màn hình, tính năng, nhiều thành phần, có trạng thái. Không lan sang nhóm khác.

| Issue cùng nhóm | Trước → sau (SWP) |
|---|---|
| #4, #23, #48, #54 | 3 → 5 |
| #27, #36, #145, #147 | 4 → 6 |
| #22, #49, #56, #72, #79, #150 | 5 → 8 |
| #121, #143 | 8 → 12 |

Người duyệt chọn cho lan vì 5 mẫu màn hình trong bộ ước tay (#27, #7, #51, #83, #105) đều có giờ trên điểm cao hơn hệ số chung, tức skill chấm nhẹ cả nhóm, không riêng #7.

## 2. Cách quy ra giờ

**Cách chọn:** quy ước đổi SWP ra giờ bằng một hệ số k chung, không ước giờ trực tiếp từng issue.
**Vì sao:** skill không tự đổi điểm ra giờ; ước tay 114 issue thì tốn và không nhất quán. Một hệ số lấy từ bộ ước tay độc lập giữ được thang đo của skill và vẫn bám kinh nghiệm thật.

**Quy tắc áp dụng nhất quán:**
1. k = tổng giờ ước tay ÷ tổng SWP của cùng 15 issue = 248 ÷ 110 = **2,25 giờ/SWP** (sau hiệu chỉnh; trước là 248 ÷ 99 = 2,51). Issue cha ước tay lấy SWP bằng tổng issue con.
2. Issue lá ước tay giữ số tay. Issue cha ước tay chia giờ tay cho issue con theo tỷ lệ SWP.
3. Issue lá còn lại: giờ = SWP × k, làm tròn 0,5 giờ.
4. Issue cha và epic: giờ = tổng con. Script [`skills/ghi-swp-len-project.py`](skills/ghi-swp-len-project.py) làm cả 4 bước và ghi lên Project.

**Độ tin cậy của k:**

| Nhóm | Số mẫu | Giờ | SWP | Giờ/SWP |
|---|---|---|---|---|
| Cả bộ | 15 | 248 | 110 | 2,25 |
| Issue không tách | 9 | 110 | 54 | 2,04 |
| Issue đã tách con sau khi ước | 6 | 138 | 56 | 2,46 |
| Thấp nhất / cao nhất | — | — | — | 1,4 (#18) / 3,2 (#65) |

- Trước khi sửa #7, khoảng giờ/SWP là 1,4–4,7; sau khi sửa còn 1,4–3,2, nên k đại diện tốt hơn cho cả bộ.
- Tính cả nhóm, issue người ước vượt 16 giờ vẫn có số giờ trên điểm cao hơn (2,46 so với 2,04). Xét từng issue thì không đều: #114 (20 giờ) chỉ 2,0.
- Chỉ có 1 mẫu QA (#128, 2,8 giờ/SWP) nên không đủ để tính k riêng cho QA; dùng chung k.
- Giờ ước tay gồm cả tự kiểm theo tiêu chí xong, chưa gồm QA viết testcase và chạy kiểm thử riêng.

- Bảng 15 issue ước tay và hai điều phát hiện khi ước nằm ở **Phụ lục A** cuối file.

## 3. Tổng theo epic

| Epic | Số issue lá | Tổng SWP | Tổng giờ | Ghi chú |
|---|---|---|---|---|
| E-T02 Bảng điều khiển đầu ca | 4 | 22 | 47 |  |
| E-T03 Quản trị tài khoản | 3 | 17 | 38,5 |  |
| E-T04 Tư cách tham gia thị trường | 8 | 53 | 112 |  |
| E-T05 Lô hàng: nhận, thẩm định, công khai | 5 | 42 | 91 |  |
| E-T06 Giao dịch: bán thoả thuận và đấu giá | 9 | 58 | 129,5 |  |
| E-T08 Giao nhận nhiều đợt | 7 | 36 | 82,5 |  |
| E-T09 Đối soát, khoá ngày, lịch chợ | 9 | 52 | 121 | Có #51 ước tay, đã tách 2 con |
| E-T10 Điều chỉnh sau khoá sổ | 5 | 36 | 84 | Có #7 ước tay (mẫu đã sửa) |
| E-INC 完納奨励金 (thưởng thanh toán đủ hạn) | 16 | 67 | 158 | Có 1 issue ước tay (#65) |
| E-T12 Phiên bản tỷ lệ thưởng | 3 | 28 | 56,5 |  |
| E-T13 Nhật ký thao tác | 4 | 25 | 60 |  |
| E-T14 Báo cáo và xuất dữ liệu | 10 | 50 | 116 | Có #88 ước tay, đã tách 2 con |
| E-T15 Quy tắc và gửi thông báo | 10 | 63 | 143,5 | Có #105 ước tay, đã tách 2 con |
| E-T16 Hộp thư thông báo | 3 | 14 | 32 |  |
| E-X01 Nền tảng vận hành | 7 | 38 | 83,5 |  |
| E-X02 Bảo mật và phân quyền | 5 | 34 | 81 |  |
| E-X03 Kiểm thử và triển khai | 6 | 32 | 75 | Đội QA; chỉ 1 mẫu ước tay (#128) nên dùng chung k |
| **Tổng** | **114** | **667** | **1.511** | Không gồm 10 câu hỏi khách E-X04 |

## 4. So với estimate LAB-1

LAB-1 ước theo vai (FE, BE, QA) cho 13 nhóm chức năng: FE + BE 156 ngày công, QA 45 ngày công. Giờ LAB-5 đã gồm tự kiểm nhưng không gồm QA chạy kiểm thử riêng, nên bảng chỉ so với phần FE + BE của LAB-1.
Bảng gồm 13 nhóm chức năng và dòng nền tảng chung (共通基盤) của LAB-1. Để ngoài bảng: E-X03 kiểm thử và triển khai (75 giờ), vì LAB-1 tính phần này trong vai QA và hạ tầng; các khoản design, BrSE, PM, hạ tầng, sửa lỗi, dự phòng và kết nối kế toán của LAB-1, vì LAB-5 không chia chúng thành issue.

**So theo tỷ trọng** (phần trăm trong tổng của cùng bảng) **và theo giờ:**

| Phần | Epic LAB-5 | LAB-1 FE + BE, giờ (%) | LAB-5, giờ (%) | Chênh | Vì sao |
|---|---|---|---|---|---|
| FEAT-01 Xác thực, tài khoản | E-T03 + E-X02 | 56 (4,6%) | 119,5 (8,3%) | +63,5 giờ · +3,8 điểm phần trăm | LAB-1 bỏ sót ràng buộc nên tăng: xác thực hai lớp bắt buộc theo vai, giới hạn đăng nhập sai, chặn vai theo ma trận menu (D-11 trong thiết kế LAB-4) |
| FEAT-02 Tư cách tham gia | E-T04 | 63 (5,1%) | 112 (7,8%) | +49 giờ · +2,7 điểm phần trăm | LAB-1 bỏ sót ràng buộc nên tăng: bốn trạng thái tư cách, ba đường gỡ tạm ngưng, xét lại; thêm lịch sử tư cách theo PREMISE Bảng 1 dòng D-45 |
| FEAT-03 Nhận và thẩm định lô | E-T05 | 98 (8%) | 91 (6,3%) | -7 giờ · -1,7 điểm phần trăm | Prototype đã làm màn nhận lô và thẩm định nên giảm; thêm bước công khai lô theo PREMISE Bảng 3 dòng Q5 · D-29 |
| FEAT-04 + 05 Giao dịch, đấu giá | E-T06 | 147 (12%) | 129,5 (9%) | -17,5 giờ · -3 điểm phần trăm | Prototype đã làm luồng giao dịch nên giảm; tăng lại phần nhỏ theo PREMISE Bảng 1 dòng D-41 (mã giao dịch) và D-42 (chờ xác nhận kết quả đấu giá) |
| FEAT-06 Điều chỉnh sau khoá sổ | E-T10 | 63 (5,1%) | 84 (5,8%) | +21 giờ · +0,7 điểm phần trăm | LAB-1 bỏ sót ràng buộc nên tăng: chứng cứ đính kèm phải là tệp thật (luồng nháp, kho tệp riêng) |
| FEAT-07 Giao nhận | E-T08 | 112 (9,1%) | 82,5 (5,7%) | -29,5 giờ · -3,4 điểm phần trăm | Prototype đã làm giao nhận nhiều đợt nên giảm; chỉ sửa theo PREMISE Bảng 1 dòng Q3 · D-14 và D-40 |
| FEAT-08 Đối soát, khoá ngày | E-T09 + E-T02 | 112 (9,1%) | 168 (11,7%) | +56 giờ · +2,6 điểm phần trăm | Đổi tiền đề nên tăng: PREMISE Bảng 1 dòng D-43 (lịch chợ, job mở và đóng ngày) và Q4 · D-10 (khoá ngày chặn mềm). Bảng điều khiển đầu ca (E-T02) xếp vào đây vì LAB-1 tính nó trong nhóm đối soát |
| FEAT-09 完納奨励金 | E-INC | 84 (6,9%) | 158 (11%) | +74 giờ · +4,1 điểm phần trăm | Đổi tiền đề nên tăng: PREMISE Bảng 2 dòng Q2 · D-08 (bảng tiền về, nhập CSV), Bảng 1 dòng Q6 · D-39 (cột loại bên mua) và D-44 (đẩy chênh lệch sang kỳ mở). Lưu ý LAB-1 còn tính riêng 77 giờ kết nối kế toán và chuyển dữ liệu, trùng một phần với việc nhập CSV ở đây |
| FEAT-10 Báo cáo | E-T14 | 126 (10,3%) | 116 (8,1%) | -10 giờ · -2,2 điểm phần trăm | Prototype đã làm 2 báo cáo nên giảm, bù lại LAB-1 bỏ sót ràng buộc sinh sẵn báo cáo ngày trước 11:00 và chống chèn công thức vào CSV nên tăng; kết quả giảm nhẹ |
| FEAT-11 Nhật ký thao tác | E-T13 | 63 (5,1%) | 60 (4,2%) | -3 giờ · -1 điểm phần trăm | Prototype đã có màn nhật ký nên giảm, bù lại LAB-1 bỏ sót ràng buộc tra theo mã giao dịch và ghi vết mỗi lần tra (luật bảo vệ dữ liệu cá nhân của Nhật) nên tăng; kết quả gần bằng |
| FEAT-12 Thông báo | E-T15 + E-T16 | 91 (7,4%) | 175,5 (12,2%) | +84,5 giờ · +4,8 điểm phần trăm | LAB-1 bỏ sót ràng buộc vận hành nên tăng: gửi email thật, thử lại tối đa 3 lần, hàng đợi cảnh báo, quy tắc có phiên bản |
| FEAT-13 Phiên bản tỷ lệ | E-T12 | 77 (6,3%) | 56,5 (3,9%) | -20,5 giờ · -2,4 điểm phần trăm | Prototype đã có màn quản trị tỷ lệ nên giảm; LAB-5 chỉ sửa chỗ lệch |
| Nền tảng chung (共通基盤) | E-X01 | 133 (10,9%) | 83,5 (5,8%) | -49,5 giờ · -5 điểm phần trăm | Prototype đã có khung ứng dụng nên giảm; LAB-5 chỉ thêm bảng mã lỗi chung, kiểm biến môi trường, sao lưu, hàng đợi mất mạng cho một màn |
| **Tổng** | | **1.225** | **1.436** | **+211 giờ** | |

Tổng LAB-5 lớn hơn LAB-1 khoảng 17%, nên một phần giữ nguyên số giờ vẫn hiện tỷ trọng giảm (ví dụ báo cáo, nhật ký).

**So giờ trực tiếp** (chỉ hai gói báo cáo và thông báo, theo cách so đã chốt ngày 15/10 trong báo cáo brainstorm LAB-5):

| Gói | LAB-1 FE + BE | LAB-1 có QA | LAB-5 | Nhận xét |
|---|---|---|---|---|
| T-14 Báo cáo (FEAT-10) | 126 giờ | 154 giờ | 116 giờ | Thấp hơn khoảng 8%: prototype đã có 2 báo cáo |
| T-15 Thông báo (FEAT-12) | 91 giờ | 119 giờ | 143,5 giờ (175,5 giờ nếu gộp hộp thư E-T16) | Tăng khoảng 60–90%: LAB-1 chưa tính gửi email thật, thử lại và hàng đợi cảnh báo |

## Phụ lục A — Bộ ước tay (ước "mù", trước khi chạy skill)

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
