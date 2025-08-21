from django.db import models
from django.utils.text import slugify

class Story(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author_name = models.CharField(max_length=120, blank=True)
    summary = models.TextField(blank=True)
    body = models.TextField()
    cover = models.ImageField(upload_to='stories/covers/', blank=True, null=True)
    category = models.CharField(max_length=60, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[('draft', 'Draft'), ('published', 'Published')],
        default='draft'
    )
    is_featured = models.BooleanField(default=True)  # ✅ featured = True
    published_at = models.DateField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    word_file = models.FileField(upload_to='stories/docs/', blank=True, null=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if empty
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Story.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
