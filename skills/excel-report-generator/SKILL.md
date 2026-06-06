---
name: excel-report-generator
description: "Tạo báo cáo Excel cao cấp, tô màu có điều kiện (Conditional Formatting) và tạo biểu đồ bằng openpyxl."
---

# Excel Report Generator (Portable & Non-Admin)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn tự động tạo lập, định dạng thẩm mỹ và chèn các quy tắc định dạng có điều kiện (tô màu cảnh báo) cho báo cáo Excel bằng thư viện `openpyxl`. Thao tác trực tiếp với file nhị phân của Excel nên chạy độc lập hoàn toàn mà không cần cài đặt phần mềm Microsoft Excel trên hệ điều hành.

## 1. Định dạng Bảng dữ liệu Excel Chuyên nghiệp (Styling)

### Mã nguồn Python mẫu:
```python
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

def format_excel_report(input_df, output_path):
    # Khởi tạo Workbook và Worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Báo cáo phân tích"
    
    # 1. Ghi Header (Tiêu đề cột)
    headers = list(input_df.columns)
    ws.append(headers)
    
    # Thiết lập Style cho Header (Chữ đậm, nền xanh dương đậm, chữ trắng, căn giữa)
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_align = Alignment(horizontal="center", vertical="center")
    
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_align
        
    # 2. Ghi Dữ liệu (Rows)
    for index, row in input_df.iterrows():
        ws.append(list(row))
        
    # Thiết lập Border (Đường viền mảnh cho bảng)
    thin_border = Border(
        left=Side(style='thin', color='D3D3D3'),
        right=Side(style='thin', color='D3D3D3'),
        top=Side(style='thin', color='D3D3D3'),
        bottom=Side(style='thin', color='D3D3D3')
    )
    
    # Tự động căn chỉnh độ rộng của các cột dựa trên nội dung
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 3, 12)
        
        # Áp dụng Border cho các hàng dữ liệu
        for cell in col[1:]: # Bỏ qua header
            cell.border = thin_border
            
    wb.save(output_path)
```

## 2. Tô màu Cảnh báo Bất thường có điều kiện (Conditional Formatting)

Tô màu đỏ nhạt (`FFC7CE` với chữ đỏ đậm `9C0006`) cho các dòng hoặc ô chứa các giá trị bất thường đã phát hiện.

### Mã nguồn Python mẫu:
```python
from openpyxl.formatting.rule import CellIsRule

def apply_anomaly_highlighting(excel_file_path, sheet_name, anomaly_col_letter):
    wb = openpyxl.load_workbook(excel_file_path)
    ws = wb[sheet_name]
    
    # Thiết lập màu đỏ nhạt cảnh báo
    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    red_font = Font(color="9C0006", bold=True)
    
    # Tạo quy tắc: Nếu cột chứa nhãn bất thường có giá trị là TRUE hoặc 'Bất thường'
    rule = CellIsRule(operator='equal', formula=['"Bất thường"'], stopIfTrue=True, fill=red_fill, font=red_font)
    
    # Áp dụng quy tắc cho toàn bộ dải ô của cột chứa nhãn bất thường
    max_row = ws.max_row
    ws.conditional_formatting.add(f"{anomaly_col_letter}2:{anomaly_col_letter}{max_row}", rule)
    
    wb.save(excel_file_path)
```

## 3. Chèn Biểu đồ (Chart) tự động bằng openpyxl

### Mã nguồn Python mẫu:
```python
from openpyxl.chart import BarChart, Reference

def add_bar_chart(excel_file_path, sheet_name, data_col_idx, label_col_idx):
    wb = openpyxl.load_workbook(excel_file_path)
    ws = wb[sheet_name]
    
    chart = BarChart()
    chart.type = "col"
    chart.style = 10
    chart.title = "Biểu đồ Phân tích Số liệu"
    chart.y_axis.title = "Giá trị"
    chart.x_axis.title = "Mục"
    
    # Chọn dữ liệu làm cột biểu diễn (ví dụ từ cột data_col_idx hàng 1 đến hết)
    data = Reference(ws, min_col=data_col_idx, min_row=1, max_row=ws.max_row)
    # Chọn nhãn trục X (từ cột label_col_idx hàng 2 đến hết)
    labels = Reference(ws, min_col=label_col_idx, min_row=2, max_row=ws.max_row)
    
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(labels)
    
    # Chèn biểu đồ vào ô cụ thể (ví dụ ô F2)
    ws.add_chart(chart, "F2")
    wb.save(excel_file_path)
```
