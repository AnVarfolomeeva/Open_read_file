
class Food_maker():
    cook_book = {}

    def file_manger(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def __init__(self,path = "recipes.txt"):
        list_data = self.file_manger(path).split("\n\n")
        cook_book = {}
        for elem in list_data:
            elem = elem.split("\n")
            food_list = {}
            food_list_nest = {}
            for food in range(2,len(elem)):
                sort, quantity, measure = elem[food].split(' | ')
                food_list_nest[sort] = dict({'measure': measure, 'quantity': quantity})
                food_list.update(food_list_nest)
            if elem[0] not in food_list:
                    cook_book[elem[0]] = food_list_nest
        self.cook_book = cook_book

    def get_shop_list_by_dishes(self, list, persons):
        cook_book = self.cook_book
        cook_book2 = self.cook_book
        for name in list:
            for elem in cook_book[name].keys():
                    result = cook_book[name][elem]['quantity']
                    cook_book2[name][elem]['quantity'] = int(result) * int(persons)
            print(cook_book2[name])

    def print_cook_book(self):
        print(self.cook_book)


list = ['Запеченный картофель', 'Омлет']
persons = 2
fm = Food_maker()
fm.print_cook_book()
fm.get_shop_list_by_dishes(list, persons)


# cook_book = []
# with open('recipes.txt', 'r', encoding='utf-8') as cook_book_list:
#     for line in cook_book_list:
#         recipes_name = line.strip()
#         recipes = {recipes_name: []}
#         number_eng = cook_book_list.readline()
#         for i in range(int(number_eng)):
#             eng = cook_book_list.readline()
#             ingredient_name, quantity,measure = eng.split(' | ')
#             num_eng = {"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure.strip()}
#             recipes[recipes_name].append(num_eng)
#
#         cook_book_list.readline()
#         cook_book.append(recipes)
#
# print(cook_book)
#
# food = cook_book["Омлет"]
# print(food)
#
# li=[]
# for i in cook_book:
#     # print(i)
#     for j in i.values():
#         # print(j)
#         li.append(j)
# print(li)
# dishes = li[0]
# r1 = li[1]
# # print(dishes)
# # for ingridients in r1:
#   # print(ingridients)

# dishes = cook_book[0]
# print(dishes)
# for elem in cook_book:
#     print(elem)
# #     for z in elem[recipes_name]:
#         print(z)
# print(cook_book[0])
# print(cook_book[1])
# print(cook_book[2])
# print(cook_book[1]["Утка по-пекински"][0]["quantity"])
# print(cook_book[0]["Омлет"][0]["quantity"])


