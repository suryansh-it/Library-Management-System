from django.contrib.admin import SimpleListFilter

class GenreFilter(SimpleListFilter):
    title ='Genre'
    parameter_name ='genre'

    def lookups(self, request, model_admin):
        return[
            ('fiction', 'Fiction'),
            ('non-fiction', 'Non-Fiction'),
            ('fantasy', 'Fantasy'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(additional_info_genre= self.value())
        return queryset  