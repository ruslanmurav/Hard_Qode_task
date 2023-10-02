from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from lesson.models import Lesson, ProductLesson
from product.models import Product, Access
from product.serializers import ProductSerializer, AccessSerializer, UserLessonSerializer, UserProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AccessViewSet(ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer


class UserLessonViewSet(ModelViewSet):
    serializer_class = UserLessonSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = User.objects.get(pk=user_id)

        lessons = Lesson.objects.filter(productlesson__product__access__user=user)
        return lessons


class UserProductViewSet(ModelViewSet):
    serializer_class = UserProductSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        product_id = self.kwargs['product_id']
        if user_id and product_id:
            access = Access.objects.filter(user_id=user_id, product_id=product_id).first()

            if access:
                lessons = Lesson.objects.filter(productlesson__product_id=product_id)
                return lessons
        return Lesson.objects.none()

