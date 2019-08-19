#1
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