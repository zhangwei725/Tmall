import xadmin

from .models import Banner, Review, User, Property, PropertyValue, ShopCar

# class BannerAdmin:
xadmin.site.register(Banner)
xadmin.site.register(Review)
xadmin.site.register(User)
xadmin.site.register(PropertyValue)
# xadmin.site.register(Property)
xadmin.site.register(ShopCar)
