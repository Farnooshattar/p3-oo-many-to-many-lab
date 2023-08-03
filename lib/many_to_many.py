class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.book == self:
                contract_list.append(contract)
        return contract_list

    def authors(self):
        author_list = []
        for contract in Contract.all:
            if contract.book == self:
                author_list.append(contract.author)
        return author_list


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.author == self:
                contract_list.append(contract)
        return contract_list

    def books(self):
        book_list = []
        for contract in Contract.all:
            if contract.author == self:
                book_list.append(contract.book)
        return book_list

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")

        if not isinstance(date, str):
            raise Exception("Invalid date")

        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")

        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
                total = + total + contract.royalties
        return total


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")

        if not isinstance(book, Book):
            raise Exception("Invalid book")

        if not isinstance(date, str):
            raise Exception("Invalid date")

        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    # @classmethod
    # def contracts_by_date(cls, date):
    #     return [contract for contract in cls.all if contract.date == date]
