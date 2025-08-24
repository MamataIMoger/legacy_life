import os
import django
from django.utils import timezone

# --- setup Django environment ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "legacy_life.settings")
django.setup()

from stories.models import Story

def run():
    stories = [
        Story(
            title="Story 1: The Brave Boy",
            author_name="Editorial Team",
            content="Once upon a time, there was a brave boy who helped his village...",
            created_at=timezone.now(),
            is_approved=True
        ),
        Story(
            title="Story 2: Kind Girl",
            author_name="Editorial Team",
            content="There was a kind girl who always helped others and inspired her friends...",
            created_at=timezone.now(),
            is_approved=True
        ),
        Story(
            title="Story 3: Honest Farmer",
            author_name="Editorial Team",
            content="There was once a farmer who always spoke the truth, no matter the cost...",
            created_at=timezone.now(),
            is_approved=True
        ),
        # 👉 keep adding your other 30 stories here
    ]

    Story.objects.bulk_create(stories)
    print(f"✅ Added {len(stories)} stories to the database.")

if __name__ == "__main__":
    run()
