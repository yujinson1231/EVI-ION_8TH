import os
import json
from analyzer import analyze_php_file

PLUGIN_ROOT = "/app/plugins"


def scan_plugins():
    """
    plugins 디렉토리 하위의 모든 플러그인을 순회하며
    Broken Access Control 취약점을 탐지한다.
    """
    results = []

    for plugin in os.listdir(PLUGIN_ROOT):
        plugin_path = os.path.join(PLUGIN_ROOT, plugin)

        if not os.path.isdir(plugin_path):
            continue

        findings = []

        for root, _, files in os.walk(plugin_path):
            for file in files:
                if file.endswith(".php"):
                    full_path = os.path.join(root, file)
                    findings.extend(
                        analyze_php_file(full_path, plugin)
                    )

        results.append({
            "plugin": plugin,
            "findings": findings
        })

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    scan_plugins()
