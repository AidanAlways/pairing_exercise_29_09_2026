from lib.group_chat import *

def test_group_chat_empty_string():
    result = group_chat_empty_string([])
    assert result == ""

def test_group_chat_name():
    result = group_chat_name(["Bart"])
    assert result == "Bart"