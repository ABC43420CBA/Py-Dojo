class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_


class LList:
    def __init__(self):
        self._head=None

    def is_empty(self):
        return self._head is None

    def prepend(self,elem):
        self._head=LNode(elem,self._head)

    def pop(self):
        if self._head is None:
            pass
        e=self._head.elem
        self._head=self._head.next
        return e


class LCList(LList):
    def __init__(self):
        self._rear=None

    def is_empty(self):
        return self._rear == None

    def prepend(self,elem):
        if self.is_empty:
            self._head=LNode(elem)
            self._rear=self._head
        else:
            #temp=self._head
            self._rear.next=LNode(self,elem,self._head)
            self._head=self._rear.next



a=LList()
a.prepend(100)
a.prepend(33)
p=a._head
print(p.elem)
a.pop()
p=a._head
print(p.elem)
a.pop()
p=a._head
print(p.elem)