import os
import sys

# Đảm bảo in ký tự tiếng Việt an toàn trên console Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def update_readme():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(base_dir, 'skills')
    readme_path = os.path.join(base_dir, 'README.md')
    
    if not os.path.exists(skills_dir) or not os.path.exists(readme_path):
        print("[-] Thiếu thư mục skills hoặc tệp README.md")
        return False
        
    # Phân loại kỹ năng vào 4 nhóm
    groups = {
        'qa': [],
        'automation': [],
        'media': [],
        'data': []
    }
    
    # Định nghĩa nhóm cho từng skill name
    skill_groups_mapping = {
        'reasoning-critic-qa': 'qa',
        'diagnose': 'qa',
        'grill-me': 'qa',
        'handoff': 'qa',
        'prototype': 'qa',
        'git-commit-helper': 'qa',
        'skill-documenter': 'qa',
        'exploratory-testing': 'qa',
        'ai-bug-triage': 'qa',
        'code-review-and-qa': 'qa',
        
        'web-scraping-headless': 'automation',
        'sap-automation-win32': 'automation',
        
        'image-computer-vision': 'media',
        'ai-video-filmmaking': 'media',
        'premium-ui-assets': 'media',
        'wincommerce-luminous-liquid-glass': 'media',
        
        'statistical-anomaly-detector': 'data',
        'ml-anomaly-detector': 'data',
        'time-series-anomaly-detector': 'data',
        'data-cleaning-and-formatting': 'data',
        'excel-report-generator': 'data',
        'pdf-data-extractor': 'data'
    }
    
    skill_folders = [f for f in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, f))]
    
    for skill_name in sorted(skill_folders):
        skill_path = os.path.join(skills_dir, skill_name, 'SKILL.md')
        if not os.path.exists(skill_path):
            continue
            
        try:
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            parts = content.split('---')
            metadata = {}
            for line in parts[1].split('\n'):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' in line:
                    key, val = line.split(':', 1)
                    metadata[key.strip()] = val.strip().strip('"').strip("'")
            
            name = metadata.get('name', skill_name)
            desc = metadata.get('description', '')
            
            group_key = skill_groups_mapping.get(name, 'qa') # default to qa if unknown
            groups[group_key].append((name, desc))
            
        except Exception as e:
            print(f"[-] Lỗi khi đọc kỹ năng {skill_name}: {str(e)}")
            
    # Xây dựng nội dung danh sách kỹ năng mới
    new_skills_list = []
    new_skills_list.append(f"*   **`skills/`**: Danh sách {len(skill_folders)} kỹ năng tùy chỉnh:")
    
    # 1. Nhóm năng suất & QA
    new_skills_list.append("    *   **Nhóm năng suất & QA:**")
    for name, desc in groups['qa']:
        new_skills_list.append(f"        *   `{name}`: {desc}")
        
    # 2. Nhóm cào dữ liệu & Tự động hóa
    new_skills_list.append("    *   **Nhóm cào dữ liệu & Tự động hóa:**")
    for name, desc in groups['automation']:
        new_skills_list.append(f"        *   `{name}`: {desc}")
        
    # 3. Nhóm xử lý đa phương tiện
    new_skills_list.append("    *   **Nhóm xử lý đa phương tiện:**")
    for name, desc in groups['media']:
        new_skills_list.append(f"        *   `{name}`: {desc}")
        
    # 4. Nhóm xử lý dữ liệu nâng cao
    new_skills_list.append("    *   **Nhóm xử lý dữ liệu nâng cao:**")
    for name, desc in groups['data']:
        new_skills_list.append(f"        *   `{name}`: {desc}")
        
    new_skills_text = '\n'.join(new_skills_list)
    
    # Đọc README.md và thay thế
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
        
    # Tìm vùng cần thay thế
    start_marker = "*   **`skills/`**:"
    end_marker = "---"
    
    try:
        start_idx = readme_content.index(start_marker)
        # Tìm vị trí phân tách '---' sau start_idx
        end_idx = readme_content.index(end_marker, start_idx)
        
        # Tạo nội dung mới
        updated_content = (
            readme_content[:start_idx] + 
            new_skills_text + "\n\n" + 
            readme_content[end_idx:]
        )
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print("[+] Đã đồng bộ thành công danh sách kỹ năng mới vào README.md!")
        return True
    except Exception as e:
        print(f"[-] Lỗi khi cập nhật README.md: {str(e)}")
        return False

if __name__ == '__main__':
    update_readme()
