from django.contrib import admin
from categories.models import Category, Section, Group, Subgroup, Card


admin.site.register(Card)


class SectionInline(admin.TabularInline):
    model = Section


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [SectionInline]


admin.site.register(Category, CategoryAdmin)



class GroupInline(admin.TabularInline):
    model = Group


class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [GroupInline]


admin.site.register(Section, SectionAdmin)


class SubgroupInline(admin.TabularInline):
    model = Subgroup


class GroupAdmin(admin.ModelAdmin):
    model = Group
    inlines = [SubgroupInline]

admin.site.register(Group,GroupAdmin)



class CardInline(admin.TabularInline):
    model = Card


class SubgroupAdmin(admin.ModelAdmin):
    model = Subgroup
    inlines = [CardInline]

admin.site.register(Subgroup, SubgroupAdmin)
