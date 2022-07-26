from django.shortcuts import render

# Create your views here.
def post_list(request):  #take a request as para
    return render(request, 'blog/post_list.html', {}) #return render pass the request and render .html
