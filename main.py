
from dataclasses import dataclass

@dataclass
class Test:
    name: str

    @property
    def double(self):
        return self.name + self.name

def main():

    test = Test('word')
    print(test.name)

    print(test.double)

main()
