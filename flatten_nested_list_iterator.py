# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

    def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    # time O(N) - linear
    # lembrar considerar recursão
    # space O(N)
    # reforçar recursão
    # tipagem para ajudar no raciocionio
    # melhorar:
    # problem solving
    # análise e sintese do problema
    # melhorar verbalização da solução
    def __init__(self, nestedList: [NestedInteger]):
        self.flat_list = []
        self.unpack(nestedList)
        self.index = 0

    def next(self) -> int:
        element = self.flat_list[self.index]
        self.index += 1
        return element

    def hasNext(self) -> bool:
        return self.index < len(self.flat_list)

    def unpack(self, nested_list):
        for i in range(len(nested_list)):
            if nested_list[i].isInteger():
                self.flat_list.append(nested_list[i].getInteger())
            else:
                self.unpack(nested_list[i].getList())


if __name__ == '__main__':
    # Your NestedIterator object will be instantiated and called as such:
    nestedList = [[1, 1], 2, [1, 1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        temp = i.next()
        v.append(temp)
        print(temp)

