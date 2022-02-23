
from django.urls import path
from .import views
from store.controllers import authview,cart,checkout,order,contactus,blog,review

urlpatterns = [
    path('',views.home,name = 'home'),
    path('shop',views.shop,name = 'shop'),
    path('blog',views.blog,name = 'blog'),
    path('search',views.search,name = 'search'),
    path('searchproduct',views.searchproduct,name = 'searchproduct'),
    path('detail/<int:pk>/<str:pro_cate>', views.detail, name='detail'),

    path('register/', authview.register, name = 'register' ),
    path('login/', authview.loginpage, name = 'login' ),
    path('logout/', authview.logoutpage, name = 'logout' ),

    path('add-to-cart',cart.addtocart, name= 'addtocart'),
    path('viewcart',cart.cart , name= 'viewcart'),
    path('update-cart',cart.updatecart , name= 'updatecart'),
    path('delete-cart-item',cart.deletecartItem , name= 'deletecartItem'),


    path('checkout',checkout.index , name= 'checkout'),
    path('place-order',checkout.placeorder , name= 'placeorder'),
    
    path('account',views.account,name = 'account'),
    path('view_order/<str:t_no>',order.vieworder,name = 'vieworder'),


    path('contactus',views.contactus,name = 'contactus'),
    path('add-contactus',contactus.addcontact , name= 'addcontact'),

    path('blogdiscdetail/<int:pk>', blog.discount, name='blogdiscdetail'),
    path('blogdetail/<int:pk>', blog.post, name='blogdetail'),

    path('add-review',review.addreview , name= 'addreview'),
]