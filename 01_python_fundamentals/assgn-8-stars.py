
x = [1,2,'Tim',4,'Julianna',8,9,10]

def draw_stars(arr):
	for elem in arr:
		if isinstance (elem, str) == True:  # checks if elem is a str
			print elem[:1].lower() * len(elem) # the [:1] command takes the first value in the string and then multiplies it by the # of index values in the string - this is how we get the lower case value multipled by the # of places in our name
		else:
			print elem * "*"

draw_stars(x)