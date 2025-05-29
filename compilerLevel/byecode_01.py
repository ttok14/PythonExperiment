import dis

source_code = """
class MyClass:
    def Say(self):
        print("HELLO WORLD")

instance = MyClass()
instance.Say()
"""

code_object = compile(source_code, "<string>", "exec")

dis.dis(code_object)