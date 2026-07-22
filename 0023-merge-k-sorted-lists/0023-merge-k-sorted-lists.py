import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Add the first node of every linked list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next