import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredients
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
# work fine


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('__all__')


class IngredientsType(DjangoObjectType):
    class Meta:
        model = Ingredients
        fields = ('__all__')


class Query(graphene.ObjectType):
    # above  class for query
    all_ingredients = graphene.List(IngredientsType)
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredients.objects.select_related('category').all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)

        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)


# for django filter
# class CategoryNode(DjangoObjectType):
#     class Meta:
#         model = Category
#         filter_fields = ['name', 'ingredients']
#         interfaces = (relay.Node, )


# class IngredientNode(DjangoObjectType):
#     class Meta:
#         model = Ingredients
#         # Allow for some more advanced filtering here
#         filter_fields = {
#             'name': ['exact', 'icontains', 'istartswith'],
#             'notes': ['exact', 'icontains'],
#             'category': ['exact'],
#             'category__name': ['exact'],
#         }
#         interfaces = (relay.Node, )


# class Query(graphene.ObjectType):
#     category = relay.Node.Field(CategoryNode)
#     all_categories = DjangoFilterConnectionField(CategoryNode)

#     ingredient = relay.Node.Field(IngredientNode)
