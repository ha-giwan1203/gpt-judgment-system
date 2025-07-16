
import random

def simulate_tree_of_thought():
    thoughts = {
        "zip_backup_generator.py": [
            "백업은 전체 시스템 복구를 가능하게 한다.",
            "실패 시 치명적이기 때문에 항상 우선시해야 한다."
        ],
        "upload_final_runner.py": [
            "실행 결과가 외부와 공유되지 않으면 내부 판단만으로 끝난다.",
            "보고를 통해 판단 정당성을 확보할 수 있다."
        ],
        "file_sort_for_지완OS_v2.py": [
            "정리되지 않으면 기억 흐름이 연결되지 않는다.",
            "사고 흐름을 유지하기 위해 정리가 선행되어야 한다."
        ]
    }

    branches = {}
    for action, reasons in thoughts.items():
        # 각각 이유에 대해 GPT 판단자들이 0~1.0 점수 부여
        scored_reasons = []
        for r in reasons:
            score = round(random.uniform(0.4, 1.0), 2)
            scored_reasons.append({"reason": r, "score": score})
        branches[action] = scored_reasons

    print("\n🌳 Tree-of-Thought 판단 시뮬레이션 결과")
    for action, reasons in branches.items():
        print(f"\n▶ 실행기: {action}")
        for i, r in enumerate(reasons, 1):
            print(f"  {i}. {r['reason']} (score: {r['score']})")

    # 평균 점수 계산
    final_scores = {
        k: round(sum(r["score"] for r in v) / len(v), 2)
        for k, v in branches.items()
    }

    selected = max(final_scores, key=final_scores.get)
    print(f"\n✅ 최종 선택된 실행기: {selected} (평균 score: {final_scores[selected]})")
    return selected, branches, final_scores


if __name__ == "__main__":
    simulate_tree_of_thought()
