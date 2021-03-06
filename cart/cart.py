from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def add(self, product):
        #comprobar si e producto esta en el carrito
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "quantity": 1,
                "price": str(product.price),
                "image": product.image.url
            }
        #Incrementar la cantidad si ya tengo el producto
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.save()

    #Quitar cantidad de los productos
    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    #Guardar la sesion del carrito
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    #Eliminar producto el carrito
    def remove(self, product):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    #Limpiar carrito
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

