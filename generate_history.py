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
        
    # 2. 逐行过滤 [!NOTE] / [!WARNING] 等块
    cleaned_lines = []
    in_alert = False
    for line in body.split('\n'):
        stripped = line.strip()
        
        # 开启警报屏蔽
        if re.match(r'^>\s*\[!(?:NOTE|WARNING|IMPORTANT|TIP|CAUTION)\]', stripped, re.IGNORECASE):
            in_alert = True
            continue
        
        # 如果处于屏蔽状态
        if in_alert:
            if stripped.startswith('>'): 
                continue # 继续过滤掉警告下面的 > 内容（包括 > ⚠️）
            else:
                in_alert = False # 遇到普通段落，解除屏蔽
                
        # 强制过滤单独的 > ⚠️ 行（防止漏网）
        if stripped.startswith('>') and "⚠️" in stripped:
            continue
            
        # 强制过滤包含网盘网址的整行
        if "http://lxgw.ys168.com" in line:
            continue
            
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

# ================= 新增：全局清理 =================
# 5. 合并连续的分隔线（允许中间有空行），统一替换为单个 ---
history_content = re.sub(r'(?m)^\s*---\s*$\s*(?:^---\s*$\s*)+', '---\n\n', history_content)

# 6. 清理因为合并 --- 可能产生的多余空行
history_content = re.sub(r'\n{3,}', '\n\n', history_content)
# ==================================================

with open("HISTORY.md", "w", encoding="utf-8") as f:
    f.write(history_content)
    
print("✅ HISTORY.md 生成完毕！")
