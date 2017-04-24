from django.shortcuts import render, redirect

def index(request):
	return render(request, 'survey/index.html')

def survey_process(request):
	if request.method == 'POST':
		request.session['form_data'] = {
			'my_name' : request.POST['my_name'],
			'dojo_location' : request.POST['dojo_location'],
			'favorite_language' : request.POST['favorite_language'],
			'user_comments' : request.POST['user_comments'],
		}
		try:
			request.session['survey_count'] += 1
			return redirect('/result')
		except KeyError:
			request.session['survey_count'] = 1
			return redirect('/result')
	else:
		return redirect('/')


def result(request):
	print request.session['form_data']
	return render(request, 'survey/result.html', {'form_data': request.session['form_data']})

'''
Note, here's the other way you could have passed along variables, see this example below:

def show_ninja(request, ninja):
	#ninja got passed in through the url parameter!
	context = {'myninja' : ninja}
	return render(request, '/myproject/showmyninja.html', context)

#In showmyninja.html the context dictionary gets unpacked, and we have access to myninja!

<!-- From inside /myproject/showmyninja.html -->
{{myninja}}


This is perhaps an easier way to extract your needed info :)
'''
