import json
from pathlib import Path

CROSSOVER_GENES_PATH = Path("logs/loop_genes_crossover.json")
OUTPUT_DIR = Path("giwanos_auto_loop")

def generate_loop_script():
    if not CROSSOVER_GENES_PATH.exists():
        print("❌ 교배 유전자 파일 없음")
        return

    new_genes = json.load(open(CROSSOVER_GENES_PATH, encoding="utf-8"))
    for loop_name, traits in new_genes.items():
        filename = OUTPUT_DIR / loop_name
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Auto-generated loop: {loop_name}\n")
            f.write(f"# Traits: {traits}\n")
            f.write("def run():\n")
            f.write(f"    print('🚀 루프 {loop_name} 실행 중...')\n")
            f.write("    return True\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    run()\n")
        print(f"✅ 자동 생성된 루프: {loop_name}")

if __name__ == "__main__":
    generate_loop_script()