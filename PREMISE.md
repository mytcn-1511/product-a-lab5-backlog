# PREMISE — tiền đề của backlog LAB-5 so với thiết kế LAB-4

**Sản phẩm:** Product A, hệ thống hỗ trợ vận hành chợ bán buôn thủy sản (khách hàng hư cấu trong đề). **Mốc so sánh:** bộ thiết kế LAB-4 đã nộp ngày 08/10/2026. **Ngày viết:** 17/10/2026.

Backlog trong Project này bám bản LAB-4, cộng và trừ đúng những gì khai dưới đây. Chỗ nào không khai thì hiểu là giữ nguyên LAB-4.

Khác biệt đến từ hai nguồn: chỗ hở tự phát hiện khi bẻ việc, và nhận xét của giảng viên cho prototype LAB-3 (nhận ngày 16/10/2026). Không có góp ý review LAB-4 từ người khác, nên nhánh "bổ sung từ review" để trống.

## Cách đọc mã trong file

| Mã | Nghĩa |
|---|---|
| D-xx | Một điểm khác biệt hoặc quyết định thiết kế, đánh số nối tiếp danh sách 68 điểm của LAB-4 (D-01 đến D-38); D-39 trở đi là mới ở LAB-5 |
| B-xx | Một quyết định nghiệp vụ còn treo từ LAB-4 |
| Q1 đến Q8 | Tám câu chưa có khách trả lời, đã chốt cách xử lý ngày 15/10 và 16/10 |
| DD-008 | Tài liệu thiết kế chi tiết phần tính thưởng thanh toán đủ hạn |
| T-xx | Gói việc theo màn hình, LAB-4 chia sẵn 16 gói |
| X-01 đến X-04 | Nhóm việc xuyên suốt: nền tảng, bảo mật, kiểm thử, làm rõ với khách |
| 完納奨励金 | Tiền thưởng thanh toán đủ hạn, một chuỗi nghiệp vụ riêng trong đề |
| 業務日 | Ngày nghiệp vụ của chợ, tính theo giờ Nhật |
| 許可 / 承認 | Giấy phép / giấy chấp thuận, hai cấp tư cách mua riêng |
| 公開 | Bước công khai lô hàng để bên mua thấy |
| 発効日 | Ngày hiệu lực của một phiên bản tỷ lệ |

## Bảng 1 — Spec thêm, bỏ, sửa

Không thêm tính năng mới, không bỏ tính năng nào của LAB-4. Có 5 chỗ sửa.

| Spec | Thêm / Bỏ / Sửa | Trước → sau | Vì sao | Issue bị ảnh hưởng |
|---|---|---|---|---|
| Q3 · D-14 · giao nhận | Sửa | Huỷ một phần đơn đang được **cộng** vào số đã giao → **trừ** khỏi số đã giao, xử lý như trả hàng | Chỗ hở LAB-4 (D-14): cộng làm số đã giao bị thổi phồng, xác nhận hoàn tất giao hàng sai, báo cáo kiểm toán sai. Chọn trừ vì đúng nghĩa và chỉ sửa một bộ lọc | T-08 |
| Q4 · D-10 · khoá ngày | Sửa | Chặn cứng, không cho khoá 業務日 khi còn tranh chấp mở → **chặn mềm**: cho khoá, bắt buộc ghi lý do, ghi số tranh chấp đang mở vào nhật ký | Chỗ hở LAB-4: luật chặn cứng là đội tự đặt từ LAB-3 và mâu thuẫn với B-16 (đã cho ghi tranh chấp sau khi khoá). Chặn mềm nhất quán với B-16 và cũng giải quyết B-09 (khoá phải có ghi chú) | T-09 |
| D-41 · mã giao dịch | Sửa | Mã giao dịch sinh bằng "đếm số bản ghi trong ngày cộng một" → cấp bằng **sequence của database**, không đếm, không lấy số lớn nhất cộng một | Nhận xét LAB-3 của giảng viên: tạo giao dịch báo lỗi 409 trùng mã sau khi đặt lại dữ liệu, làm luồng bán, đấu giá và giao hàng không chạy được. Đã xác minh trong mã nguồn prototype | T-06, X-03 |
| Q6 · D-39 · DD-008 · bảng tỷ lệ thưởng | Sửa nhẹ cấu trúc | Bảng tỷ lệ thưởng chỉ có bậc theo số tiền → thêm cột **loại bên mua**, tuỳ chọn, để trống nghĩa là áp cho mọi loại. Cách tính giữ nguyên: nhân hệ số thuế 110/100, làm tròn xuống đơn vị yên, quá hạn thì không thưởng, tỷ lệ có phiên bản và 発効日 | Bảng tỷ lệ cụ thể là chỗ RFP để ngỏ (xem Bảng 2). Thêm cột này để nếu khách đưa bảng theo loại bên mua thì chỉ đổi dữ liệu, không đổi thiết kế | T-12, epic 完納奨励金 |
| D-40 · hoàn tất giao nhận | Sửa, định rõ tiêu chí | Tiêu chí "hoàn tất khi số lượng khớp" → ghi rõ ba ca: giao thiếu thì chưa hoàn tất; giao vượt dừng ở trạng thái ngoại lệ dù có lý do; trả lại và huỷ một phần đều trừ khỏi số đã giao | Nhận xét LAB-3 cho cả lớp: ba bài cho hoàn tất dù số lượng chưa khớp. LAB-4 có luật nhưng chưa nêu đủ ca thử | T-08 |

## Bảng 2 — Giả định bổ sung

Giả định chỉ lấp chỗ RFP để ngỏ, không ghi đè chỗ RFP đã nói rõ. Mỗi giả định có một câu hỏi gửi khách ở nhóm X-04.

| Giả định | Chỗ spec / RFP để ngỏ | Ảnh hưởng tới issue và ước lượng |
|---|---|---|
| Q1 · D-23: hạn mức tham gia là **trần giá trị giao dịch trong một ngày** của người tham gia mua bán, chặn ngay lúc tạo giao dịch. Đây là một trong ba cách hiểu | RFP nhắc "hạn mức tham gia" đúng một lần trong bảng vai trò, không nói đơn vị, phạm vi hay thời điểm áp dụng | 2 đến 3 issue ở T-06: bảng cấu hình, kiểm tra lúc tạo giao dịch, màn cài đặt. Sai cách hiểu thì bỏ các issue này, không ảnh hưởng chỗ khác |
| Q2 · D-08: ngày thanh toán lấy từ **file CSV của kế toán theo kỳ** là nguồn chính; **nhập tay có phân quyền và lý do** chỉ cho ngoại lệ. Tự viết đặc tả file CSV và để trong repo | RFP nói thưởng tính theo thanh toán đúng hạn nhưng không nói ngày thanh toán vào hệ thống bằng cách nào; LAB-4 ghi là chưa chốt | 4 issue ở epic 完納奨励金: đặc tả CSV, API nhập có kiểm trùng, màn nhập tay, cột ghi nguồn kèm nhật ký. Đây là giả định rủi ro nhất: sai thì đổi cả chuỗi thưởng. Được ghi thành rủi ro trễ trong báo cáo tiến độ |
| Q8 · D-30: trần số đợt giao **cấu hình được, mặc định 3**. Chỉ đợt cuối mới tính vào quyết toán và thưởng | RFP yêu cầu bên thầu tự đề xuất trần số lần chia, quyền xác nhận và thời điểm phản ánh | 1 issue ở T-08. Số 3 là giả định, khách đổi được qua cấu hình |
| Q6 · D-39: **bậc tỷ lệ thưởng theo số tiền mua**, giữ như LAB-4, kèm quy tắc bậc phải tăng dần khi nhập | RFP chỉ cố định cách tính (hệ số thuế 110/100, làm tròn xuống yên, quá hạn không thưởng, tỷ lệ có phiên bản và 発効日). Bảng tỷ lệ cụ thể không có trong RFP; cả lớp chỉ có bản PDF, không có gói dữ liệu kèm theo (giảng viên xác nhận 17/10) | 2 issue ở epic 完納奨励金 (cột loại bên mua, hàm tính đọc cột) và 1 câu hỏi khách ở X-04. Khách đưa bảng thật thì chỉ nhập lại dữ liệu |

## Bảng 3 — Hướng đã chốt

| Vấn đề | Các phương án ở LAB-4 | Phương án chốt | Vì sao |
|---|---|---|---|
| Q5 · D-29: khi nào lô hàng chuyển sang 公開 | A. Bước riêng, người bán buôn bấm sau thẩm định · B. Tự động ngay sau thẩm định · C. Tự động theo lịch mở phiên 02:00 | **A** | Cho phép giữ lô lại nếu chất lượng kém, đúng tinh thần con người quyết. B làm trạng thái 公開 vô nghĩa; C phụ thuộc lịch chợ chưa có. 2 issue ở T-05 |
| Q7 · DD-008: 発効日 của tỷ lệ áp theo kỳ hay theo ngày giao dịch | A. Theo kỳ, ép 発効日 là ngày 1 của tháng · B. Theo ngày giao dịch | **A** | Hết mơ hồ, hàm tính giữ nguyên, đồng thời chặn lỗi B-14 (ngày hiệu lực rơi vào kỳ đã chốt). B chính xác hơn nhưng đổi số của kỳ đang mở. 1 issue ở T-12 |
| B-05: điều chỉnh sau khoá hay cả hai đường | A. Chỉ cho điều chỉnh sau khi khoá ngày · B. Cho cả sửa trực tiếp lẫn điều chỉnh | **A**, giữ LAB-4 | Một đường sửa duy nhất, lịch sử không bị biến dạng |
| B-16: có cho ghi tranh chấp sau khi khoá không | A. Cho phép · B. Chặn | **A**, giữ LAB-4 | Khiếu nại phát hiện sau chốt sổ là tình huống thật và là căn cứ mở yêu cầu điều chỉnh |
| D-25: múi giờ | A. Asia/Tokyo cố định cho hiển thị lẫn tính 業務日 · B. Theo máy người xem | **A**, giữ LAB-4 | Nhận xét LAB-3 cho cả lớp: bốn bài lệch 業務日 vì tính theo giờ máy hoặc UTC. Bài LAB-3 của tôi được ghi nhận đúng. Mọi issue chạm 業務日 có ca thử nhập giao dịch lúc 02:31 giờ Nhật trên máy đặt múi giờ Việt Nam |
| D-21: tư cách mua | A. Tách 許可 và 承認, hai ngày hết hạn riêng · B. Gộp một trạng thái | **A**, giữ LAB-4 | RFP cấm gộp hai căn cứ; một bài trong lớp gộp và bị nhận xét. Không thêm issue |

## Những gì giữ nguyên LAB-4, không khai lại

13 nhóm tính năng, 26 màn hình gom thành 14 đường dẫn phát triển, kiến trúc một khối có bản ghi chênh lệch, bốn điểm con người quyết (thẩm định, chốt đấu giá, duyệt sửa, xác nhận giao hàng), múi giờ Nhật. Prototype LAB-3 giữ nguyên, không sửa; các lỗi của nó đi vào backlog này dưới nhãn "gia cố".

## Câu hỏi gửi khách (nhóm X-04, không chấm điểm)

| Mã | Câu hỏi |
|---|---|
| D-23 | Hạn mức tham gia tính theo đơn vị gì, phạm vi nào, áp lúc nào? |
| D-08 | Ngày thanh toán vào hệ thống bằng file từ kế toán, nhập tay, hay kết nối trực tiếp? |
| D-39 | Bảng tỷ lệ thưởng thật: theo loại bên mua, theo bậc số tiền, hay một tỷ lệ chung? |
| D-30 | Trần số đợt giao là bao nhiêu và ai có quyền xác nhận đợt cuối? |
| D-10 | Có được khoá ngày khi còn tranh chấp mở không? |

Cột "Issue bị ảnh hưởng" đang ghi mã gói. Sau khi backlog lên Project, cột này sẽ đổi thành số issue thật.
