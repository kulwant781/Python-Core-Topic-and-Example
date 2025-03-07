class libary:
 def __init__(self):
    self.books = []
    self.number_books =0

 def addbooks(self, books):
     self.books.append(books)
     self.number_books =len(self.books)

 def showboks(self):
    print(f"Total Number of Books {self.number_books}")

    for index,bk in enumerate(self.books, start=1):
        print(f"this is the new book {bk} and total number of book {index}")

L1 = libary()
L1.addbooks("Python new Courese Book")
L1.addbooks("Php new Courese Book")
L1.addbooks("Javascript new Courese Book")


L1.showboks()

