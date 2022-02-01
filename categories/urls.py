from rest_framework.routers import DefaultRouter

from categories.views import CategoryView, SectionView, GroupView, SubgroupView, CardView


router = DefaultRouter()
router.register("category", CategoryView, basename="category")
router.register("section", SectionView, basename="section")
router.register("group", GroupView, basename="group")
router.register("subgroup", SubgroupView, basename="subgroup")
router.register("card", CardView, basename="card")
urlpatterns = router.urls