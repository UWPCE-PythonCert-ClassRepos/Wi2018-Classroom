#!/usr/bin/env python3


def test_prompt_for_amount(monkeypatch):
    from mailroom4 import prompt_for_amount
    
    monkeypatch.setattr('builtins.input', lambda x: "$5,501.39")
    
    i = prompt_for_amount("Smith")

    assert i == '5501.39'
