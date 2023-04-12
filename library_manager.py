from typing import List, Any


class Book:
    def __init__(
        self,
        title: str,
        *,
        author: str = "",
        prev_position = None,
        next_position = None,
    ):
        self.title = title
        self.author = author
        self.prev_position = prev_position
        self.next_position = next_position


class LibraryManager:
    """ 도서 CRUD """
    def __init__(self):
        self.head = None
        self.tail = self.head

    def create(self, title: str, is_before: bool = False, is_after: bool = False, specific_title: str = ''):
        """ 전체 책의 맨 마지막을 조회하여 책을 Insert """
        if self.head is None:
            self.head = Book(title)
            self.tail = self.head
            return False

        old_book = self.head
        while old_book.next_position:
            old_book = old_book.next_position

        new_book = Book(title)
        new_book.prev_position = old_book
        old_book.next_position = new_book

    def create_prev(self, title: str, searched_title: str):
        if self.head is None:
            self.head = Book(title)
            self.tail = self.head
            return False

        old_book = self.tail
        while old_book:
            if old_book.title == searched_title:
                new_book = Book(title)
                prev_old_book = old_book.prev_position
                new_book.next_position = old_book
                old_book.prev_position = new_book
                if prev_old_book:
                    prev_old_book.next_position = new_book
                else:
                    self.head = new_book
                new_book.prev_position = prev_old_book
                break
            else:
                old_book = old_book.prev_position

    def create_next(self, title: str, searched_title: str):
        if self.head is None:
            self.head = Book(title)
            self.tail = self.head
            return False

        old_book = self.head
        while old_book:
            if old_book.title == searched_title:
                new_book = Book(title)
                next_old_book = old_book.next_position
                old_book.next_position = new_book
                new_book.prev_position = old_book
                if next_old_book:
                    next_old_book.prev_position = new_book
                else:
                    self.tail = new_book
                new_book.next_position = next_old_book
                break
            else:
                old_book = old_book.next_position

    def delete(self, title: str):
        if self.head is None:
            print("책이 한 권도 없습니다. 책을 추가하세요!")
            return False

        if self.head.title == title:
            temp = self.head
            self.head = temp.next_position
            del temp
        else:
            book = self.head
            while book.next_position:
                if book.next_position.title == title:
                    temp = book.next_position
                    book.next_position = temp.next_position
                    del temp
                    return True
                else:
                    book = book.next_position

            print("책을 찾을 수 없습니다.")

    def search(self, title: str):
        if self.head is None:
            print("책이 한 권도 없습니다. 책을 추가하세요!")
            return False

        book = self.head

        while book:
            if book.title == title:
                return book
            else:
                book = book.next_position
        print("책을 찾을 수 없습니다. 제목을 확인하세요.")
        return False

    def get_all_books(self):
        book = self.head
        print(" *********** 도 서 목 록 ***********")
        while book:
            print(book.title)
            book = book.next_position
        print(" *********************************")


def show_menu():
    menu = """
        * * * * * * * * * * * * * * * * * * * *
        *    도   서   관   리   시   스   템     *
        * * * * * * * * * * * * * * * * * * * *
        *      사용 할 기능을 숫자로 입력 하세요      *
        * * * * * * * * * * * * * * * * * * * *
        1. 목록 
        2. 추가
        3. 앞에 추가
        4. 뒤에 추가
        5. 상세 보기
        6. 수정
        7. 삭제
        9. 메뉴 보기
        0. 종료
        """
    print(menu)


def select_menu():
    selected_menu = input("메뉴를 숫자로 입력해 주세요. 예를 들어, 메뉴를 보고 싶으시면 9 을 입력하고 Enter 키를 눌러주세요.\n")
    return selected_menu


def console():
    library = LibraryManager()
    show_menu()
    menu = select_menu()
    while menu:
        if menu:
            if menu == '1':
                library.get_all_books()
            elif menu == '2':
                title = input("추가 할 책의 제목을 입력 하세요.\n")
                library.create(
                    title=title,
                )
                library.get_all_books()
            elif menu == '3':
                title = input("추가 할 책의 제목을 입력 하세요.\n")
                searched_title = input("앞에 추가 하고 싶은 책의 이름을 입력 하세요.\n")
                library.create_prev(
                    title=title,
                    searched_title=searched_title,
                )
                library.get_all_books()
            elif menu == '4':
                title = input("추가 할 책의 제목을 입력 하세요.\n")
                searched_title = input("뒤에 추가 하고 싶은 책의 이름을 입력 하세요.\n")
                library.create_next(
                    title=title,
                    searched_title=searched_title,
                )
                library.get_all_books()
            elif menu == '5':
                title = input("찾고 싶은 책의 제목을 입력 하세요.\n")
                book = library.search(
                    title=title,
                )
                print(f"책 제목은 {book.title} 이고 지은이는 {book.author} 입니다.")
            elif menu == '7':
                title = input("삭제 할 책의 제목을 입력 하세요.\n")
                library.delete(
                    title=title,
                )
                library.get_all_books()
            elif menu == '9':
                show_menu()
            else:
                print("메뉴를 잘못 입력 하셨습니다.")
            menu = select_menu()
        else:
            print("프로그램을 종료합니다!")
            menu = False


if __name__ == '__main__':
    console()
