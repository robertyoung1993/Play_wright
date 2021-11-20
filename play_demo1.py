# 创建第一个测试
import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

