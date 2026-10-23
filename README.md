# Product A — LAB-5: bẻ việc, chấm SWP, giả lập sprint

**Học viên:** Tran Cong Ngoc My (GitHub `mytcn-1511`) · **Khoá:** AIDD Leaders 2026 · **Đề:** Product A — hệ thống hỗ trợ nghiệp vụ chợ bán buôn thuỷ sản

## Tổng quan

- **Nguồn:** backlog được bẻ từ bộ thiết kế LAB-4 nộp ngày **08/10/2026** (16 gói việc theo màn hình, 26 màn hình).
- **Có thay đổi so với LAB-4**, khai đủ ở [PREMISE.md](PREMISE.md):
  - **Bảng 1 — Sửa thiết kế:** 10 dòng. Gồm 4 điểm từ góp ý review LAB-4 (D-42 đến D-45) và 1 mâu thuẫn spec phát hiện khi bẻ việc (D-49).
  - **Bảng 2 — Giả định bổ sung:** 4 dòng.
  - **Bảng 3 — Hướng đã chốt:** 6 dòng.
  - **Câu hỏi gửi khách:** 11 câu.
- **Backlog trên GitHub Project:** 155 item, gồm **18 epic**, 111 issue và 26 issue con.
  - 124 việc nhỏ nhất. Trong đó 114 việc được chấm điểm; 10 câu hỏi gửi khách không chấm.
  - Tổng **667 SWP** (điểm khối lượng chuẩn) sau khi người duyệt sửa 1 trong 5 mẫu, quy ra **1.511 giờ** với hệ số 2,25 giờ/SWP. Hệ số lấy từ 15 issue người phụ trách tự ước trước khi chạy skill.
- **Sprint đã giả lập:** **Iteration 1** (23/10–05/11/2026). Xong 16/21 issue, 78/107 SWP. Iteration 2 đã xếp sẵn 21 issue, chưa chạy.
- **完納奨励金** (tiền thưởng thanh toán đủ hạn) là ràng buộc đặc thù của đề. Phần này tách thành epic riêng **#59 E-INC**. Mọi issue chạm tới thưởng có nhãn `constraint:kanno-shoreikin`.

## Link

| Mục | Link |
|---|---|
| Repo | https://github.com/mytcn-1511/product-a-lab5-backlog |
| GitHub Project | https://github.com/users/mytcn-1511/projects/1 |
| Báo cáo HTML của skill chấm SWP | [`swp-report/estimate-swp-mytcn-1511-project-1-20261023-1115.html`](swp-report/estimate-swp-mytcn-1511-project-1-20261023-1115.html) (bản dùng) · bản hiệu chỉnh lần đầu: [`…-20261022-1031.html`](swp-report/estimate-swp-mytcn-1511-project-1-20261022-1031.html) |

- **Báo cáo HTML:** chạy `tkm:estimate-swp` ngày 22/10/2026, mức `high`, không đẩy kết quả lên KPI (bản đầu ở commit `7555d17`). Ngày 23/10 hiệu chỉnh lại sau khi người duyệt nâng mẫu #7 từ 3 lên 5 SWP; điểm ban đầu của skill không đổi.
- **Cách xem báo cáo HTML:** tải file về rồi mở bằng trình duyệt. File tự chứa toàn bộ, không cần mạng.
- **Kiểm truy cập ẩn danh (23/10/2026):** khi chưa đăng nhập, repo, Project và file HTML đều mở được (HTTP 200). Người phụ trách đã mở thử bằng cửa sổ ẩn danh ngày 23/10/2026: repo và Project xem được đầy đủ, không cần đăng nhập.
- **Prototype:** bản `product-a-prototype` (LAB-3) đang để riêng tư theo mốc LAB-4. Vì vậy cột "File chạm" trong issue ghi đường dẫn dạng chữ. Các đường dẫn này sẽ đổi thành link khi prototype được công khai ở LAB-7.

## Cấu trúc repo

| File / thư mục | Nội dung |
|---|---|
| [README.md](README.md) | File này |
| [PREMISE.md](PREMISE.md) | Tiền đề: backlog khác LAB-4 ở đâu. Có 3 bảng (sửa thiết kế, giả định bổ sung, hướng đã chốt) và bảng câu hỏi gửi khách, mỗi dòng trỏ tới số issue |
| [task-breakdown.md](task-breakdown.md) | Nguyên tắc chia task, bảng spec → issue, hạng mục 完納奨励金, chỗ hở của spec LAB-4 |
| [estimate.md](estimate.md) | Đường dẫn báo cáo HTML, 5 issue mẫu đã kiểm, cách quy ra giờ, tổng theo epic, so với LAB-1. Phụ lục A là bộ ước tay |
| [progress-report.md](progress-report.md) | Báo cáo tiến độ Sprint 1: trạng thái, biểu đồ SWP còn lại, rủi ro trễ |
| [AI-report.md](AI-report.md) | Đã dùng AI thế nào, con người review ở đâu, điểm hiệu quả và chưa tốt |
| [swp-report/](swp-report/) | Báo cáo HTML của skill `tkm:estimate-swp`: bản dùng (23/10, sau khi sửa mẫu #7) và bản hiệu chỉnh lần đầu (22/10) để đối chiếu |
| [uoc-gio-tay/](uoc-gio-tay/) | File Excel 15 issue người phụ trách tự ước giờ trước khi chạy skill |
| [skills/backlog.yaml](skills/backlog.yaml) | Nguồn duy nhất của backlog: 18 epic, issue, issue con, tiêu chí xong, file chạm, thứ tự làm |
| [skills/tao-backlog-len-project.py](skills/tao-backlog-len-project.py) | Đọc YAML, tạo hoặc cập nhật issue, nối cha–con, thêm vào Project. Chạy lại không tạo trùng |
| [skills/ghi-swp-len-project.py](skills/ghi-swp-len-project.py) | Đọc SWP từ báo cáo HTML và bộ ước tay, tính giờ, ghi hai trường SWP và "Giờ ước lượng" lên Project |
| [skills/kich-ban-sprint-1.yaml](skills/kich-ban-sprint-1.yaml) | Kịch bản giả lập Sprint 1 theo ngày và theo vai |
| [skills/ap-kich-ban-sprint.py](skills/ap-kich-ban-sprint.py) | Áp kịch bản: bình luận "Ngày giả lập" lên issue, đặt Status, đóng issue Done |
| [skills/xuat-tien-do.py](skills/xuat-tien-do.py) | Xuất bảng trạng thái và bảng SWP còn lại theo ngày cho báo cáo tiến độ; kiểm Project khớp kịch bản |

## Spec → epic

| Spec LAB-4 (gói việc, màn hình) hoặc dòng PREMISE | Epic trên Project | Ghi chú |
|---|---|---|
| T-01 Đăng nhập (SCR-01) | #113 E-X01 Nền tảng vận hành · #120 E-X02 Bảo mật và phân quyền | Gói đăng nhập gộp vào hai epic xuyên suốt |
| T-02 Bảng điều khiển (SCR-02) | #8 E-T02 | Có #143 cho 8 màn đích đọc tham số lọc |
| T-03 Tài khoản và quyền (SCR-03) | #12 E-T03 | |
| T-04 Hồ sơ người tham gia (SCR-04, SCR-05) | #16 E-T04 | PREMISE D-45 (bảng lịch sử tư cách) |
| T-05 Nhận lô, thẩm định (SCR-06, SCR-07) | #25 E-T05 | PREMISE Q5 · D-29 (bước công khai lô) |
| T-06, T-07 Giao dịch, đấu giá (SCR-08 đến SCR-10) | #31 E-T06 | PREMISE D-41 (mã giao dịch), D-42 (chờ xác nhận kết quả đấu giá), Q1 · D-23 (hạn mức) |
| T-08 Giao nhận (SCR-14 đến SCR-16) | #42 E-T08 | PREMISE Q3 · D-14, D-40, Q8 · D-30. #46 có nhãn 完納奨励金 |
| T-09 Đối soát, khoá ngày, tranh chấp (SCR-17 đến SCR-19) | #50 E-T09 | PREMISE D-43 (lịch chợ), Q4 · D-10 (khoá ngày chặn mềm) |
| T-10 Điều chỉnh sau khoá sổ (SCR-12, SCR-13) | #1 E-T10 | #3 có nhãn 完納奨励金 (dòng chênh lệch là đầu vào của thưởng) |
| T-11 Kết quả 完納奨励金 (SCR-20) | #59 E-INC | **Ràng buộc đặc thù 完納奨励金.** PREMISE Q2 · D-08, Q6 · D-39, D-44, Q7 |
| T-12 Phiên bản tỷ lệ (SCR-21) | #76 E-T12 | **Ràng buộc đặc thù 完納奨励金** |
| T-13 Nhật ký thao tác (SCR-11, SCR-23) | #80 E-T13 | |
| T-14 Báo cáo (SCR-22) | #84 E-T14 | #85, #86, #89, #90 có nhãn 完納奨励金 (báo cáo thưởng RPT-07) |
| T-15 Quy tắc và gửi thông báo (SCR-24, SCR-25) | #96 E-T15 | #103 có nhãn 完納奨励金 (thông báo chốt kỳ thưởng) |
| T-16 Hộp thư thông báo (SCR-26) | #109 E-T16 | |
| Thiết kế dữ liệu, danh sách API, mã lỗi chung (system-design, `_common`) | #113 E-X01 | PREMISE D-45, D-49 |
| Yêu cầu kiểm thử và triển khai | #125 E-X03 | Bộ kiểm thử tự động, kiểm nhanh sau khi đặt lại dữ liệu |
| Câu hỏi gửi khách trong PREMISE | #132 E-X04 | 10 issue, không chấm điểm |

Bảng truy vết chi tiết từng màn hình tới từng issue nằm ở [task-breakdown.md](task-breakdown.md), mục 2.
