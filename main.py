
from dataclasses import dataclass

@dataclass
class Test:
    name: str

def main():

    test = Test('word')
    print(test.name)

main()
