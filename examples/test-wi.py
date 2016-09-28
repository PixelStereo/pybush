#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import uic
from PyQt5.QtCore import (QAbstractItemModel, QFile, QIODevice,
        QItemSelectionModel, QModelIndex, Qt)
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem


def fill_item(item, value):
  item.setExpanded(True)
  if type(value) is dict:
    for key, val in sorted(value.iteritems()):
      child = QTreeWidgetItem()
      child.setText(0, unicode(key))
      item.addChild(child)
      fill_item(child, val)
  elif type(value) is list:
    for val in value:
      child = QTreeWidgetItem()
      item.addChild(child)
      if type(val) is dict:      
        child.setText(0, '[dict]')
        fill_item(child, val)
      elif type(val) is list:
        child.setText(0, '[list]')
        fill_item(child, val)
      else:
        child.setText(0, unicode(val))              
      child.setExpanded(True)
  else:
    child = QTreeWidgetItem()
    child.setText(0, unicode(value))
    item.addChild(child)

def fill_widget(widget, value):
  widget.clear()
  fill_item(widget.invisibleRootItem(), value)

d = { 'key1': 'value1', 
  'key2': 'value2',
  'key3': [1,2,3, { 1: 3, 7 : 9}],
  'key4': object(),
  'key5': { 'another key1' : 'another value1',
            'another key2' : 'another value2'} }


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QTreeWidget()
    fill_widget(widget, d)
    widget.show()
    try:
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    except:
        pass
    sys.exit(app.exec_())
