import streamlit as st
import json
from pathlib import Path
from collections import defaultdict

st.set_page_config(page_title="GIWANOS 루프 상태 종합 대시보드", layout="wide")
st.title("📊 GIWANOS 루프 운영 상태 통합 대시보드")

# 실행 이력
mem_file = Path("logs/loop_execution_memory.json")
if mem_file.exists():
    data = json.load(open(mem_file, encoding="utf-8"))
    st.subheader("🧠 루프 실행 이력 (최근 10개)")
    for d in data[-10:][::-1]:
        st.markdown(f"- `{d['executed_at']}` → `{d['loop']}` → `{d['result']}` | {d.get('notes','')}")
else:
    st.warning("실행 이력 없음")

# 실패 감시
fail_counts = defaultdict(int)
for d in data:
    if d["result"] == "fail":
        fail_counts[d["loop"]] += 1

if fail_counts:
    st.subheader("❗ 누적 실패 수")
    for loop, count in fail_counts.items():
        st.markdown(f"- `{loop}`: {count}회 실패")
else:
    st.success("모든 루프 정상 실행 중")

# 우선순위 모델
model_file = Path("logs/loop_priority_model.json")
if model_file.exists():
    model = json.load(open(model_file, encoding="utf-8"))
    st.subheader("📈 루프 우선순위 모델 (weight)")
    st.bar_chart({k: v["weight"] for k, v in model.items()})
else:
    st.warning("우선순위 모델 없음")