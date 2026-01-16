import os
import re


def analyze_php_file(path, plugin_name):
    """
    PHP 파일에서 wp_ajax_*, admin_post_* 핸들러 중
    권한 검증 누락(Broken Access Control)을 탐지한다.
    """
    findings = []

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    # add_action('wp_ajax_xxx', 'callback')
    hook_pattern = re.findall(
        r"add_action\s*\(\s*['\"](wp_ajax_[^'\"]+|admin_post_[^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]",
        code
    )

    for handler, callback in hook_pattern:
        # 콜백 함수 정의 찾기
        func_pattern = re.search(
            rf"function\s+{re.escape(callback)}\s*\(",
            code
        )

        if not func_pattern:
            continue

        # 권한 체크 여부 확인
        has_cap_check = re.search(
            r"current_user_can\s*\(|user_can\s*\(",
            code
        )

        if not has_cap_check:
            findings.append({
                "type": "Broken Access Control",
                "handler": handler,
                "callback": callback,
                "file": os.path.basename(path),
                "risk": "High",
                "confidence": "Medium",
                "reason": "Handler without capability (regex-based detection)"
            })

    return findings
