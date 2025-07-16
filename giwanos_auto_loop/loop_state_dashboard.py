import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="GIWANOS 루프 상태 대시보드", layout="wide")
st.title("🧠 GIWANOS 전체 루프 상태 대시보드")

st.markdown("### ✅ 추천 피드백 정확도")
feedback_path = Path("logs/loop_feedback_log.json")
if feedback_path.exists():
    feedback = json.load(open(feedback_path, encoding="utf-8"))
    acc = {}
    for entry in feedback:
        loop = entry["executed_loop"]
        if loop not in acc:
            acc[loop] = {"match": 0, "total": 0}
        acc[loop]["total"] += 1
        if entry["matched"]:
            acc[loop]["match"] += 1
    for loop, stat in acc.items():
        accuracy = stat["match"] / stat["total"] * 100
        st.markdown(f"- `{loop}`: 정확도 {accuracy:.1f}% ({stat['match']}/{stat['total']})")
else:
    st.warning("피드백 로그가 없습니다.")

st.markdown("### 📊 루프 우선순위 모델")
model_path = Path("logs/loop_priority_model.json")
if model_path.exists():
    model = json.load(open(model_path, encoding="utf-8"))
    for loop, m in model.items():
        st.markdown(f"- `{loop}`: weight={m['weight']}, accuracy={m['accuracy']}, usage={m['recent_usage']}")
    st.bar_chart({loop: m['weight'] for loop, m in model.items()})
else:
    st.warning("우선순위 모델 파일이 없습니다.")

st.markdown("### 🔁 마지막 진화 계획")
plan_path = Path("logs/evolution_plan_log.json")
if plan_path.exists():
    plan = json.load(open(plan_path, encoding="utf-8"))
    st.markdown(f"**Trigger:** {plan.get('trigger_reason')}")
    st.markdown(f"**Action:** {plan.get('action')}")
    for loop, adj in plan.get("adjustments", {}).items():
        st.markdown(f"- `{loop}`: 정확도 {adj['accuracy']:.1f} → weight {adj['adjust_weight']}")
else:
    st.info("진화 계획 로그가 없습니다.")