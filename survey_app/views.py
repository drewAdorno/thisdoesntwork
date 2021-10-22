from django.shortcuts import render, redirect

def index(request):
    print('we got here')
    return render(request, 'index.html')

#render the create post form
def write_post(request):
    return render(request, 'write_post.html')


#store form info in session
def process_post(request):
    if 'list_of_posts' not in request.session:
        request.session['list_of_posts']=[]
    
    temp={
        'name':request.POST['name'],
        'content':request.POST['post']
    }

    request.session['list_of_posts'].append(temp)
    return redirect('/')

def clear_session(request):
    request.session.clear()
    return redirect('/')