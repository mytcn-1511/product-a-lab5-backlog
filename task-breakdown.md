# Bẻ việc LAB-5 — Product A (chợ bán buôn thuỷ sản)

**Tóm tắt.** Thiết kế chi tiết LAB-4 đã được bẻ thành backlog trên GitHub Project công khai:
18 epic, 111 issue và 26 issue con, đánh số #1–#155. Trong đó 114 việc nhỏ nhất được chấm điểm.
10 issue còn lại là câu hỏi gửi khách (epic X-04), không chấm điểm.
Nguồn duy nhất của backlog là [`skills/backlog.yaml`](skills/backlog.yaml). Script [`skills/tao-backlog-len-project.py`](skills/tao-backlog-len-project.py)
đọc file này và đẩy lên Project; chạy lại nhiều lần cũng không tạo trùng.
Mọi chỗ khác với LAB-4 đã khai ở [`PREMISE.md`](PREMISE.md).

Project: https://github.com/users/mytcn-1511/projects/1

## Chú giải mã

| Mã | Nghĩa |
|---|---|
| E-xx | Epic. E-T02..E-T16 theo gói việc màn hình của LAB-4; E-INC là epic thưởng thanh toán đủ hạn; E-X01..E-X04 là việc xuyên suốt |
| T10-04, INC-08a | Issue. Mã đứng đầu tiêu đề issue trên GitHub, ví dụ `[T10-04] …` |
| T10-04.1 | Issue con của T10-04 |
| D-xx, B-xx, Q1..Q8 | Dòng trong PREMISE.md: D là điểm khác biệt hoặc quyết định thiết kế, B là quyết định nghiệp vụ còn treo từ LAB-4, Q là tám câu chưa có khách trả lời |
| SCR-xx | Màn hình trong spec LAB-4 |
| FEAT-xx | Nhóm chức năng trong danh sách chức năng LAB-1 |
| 完納奨励金 | Tiền thưởng thanh toán đủ hạn, chuỗi nghiệp vụ đặc thù của đề Product A |
| 業務日 | Ngày nghiệp vụ của chợ, tính theo giờ Nhật |

## 1. Nguyên tắc chia task

### Độ hạt: chia tới đâu thì dừng

- **Một issue là một thứ bàn giao được:** một màn hình, một API, một migration (bước đổi cấu trúc database), một báo cáo hay một bộ kiểm thử. Không tách một tính năng thành ba issue FE / BE / QA. Lý do: issue quá mỏng thì không tự kiểm được, và skill chấm SWP (điểm độ lớn công việc) chấm kém tin cậy.
- **Dừng khi một người làm xong trong khoảng 16 giờ** và mọi tiêu chí xong kiểm được trên một bản deploy.
- **Tách issue con khi issue vượt 16 giờ.** Lần rà ngày 21/10 tìm được 7 issue vượt trần: #34, #5, #85, #92, #97, #100, #106. Bộ ước tay cùng ngày (xem [estimate.md](estimate.md)) thấy thêm 6 issue vượt trần: #51, #83, #88, #105, #114, #124. Mỗi issue thành một issue cha có 2 issue con. Issue cha giữ bối cảnh. Issue con giữ phần việc và tiêu chí xong của mình. Điểm SWP chấm ở issue con, issue cha lấy tổng.
- **Không tách khi issue có nhiều tiêu chí nhưng cùng một thứ bàn giao.** 28 issue có 7–8 tiêu chí đều là ca thử của cùng một API hay một màn, nên vẫn giữ một issue.
- **Câu hỏi gửi khách là issue riêng** ở epic E-X04 (#133–#142), nhãn `lam-ro-voi-khach`, không chấm điểm. Issue phụ thuộc câu trả lời của khách cũng gắn nhãn này và ghi rõ đang dùng giả định nào.

### Định nghĩa xong

Mỗi issue có 4 khối cố định trong thân: **Bối cảnh · Việc · Tiêu chí xong · File chạm**. Issue tự đủ nghĩa, người đọc không cần mở tài liệu LAB-4.

- **Tiêu chí xong riêng:** viết dạng ca thử có số cụ thể. Ví dụ ở #3: giao dịch 100,3 kg giá 1.000 yên sửa về 100,1 kg thì chênh lệch là âm 200 yên, không phải âm 201. Issue chạm quy tắc nghiệp vụ phải có ca chứng minh chặn đúng, không chỉ luồng bình thường.
- **Định nghĩa xong chung cho mọi issue màn hình** (nhãn `doi:fe`), script chép vào thân issue:
  - Nhãn tiếng Nhật đúng thuật ngữ ở các màn khách sẽ tự thử.
  - Không lộ mã kỹ thuật (UUID, mã trạng thái thô, JSON thô) ra màn hình và nhật ký.
  - Ngày giờ một định dạng YYYY/MM/DD, theo giờ Nhật.
  - Lỗi hiện ngay tại ô nhập; nút đổi thành "Đang lưu" và khoá sau khi bấm; huỷ phải ghi lý do.
  - Thông báo chặn nói rõ hết hạn ngày nào và căn cứ gì.
  - Một luồng dùng được trên màn điện thoại 390 px, không cuộn ngang.
- **Issue chạm 業務日:** có ca thử "nhập giao dịch lúc 02:31 giờ Nhật trên máy chủ đặt múi giờ UTC" (PREMISE Bảng 3, dòng D-25).
- **Trạng thái Done** chỉ ghi khi tiêu chí xong đã kiểm được trên bản deploy thật.

### Cách dùng epic → issue → issue con trên Project

| Tầng | Trên GitHub | Ví dụ |
|---|---|---|
| Epic | Issue có tiêu đề `[E-xx] Epic: …`, thân nêu tiền đề, giả định, thứ tự làm | #1 `[E-T10] Epic: Yêu cầu điều chỉnh sau khoá sổ…` |
| Issue | Sub-issue (issue con theo tính năng của GitHub) của epic | #5 `[T10-04] Chứng cứ đính kèm thật…` |
| Issue con | Sub-issue của issue | #6 `[T10-04.1]`, #7 `[T10-04.2]` |

- Mọi tầng đều nằm trong Project, kể cả issue con, vì skill chấm điểm chỉ đọc item có trong Project.
- **Nhãn:** mỗi issue có một nhãn nguồn gốc (`nguon:moi` việc mới, `nguon:chenh-lech` sửa chỗ prototype lệch thiết kế, `nguon:gia-co` gia cố lỗi đã thấy) và một nhãn đội (`doi:fe`, `doi:be`, `doi:qa`, gắn theo lớp nặng nhất). Hai nhãn riêng: `constraint:kanno-shoreikin` và `lam-ro-voi-khach`.
- **Phụ thuộc:** khối "Làm sau" trong thân issue liệt kê số các issue phải xong trước.
- **Gom nhóm:** gõ `T10-` vào ô lọc của Project, hoặc chọn Group by → Parent issue.

## 2. Spec → issue

Mỗi dòng là một màn hình (SCR-xx) hoặc một tài liệu dùng chung của spec LAB-4. Mã FEAT ghi theo danh sách chức năng LAB-1. Cột cuối nêu phần spec chưa thành issue và lý do. "Không còn" nghĩa là mọi điểm chênh lệch giữa spec và prototype đã có issue. Phần giữ nguyên như prototype thì không cần issue. Issue con ghi dạng `#34 → #35, #36`.

| Spec | Epic | Issue / issue con | Phần spec chưa thành issue và vì sao |
|---|---|---|---|
| SCR-01 Đăng nhập · FEAT-01 | E-X01, E-X02, E-T03 | #117 (giới hạn đăng nhập sai, S-03), #121 (danh sách đường dẫn cho phép sau đăng nhập, S-06, S-04), #123, #124 (xác thực hai lớp, phiên 8 giờ), #15 (bỏ suy vai trò từ email, D-09) | Không còn — mọi điểm chênh lệch của spec đã có issue. Gói T-01 không có epic riêng; thân E-X01 ghi đã gộp vào X-01. |
| SCR-02 Bảng điều khiển theo vai trò · FEAT-08, FEAT-10 | E-T02, E-T16 | #9, #10, #11, #143 (màn đích đọc tham số lọc); #111 (dùng chung hàm đếm thông báo chưa đọc) | Không còn — mọi điểm chênh lệch của spec đã có issue. Nguồn sinh thông báo (D-31) nằm ở dòng SCR-26. |
| SCR-03 Tài khoản và quyền · FEAT-01 | E-T03, E-X02 | #13, #14, #15; #123 (cột bật/tắt xác thực hai lớp) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-04 Hồ sơ người tham gia · FEAT-02 (gộp SUSPENSION_RELEASE, REEXAMINATION_DECIDE) | E-T04, E-T06 | #17, #18, #19, #20, #21, #22, #24; #37 (cấu hình hạn mức tham gia, D-23) | 参加上限 chỉ làm theo giả định của đội; câu hỏi gửi khách ở X04-01 (#133). Thân E-T04 còn ghi: đường nộp lại hồ sơ sau khi hết hiệu lực (申請, nộp đơn) không có issue vì RFP chưa đủ bằng chứng. |
| SCR-05 Hồ sơ sắp hết hạn · FEAT-02 | E-T04, E-T02, E-T15, E-T14 | #21 (tìm kiếm an toàn, lọc theo trạng thái tư cách), #23 (bộ lọc lên URL, gõ tìm có trễ), #9 (bảng cấu hình ngưỡng), #98, #104 (quét hồ sơ sắp hết hạn, sinh thông báo), #105 (sửa ngưỡng, nhãn nút tự đổi), #91 (báo cáo hồ sơ hết hạn) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-06 Nhận lô · FEAT-03 | E-T05, E-T06, E-X02 | #30 (受入証憑, danh sách đơn vị, nút "Lưu và nhập tiếp", lỗi khoá ngoại 422), #32 (bộ đếm mã lô), #26, #27 (bước công khai lô, D-29); #121 (thêm vai đối soát vào menu, D-11) | Chặn khoá ngày khi lô thiếu chứng từ làm ở #53. Khoá chống gửi trùng khi tạo lô: để giai đoạn sau, vì lô do một người ở quầy nhập, rủi ro gửi trùng thấp hơn giao dịch; sẽ làm cùng lúc nối hàng đợi mất mạng. Hàng đợi mất mạng (D-15) chưa nối vào màn này: để giai đoạn sau, vì ở hiện trường mất mạng chủ yếu xảy ra ở bước ghi đợt giao; X01-05 (#118) làm màn đó trước và dựng khung dùng chung. |
| SCR-07 Ghi kết quả 目利き · FEAT-03 (gộp JUDGEMENT_RECORD) | E-T05 | #28 (ghi thẩm định bằng một hàm database, chặn ngày khoá, chống gửi trùng, giờ bấm trên thiết bị), #29 (bộ lọc lô chờ, lịch sử, hạng lấy từ bảng tra cứu) | Tra nhật ký theo mã lô làm ở #82. Hàng đợi mất mạng (D-15) chưa nối vào màn này: để giai đoạn sau, vì ở hiện trường mất mạng chủ yếu xảy ra ở bước ghi đợt giao; X01-05 (#118) làm màn đó trước và dựng khung dùng chung. |
| SCR-08 Xác nhận 相対取引 · FEAT-04 (gộp TRADE_CREATE) | E-T06, E-T05, E-T09, E-X02 | #32 (bộ đếm mã giao dịch), #41 (nhật ký cùng giao dịch, chống gửi trùng, kiểm dữ liệu vào, phân trang), #40 (tách thông điệp 許可/承認 — giấy phép/giấy chấp thuận, lọc lô theo ngày mở), #38 (chặn vượt hạn mức), #26 (chỉ lô đã công khai mới bán), #52 (chặn giao dịch ngoài giờ chợ), #121 (quyền vào màn) | Hàng đợi mất mạng (D-15) chưa nối vào màn này: để giai đoạn sau, vì ở hiện trường mất mạng chủ yếu xảy ra ở bước ghi đợt giao; X01-05 (#118) làm màn đó trước và dựng khung dùng chung. |
| SCR-09 Huỷ giao dịch trước khi khoá · FEAT-04 (gộp TRADE_CANCEL) | E-T06, E-X02 | #39 (hàm huỷ hoàn tồn đúng, chặn khi đã có chênh lệch, người và giờ huỷ), #40 (điều kiện hiện nút, hộp thoại huỷ), #121 (thêm vai đối soát, giao hàng vào menu) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-10 Nhập kết quả せり · FEAT-05 | E-T06, E-T09 | #33, #34 → #35, #36 (trạng thái chờ xác nhận, xác nhận hoặc trả lại), #41 (ép định dạng mã phiên SERI-MMDD-X), #32 (bộ đếm mã), #38 (hạn mức), #40 (nhãn, hộp thoại chung), #52 (chặn ngoài giờ chợ), #143 (cột và bộ lọc mã phiên), #53, #54 (cảnh báo lô chưa bán khi khoá ngày) | Bảng phiên đấu giá riêng (seri_sessions có khoá ngoại) chưa làm: thân E-T06 để ngoài epic, chờ khách trả lời X04-06 (#138). Nút "Lưu và nhập lô tiếp theo" của form せり: để giai đoạn sau, vì chỉ là tiện ích nhập liệu, không đổi quy tắc nghiệp vụ. |
| SCR-11 Lịch sử せり đã sửa · FEAT-05 | E-T13 | #81 (cột mã nghiệp vụ, mã giao dịch, từ vựng mã thao tác), #82 (tra theo mã giao dịch, sửa D-19, tìm kiếm an toàn, ghi vết mỗi lần tra), #83 | Gộp màn vào đường dẫn /audit giữ nguyên (spec ghi D-02 "GIỮ"). Lưu nhật ký 7 năm và lưu trữ dài hạn (D-27): để giai đoạn vận hành, vì cần chọn hạ tầng lưu trữ; trong giai đoạn này phân trang con trỏ ở #82 đủ để tra. |
| SCR-12 Yêu cầu điều chỉnh sau chốt · FEAT-06 | E-T10, E-T06, E-INC, E-T15 | #2, #3, #4, #5 → #6, #7; #32 (mã yêu cầu bằng bộ đếm); #70, #71 (dòng chênh lệch lạc kỳ, bị nuốt — B-02, B-03); #103 (thông báo khi gửi yêu cầu) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-13 Duyệt / từ chối yêu cầu điều chỉnh · FEAT-06 (gộp CORRECTION_DECIDE) | E-T10, E-INC | #3 (duyệt trong một giao dịch database, mở lại need_info, kiểm tồn), #4 (ba số và số tiền dự kiến trên bảng duyệt), #5 → #7 (mở tệp chứng cứ từ bảng duyệt); #70, #71 | Không còn — mọi điểm chênh lệch của spec đã có issue. Bộ lọc tra lịch sử sửa せり (D-19) nằm ở dòng SCR-11. |
| SCR-14 Theo dõi giao hàng · FEAT-07 | E-T08, E-X02 | #43 (cột số đã huỷ, đã trả lại, sửa D-14), #47 (mở lại giao dịch đã hoàn tất), #49 (bộ lọc lên URL, phân trang, tự làm mới), #48 (khoá nút); #121 (D-11) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-15 Hoàn tất / ghi ngoại lệ giao hàng · FEAT-07 (gộp DELIVERY_RECORD, DELIVERY_COMPLETE) | E-T08, E-X01, E-X02, E-INC | #44 (ghi đợt an toàn, chống gửi trùng), #45 (hoàn tất khi khớp số lượng), #46 (trần số đợt), #47, #48 (hộp thoại thật), #118 (hàng đợi mất mạng), #121 (quyền vào /deliveries), #61, #62 (nguồn ngày thanh toán, D-08) | Trần số đợt: spec ghi 10, backlog lấy mặc định 3 theo PREMISE D-30; đây là giả định chờ khách, câu hỏi X04-04 (#136). Ngoài điểm này không còn. |
| SCR-16 Giao hàng nhiều đợt · FEAT-07 | E-T08 | #49 (cột luỹ kế, còn lại, đóng góp, người ghi, cảnh báo trần), #43 (loại ngoại lệ "điều chỉnh"), #44 (ghi đợt an toàn khi hai người cùng thao tác), #46 | Tham số `?expand=` mở sẵn đợt giao từ màn đối soát và từ thông báo: để giai đoạn sau, vì là tiện ích điều hướng; người dùng vẫn mở được đợt giao bằng một lần bấm. Ô lý do tự do có thể chứa dữ liệu cá nhân (D-32): để giai đoạn sau, làm cùng quy trình dữ liệu cá nhân ở dòng thiết kế dữ liệu. |
| SCR-17 Đối soát ngày (日次精算) · FEAT-08 | E-T09, E-T08 | #57 (tổng tiền hiệu lực, ô tranh chấp, phân trang), #58 (sửa thuộc tính lô có khoá lạc quan), #43 (bảng số dư dùng chung) | Không sửa số lượng lô: giữ nguyên (spec ghi D-13 "GIỮ"). Việc màn đọc `?day=` trên URL xem dòng điều hướng. |
| SCR-18 Khoá 業務日 · FEAT-08 (gộp BUSINESS_DAY_LOCK) | E-T09, E-T05 | #53 (hàm khoá ngày có lý do, trigger lớp hai, chặn ngày tương lai), #54 (hộp thoại tóm tắt, cảnh báo ngày cũ quá 7 ngày), #28 (trigger ngày khoá cho bảng đánh giá lô, B-17) | Màn 締め再開 chưa làm: thân E-T09 ghi ngoài phạm vi LAB-5 vì cần người thứ hai duyệt và chưa có thiết kế chi tiết; câu hỏi khách ở X04-09 (#141). Điều kiện khoá khi còn tranh chấp (D-10) làm theo giả định chặn mềm, chờ khách ở X04-05 (#137). |
| SCR-19 Theo dõi tranh chấp · FEAT-08 | E-T09, E-T15, E-T14 | #55 (ghi và đóng sau khoá ngày, người xử lý có khoá ngoại, ghi chú đóng), #56 (chọn người xử lý, cột quá hạn), #103 (thông báo khi mở tranh chấp), #89 (báo cáo tranh chấp) | Leo thang một cấp (cột escalated_to, escalated_at): để giai đoạn sau, vì mốc leo thang phụ thuộc hạn xử lý tranh chấp đang chờ khách trả lời. Hạn xử lý 2 ngày nghiệp vụ là giả định, chờ khách ở X04-10 (#142). |
| SCR-20 Kết quả 完納奨励金 · FEAT-09 (gộp INCENTIVE_CALCULATE) | E-INC, E-T14, E-X02 | #60, #61, #62, #63 (nguồn ngày thanh toán), #65, #66, #67, #68, #69, #70, #71, #72, #73, #75; #90 (xuất tệp từ màn); #121 (quyền vào /incentives) | Ba điểm làm theo giả định chờ khách: nguồn ngày thanh toán (X04-02, #134), bảng tỷ lệ thật (X04-03, #135), không mở lại kỳ đã chốt (X04-07, #139). Ngoài các điểm này không còn. |
| SCR-21 Phiên bản quy tắc / tỷ lệ · FEAT-13 (gộp RULE_DECIDE, RULE_ROLLBACK) | E-T12, E-INC | #77, #78, #79; #64 (cột loại bên mua, ép bậc tăng dần, tối đa 4 chữ số thập phân), #74 (ngày hiệu lực theo kỳ) | Cách đếm trần 4 lần một năm khi có bản thu hồi (B-08) làm theo giả định, chờ khách ở X04-08 (#140). Ngoài điểm này không còn. |
| SCR-22 Trung tâm báo cáo · FEAT-10 (spec ghi FEAT-11) | E-T14, E-X01, E-X02 | #85 → #86, #87; #88, #89, #90, #91; #92 → #93, #94; #95; #114 (không lộ lỗi database, S-02); #121 (thêm vai quản trị quy tắc vào menu) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-23 Tra cứu nhật ký thao tác · FEAT-11 (spec ghi FEAT-12) | E-T13, E-INC | #81, #82, #83; #63 (lọc nhật ký theo thao tác ghi ngày thanh toán) | Lưu nhật ký 7 năm (D-27): để giai đoạn vận hành, cùng lý do với SCR-11. Nhật ký truy cập (D-32) đã có ở #82. |
| SCR-24 Cài đặt thông báo · FEAT-12 (spec ghi FEAT-09) | E-T15, E-T02, E-T09 | #97 → #98, #99; #105 (màn cài đặt, nút gửi thử); #9 (ngưỡng hết hạn dùng chung); #51 (lịch chợ cho ngày gửi) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-25 Hàng đợi cảnh báo vận hành · FEAT-12 (spec ghi FEAT-09) | E-T15, E-T14 | #100 → #101, #102 (gửi email, thử lại 1/5/30 phút, chuyển hết lượt); #106 → #107, #108 (màn hàng đợi, gửi lại theo lô, đóng thủ công); #94 (báo lỗi khi thiếu tệp báo cáo ngày) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| SCR-26 Hộp thư thông báo · FEAT-12 (spec ghi FEAT-09) | E-T16, E-T15 | #110 (sửa link 404), #111 (đếm chưa đọc ở máy chủ), #112 (bộ lọc, phân trang); #103, #104 (sinh thông báo thật từ sự kiện và tác vụ quét) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| Thiết kế dữ liệu (database-design: sơ đồ đích, từ điển dữ liệu, DB-PRA-001) | E-X01 và các epic nghiệp vụ | #115 (sinh lại bảng thiết kế từ sơ đồ đích, D-45); bảng còn thiếu: #17 (lịch sử tư cách), #37 (hạn mức tham gia), #30 (chứng từ lô), #6 (tệp chứng cứ điều chỉnh), #98 (quy tắc thông báo), #101 (hàng gửi thông báo), #51 (lịch chợ), #46 (chính sách trần đợt); ràng buộc: #32 (bộ đếm mã), #43 (bảng số dư giao hàng) | Bảng personal_data_requests (nhận yêu cầu xem, đính chính, xoá dữ liệu cá nhân theo luật APPI của Nhật, D-32): để giai đoạn sau, vì là quy trình pháp lý cần khách chỉ định người phụ trách trước khi làm. |
| Danh sách API (api-design: 36 file route và bản chụp hợp đồng LAB-3) | E-X01, E-X02 | #114 (bảng mã lỗi chung, ánh xạ lỗi database), #122 (rà quyền ghi trên mọi route tạo, sửa, xoá); route nào lệch thì sửa trong issue của màn dùng route đó | Không tách issue cho tài liệu API: route nào lệch được sửa trong issue của màn dùng nó. Chưa rà riêng từng file trong 36 file API; việc này làm khi cập nhật tài liệu API ở giai đoạn sau. |
| Mã lỗi chung (error-codes) | E-X01 và các epic đăng ký mã mới | #114 (một nơi khai báo mã lỗi, không trả nguyên văn lỗi database); mã mới do epic đăng ký: #26 (LOT_NOT_PUBLISHED), #33 (SERI_RESULT_PENDING), #38 (LIMIT_EXCEEDED), #39 (HAS_DELTA), #46 (BATCH_LIMIT_EXCEEDED) | Không còn — mọi điểm chênh lệch của spec đã có issue. |
| Điều hướng (navigation) | E-T02, E-T04, E-T08, E-T13, E-T16, E-X02, E-T06 | #11 (ô chỉ số là link lọc sẵn), #23 (`?filter=` và `?q=` lên URL), #49 (`?day=` và `?only=` ở /deliveries), #83 (bộ lọc nhật ký lên URL), #110, #112 (link thông báo, bộ lọc hộp thư lên URL), #121 (`?next=` theo ma trận menu), #40 (dòng ngày đã khoá dẫn sang /corrections), #143 (tám màn còn lại đọc và giữ tham số lọc) | Không còn — mọi điểm của hợp đồng tham số đã có issue. |

### Spec ghi mã FEAT lệch danh sách chức năng LAB-1

Căn cứ: danh sách tính năng LAB-1 (`03-feature-list-jp.xlsx`, cột "関連機能", tức chức năng liên quan) và danh sách chức năng LAB-1 (`02-function-list-jp.xlsx`).
Theo LAB-1: FEAT-09 là 完納奨励金 (FN-08-04, FN-08-05); FEAT-10 là báo cáo (FN-11-*); FEAT-11 là nhật ký kiểm toán (FN-12-*); FEAT-12 là thông báo (FN-09-*).

| Spec | Mã đang ghi | Mã đúng theo LAB-1 |
|---|---|---|
| SCR-22 Trung tâm báo cáo (FN-11-01, FN-11-03) | FEAT-11 | FEAT-10 |
| SCR-23 Tra cứu nhật ký thao tác (FN-12-01, FN-12-02) | FEAT-12 | FEAT-11 |
| SCR-24 Cài đặt thông báo (FN-09-03) | FEAT-09 | FEAT-12 |
| SCR-25 Hàng đợi cảnh báo vận hành (FN-09-02) | FEAT-09 | FEAT-12 |
| SCR-26 Hộp thư thông báo (FN-09-01) | FEAT-09 | FEAT-12 |

Hai chỗ thiếu mã, không phải lệch: SCR-02 có FN-02-03 nhưng không ghi FEAT-02; SCR-17 có FN-03-04 và FN-07-04 nhưng chỉ ghi FEAT-08 (thiếu FEAT-03, FEAT-07).
SCR-20 ghi "FEAT-09 (+ FEAT-11)" cho FN-12-03 là đúng, vì FN-12-03 thuộc FEAT-11.

### Issue không gắn với một spec cụ thể

Các issue dưới đây là việc nền, kiểm thử, triển khai hoặc câu hỏi khách. Chúng không bám một màn hay tài liệu cụ thể của spec.

| Issue | Việc | Ghi chú |
|---|---|---|
| #116 | X01-03 Kiểm biến môi trường lúc build và lúc khởi động | Việc nền vận hành |
| #119 | X01-06 Sao lưu và diễn tập khôi phục (D-28b) | Yêu cầu phi chức năng của RFP, không có màn |
| #126 | X03-00 Dựng database thử bằng một lệnh | Hạ tầng kiểm thử |
| #127 | X03-01 Đặt lại dữ liệu mẫu kèm kiểm nhanh luồng chính | Hạ tầng kiểm thử |
| #128 | X03-02 Kiểm thử tự động bốn chốt chặn | Chạm nhiều màn (SCR-08, SCR-15, SCR-18), không riêng màn nào |
| #129 | X03-03 Máy kiểm tự động của GitHub trước khi gộp và sau deploy | Triển khai |
| #130 | X03-04 Kiểm thử màn điện thoại 390 px cho ba luồng chính | Chạm SCR-07, SCR-08, SCR-15 nhưng là kiểm thử chung |
| #131 | X03-05 Kịch bản demo theo vai | Chuẩn bị demo |
| #133–#142 | X04-01 … X04-10 Mười câu hỏi gửi khách, không chấm điểm | Đã nhắc ở cột cuối của bảng: #133 (SCR-04), #134, #135, #139 (SCR-20), #136 (SCR-15), #137, #141 (SCR-18), #138 (SCR-10), #140 (SCR-21), #142 (SCR-19) |

## 3. Hạng mục chịu ràng buộc đặc thù của đề: 完納奨励金

完納奨励金 (tiền thưởng thanh toán đủ hạn) có ba ràng buộc mà màn hình thông thường không có. Thứ nhất, tiền phải đúng tới từng yên. Thứ hai, kỳ đã chốt không được đổi số. Thứ ba, đầu vào đến từ nhiều chuỗi khác (giao nhận, điều chỉnh, thanh toán).
Vì vậy phần này gom thành epic riêng **E-INC (#59)**. Mọi issue ở epic khác có chạm tới thưởng đều gắn nhãn `constraint:kanno-shoreikin`, nên lọc theo nhãn là thấy đủ chuỗi.

| Ràng buộc | Issue | Vì sao tách riêng |
|---|---|---|
| Ngày thanh toán quyết định đúng hạn hay trễ, nhưng RFP không nói nguồn (PREMISE Bảng 2 dòng Q2 · D-08) | #60 đặc tả CSV, #61 API nhập CSV, #62 nhập tay ngoại lệ, #63 nguồn và nhật ký; câu hỏi khách #134 | Ngày thanh toán lưu bảng tiền về riêng vì giao dịch thuộc ngày đã khoá không sửa được. Nguồn còn chờ khách, tách riêng thì khách trả lời khác chỉ thay 4 issue này |
| Bảng tỷ lệ thật chưa có, dùng bậc theo số tiền làm giả định (PREMISE Bảng 2 dòng Q6 · D-39) | #64 cột loại bên mua, #65 hàm tính; câu hỏi khách #135 | Khách đưa bảng thật thì chỉ nhập lại dữ liệu, không đổi mã |
| Công thức thưởng: hệ số 110/100, làm tròn xuống tới yên, ba ca biên của RFP | #65, #75 bộ kiểm thử tự động cho chuỗi thưởng | Sai một yên là sai tiền thật trả cho người mua; cần bộ kiểm thử riêng chạy mỗi lần gộp mã |
| Tính và chốt kỳ không được chạy chồng, nhật ký phải cùng giao dịch database | #66, #67, #68, #69, #72, #73 | Kỳ đã chốt là số đã báo cho người mua; chốt hỏng giữa chừng là mất dấu vết |
| Điều chỉnh rơi vào kỳ đã chốt (PREMISE Bảng 1 dòng D-44) | #70 đẩy sang kỳ mở gần nhất, #71 cảnh báo; nguồn dòng chênh lệch #3; báo cáo #89 (RPT-08); câu hỏi khách #139 | Không sửa kỳ đã chốt, không làm mất tiền chênh lệch |
| Phiên bản tỷ lệ: ngày hiệu lực theo kỳ, trần 4 lần một năm (PREMISE Bảng 3 dòng Q7; câu hỏi B-08) | #74, #77, #78, #79; câu hỏi khách #140 | Đổi tỷ lệ giữa kỳ làm hai người mua cùng kỳ nhận hai tỷ lệ khác nhau |
| Chỉ đợt giao cuối tính vào quyết toán và thưởng (PREMISE Bảng 2 dòng Q8 · D-30) | #46 trần số đợt giao | Thưởng chỉ đọc giao dịch đã hoàn tất giao nhận |
| Báo cáo và thông báo về thưởng | #86 danh mục báo cáo có RPT-07, #90 báo cáo theo kỳ và nút xuất ở màn kết quả thưởng, #103 thông báo khi chốt kỳ | Cột và nhãn phải khớp màn kết quả thưởng, nên dùng chung một định nghĩa |

## 4. Chỗ hở hoặc mâu thuẫn của spec LAB-4 phát hiện khi bẻ việc

Cột "Xử lý" chỉ dùng một trong bốn cách: đã sửa thiết kế · giả định · tạo issue làm rõ · để mở.

| Spec | Chỗ hở / mâu thuẫn | Xử lý |
|---|---|---|
| Giao nhận (SCR-15, DELIVERY_COMPLETE_DETAIL) | Huỷ một phần đơn được cộng vào số đã giao | Đã sửa thiết kế: PREMISE Bảng 1 dòng Q3 · D-14 (#43) |
| Giao nhận (SCR-15) | Tiêu chí hoàn tất chỉ nói "khi số lượng khớp", thiếu ca giao vượt và trả lại | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-40 (#45, #128) |
| Khoá ngày (SCR-18) | Chặn cứng khoá ngày khi còn tranh chấp, trong khi tranh chấp có thể kéo dài nhiều ngày | Đã sửa thiết kế: PREMISE Bảng 1 dòng Q4 · D-10, chặn mềm (#53). Khách vẫn được hỏi ở #137 |
| Tạo giao dịch (TRADE_CREATE_DETAIL) | Spec không nêu cách sinh mã giao dịch; prototype đếm bản ghi cộng một nên báo lỗi 409 trùng mã sau khi đặt lại dữ liệu | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-41 (#32, #44, #127) |
| Nhập kết quả せり (đấu giá, SCR-10) | Kết quả ghi thẳng là đã xác nhận, trong khi sơ đồ trạng thái của khách có bước chờ xác nhận | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-42 (#33, #34). Bản ghi phiên đấu giá hỏi khách ở #138 |
| Đối soát và khoá ngày (SCR-17, SCR-18) | Lịch chợ chỉ có tên bảng, không có cột; ngày nghiệp vụ chọn tay | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-43 (#51, #52) |
| Tính thưởng (INCENTIVE_CALCULATE_DETAIL) | Điều chỉnh rơi vào kỳ đã chốt chỉ được cảnh báo, chưa nói xử lý | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-44 (#70). Nhu cầu mở lại kỳ hỏi khách ở #139 |
| Thiết kế dữ liệu (database-design) | Bảng cột sinh từ schema prototype, lệch sơ đồ đích: lịch sử tư cách thiếu cột, lô thiếu 公開 (công khai), thiếu ràng buộc số lượng lớn hơn 0 | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-45 (#17, #26, #115) |
| Ô tìm kiếm (SCR-04, nhật ký, mã lỗi chung) | Spec vừa chốt "chuỗi tìm truyền vào hàm database như tham số", vừa có mã lỗi 422 "ký tự không cho phép" | Đã sửa thiết kế: PREMISE Bảng 1 dòng D-49 (#21, #82, #107, #114) |
| Bảng tỷ lệ thưởng (SCR-21, DD-008) | RFP chỉ cho cách tính, không cho bảng tỷ lệ thật | Giả định: PREMISE Bảng 2 dòng Q6 · D-39 (#64, #65); hỏi khách ở #135 |
| Hạn mức tham gia (SCR-08) | RFP nhắc 参加上限 (hạn mức tham gia) một lần, không nói đơn vị, phạm vi, thời điểm áp | Giả định: PREMISE Bảng 2 dòng Q1 · D-23 (#37, #38); hỏi khách ở #133 |
| Ngày thanh toán (SCR-20) | RFP không nói ngày thanh toán vào hệ thống bằng đường nào | Giả định: PREMISE Bảng 2 dòng Q2 · D-08 (#60–#63); hỏi khách ở #134 |
| Giao hàng nhiều đợt (SCR-16) | Không có trần số đợt; "chỉ đợt cuối tính vào quyết toán" chưa rõ nghĩa | Giả định: PREMISE Bảng 2 dòng Q8 · D-30 (#46); hỏi khách ở #136 |
| Công khai lô (SCR-07) | Có trạng thái 公開 nhưng không nói khi nào chuyển | Đã sửa thiết kế: PREMISE Bảng 3 dòng Q5 · D-29 (#26, #27) |
| Phiên bản tỷ lệ (SCR-21) | 発効日 (ngày hiệu lực) áp theo kỳ hay theo ngày giao dịch chưa chốt | Đã sửa thiết kế: PREMISE Bảng 3 dòng Q7 (#74) |
| Phiên bản tỷ lệ (RULE_ROLLBACK_DETAIL) | Trần 4 lần đổi tỷ lệ mỗi năm có tính bản đã thu hồi không | Tạo issue làm rõ (#140) |
| Khoá ngày (SCR-18) | Khoá nhầm ngày thì mở lại thế nào, ai duyệt | Tạo issue làm rõ (#141) |
| Tranh chấp và giao nhận (SCR-19, SCR-15) | Hạn xử lý tranh chấp bao nhiêu ngày; mở lại giao nhận đã hoàn tất cần mấy người duyệt | Tạo issue làm rõ (#142) |
| Hồ sơ người tham gia (REEXAMINATION_DECIDE_DETAIL) | RFP không gắn vai cho "người có quyền chấp thuận" | Để mở: đội chọn vai tiếp nhận, khác người nhập (ghi ở #20 và mô tả epic #16). Đổi vai chỉ sửa một ma trận quyền, không cần hỏi khách trước khi làm |
| Gửi thông báo (SCR-25) | "Thử lại tối đa 3 lần" chưa rõ là 3 lần tính cả lần đầu hay sau lần đầu | Để mở: đội hiểu là 3 lần sau lần đầu, cách nhau 1, 5, 30 phút (#102). Số lần thử lại nằm trong quy tắc thông báo, sửa được qua màn cài đặt |
| `_common/screen-matrix.md` | Ghi "mỗi spec có mục 10 chứa sẵn danh sách task", nhưng khuôn spec chỉ có 9 mục | Để mở: backlog này thay thế danh sách task đó; dọn câu chữ khi sửa bài LAB-4 |
| `README.md` và `checklist-doi-chieu-de-bai.md` của LAB-4 | Hai file nêu số tham chiếu bảng.cột khác nhau (406 và 292) | Để mở: là số đo của công cụ kiểm LAB-4, không ảnh hưởng thiết kế sản phẩm |
| Cây spec LAB-4 (góp ý review 19/10) | Cây thư mục, hậu tố tên file, thông tin đầu file API lệch chuẩn | Để mở: việc dọn bài LAB-4, không phải việc của sản phẩm; không đưa vào backlog |
| Năm spec báo cáo, nhật ký, thông báo | Nhãn chức năng FEAT ghi lệch danh sách chức năng LAB-1 | Để mở: bảng ở phần 2 dùng mã đúng theo LAB-1; sửa nhãn trong spec khi dọn bài LAB-4 |
| Góp ý điểm cộng review LAB-4 | Chưa có kế hoạch nạp dữ liệu ban đầu và yêu cầu phi chức năng có ngưỡng đo | Để mở: ngoài phạm vi bẻ việc lần này, ghi lại cho giai đoạn sau |
