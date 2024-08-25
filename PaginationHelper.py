# # https://www.codewars.com/kata/515bb423de843ea99400000a/train/python
# # PaginationHelper
#
#
#
# class PaginationHelper:
#
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page
#
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
#
#     # returns the number of pages
#     def page_count(self):
#         if self.item_count() % self.items_per_page > 0:
#             return self.item_count() // self.items_per_page + 1
#         else:
#             return self.item_count() // self.items_per_page
#
#     # returns the number of items on the given page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         if page_index >= self.page_count() or page_index < 0:
#             return -1
#         elif page_index + 1 == self.page_count():
#             return self.item_count() - self.items_per_page * (self.page_count() - 1)
#         else:
#             return self.items_per_page
#
#     # determines what page an item at the given index is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         if item_index >= self.item_count() or item_index < 0:
#             return -1
#         else:
#             return item_index // self.items_per_page

# clever

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1


collection = ['a', 'b', 'c', 'd', 'e', 'f']
helper = PaginationHelper(collection, 4)
print(-(7 // -4))

# print(helper.page_count()) # 2
# print(helper.item_count()) # 6
# print(helper.page_item_count(1)) # 2
# print(helper.page_index(5))
