# When we create a list object and pring the list, we will get the list object containing the list. However if I create a book object
# using this book class what we will get is the object in memory. Behind the scene the pring object gets the string representation of the
# book object and prints that.  So inorder to enable the print() method to print the real book object i-e the title, author and pages of
# the book we have to overwrite the __str__(self) method.


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation of this book class

    def __str__(self):
        return "{} by {}".format(self.title, self.author)
    
    def __len__(self):
        return self.pages

myBook = Book('My story', 'Asim', '202')
print(myBook)
print(str(myBook))