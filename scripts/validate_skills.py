import os
import sys

# Đảm bảo in ký tự tiếng Việt an toàn trên console Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def validate_skills():
    # Thư mục gốc chứa các skills
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(base_dir, 'skills')
    
    if not os.path.exists(skills_dir):
        print(f"[-] Thư mục skills không tồn tại tại: {skills_dir}")
        return False
        
    errors = 0
    skill_folders = [f for f in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, f))]
    
    print(f"[i] Bắt đầu kiểm tra {len(skill_folders)} kỹ năng (kiểm duyệt dependency-free)...")
    
    for skill_name in skill_folders:
        skill_path = os.path.join(skills_dir, skill_name, 'SKILL.md')
        if not os.path.exists(skill_path):
            print(f"[-] Lỗi: Thiếu tệp SKILL.md trong kỹ năng '{skill_name}'")
            errors += 1
            continue
            
        try:
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Kiểm tra xem có cấu trúc frontmatter --- không
            if not content.startswith('---'):
                print(f"[-] Lỗi: {skill_name}/SKILL.md thiếu YAML frontmatter ở đầu file.")
                errors += 1
                continue
                
            parts = content.split('---')
            if len(parts) < 3:
                print(f"[-] Lỗi: {skill_name}/SKILL.md frontmatter không hợp lệ hoặc thiếu ký tự đóng '---'.")
                errors += 1
                continue
                
            # Parse YAML frontmatter thủ công (dependency-free)
            metadata = {}
            for line in parts[1].split('\n'):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' in line:
                    key, val = line.split(':', 1)
                    metadata[key.strip()] = val.strip().strip('"').strip("'")
            
            # Kiểm tra các trường bắt buộc
            if 'name' not in metadata:
                print(f"[-] Lỗi: {skill_name}/SKILL.md thiếu trường 'name' trong frontmatter.")
                errors += 1
            if 'description' not in metadata:
                print(f"[-] Lỗi: {skill_name}/SKILL.md thiếu trường 'description' trong frontmatter.")
                errors += 1
                
        except Exception as e:
            print(f"[-] Lỗi khi phân tích {skill_name}/SKILL.md: {str(e)}")
            errors += 1

    if errors == 0:
        print("[+] Kiểm tra thành công! Toàn bộ các file SKILL.md đều hợp lệ.")
        return True
    else:
        print(f"[-] Kiểm tra thất bại: Tìm thấy {errors} lỗi định dạng.")
        return False

if __name__ == '__main__':
    success = validate_skills()
    sys.exit(0 if success else 1)
