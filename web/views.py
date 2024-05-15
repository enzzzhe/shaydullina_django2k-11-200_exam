from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .models import Review, Category
# from .forms import ReviewForm
# # Create your views here.

def main(request):
    # categories = Category.objects.all()
    # form = ReviewForm(request.POST or None)
    # if form.is_valid():
    #     review = form.save(commit=False)
    #     review.save()
    # category_id = request.GET.get('category', None)
    # if category_id:
    #     reviews = Review.objects.filter(category__id=category_id)
    # else:
    #     reviews = Review.objects.all()
    # context = {
    #     "categories": categories,
    #     "form": form,
    #     "reviews": reviews
    # }
    return render(request, "web/index.html")

