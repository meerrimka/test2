import peewee
from models import Category, Product

def post_category(category_name):
    try:
        category = Category(name = category_name)
        category.save()
        print('Saved!!!!!!!!!')
    except peewee.IntegrityError:
        print('ТАКАЯ КАТЕГОРИЯ УЖЕ СУЩЕСТВУЕТ !!!ё!!!!!!!!!!!!!!!!')

# post_category('game3')

def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'{category.id} -- {category.name} -- {category.created_at}')

def delete_category(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        print('DELETE!!!!1')
    except peewee.DoesNotExist:
        print('КАтегория не найдена !!!!')

def update_category(category_id, new_name):
    try:
        category = Category.get(id=category_id)
        category.name = new_name
        category.save()
        print('UPDATE')
    except peewee.DoesNotExist:
        print('Категория обновлена')


def detail_category(id_category):
    try:
        category =  Category.get(id=id_category)
        print(category.id, end='\t')
        print(category.name, end='\t')
        print(category.created_at)
        # print(category.products)
        for i in category.products:
            print(f'{i.name} -- {i.price} -- {i.amount}')
    except peewee.DoesNotExist:
        print('НЕт такой категори!)')

def post_product(name, price, amount, category):
    try:
        product  = Product(name=name, price=price, amount=amount, category=category)
        product.save()
    except peewee.IntegrityError:
        print('Такой категории не существует !')

def get_products():
    products = Product.select()
    for product in products:
        print(f'{product.id} -- {product.name} -- {product.price} -- {product.amount} -- {product.category_id}')

def get_product_by_name(name):
    products = Product.select().where(Product.name==name)
    for i in products:

        print(i.name, i.price)


get_product_by_name('product1')

# get_products()
# # get_categories()
# # # delete_category()
# # update_category(6, 'game')
# # get_categories()
# # post_category('game2')
# # detail_category(6)
# post_product('product1', 30, 10, 6)
# post_product('product', 700, 8, 8)
# detail_category(8)
