from django.urls import path
from .views import *

app_name ="ecomapp"
urlpatterns = [
    path("",HomeView.as_view(),name='home'),
    path("about/",AboutView.as_view(),name='about'),
    path("contact/",ContactView.as_view(),name='contact'),
    path("all-products/",AllProductView.as_view(),name='allproducts'),
    path("productdetials/<slug:slug>",ProductDetail.as_view(),name='productdetials'),
    path("add-to-cart/<int:pro_id>",AddToCartView.as_view(),name='addtocart'),
    path("mycart/",MyCart.as_view(),name='mycart'),
    path("managecart/<int:cp_id>",ManageCartView.as_view(),name="managecart"),
    path("emptycart/",EmptyCartView.as_view(),name="emptycart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
    path("register/",CustomerRegisterView.as_view(),name="register"),
    path("logout/",CustomerLogoutView.as_view(),name="logout"),
    path("login/",CustomerLoginView.as_view(),name="login"),
    path("profile/",CustomerProfileView.as_view(),name="profile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(), name="customerorderdetail"),
    path("adminlogin/",AdminLoginView.as_view(),name="adminlogin"),
    path("adminhome/",AdminHomeView.as_view(),name="adminhome"),
    path("admin-order-detail/<int:pk>",AdminOrderDetailView.as_view(),name="admindetail"),
    path("admin-all-order/",AdminAllOrderView.as_view(),name="adminallorder"),

]