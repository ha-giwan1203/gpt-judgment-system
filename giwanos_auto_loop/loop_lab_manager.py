import json
import random
from pathlib import Path
from datetime import datetime

GENES_PATH = Path("logs/loop_genes.json")
LAB_LOG_PATH = Path("logs/loop_lab_experiments.json")

def run_experiment_group(group_name, count=3):
    if not GENES_PATH.exists():
        print("❌ 루프 유전자 파일 없음")
        return

    genes = json.load(open(GENES_PATH, encoding="utf-8"))
    loops = list(genes.keys())
    selected = random.sample(loops, min(count, len(loops)))

    result = {
        "group": group_name,
        "executed_at": datetime.now().isoformat(),
        "tested_loops": selected,
        "notes": f"{group_name} 실험 그룹 자동 실행"
    }

    if LAB_LOG_PATH.exists():
        log = json.load(open(LAB_LOG_PATH, encoding="utf-8"))
    else:
        log = []

    log.append(result)
    with open(LAB_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

    print(f"🧪 실험 그룹 '{group_name}' 실행 완료 → 루프들: {selected}")
    return selected

if __name__ == "__main__":
    run_experiment_group("exploration_alpha")