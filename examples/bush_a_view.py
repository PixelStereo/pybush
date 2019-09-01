#!/usr/bin/env python

from pybush import new_device
my_device = new_device(name='test device', author='Pixel Stereo', version='0.1.0')
osc_output = my_device.new_output(protocol='OSC', port='127.0.0.1:5000')
midi_output = my_device.new_output(protocol='MIDI', port='IAC 1')

my_int = my_device.add_param({
                                    'name':'int',
                                    'value':8,
                                    'tags':['int', 'no_dot'],
                                    'datatype':'integer',
                                    'domain':[1,35],
                                    'clipmode':'low',
                                    'unique':False})


my_float = my_device.add_param({
                                    'name':'float',
                                    'value':0.2,
                                    'tags':['float', 'decimal'],
                                    'datatype':'float',
                                    'domain':[-1,1],
                                    'clipmode':'both',
                                    'unique':True})



from PyQt5.QtCore import QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView


class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0


class DeviceModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super(DeviceModel, self).__init__(parent)
        self.rootItem = TreeItem(my_device)

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    model = DeviceModel(my_device)
    view = QTreeView()
    view.setModel(model)
    view.setWindowTitle("View a Bush")
    view.show()
    sys.exit(app.exec_())
