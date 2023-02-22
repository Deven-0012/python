class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return '{} by {}'.format(self.title,self.author)

mybook = Book('The boy','Deven',267)
print(mybook.pages)
print(mybook)

