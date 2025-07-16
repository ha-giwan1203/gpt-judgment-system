import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="GIWANOS 진화 상태 대시보드", layout="wide")
st.title("🧠 GIWANOS 진화 상태 대시보드")

plan_path = Path("logs/evolution_plan_log.json")

if not plan_path.exists():
    st.warning("진화 계획 파일이 없습니다.")
    st.stop()

plan = json.load(open(plan_path, encoding="utf-8"))
st.markdown(f"### 🕒 생성 시각: `{plan.get('timestamp')}`")
st.markdown(f"**Trigger Reason:** {plan.get('trigger_reason')}")
st.markdown(f"**Action:** {plan.get('action')}")

adjustments = plan.get("adjustments", {})

if not adjustments:
    st.info("현재 조정할 루프가 없습니다. 피드백 데이터가 충분하지 않음.")
else:
    st.subheader("📊 루프별 정확도 및 가중치 조정")
    for loop, detail in adjustments.items():
        st.markdown(f"- `{loop}`: 정확도 {detail['accuracy']:.1f}% → weight {detail['adjust_weight']}")
    st.bar_chart({loop: detail["accuracy"] for loop, detail in adjustments.items()})