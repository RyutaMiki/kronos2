#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate_models.py
"""

import sys
import json
import re
import traceback
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

# ------------------------------------------------------------
# 1. 入力ファイルを決定
# ------------------------------------------------------------
if len(sys.argv) >= 2:
    src_file = Path(sys.argv[1])
else:
    # ★ デフォルトは schema.yaml に変更
    src_file = Path("schema.yaml")
    print(f"[INFO] 引数が無いので {src_file} を読みます")

if not src_file.exists():
    sys.exit(f"[ERROR] ファイルが見つかりません: {src_file}")

# ------------------------------------------------------------
# 2. JSON / YAML ロード
# ------------------------------------------------------------
def load_file(path: Path):
    if path.suffix.lower() in (".yaml", ".yml"):
        try:
            import yaml
        except ImportError:
            sys.exit("[ERROR] PyYAML が未インストールです → pip install pyyaml")
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return json.loads(path.read_text(encoding="utf-8"))

data = load_file(src_file)

# ルートが list ならそのまま、dict の場合は models キーを探す
if isinstance(data, list):
    models_list = data
elif isinstance(data, dict) and isinstance(data.get("models"), list):
    models_list = data["models"]
else:
    sys.exit("[ERROR] ルートが list でも dict(models=[]) でもありません。")

print(f"[DEBUG] 読み込んだモデル数: {len(models_list)}")

# ------------------------------------------------------------
# 3. Jinja2 環境
# ------------------------------------------------------------
TEMPLATE_DIR = Path(__file__).parent / "templates"
TEMPLATE_NAME = "models_template.j2"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=select_autoescape([]),
    trim_blocks=True,
    lstrip_blocks=True,
)

# regex_replace フィルタ
env.filters["regex_replace"] = lambda v, p, r: re.sub(p, r, v)

# テンプレ取得
try:
    template = env.get_template(TEMPLATE_NAME)
except Exception as e:
    sys.exit(f"[ERROR] テンプレート読み込み失敗: {e}")

# ------------------------------------------------------------
# 4. レンダリング
# ------------------------------------------------------------
try:
    rendered = template.render(models=models_list)
except Exception:
    traceback.print_exc()
    sys.exit("[ERROR] テンプレートレンダリングで例外発生 → 上のトレースを確認")

# ------------------------------------------------------------
# 5. 出力
# ------------------------------------------------------------
output_file = Path("models.py")
output_file.write_text(rendered, encoding="utf-8")
print(f"生成完了: {output_file.resolve()}")
