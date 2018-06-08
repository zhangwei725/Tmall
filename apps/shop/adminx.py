import xadmin

from .models import Banner, Review, User, Property, PropertyValue

# class BannerAdmin:
xadmin.site.register(Banner)
xadmin.site.register(Review)
xadmin.site.register(Property)
xadmin.site.register(PropertyValue)
