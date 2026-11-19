import os
import json
import re
import urllib.request

repo = os.environ.get("GITHUB_REPOSITORY")
token = os.environ.get("GITHUB_TOKEN")

if not repo or not token:
    print("❌ 缺少必要的环境变量")
    exit(1)

url = f"https://api.github.com/repos/{repo}/releases?per_page=100"
req = urllib.request.Request(url)
req.add_header("Authorization", f"Bearer {token}")
req.add_header("Accept", "application/vnd.github.v3+json")

print("正在获取 Release...")
with urllib.request.urlopen(req) as response:
    releases = json.loads(response.read().decode('utf-8'))

history_content = "# 版本更新记录\n\n"

for rel in releases:
    tag = rel.get("tag_name", "")
    date = rel.get("published_at", "")[:10]
    body = rel.get("body", "") or ""
    
    # 1. 截断 Magisk 警告及后续内容
    magisk_keyword = "Assets 里的 zip 格式压缩包"
    if magisk_keyword in body:
        body = body.split(magisk_keyword)[0]
        
    # 2. 逐行过滤 [!NOTE] / [!WARNING] 等
    cleaned_lines = []
    in_alert = False
    for line in body.split('\n'):
        # 如果遇到警报标记，开始屏蔽
        if re.match(r'^\s*>\s*\[!(?:NOTE|WARNING|IMPORTANT|TIP|CAUTION)\]', line, re.IGNORECASE):
            in_alert = True
            continue
        
        # 如果处于屏蔽状态
        if in_alert:
            if line.strip().startswith('>'): # 如果还是引用块，继续跳过
                continue
            else:
                in_alert = False # 引用块结束，恢复正常
                
        # 3. 过滤 Full Changelog 和包含“更新日志”的行
        if "**Full Changelog**" in line or "更新日志" in line:
            continue
        if "compare" in line and "https://github.com" in line:
            continue
            
        cleaned_lines.append(line)
        
    body = '\n'.join(cleaned_lines)
    # 4. 清理连续空行
    body = re.sub(r'\n{3,}', '\n\n', body).strip()

    if body: 
        history_content += f"## [{tag}] - {date}\n\n{body}\n\n---\n\n"

with open("HISTORY.md", "w", encoding="utf-8") as f:
    f.write(history_content)
    
print("✅ HISTORY.md 生成完毕！")
