
import os
import json
from datetime import datetime

class AgentMemory:
    def __init__(self, memory_dir="giwanos_memory"):
        self.memory_dir = memory_dir
        os.makedirs(memory_dir, exist_ok=True)
        self.judgement_file = os.path.join(memory_dir, "judgement_log.json")
        self.reflection_file = os.path.join(memory_dir, "reflection_log.json")

    def _load(self, path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def record_judgement(self, action, exclude=[]):
        log = self._load(self.judgement_file)
        log.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "exclude": exclude
        })
        self._save(self.judgement_file, log)

    def record_reflection(self, action, result, reason=""):
        log = self._load(self.reflection_file)
        log.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "result": result,
            "reason": reason
        })
        self._save(self.reflection_file, log)
