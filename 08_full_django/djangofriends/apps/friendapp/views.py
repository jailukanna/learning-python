from django.shortcuts import render
from models import Users, Friendships
# Create your views here.
'''
Notes: Numbers in the comments below have been included which correspond to the question number in the assignment
I tried my best to choose appropriate variable names, but believe my variable naming could be improved, as some
are a bit clunky, and I apologize in advance :) Please also note that I understand we are to emulate fat models and skinny
controllers, but for this assignment all the logic will be done in the controller (haven't yet learned how to do
it in the model)
'''

def index(req):

	#########################
	#########################
	##
	##	FRIENDSHIPS ASSIGNMENT PART ONE (1)
	##
	#########################
	#########################

	# 1a. get all() objects from Users
	users = Users.objects.all()
	print '*'*25 + 'filter()' + '*'*25
	print users.query
	print users
	print '*'*57

	# 1. filter() for only last name of Rodriguez
	filtered_users = Users.objects.filter(last_name='Rodriguez')
	print '*'*25 + 'filter()' + '*'*25
	print filtered_users.query
	print filtered_users
	print '*'*57

	# 2. give all users but exclude() last name Rodriguez
	not_excluded_users = Users.objects.exclude(last_name='Rodriguez')
	print '*'*25 + 'exclude()' + '*'*25
	print not_excluded_users.query
	print not_excluded_users
	print '*'*57

	# 3. use the set operator (|) to filter()ing for last name of Rodriguez and Daniels
	and_users = Users.objects.filter(last_name='Rodriguez') | Users.objects.filter(last_name='Daniels')
	print '*'*25 + 'filter() | filter()' + '*'*25
	print and_users.query
	print and_users
	print '*'*57

	# 4. chaining: filter() for last name Rodriguez exclude() first name of Madison
	filtered_except_users = Users.objects.filter(last_name='Rodriguez').exclude(first_name='Madison')
	print '*'*25 + 'filter() and exclude()' + '*'*25
	print filtered_except_users.query
	print filtered_except_users
	print '*'*57

	# 5. chaining: get all() but exclude() first name of Daniel or first name of Michael
	get_exclude_users = Users.objects.all().exclude(first_name='Daniel').exclude(first_name='Michael')
	print '*'*25 + 'all() and exclude()' + '*'*25
	print get_exclude_users.query
	print get_exclude_users
	print '*'*57

	# 6. use get() to get user with id=1
	get_user_id = Users.objects.get(id=1)
	print '*'*25 + 'get() user by id' + '*'*25
	# print get_user.query # this is commented out because for get() there is no query attribute
	print get_user_id
	print '*'*57

	# 7. use get() to get user with id=1:
	# get_user_last_name = Users.objects.get(last_name='Rodriguez')
	'''
	the above line is commented out because .get can only return one object
	in this case, 3 items matched, therefor an error is thrown in django
	the difference between filter is that it will return a list/array of objects
	get will only return a single matching object
	use get when you want to be specific and singular
	use filter when you want to filter groups
	'''

	# 8. get_large_id = Users.objects.get(id=1000)
	# print get_large_id
	'''
	the above is commented out also, if we use get and the value is out of range,
	then django will throw an error.
	'''
	# 8b. filter id by lesser than or greater than
	grtr_or_lssr_users = Users.objects.filter(id__lte=7) | Users.objects.filter(id__gte=9)
	print grtr_or_lssr_users


	# 9. all users order_by() first name
	order_by_first_name_users = Users.objects.order_by('first_name')
	print order_by_first_name_users

	# 10. all users order_by() last name reverse
	last_name_reverse_users = Users.objects.order_by('last_name').reverse()
	print last_name_reverse_users

	# 11. print all friendships objects in terminal only
	friendship_objects = Friendships.objects.all().order_by('user') # order by user added to help confirm accuracy with Part II, # 1
	print '$'*50
	print friendship_objects
	print '$'*50

	# 12. show friendships for user.id=4
	friendships_m2m_by_id = Friendships.objects.filter(user=(Users.objects.get(id=4)))
	print friendships_m2m_by_id

	# 13. show friendships where user.id=4 is the friend
	friendships_m2m_by_friend = Friendships.objects.filter(friend=(Users.objects.get(id=4)))
	print friendships_m2m_by_friend

	# 14. show friendships where user.id != 4,5 or 6
	# used chaining
	friendships_m2m_exclude_by_id = Friendships.objects.exclude(user=(Users.objects.get(id=4))).exclude(user=(Users.objects.get(id=5))).exclude(user=(Users.objects.get(id=6))).order_by('user')
	users_excluded = Users.objects.filter(id=4) | Users.objects.filter(id=5) | Users.objects.filter(id=6)
	print '%'*60
	print friendships_m2m_exclude_by_id
	print '%'*60
	print users_excluded

	# note this now ends the 'Friendships' assignment (Part One [1])


	#########################
	#########################
	##
	##	FRIENDSHIPS ASSIGNMENT CONTINUED -- PART TWO (2)
	##
	#########################
	#########################

	# 1. show first and last name of users in 'friend' and 'user' column of 'Friendships' model:
	all_friendships = Friendships.objects.all().order_by('user') # order by user helps confirm all values were listed (see Part I, #11)
	print '%'*75
	print all_friendships

	#2. show first and last name of all friends associated with user with first name of 'Michael':
	michael_friends = Friendships.objects.filter(user__first_name='Michael')
	print '%'*75
	print michael_friends

	#3. show the first and last name of all friends who daniel is not friends with
	#*** Come back to this one-- you're not getting the right output and you maybe
	#misunderstanding the question.

	friends_of_daniel = Friendships.objects.filter(user__first_name='Daniel')
	daniels_friends = []
	print '%'*75
	for friend_of_daniel in friends_of_daniel:
		print friend_of_daniel.friend.id
		print str(friend_of_daniel.user.id) + '&&'
		daniels_friends.append(friend_of_daniel.friend.id)

	daniels_friends = list(set(daniels_friends)) # removes any duplicates and then converts back to list
	daniels_friends.append(friends_of_daniel[0].user.id) # adds daniel's id himself to the list
	print daniels_friends
	print '^'*50
	print friends_of_daniel[0].user.id
	print '^'*50

	not_daniels_friends = Users.objects.exclude(id__in=daniels_friends) # exclude any user whom is daniel or a friend of daniel
	print not_daniels_friends

	print '%'*75
	print friends_of_daniel
	print '%'*75

	#4. Print all of the friends who are friends with both User with the id of 1 and with Users with the last name Hernandez
	user_friends = Friendships.objects.filter(user__id=1).filter(user__last_name='Hernandez')
	print user_friends.query
	print user_friends # note this prints nothing, as no condition is such that a friend with the user id of 1 is also a friend of anyone with the user last_name of Hernandez

	friends_id_1 = Friendships.objects.filter(user__id=1)
	hernandez_friends = Friendships.objects.filter(friend__last_name='Hernandez')
	print friends_id_1 # this is any friends of user.id=1
	print friends_id_1.query
	print hernandez_friends # this any friends with user.last_name=Hernandez
	print hernandez_friends.query

	#5. Order these by friend first_name and print them on your index.html page. (Note the double output of Daniel Moore!).
	# order friends with user.id=1 by first_name
	ordered_friends = Friendships.objects.filter(user__id=1).order_by('friend__first_name')
	print '&'*50
	for ordered_friend in ordered_friends:
		print ordered_friend.friend.first_name, ordered_friend.friend.last_name
	print '&'*50

	# order friends with user.last_name='Hernandez' by first_name
	ordered_hernandezes = Friendships.objects.filter(friend__last_name='Hernandez').order_by('friend__first_name')
	# .distinct('friend__first_name') will not work - throws error
	print '@'*50
	for ordered_hernandez in ordered_hernandezes:
		print ordered_hernandez.friend.first_name, ordered_hernandez.friend.last_name
	print '@'*50


	#6. Try the following:
	# using 'related_name' strategy below:
	question_six_users = Users.objects.filter(usersfriend__friend__id=2) # .filter(<values_table><foreign_key_field>__<foreign_key_field>__<filter_value>) Note:be sure to include the double (__) - this lets us go backwards, from 'users' table we bind up the 'friend' ('usersfriend__' will associate all `friend` values with a valid `user.id` ) then we look for any friend(s) whose associated user.id=2 (this will be a list of the acutual User objects themselves)
	print '^'*50
	print (question_six_users.query)
	# in SQL terms: 'SELECT * FROM users INNER JOIN friendships ON (users.id=friendships.user_id) WHERE friendships.friend_id=2;'

	#7. use the query in question #6, but on the template side, of the friends returned, print first and last name of users with id=2:

	#8. Re-do #4 using the related_name method:
	# Print all of the friends who are friends with both User with the id of 1 and with Users with the last name Hernandez
	id_of_one_users = Users.objects.filter(usersfriend__friend__id=1)
	hernandez_users = Users.objects.filter(usersfriend__friend__last_name='Hernandez')

	books = Book.objects.filter(authorauthor__)

	print '^'*50
	print id_of_one_users
	print hernandez_users
	print '^'*50



	#####
	#
	#	If getting caught up:
	#
	#####

	# Note: If things get too tricky, you can always add another DB query.
	# e.g. number2 = models.Users.get(id=2) and pass that to the context dictionary!

	# Remember: you can always write your own query using. Users.objects.raw('your query here') if you need.


	# all data from above queries (parts 1 and 2) saved into one contex dictionary and passed to views(templates)
	context = {
		'users':users,
		'filtered_users':filtered_users,
		'not_excluded_users':not_excluded_users,
		'and_users':and_users,
		'filtered_except_users':filtered_except_users,
		'get_exclude_users':get_exclude_users,
		'get_user_id':get_user_id,
		'grtr_or_lssr_users':grtr_or_lssr_users,
		'order_by_first_name_users':order_by_first_name_users,
		'last_name_reverse_users':last_name_reverse_users,
		'friendship_objects':friendship_objects,
		'friendships_m2m_by_id':friendships_m2m_by_id,
		'friendships_m2m_by_friend':friendships_m2m_by_friend,
		'friendships_m2m_exclude_by_id':friendships_m2m_exclude_by_id,
		'users_excluded':users_excluded,
		'all_friendships':all_friendships,
		'michael_friends':michael_friends,
		'not_daniels_friends':not_daniels_friends,
		'user_friends':user_friends,
		'friends_id_1':friends_id_1,
		'hernandez_friends':hernandez_friends,
		'ordered_friends':ordered_friends,
		'ordered_hernandezes':ordered_hernandezes,
		'question_six_users':question_six_users,
		'id_of_one_users':id_of_one_users,
		'hernandez_users':hernandez_users,
	}

	return render(req, "friendapp/index.html",context)


# aren't you glad all of these print statements are over? me too! onwards!
