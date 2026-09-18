import csv
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đọc dữ liệu 100 jobs EB-3 đã tạo
csv_path = "C:/Users/essel/.gemini/antigravity/scratch/us_jobs_scraper/eb3_unskilled_100_jobs.csv"
jobs = []
with open(csv_path, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        jobs.append(row)

# Tạo README.md cho GitHub Repository
readme_content = """# 🇺🇸 US EB-3 Unskilled Workers Sponsorship Requirements & 100 Job Benchmark Database
### Tài liệu Yêu cầu & Danh mục 100 Việc làm EB-3 Lao động phổ thông (Other Workers)

---

## 🎯 Mục đích tài liệu (Purpose)
Tài liệu và trang web này được tạo để gửi cho người thân / đối tác / nhà tuyển dụng tại Mỹ xem xét, hỗ trợ tìm kiếm và đánh giá các vị trí công việc phù hợp cho diện **Định cư Mỹ EB-3 Lao động phổ thông (EB-3 Unskilled / Other Workers)**.

This repository outlines key job categories, prevailing wage benchmarks, Department of Labor (DOL) requirements, and a 100-job reference dataset for US Employment-Based 3rd Preference (EB-3) Unskilled Worker sponsorship.

---

## 📌 Tổng quan diện EB-3 Unskilled (Overview)
- **Định danh USCIS/DOL:** EB-3 Other Workers (Unskilled Workers).
- **Yêu cầu ứng viên:** Dưới 2 năm đào tạo hoặc **không cần kinh nghiệm, không cần bằng cấp**.
- **Yêu cầu nhà tuyển dụng tại Mỹ (US Employer):**
  1. Nộp chứng nhận lao động **PERM (ETA Form 9089)** lên Bộ Lao Động Mỹ (DOL).
  2. Chứng minh khả năng tài chính trả lương (**Ability to Pay**) qua Form I-140 (USCIS).
  3. Cam kết công việc toàn thời gian lâu dài (Permanent, Full-Time: 35-40h/tuần).

---

## 📊 7 Nhóm ngành mục tiêu chính (7 Target Job Sectors)
1. **Chế biến gia cầm & Thực phẩm (Poultry & Meat Processing):** SOC `51-3022` (~$15.00 - $20.50/h). Tỷ lệ duyệt PERM cao nhất.
2. **Chuỗi thức ăn nhanh & Nhà hàng (Fast Food & Dining):** SOC `35-3023`, `35-9021` (~$13.00 - $18.00/h). Môi trường dịch vụ, dễ hòa nhập.
3. **Dọn phòng khách sạn & Khu nghỉ dưỡng (Hospitality Housekeeping):** SOC `37-2012` (~$14.00 - $19.50/h).
4. **Kho bãi, Đóng gói & Bốc xếp (Warehousing & Material Moving):** SOC `53-7064` (~$15.50 - $21.00/h).
5. **Vệ sinh công nghiệp tòa nhà (Janitorial Services):** SOC `37-2011` (~$14.00 - $19.00/h).
6. **Nông trại & Nhà kính trồng trọt (Agriculture & Greenhouse):** SOC `45-2092` (~$13.50 - $18.00/h).
7. **Giặt là công nghiệp (Commercial Laundry):** SOC `51-6011` (~$13.50 - $17.50/h).

---

## 📁 Cấu trúc thư mục (File Structure)
- `index.html`: Giao diện web tương tác trực tiếp trên **GitHub Pages** (tìm kiếm, lọc 100 công việc, xem tiêu chí đánh giá song ngữ Anh - Việt).
- `eb3_unskilled_100_jobs.csv`: File Excel chứa 100 công việc mẫu thực tế kèm mức lương và mã nghề DOL.
- `README.md`: Hướng dẫn và tiêu chí đánh giá tổng quan.
"""

with open("C:/Users/essel/.gemini/antigravity/scratch/eb3_github_page/README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

# Sao chép file CSV sang thư mục GitHub Page
with open("C:/Users/essel/.gemini/antigravity/scratch/eb3_github_page/eb3_unskilled_100_jobs.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(jobs[0].keys()))
    writer.writeheader()
    writer.writerows(jobs)

# Tạo bảng HTML cho 100 công việc
table_rows = ""
for j in jobs:
    badge_color = "bg-primary"
    cat_lower = j['Category'].lower()
    if "chế biến" in cat_lower or "poultry" in cat_lower:
        badge_color = "bg-danger"
    elif "fast food" in cat_lower:
        badge_color = "bg-warning text-dark"
    elif "khách sạn" in cat_lower or "housekeeping" in cat_lower:
        badge_color = "bg-info text-dark"
    elif "kho bãi" in cat_lower:
        badge_color = "bg-success"

    table_rows += f"""
    <tr data-cat="{j['Category']}" data-state="{j['State']}">
        <td><span class="badge bg-secondary">#{j['STT']}</span></td>
        <td>
            <div class="fw-bold text-primary">{j['Title']}</div>
            <div class="small text-muted mt-1">{j['Duties']}</div>
            <div class="mt-1"><span class="badge bg-light text-dark border">SOC: {j['SOC_Code']}</span></div>
        </td>
        <td>
            <div class="fw-bold text-dark">{j['Company']}</div>
            <div class="small text-muted"><i class="bi bi-geo-alt"></i> {j['Location']}</div>
        </td>
        <td><span class="badge {badge_color}">{j['Category']}</span></td>
        <td>
            <div class="text-success fw-bold fs-6">{j['Hourly_Wage']}</div>
            <div class="small text-muted">{j['Annual_Wage']}</div>
        </td>
        <td><small>{j['Physical_Demand']}</small></td>
        <td><span class="badge bg-light text-secondary border">{j['English_Requirement']}</span></td>
        <td><span class="badge bg-success-subtle text-success border border-success">{j['PERM_Success_Rate']}</span></td>
    </tr>
    """

# Tạo file index.html hoàn chỉnh
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>US EB-3 Unskilled Workers Sponsorship Guide & 100 Job Benchmark</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        :root {{
            --primary-navy: #0f172a;
            --accent-blue: #2563eb;
            --light-bg: #f8fafc;
        }}
        body {{
            background-color: var(--light-bg);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            color: #334155;
        }}
        .hero-banner {{
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
            color: white;
            padding: 45px 0 35px 0;
            margin-bottom: 30px;
        }}
        .card-custom {{
            border-radius: 14px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03);
            background: white;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .card-custom:hover {{
            box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        }}
        .table-custom thead {{
            background-color: #0f172a;
            color: white;
        }}
        .badge-rule {{
            font-size: 0.85rem;
            padding: 6px 12px;
            border-radius: 8px;
        }}
        .lang-switch {{
            background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            border-radius: 20px;
            padding: 4px 15px;
        }}
    </style>
</head>
<body>

<!-- HERO HEADER -->
<header class="hero-banner shadow-sm">
    <div class="container-fluid px-lg-5 px-3">
        <div class="row align-items-center">
            <div class="col-lg-9">
                <div class="d-inline-flex align-items-center gap-2 mb-2">
                    <span class="badge bg-warning text-dark fw-bold px-3 py-1">🇺🇸 US IMMIGRATION DIRECTORY</span>
                    <span class="badge bg-info text-dark px-3 py-1">EB-3 OTHER WORKERS (UNSKILLED)</span>
                </div>
                <h1 class="fw-bold mb-2 display-6">Danh mục Yêu cầu & 100 Việc làm EB-3 Lao Động Phổ Thông tại Mỹ</h1>
                <p class="lead mb-0 text-white-50 fs-6">
                    <em>US EB-3 Unskilled Worker Sponsorship Guidelines, Target Occupations, Wage Benchmarks & 100 Sample Job Database</em>
                </p>
            </div>
            <div class="col-lg-3 text-lg-end mt-3 mt-lg-0">
                <a href="eb3_unskilled_100_jobs.csv" download class="btn btn-success btn-lg shadow-sm fw-bold">
                    <i class="bi bi-file-earmark-excel-fill me-1"></i> Tải File Excel (.CSV)
                </a>
            </div>
        </div>
    </div>
</header>

<main class="container-fluid px-lg-5 px-3 pb-5">

    <!-- PHẦN 1: TÓM TẮT DÀNH CHO NGƯỜI THÂN TẠI MỸ / EMPLOYER -->
    <div class="row g-4 mb-4">
        <div class="col-lg-6">
            <div class="card card-custom p-4 h-100">
                <h5 class="fw-bold text-primary mb-3">
                    <i class="bi bi-info-circle-fill me-2"></i> Tóm tắt Diện EB-3 Unskilled (Cho Người Nhà Tại Mỹ)
                </h5>
                <ul class="list-unstyled mb-0 d-flex flex-column gap-2 text-secondary">
                    <li><strong class="text-dark">1. Tính chất diện:</strong> Định cư cấp Thẻ Xanh vĩnh viễn (Permanent Resident) cho người lao động và gia đình (vợ/chồng, con cái dưới 21 tuổi).</li>
                    <li><strong class="text-dark">2. Yêu cầu ứng viên:</strong> Không yêu cầu bằng cấp Đại học/Cao đẳng, không đòi hỏi kinh nghiệm làm việc trước đó.</li>
                    <li><strong class="text-dark">3. Trách nhiệm của Employer tại Mỹ:</strong>
                        <ul>
                            <li>Bảo lãnh vị trí làm việc toàn thời gian (Full-time: 35-40h/tuần).</li>
                            <li>Được Bộ Lao Động Mỹ (DOL) cấp Chứng nhận Lao Động (Labor Certification / PERM Form ETA-9089).</li>
                            <li>Chứng minh công ty có khả năng tài chính trả lương (Ability to Pay) qua thuế thu nhập doanh nghiệp.</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>

        <div class="col-lg-6">
            <div class="card card-custom p-4 h-100">
                <h5 class="fw-bold text-success mb-3">
                    <i class="bi bi-check2-circle me-2"></i> 4 Tiêu Chí Chọn Nhà Tuyển Dụng (Employer Criteria)
                </h5>
                <div class="row g-2">
                    <div class="col-6">
                        <div class="p-3 bg-light rounded-3 h-100 border">
                            <strong class="d-block text-dark mb-1">🏢 Quy mô & Doanh thu</strong>
                            <small class="text-muted">Doanh nghiệp hoạt động tối thiểu 2-3 năm, có lợi nhuận ròng hoặc vốn lưu động lớn hơn mức lương bảo lãnh.</small>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="p-3 bg-light rounded-3 h-100 border">
                            <strong class="d-block text-dark mb-1">📋 Hồ sơ PERM minh bạch</strong>
                            <small class="text-muted">Ngành nghề thuộc danh mục khó tuyển người bản xứ tại Mỹ (nhà máy, fast food, dọn phòng) để tỷ lệ duyệt PERM cao.</small>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="p-3 bg-light rounded-3 h-100 border">
                            <strong class="d-block text-dark mb-1">💵 Mức lương chuẩn (PW)</strong>
                            <small class="text-muted">Trả đúng mức lương Prevailing Wage do DOL quy định (thường từ $13.50 – $21.00/h tùy khu vực).</small>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="p-3 bg-light rounded-3 h-100 border">
                            <strong class="d-block text-dark mb-1">📍 Địa điểm thuận tiện</strong>
                            <small class="text-muted">Các bang có cộng đồng người Việt đông đảo hoặc chi phí sinh hoạt vừa phải (Texas, Florida, North Carolina, Georgia).</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- PHẦN 2: BẢNG 7 NHÓM NGÀNH NGHỀ CHỦ LỰC -->
    <div class="card card-custom p-4 mb-4">
        <h5 class="fw-bold text-dark mb-3">
            <i class="bi bi-grid-3x3-gap-fill text-primary me-2"></i> 7 Nhóm Ngành Lao Động Phổ Thông EB-3 Chủ Lực
        </h5>
        <div class="table-responsive">
            <table class="table table-bordered align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th>Nhóm ngành</th>
                        <th>Mã nghề DOL (SOC)</th>
                        <th>Mức lương ($/h)</th>
                        <th>Mức độ thể lực</th>
                        <th>Yêu cầu tiếng Anh</th>
                        <th>Tỷ lệ duyệt PERM</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong class="text-danger">1. Chế biến thịt & Gia cầm (Poultry/Meat)</strong></td>
                        <td><code>51-3022</code></td>
                        <td><strong class="text-success">$15.00 - $20.50/h</strong></td>
                        <td>Nặng (Phòng lạnh 4-8°C, đứng chuyền)</td>
                        <td>Không yêu cầu</td>
                        <td><span class="badge bg-success">Rất cao (~95%)</span></td>
                    </tr>
                    <tr>
                        <td><strong class="text-warning text-dark">2. Fast Food & Chuỗi nhà hàng</strong></td>
                        <td><code>35-3023</code>, <code>35-9021</code></td>
                        <td><strong class="text-success">$13.00 - $18.00/h</strong></td>
                        <td>Trung bình (Phụ bếp, làm bánh, rửa chén)</td>
                        <td>Cơ bản (Giao tiếp đơn giản)</td>
                        <td><span class="badge bg-primary">Cao (~85%)</span></td>
                    </tr>
                    <tr>
                        <td><strong class="text-info text-dark">3. Dọn phòng khách sạn (Housekeeping)</strong></td>
                        <td><code>37-2012</code></td>
                        <td><strong class="text-success">$14.00 - $19.50/h</strong></td>
                        <td>Trung bình - Nặng (Thay ga nệm, lau dọn)</td>
                        <td>Tối thiểu</td>
                        <td><span class="badge bg-primary">Cao (~85%)</span></td>
                    </tr>
                    <tr>
                        <td><strong class="text-success">4. Kho bãi & Đóng gói (Warehouse Packaging)</strong></td>
                        <td><code>53-7064</code></td>
                        <td><strong class="text-success">$15.50 - $21.00/h</strong></td>
                        <td>Nặng (Bốc dỡ thùng hàng, đóng pallet)</td>
                        <td>Cơ bản</td>
                        <td><span class="badge bg-primary">Cao (~85%)</span></td>
                    </tr>
                    <tr>
                        <td><strong>5. Vệ sinh công nghiệp (Janitorial Services)</strong></td>
                        <td><code>37-2011</code></td>
                        <td><strong class="text-success">$14.00 - $19.00/h</strong></td>
                        <td>Trung bình (Lau sàn, vệ sinh tòa nhà)</td>
                        <td>Không yêu cầu</td>
                        <td><span class="badge bg-primary">Cao (~85%)</span></td>
                    </tr>
                    <tr>
                        <td><strong>6. Nông trại & Nhà kính (Agriculture/Greenhouse)</strong></td>
                        <td><code>45-2092</code></td>
                        <td><strong class="text-success">$13.50 - $18.00/h</strong></td>
                        <td>Nặng (Hái nấm, thu hoạch rau quả)</td>
                        <td>Không yêu cầu</td>
                        <td><span class="badge bg-success">Rất cao (~90%)</span></td>
                    </tr>
                    <tr>
                        <td><strong>7. Giặt là công nghiệp (Commercial Laundry)</strong></td>
                        <td><code>51-6011</code></td>
                        <td><strong class="text-success">$13.50 - $17.50/h</strong></td>
                        <td>Trung bình (Vận hành máy giặt, gấp khăn)</td>
                        <td>Không yêu cầu</td>
                        <td><span class="badge bg-success">Cao (~85%)</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- PHẦN 3: DANH SÁCH 100 VIỆC LÀM EB-3 MẪU THỰC TẾ CÓ TÌM KIẾM & BỘ LỌC -->
    <div class="card card-custom p-4">
        <div class="d-flex justify-content-between align-items-center flex-wrap gap-2 mb-3">
            <div>
                <h5 class="fw-bold text-dark mb-0">
                    <i class="bi bi-table text-primary me-2"></i> Danh Sách 100 Vị Trí Việc Làm Mẫu EB-3 Unskilled
                </h5>
                <small class="text-muted">Tổng hợp từ các nhà tuyển dụng thực tế thường xuyên bảo lãnh diện EB-3 tại các bang</small>
            </div>
            <div class="text-muted small">
                Hiển thị <span id="visibleCount" class="fw-bold text-primary">100</span> / 100 công việc
            </div>
        </div>

        <!-- BỘ LỌC VÀ TÌM KIẾM -->
        <div class="row g-2 mb-3 p-3 bg-light rounded-3 border">
            <div class="col-md-5">
                <div class="input-group">
                    <span class="input-group-text bg-white border-end-0"><i class="bi bi-search text-muted"></i></span>
                    <input type="text" id="searchInput" class="form-control border-start-0" placeholder="Tìm theo tên công ty, vị trí, thành phố...">
                </div>
            </div>
            <div class="col-md-4">
                <select id="filterCat" class="form-select">
                    <option value="">-- Tất cả nhóm ngành --</option>
                    <option value="Chế biến thực phẩm">Chế biến gia cầm & Thực phẩm (Poultry/Meat)</option>
                    <option value="Fast Food">Chuỗi thức ăn nhanh & Nhà hàng (Fast Food)</option>
                    <option value="Housekeeping">Dọn phòng khách sạn (Housekeeping)</option>
                    <option value="Kho bãi">Kho bãi & Đóng gói (Warehouse Packaging)</option>
                    <option value="Vệ sinh công nghiệp">Vệ sinh công nghiệp (Janitorial)</option>
                    <option value="Nông trại">Nông trại & Nhà kính (Agriculture)</option>
                    <option value="Giặt là">Giặt là công nghiệp (Laundry)</option>
                </select>
            </div>
            <div class="col-md-3">
                <select id="filterState" class="form-select">
                    <option value="">-- Tất cả các bang --</option>
                    <option value="NC">North Carolina (NC)</option>
                    <option value="TX">Texas (TX)</option>
                    <option value="FL">Florida (FL)</option>
                    <option value="GA">Georgia (GA)</option>
                    <option value="PA">Pennsylvania (PA)</option>
                    <option value="OH">Ohio (OH)</option>
                    <option value="MS">Mississippi (MS)</option>
                    <option value="AL">Alabama (AL)</option>
                    <option value="NV">Nevada (NV)</option>
                    <option value="SC">South Carolina (SC)</option>
                    <option value="TN">Tennessee (TN)</option>
                    <option value="IN">Indiana (IN)</option>
                    <option value="CA">California (CA)</option>
                    <option value="NE">Nebraska (NE)</option>
                </select>
            </div>
        </div>

        <!-- BẢNG DỮ LIỆU -->
        <div class="table-responsive">
            <table class="table table-hover align-middle" id="jobsTable">
                <thead class="table-dark">
                    <tr>
                        <th style="width: 50px;">#</th>
                        <th style="width: 28%;">Vị trí & Nhiệm vụ</th>
                        <th>Nhà tuyển dụng & Địa điểm</th>
                        <th>Nhóm ngành</th>
                        <th>Mức lương ($/h)</th>
                        <th>Thể lực</th>
                        <th>Tiếng Anh</th>
                        <th>Xét duyệt PERM</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
    </div>
</main>

<footer class="bg-dark text-white py-4 mt-5">
    <div class="container-fluid px-lg-5 px-3 text-center">
        <p class="mb-1 fw-bold">US EB-3 Unskilled Workers Reference Guide & Directory</p>
        <small class="text-white-50">Dữ liệu được biên soạn phục vụ mục đích tham khảo và đánh giá tuyển dụng định cư diện EB-3 Other Workers tại Hoa Kỳ.</small>
    </div>
</footer>

<!-- SCRIPT TÌM KIẾM & LỌC -->
<script>
    const searchInput = document.getElementById('searchInput');
    const filterCat = document.getElementById('filterCat');
    const filterState = document.getElementById('filterState');
    const rows = document.querySelectorAll('#jobsTable tbody tr');
    const countDisplay = document.getElementById('visibleCount');

    function applyFilter() {{
        const search = searchInput.value.toLowerCase().trim();
        const cat = filterCat.value;
        const state = filterState.value;
        let visible = 0;

        rows.forEach(r => {{
            const text = r.innerText.toLowerCase();
            const rCat = r.getAttribute('data-cat');
            const rState = r.getAttribute('data-state');

            const matchSearch = !search || text.includes(search);
            const matchCat = !cat || rCat.includes(cat);
            const matchState = !state || rState === state;

            if (matchSearch && matchCat && matchState) {{
                r.style.display = '';
                visible++;
            }} else {{
                r.style.display = 'none';
            }}
        }});

        countDisplay.innerText = visible;
    }}

    searchInput.addEventListener('input', applyFilter);
    filterCat.addEventListener('change', applyFilter);
    filterState.addEventListener('change', applyFilter);
</script>

</body>
</html>
"""

with open("C:/Users/essel/.gemini/antigravity/scratch/eb3_github_page/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("[✓] Đã tạo trọn bộ file cho GitHub Page tại C:/Users/essel/.gemini/antigravity/scratch/eb3_github_page/")
