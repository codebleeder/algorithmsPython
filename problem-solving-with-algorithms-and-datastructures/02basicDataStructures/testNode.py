__author__ = 'cloudera'
from node import Node
from unorderedList import UnorderedList

newNode = Node(45)
print newNode.getData()
newNode.setData(34)
print newNode.getData()

uList = UnorderedList()

print 'checking size() and add(item):'
print uList.size()
uList.add(55)
print uList.size()

print 'checking search(item):'
print uList.search(3)
print uList.search(55)

print 'checking remove(item):'
uList.add(88)
uList.add(77)
print uList.size()
#uList.remove(55)
#print uList.size()
uList.remove(77)
print uList.size()

print 'checking append(item):'
print 'append(33):'
uList.append('33')
print uList.size()
print 'append(44):'
uList.append(44)
print uList.size()

print 'checking insert(1, 55):'
uList.insert(1, 55)
print 'search(55):'
print uList.search(55)

print 'index(55):'
print uList.index(55)

print 'pop():'
print uList.pop()

print 'pop(2):'
print uList.pop(2)

