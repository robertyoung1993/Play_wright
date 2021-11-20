"""
demo17
"""

def demo(ham: str, eggs: int = 'spam') -> "Nothing to be here":
    print("函数注释", demo.__annotations__)
    print("参数值打印", ham, eggs)
    print(type(ham), type(eggs))

demo('www')