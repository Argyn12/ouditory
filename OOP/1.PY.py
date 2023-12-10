class NoteBook:
    fail = ''
    brand = ''
    ozu = 0

    def __init__(self, fail,brand, ozu):
        self.fail = fail
        self.brand = brand
        self.ozu = ozu

    def open_fail(self):
        print('fail opened', self.fail)

computer = NoteBook('Paithon','Q_MAX', 2)
print(computer.fail, computer.brand, computer.ozu)
computer.open_fail()