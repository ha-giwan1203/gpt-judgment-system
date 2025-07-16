
log_path = "./giwanos_auto_loop/loop_reflection_log.md"
summary_path = "./giwanos_auto_loop/loop_reflection_summary.md"

if not os.path.exists(log_path):
    print("❌ 회고 로그 파일 없음")
    exit()

with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

executions = [line for line in lines if line.startswith("## 🧠 루프 실행")]
summary = f"# ✅ 루프 실행 요약 ({len(executions)}회)

" + "".join(executions)

with open(summary_path, "w", encoding="utf-8") as f:
    f.write(summary)

print(f"📄 회고 요약 저장 완료: loop_reflection_summary.md")
