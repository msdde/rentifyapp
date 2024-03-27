class SlugMixin:
    def __init__(self):
        self.kwargs = None

    def get_slug(self):
        slug = self.kwargs["slug"]
        return slug


