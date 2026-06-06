---
name: ai-video-filmmaking
description: "Làm phim AI bằng API và biên tập video tự động bằng MoviePy & FFmpeg portable."
---

# AI Video & Filmmaking (Portable & Non-Admin)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) tương tác với các dịch vụ sinh video AI thông qua API và viết mã nguồn biên tập video tự động bằng thư viện MoviePy kết hợp FFmpeg Portable không đòi hỏi cài đặt hệ thống.

## 1. Cài đặt Thư viện Python cục bộ

```powershell
.venv\Scripts\pip install moviepy requests
```

## 2. Nhúng FFmpeg Portable (Không cần cấu hình PATH Windows)

MoviePy yêu cầu phần mềm FFmpeg để giải mã và mã hóa video. Để tránh việc yêu cầu người dùng cài đặt FFmpeg vào hệ thống Windows hoặc sửa đổi biến môi trường `PATH` (thường đòi hỏi quyền Admin):

1. Tải bản build tĩnh `ffmpeg.exe` cho Windows (ví dụ từ gyan.dev) và đặt nó vào thư mục `bin/` trong dự án.
2. Cấu hình biến môi trường `FFMPEG_BINARY` của MoviePy trong mã nguồn Python trỏ trực tiếp đến tệp này:

```python
import os

# Thiết lập đường dẫn tới tệp ffmpeg.exe cục bộ
project_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(project_dir, "bin", "ffmpeg.exe")

# Đặt biến môi trường cho MoviePy nhận diện
os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
```

## 3. Mã nguồn Biên tập Video tự động bằng MoviePy (Mẫu)

```python
import os
# Đặt biến môi trường FFmpeg trước khi import moviepy
project_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["IMAGEIO_FFMPEG_EXE"] = os.path.join(project_dir, "bin", "ffmpeg.exe")

from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def compile_movie(video_paths, audio_path, output_path):
    clips = []
    try:
        # Load các đoạn video cắt nhỏ (ví dụ sinh ra từ Runway/Luma API)
        for path in video_paths:
            clip = VideoFileClip(path)
            clips.append(clip)
        
        # Ghép nối các đoạn video lại
        final_video = concatenate_videoclips(clips, method="compose")
        
        # Lồng nhạc nền
        audio = AudioFileClip(audio_path)
        final_video = final_video.set_audio(audio)
        
        # Xuất video thành phẩm
        final_video.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio_codec="aac"
        )
    finally:
        # Giải phóng tài nguyên tệp tin tránh lỗi khóa file trên Windows
        for clip in clips:
            clip.close()
        if 'audio' in locals():
            audio.close()
        if 'final_video' in locals():
            final_video.close()
```

## 4. Tích hợp Gọi API các dịch vụ Sinh Video AI (Runway/Luma)

Ví dụ mẫu gọi API sinh video từ ảnh (Image-to-Video) hoặc chữ (Text-to-Video):

```python
import requests
import json
import time

def generate_video_luma(prompt, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "aspect_ratio": "16:9",
        "loop": False
    }
    
    # 1. Gửi yêu cầu sinh video
    response = requests.post("https://api.lumalabs.ai/v1/generations", headers=headers, json=payload)
    gen_id = response.json().get("id")
    
    # 2. Vòng lặp kiểm tra trạng thái (polling) cho tới khi hoàn thành
    while True:
        status_resp = requests.get(f"https://api.lumalabs.ai/v1/generations/{gen_id}", headers=headers)
        status_data = status_resp.json()
        
        if status_data.get("state") == "completed":
            video_url = status_data.get("assets", {}).get("video")
            return video_url
        elif status_data.get("state") == "failed":
            raise Exception("Sinh video thất bại từ API Luma.")
            
        time.sleep(10) # Chờ 10 giây trước khi kiểm tra lại
```
