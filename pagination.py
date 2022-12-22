# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if self.item_count()%self.items_per_page != 0:
            return int(self.item_count()/self.items_per_page)+1
        else:
            return self.item_count()/self.items_per_page

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index > self.page_count():
            return -1 
        else:
            last_page = self.item_count()%self.items_per_page
            if page_index == self.page_count():
                return last_page
            else:
                if int((self.item_count()-last_page)/self.items_per_page) == 1:
                    return int(self.item_count()-last_page)
                else:
                    return int((self.item_count()-last_page)/self.items_per_page)
    # ! NEED TO MAKE PAGE 1, PAGE INDEX 0


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index not in self.collection:
            return -1
        else:
            pass




    