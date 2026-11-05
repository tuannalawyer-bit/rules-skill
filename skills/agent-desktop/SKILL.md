---
name: agent-desktop
description: "Điều khiển và tự động hóa ứng dụng desktop (Windows, macOS, Linux) thông qua Accessibility Trees bằng CLI agent-desktop hoặc MCP Server. Hỗ trợ chụp cấu trúc UI dạng snapshot JSON, tương tác semantic refs (@ref), điền form, click, gõ phím, cuộn và quản lý cửa sổ mà không phụ thuộc tọa độ pixel hay mô hình thị giác."
---

# Agent Desktop (Vercel Labs) - Tự động hóa Desktop qua Accessibility Trees

Kỹ năng này hướng dẫn trợ lý AI (Antigravity / Gemini / Claude) quan sát, điều khiển và tự động hóa các ứng dụng desktop trên Windows, macOS và Linux thông qua công cụ mã nguồn mở **`agent-desktop`** của Vercel Labs.

Thay vì đoán tọa độ màn hình hoặc dựa vào mô hình thị giác (Vision models) dễ bị sai lệch khi giao diện co giãn hoặc đổi độ phân giải, `agent-desktop` đọc trực tiếp cây trợ năng hệ điều hành (**Microsoft UI Automation / UIA** trên Windows, **AX API** trên macOS, **AT-SPI** trên Linux) và xuất dữ liệu dạng JSON có cấu trúc kèm định danh phần tử duy nhất (`@ref`).

---

## 1. Vòng lặp cốt lõi: Quan sát - Thao tác - Xác thực (Observe - Act - Verify)

Mọi thao tác với ứng dụng desktop đều tuân theo vòng lặp 3 bước:

```
[1. Snapshot UI] ───> [2. Semantic Action (@ref)] ───> [3. Verify State / Readback]
```

### Bước 1: Khảo sát giao diện (Observe / Snapshot)
Trước khi click hay nhập liệu, chụp cấu trúc cây giao diện để lấy danh sách phần tử và mã `@ref`:

```powershell
# Xem danh sách ứng dụng GUI đang chạy
agent-desktop list-apps

# Xem danh sách cửa sổ
agent-desktop list-windows

# Chụp sơ đồ rút gọn (skeleton) của ứng dụng chỉ lấy các nút tương tác (-i --compact)
agent-desktop snapshot --app "chrome.exe" --skeleton -i --compact

# Đi sâu vào một vùng giao diện (drill-down) theo ref cha
agent-desktop snapshot --root '@s23zt45pw6ja60:e3' -i --compact
```

### Bước 2: Thực thi hành động ngữ nghĩa (Act)
Sử dụng mã `@ref` ổn định từ kết quả snapshot ở Bước 1:

```powershell
# Click vào nút (Headless semantic action)
agent-desktop click '@s23zt45pw6ja60:e1'

# Nhập giá trị trực tiếp vào ô input (không cần cướp chuột/focus)
agent-desktop set-value '@s23zt45pw6ja60:e5' "Nội dung cần nhập"

# Bật/tắt checkbox hoặc radio button
agent-desktop toggle '@s23zt45pw6ja60:e8'
agent-desktop check '@s23zt45pw6ja60:e8'

# Cuộn vùng hiển thị
agent-desktop scroll '@s23zt45pw6ja60:e2' --direction down --amount 3
```

### Bước 3: Xác thực kết quả (Verify)
- Mỗi lệnh trả về JSON Envelope: `{"ok": true, "data": ...}` hoặc `{"ok": false, "error": ...}`.
- Kiểm tra trường `data.disposition.delivery`:
  - `delivered_verified`: Thao tác thành công và hệ thống đã đọc lại kiểm chứng sự thay đổi trạng thái UI.
  - `delivered_unverified`: Thao tác đã gửi đi nhưng ứng dụng chưa báo trạng thái mới (nên re-snapshot để xác nhận).
- Nếu gặp lỗi, kiểm tra `error.disposition.retry`: chỉ thực hiện thử lại (retry) khi giá trị là `"safe"`.

---

## 2. Lưu ý quan trọng trên Windows & Môi trường Antigravity

### Bắt buộc đặt nháy đơn bao quanh `@ref` trong PowerShell
Trong PowerShell, ký tự `@token` là toán tử *splatting*. Nếu gõ trực tiếp `agent-desktop click @s8f3k2p9:e1`, PowerShell sẽ nuốt mất tham số và gây lỗi `INVALID_ARGS`.
> Luôn viết: `agent-desktop click '@s8f3k2p9:e1'` hoặc `agent-desktop set-value '@ref' "value"`.

### Headless vs Headed Mode
- **Chế độ Headless (Mặc định):** Tác động trực tiếp qua API UI Automation ngầm, **hoàn toàn không di chuyển chuột vật lý** và không cướp tiêu điểm (focus) màn hình của người dùng.
- **Chế độ Headed (`--headed`):** Bắt buộc đối với các thao tác vật lý như `type` (gõ từng phím), `right-click` (chuột phải), `double-click`, `focus`, `hover`, `drag`.
  ```powershell
  # Gõ văn bản mô phỏng phím thật:
  agent-desktop --headed type '@s23zt45pw6ja60:e5' "Hello world"

  # Chuột phải:
  agent-desktop --headed right-click '@s23zt45pw6ja60:e2'
  ```
  *Khuyến nghị:* Ưu tiên dùng `set-value` thay cho `type` để chạy headless an toàn, tốc độ cao và không cướp phím.

### Định tuyến Desktop tương tác (`WinSta0\Default`)
Khi chạy từ sandbox của agent (môi trường tạo desktop riêng biệt `exebox-...`), hệ thống đã được trang bị bộ điều phối `agent-desktop-runner.exe` tự động chuyển tiếp lệnh vào desktop tương tác `WinSta0\Default`, giúp agent có thể điều khiển trực tiếp các ứng dụng thực tế trên màn hình người dùng mà không gặp lỗi `EnumWindows failed`.

---

## 3. Bảng tra cứu lệnh thông dụng (Cheat Sheet)

| Tác vụ | Lệnh CLI | Chú thích |
|---|---|---|
| Kiểm tra trạng thái | `agent-desktop status` | Kiểm tra quyền UIA, nền tảng và bề mặt hỗ trợ |
| Xem ứng dụng chạy | `agent-desktop list-apps` | Liệt kê tên tiến trình, PID |
| Xem cửa sổ mở | `agent-desktop list-windows` | Liệt kê tiêu đề, tọa độ, trạng thái focus |
| Chụp cây UI | `agent-desktop snapshot --app <tên> -i` | Trả về JSON cấu trúc UI và các `@ref` |
| Click phần tử | `agent-desktop click '<ref>'` | Click ngầm semantic không giật chuột |
| Điền giá trị text | `agent-desktop set-value '<ref>' "text"` | Gán giá trị trực tiếp cho ô nhập liệu |
| Xóa ô nhập liệu | `agent-desktop clear '<ref>'` | Xóa sạch nội dung trong field |
| Chọn Dropdown | `agent-desktop select '<ref>' "Option"` | Chọn mục trong combo box |
| Toggle checkbox | `agent-desktop toggle '<ref>'` | Đảo trạng thái checkbox/switch |
| Cuộn màn hình | `agent-desktop scroll '<ref>' --direction down` | Cuộn lên/xuống/trái/phải |
| Bấm phím tắt | `agent-desktop press ctrl+s` | Gửi phím nóng (ctrl+c, enter, tab, esc,...) |
| Chụp ảnh màn hình | `agent-desktop screenshot --app <tên> -o screen.png` | Xuất ảnh chụp cửa sổ ứng dụng |
| Quản lý Clipboard | `agent-desktop clipboard-get` / `clipboard-set "abc"` | Đọc và ghi clipboard hệ thống |
| Chờ phần tử xuất hiện | `agent-desktop wait --text "Thành công" --timeout 5000` | Chờ sự kiện không dùng sleep tĩnh |

---

## 4. Tích hợp MCP Server trong Antigravity

`agent-desktop` cung cấp sẵn giao thức **Model Context Protocol (MCP)** qua lệnh `agent-desktop mcp`.
Đã được cấu hình trong `~/.gemini/config/mcp_config.json`:

```json
{
  "mcpServers": {
    "agent-desktop": {
      "command": "C:\\Users\\tuanna13\\AppData\\Local\\Programs\\nodejs\\node_modules\\agent-desktop\\bin\\agent-desktop-win32-x64.exe",
      "args": ["mcp"]
    }
  }
}
```

Khi Antigravity khởi động, toàn bộ **67 công cụ MCP** (`desktop_snapshot`, `desktop_click`, `desktop_set_value`, `desktop_list_apps`, `desktop_press`,...) sẽ sẵn sàng để gọi trực tiếp từ ngữ cảnh mô hình.

---

## 5. Xử lý các mã lỗi thường gặp (Troubleshooting)

1. **`STALE_REF`:**
   - *Nguyên nhân:* Giao diện ứng dụng vừa thay đổi (load trang mới, đóng mở dialog, tải lại dữ liệu), mã `@ref` cũ không còn tồn tại.
   - *Giải pháp:* Chụp lại snapshot mới (`snapshot`) và dùng `@ref` mới sinh ra.

2. **`AMBIGUOUS_TARGET`:**
   - *Nguyên nhân:* Có nhiều hơn 1 phần tử có cùng thuộc tính nhận diện trong cửa sổ (ví dụ: nhiều nút "Xóa" giống nhau trong một bảng dữ liệu).
   - *Giải pháp:* Dùng `--root` drill-down vào vùng chứa cụ thể hoặc dùng `--headed mouse-click --xy X,Y` theo tọa độ lấy từ `bounds`.

3. **`POLICY_DENIED`:**
   - *Nguyên nhân:* Thao tác yêu cầu quyền tương tác vật lý (như `type`, `right-click`) nhưng đang chạy ở chế độ Headless mặc định.
   - *Giải pháp:* Thêm cờ `--headed` vào trước lệnh (ví dụ: `agent-desktop --headed right-click '@ref'`).

4. **`APP_UNRESPONSIVE` / `TIMEOUT`:**
   - *Nguyên nhân:* Ứng dụng Electron/Chromium chưa kịp settle hoặc đang xử lý tác vụ nặng.
   - *Giải pháp:* Bổ sung `--timeout-ms 10000` vào lệnh snapshot hoặc dùng `wait --element ...`.

---

## 6. Tài liệu tham khảo bổ sung (Progressive Disclosure)

Để tra cứu chi tiết hơn khi cần tối ưu hóa các kịch bản phức tạp:
- [Lệnh quan sát chi tiết](file:///g:/Tool/AI/rule%20%26%20skill/skills/agent-desktop/references/commands-observation.md): Snapshot, find, surfaces, max-depth, skeleton.
- [Lệnh tương tác chi tiết](file:///g:/Tool/AI/rule%20%26%20skill/skills/agent-desktop/references/commands-interaction.md): Click, scroll, drag, hover, keyboard combos, post-verification.
- [Lệnh hệ thống & Windows Lifecycle](file:///g:/Tool/AI/rule%20%26%20skill/skills/agent-desktop/references/commands-system.md): Launch, close, sessions, overlay cursor, batching.
- [Kịch bản mẫu và Anti-patterns](file:///g:/Tool/AI/rule%20%26%20skill/skills/agent-desktop/references/workflows.md): Điền form phức tạp, điều hướng menu lồng, xử lý dialog.
- [Đặc thù Windows & Elevation](file:///g:/Tool/AI/rule%20%26%20skill/skills/agent-desktop/references/windows-permissions-and-elevation.md): UIPI, integrity levels, quyền admin.
- [Tối ưu hóa Chromium & Electron](file:///g:/Tool/AI/rule%20%26%20skill/skills/agent-desktop/references/windows-chromium-and-electron.md): Render settle timing, WPF, Web content.
