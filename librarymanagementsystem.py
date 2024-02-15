class Library:
    def __init__(self):
        # İlk çağrıldığında çalışan kurucu metod (constructor).
        self.file_name = "books.txt"  # Kitap bilgilerinin depolandığı dosyanın adı
        self.file = open(self.file_name, "a+")  # Dosyayı aç ve okuma/yazma modunda tut

    def __del__(self):
        # Nesne silindiğinde çalışan metot (destructor).
        if self.file:
            self.file.close()  # Dosyayı kapat

    def list_books(self):
        # Kitapları listele
        self.file.seek(0)  # Dosyanın başına git
        books = (
            self.file.readlines()
        )  # Satırlara ayır ve kitapları içeren liste oluştur
        for book in books:
            book_info = book.strip().split(
                ","
            )  # Virgülle ayrılmış kitap bilgilerini al
            print(
                f"Book: {book_info[0]}, Author: {book_info[1]}"
            )  # Kitap bilgilerini ekrana yazdır

    def add_book(self):
        # Yeni bir kitap eklemek için metot
        title = input("Enter book title: ")  # Kullanıcıdan kitap adını al
        author = input("Enter book author: ")  # Kullanıcıdan yazar adını al
        release_year = input("Enter release year: ")  # Kullanıcıdan yayın yılını al
        num_pages = input("Enter number of pages: ")  # Kullanıcıdan sayfa sayısını al

        book_info = f"{title},{author},{release_year},{num_pages}\n"  # Kitap bilgilerini birleştir
        self.file.write(book_info)  # Dosyaya yeni kitap bilgilerini ekle
        print("Book added successfully!")  # Kitap başarıyla eklendi mesajını yazdır

    def remove_book(self):
        # Bir kitabı kaldırmak için metot
        title_to_remove = input(
            "Enter the title of the book to remove: "
        )  # Kullanıcıdan kaldırılacak kitabın adını al
        self.file.seek(0)  # Dosyanın başına git
        books = self.file.readlines()  # Dosyadaki tüm kitapları oku
        self.file.seek(0)  # Dosyanın başına git
        self.file.truncate()  # Dosyanın içeriğini temizle

        for book in books:
            if title_to_remove not in book:
                self.file.write(
                    book
                )  # Kaldırılacak kitabı hariç tutarak dosyaya geri yaz

        print(
            f"Book '{title_to_remove}' removed successfully!"
        )  # Kitap başarıyla kaldırıldı mesajını yazdır


# Kütüphane nesnesi oluştur
lib = Library()

# Menü
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("0) Exit")

    choice = input("Enter your choice (0-3): ")  # Kullanıcıdan seçim yapmasını iste

    if choice == "1":
        lib.list_books()  # Kitapları listele
    elif choice == "2":
        lib.add_book()  # Yeni kitap ekle
    elif choice == "3":
        lib.remove_book()  # Kitap kaldır
    elif choice == "0":
        break  # Çıkış yap
    else:
        print(
            "Invalid choice. Please enter a number between 0 and 3."
        )  # Geçersiz seçim mesajını yazdır
