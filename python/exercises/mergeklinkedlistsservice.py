from typing import List


class ListNode:
    def __init__(self, val:int, next = None):
        self.val = val
        self.next = next
    
    def to_arr(self):
        items = []
        actual = self
        while actual is not None:
            items.append(actual.val)
            actual = actual.next
        return items
    
class MergeKLinkedListsService:

    def solution_one(self, list: List[ListNode]):
        # primeiro passo ordernar os primeiros elementos por valor
        list.sort(key=lambda node: node.val)
        
        while len(list) > 1:
            ref1 = list[0]
            ref2 = list.pop(1)

            while ref2 != None:

                if(ref1.val <= ref2.val):
                    has_next = ref1.next != None
                    
                    if(has_next and ref1.next.val <= ref2.val):
                        ref1 = ref1.next
                        continue

                    old_next = ref1.next
                    ref1.next = ref2
                    ref1 = ref2
                    ref2 = old_next
                        
        
        return list[0]