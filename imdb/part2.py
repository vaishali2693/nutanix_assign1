import imdb_pb2
import time

timee = time.strftime("%d/%m/%Y")
mov = imdb_pb2.Movie()
genre_max = 3
genre_min = 0
tempmov1 = imdb_pb2.Movie()
tempmov2 = imdb_pb2.Movie()
mov.name = 'Sultan'
mov.genre = 2
mov.duration = 160
mov.actor.append('Salman Khan')
#actori = 'Salman Khan'
mov.actor.append('Anushka Sharma')
#actori = 'Anushka Sharma'

def __enterName__(mov) : 
	mov.name = raw_input('Movie name(*) : ')
	return mov

def __enterDOR__(mov) : 
	dor = raw_input('Release Date (dd/mm/yyyy) (Today\'s date will be taken if not entered) : ')
	if dor == '' :
		dor = timee
	dor = dor.split('/')
	mov.dor.day = int(dor[0])
	mov.dor.month = int(dor[1])
	mov.dor.year = int(dor[2])
	return mov 

def __enterGenre__(mov) :
	genre = raw_input('Genre - \n0 for Adventure \n1 for Sci-fi  \n2 for Comedy \n3 for Drama \nChoose one of these : ')
	if genre != '' and int(genre) <= genre_max and int(genre) >= genre_min :
		mov.genre = int(genre)
	return mov 

def __enterDuration__(mov) :
	duration = raw_input('Duration : ')
	if duration != '' :
		mov.duration = int(duration)
	return mov 

def __enterActor__(mov) : 
	actor = 'x'
	while(actor != '') :
		actor = raw_input('Actor:')
		if actor == '' :
			break
		mov.actor.append(actor)
	return mov 

def __enterDirector__(mov) :
	director = 'x'
	while(director != '') :
		director = raw_input('Director:')
		if director == '' :
			break
		mov.director.append(director)
	return mov

def __enterReview__(mov) :
	review = mov.Review()
	review.username = 'x'
	i = 0

	while(review.username != '') :
		i += 1
		print "\nReview " + str(i) + '-'
		review.username = raw_input('Username : ')
		if review.username == '' :
			break
		rating = raw_input('Rating : ')
		if rating != '' :
			review.rating = int(rating)
		
		tme = timee.split('/')
		review.doc.day = int(tme[0])
		review.doc.month = int(tme[1])
		review.doc.year = int(tme[2])

		comment = raw_input('Comment : ')
		if comment != '' :
			review.comment = comment 

		mov.review.extend([review])
	return mov


def __newMov__() : 
	mov = imdb_pb2.Movie()
	mov = __enterName__(mov)
	mov = __enterDOR__(mov)
	mov = __enterGenre__(mov)
	mov = __enterDuration__(mov)
	mov = __enterActor__(mov)
	mov = __enterDirector__(mov)
	mov = __enterReview__(mov)
	return mov 


def __newMovByObj__(mov) :
	return mov


def __getMovByObj__(mov) :
	print mov


if __name__ == '__main__' :
	newmov = __newMovByObj__(mov)
	newmov = __newMov__()
	__getMovByObj__(newmov)

'''
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phone.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

#print person.id
#print person.name
#print person.__str__()
s = person.SerializeToString()
p.ParseFromString(s)
#print p
#print s

print s 
print "*" * 23
print p 

import redis
pool = redis.ConnectionPool(host='localhost',port=6379)
r = redis.Redis(connection_pool=pool)
r.hmset('testyy',{1:'a',2:'b',3:'c'})


r.hmset('test',{1234:s})
t = r.hget('test',1234)
z.ParseFromString(t)
#print z

r.hdel('testyy',2)
#t = r.hget('test',1234)
#print t
#r.hdel('test',1234)
#print r.hget('test',1234)
'''

'''
protoc command - 
protoc --python_out=. ./imdb.proto
'''




