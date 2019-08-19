#1
'''Возьмите задачу 1
Создайте класс наследник Market
Создайте конструктор с аргументами material, color, number (def 0), price (def 0)
Величины, которые присутствуют в Market, не должны быть заданы в Market через self
Создайте объект для красного дерева с количеством 10 и ценой 1500
Напечатайте переменные объекта, в том числе те, которые заданы в классе Building '''


class Building:

    def __init__(self, material, color, number):
        self.material = material
        self.color = color
        self.number = number

    def calc(self):
        if self.number <= 0:
            print("out of stock")
        elif 0 < self.number < 100:
            print("warehouse")
        else:
            print("Remote warehouse")


class Market(Building):

    def __init__(self, material, color, number=0, price=0):
        self.price = price
        Building.__init__(self, material, color, number)
        super().__init__(material, color, number)


board = Market('board', 'brown', 10, 50)
print(board.price)

#2
'''Фабричный метод:
Создать класс Document и его наследники: ODFDocument, MSOfficeDocument.
В каждом из них должен быть реализован метод show(), который печатает название программы,
которая должна открывать тип документа.
Создать класс, который в зависимости от типа документа, вызывает метод show().
например, для 'odf' - печатается, что этот файл открывается с помощью OpenOffice,
для 'doc' - MSOffice.'''

class Document:
    def factory(self, type):
        if type == "odf":
            return ODFDocument()
        elif type == "doc":
            return MSOfficeDocument()
   


class ODFDocument(Document):
    def show(self):
        print('Файл открывается с помощью OpenOffice')


class MSOfficeDocument(Document):
    def show(self):
        print('Файл открывается с помощью MSOffice')

d = Document().factory('odf')
d.show()

#d = Document()
#c = d.factory('doc')
#c.show()

