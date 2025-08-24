from typing import Any, Dict, Optional

def is_string_balanced(s: str, rules: Optional[Dict[str, Any]]=None) -> bool:
    """
    Determine if a string is balanced according to a provided set of rules.
    Flow:
      1. Validate the string using 'validity' rules.
      2. If valid, check that the string contains only allowed characters.
      3. If still valid, check balance using 'balance' rules.
    Returns True if balanced, otherwise False.
    """
    if rules is None:
        rules = {}

    def _is_valid(text: str) -> bool:
        validity = rules.get('validity', []) if isinstance(rules, dict) else []
        for rule in validity:
            if callable(rule):
                if not rule(text):
                    return False
            else:
                continue
        return True

    def _has_only_allowed_chars(text: str) -> bool:
        allowed_chars = rules.get('allowed_chars', None) if isinstance(rules, dict) else None
        if allowed_chars is None:
            return True
        allowed_set = set(allowed_chars)
        return all((ch in allowed_set for ch in text))

    def _is_balanced(text: str) -> bool:
        balance_rules = rules.get('balance', []) if isinstance(rules, dict) else []
        if not balance_rules:
            return True
        for rule in balance_rules:
            if callable(rule):
                if not rule(text):
                    return False
            else:
                continue
        return True
    if not _is_valid(s):
        return False
    if not _has_only_allowed_chars(s):
        return False
    return _is_balanced(s)