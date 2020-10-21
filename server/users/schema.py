from django.db.models import query
from graphene.types import schema
from graphene_django import DjangoObjectType
import graphene
from .models import Profile
from ingredients.models import Category, Ingredient

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    profiles = graphene.List(ProfileType)

    def resolve_profiles(self, info):
        return Profile.objects.all()
    
    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)