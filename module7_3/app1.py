class Shop:
    categories = {'Haine': [], 'Accesorii': [], 'Imbracaminte': []}
    first_menu_list = ['Categorii' , 'Produse' , 'Iesire' ]
    product_menu_list = ['Adaugare' , 'Vizualizare' , 'Iesire' ]

    def first_menu(self):
        print('''Bun venit la magazinul PyCharm
        1. Categorii.
        2. Produse.
        3. Iesire.    
    ''')
        try:
            option = int(input('Alegeti optiunea:'))
            if option not in range(1, 4):
                raise Exception
        except Exception:
            print('Optiunea aleasa nu e valida.')
            self.first_menu()
        else:
            if option == 1:
                self.category_menu()

    def category_menu(self):
        print(f' category '.center(80, '#'))
        for category in self.categories:
            print(f'--- {category}')
        input()
        self.first_menu()

    def product_menu(self):
        print (f' product '.center(80, '#'))
        print('''
        1.Adaugare
        2.Vizualizare
        3.Iesire
    ''')

        option = self.__get_option(self.product_menu())


    def __get_option(self, menu, menu_options):
        option= input('Introduceti optiunea: ')
        try:
            option = int(option.strip())
        except ValueError:
            print('Option is not valid')
            menu()

        else:
            if option not in range(1, len(menu_options) +1):
                print('Optiunea nu este valida:')
                menu()
                raise Exception
            return option



s = Shop()
s.first_menu()