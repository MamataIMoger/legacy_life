# stories/views.py
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Story
from .forms import StoryForm

def story_list(request):
    stories = Story.objects.filter(is_featured=True).order_by("-created_at")
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            # approval flag
            story.is_featured = False
            # safe defaults
            story.summary = story.summary or ""
            story.category = story.category or ""
            story.status = story.status or "draft"
            # slug
            if not story.slug:
                story.slug = slugify(story.title)[:200]
            story.save()
            return redirect("stories:list")
    else:
        form = StoryForm()
    # if your template path is project-level "templates/story_list.html":
    return render(request, "story_list.html", {"stories": stories, "form": form})

def story_submit(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.is_featured = False
            if not story.slug:
                story.slug = slugify(story.title)[:200]
            story.save()
            return redirect("stories:list")
    else:
        form = StoryForm()
    return render(request, "story_submit.html", {"form": form})
