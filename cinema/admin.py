from django.contrib import admin

from cinema.models import Category, Genre, Movie, MovieShot, Actor, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    actions = ["publish", "unpublish"]

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "One entry has been updated"
        else:
            message_bit = f"{row_update} entry's has been updated"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "One entry has been updated"
        else:
            message_bit = f"{row_update} entry's has been updated"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Publish"
    publish.allowed_permissions = ("change", )

    unpublish.short_description = "Remove from publication"
    unpublish.allowed_permissions = ("change", )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "movie")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


@admin.register(MovieShot)
class MovieShotAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "movie")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "star", "movie")


admin.site.register(RatingStar)
