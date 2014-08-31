import os.path

### Assign global arrays & variables
name = ''
clothes = []
items = []
limits = []
start = True
safeword = "pinapples"
gender = ""
dom_gender = ""
play_list = []
limits_master = ['anal','pissing yourself','drinking piss','shitting yourself','holding shit','eating shit','pain','CBT','humiliation','hidden public','obvious public']
items_master = ['small dildo','medium dildo','large dildo','small butt plug','medium butt plug','large butt plug','inflatable butt plug','vibrator','blindfold','gag','collar','chastity belt','daiper','paddle','wooden spoon','clothes peg','clover clamp','tweezer clamp']
clothes_master = ['male boxer shorts','mens briefs','a skirt','a dress','a blouse','a bra','ladies briefs']

### Variables to store dom(me)s mood and desires
des_anal = 0
des_piss = 0
des_shit = 0
des_pain = 0
des_CBT = 0
des_humiliation = 0
des_public = 0

des_play = 50;

pnts = 25

### Assign the current version of the program
current_version = '3'

### Main function
def main():
	global start
	if start:
		print("A reminder that your safeword is " + safeword + ", type this at ANY point during play and play will stop.")
		print()
		create_play_list()
		start = False
	while True:
		print("Do you want to play, or ask for something?")
		print("Please reply with either 'play' or 'ask'.")
		UIn = input('>>> ')
		if UIn in ['play','Play','PLAY']:
			play()
		elif UIn in ['ask','ASK','Ask']:
			question()
### Play with the user
def play():
	global des_play
	if des_play >= 35:
		### Play
		print('I will play with you today :)')
		print()
		if dom_gender == 'male':
			print('Please answer each order with a \'Yes Sir\' when you\'ve completed your order')
		elif dom_gender == 'female':
			print('Please answer each command with a \'Yes Miss\' when you\'ve completed your order')
		print('Say \'STOP\' to stop play.')
		playing = True
		while playing == True:
			## Play session
			global play_list
			global safeword
			a = randRange( 0, len(play_list) - 1 )
			print( play_list[a] )
			Input = True
			while Input == True:
				UIn = input('>>> ')
				if UIn == safeword:
					Input = False
					playing = False
				elif UIn == 'STOP':
					Input = False
					playing = False
				elif UIn == 'Yes Miss' or UIn == 'Yes Sir':
					Input = False
				else:
					print('Use one of the replies I told you too!')
	else:
		### Don't play
		print('Not at the moment, but sometime soon.')
### Asks a question
def question():
	print("Ask away " + name + ". You might not like the answer though.")
	print("Hint: type 'help' if you don't know what you can ask.")
	while True:
		UIn = input('>>> ')
		UIn = UIn.lower()
		if UIn in ['help']:
			print('Help text:')
			print('You can ask your dominant many questions, the ones below are model questions although you *should* be able to ask it anything along a similar vien.')
			print()
			print('These ones will always be answered positively:')
			print('   Can I update my items?')
			print('   Can I update my limits?')
			print('   Can I update your information?')
			print('   What is my safeword?')
			print()
			print('The answer to these ones depends on various factors:')
			print('   Can I edge?')
			print('   Can I cum?')
			print('   Can I orgasm?')
			print('   Can I pee?')
			print('   Can I shit?')
			print('   Can I sleep?')
			print('   Can I play with you?')
			print()
		elif 'can' in UIn and 'i' in UIn:
			if 'play' in UIn:
				play()
			elif 'edge' in UIn:
				global pnts
				pnts = pnts - 25
				if pnts >= 50:
					print('You may edge once only')
				elif pnts >= 75:
					print('You may edge twice today')
				else:
					print('You cannot edge today, you\'ve also lost some points')
			elif 'cum' in UIn:
				global pnts
				pnts = pnts - 50
				if pnts >= 150:
					print('You can have a full orgasm today :)')
				elif pnts >= 100:
					print('You can have a ruined orgasm')
				else:
					print('You can\'t cum yet, what are you?')
			elif 'orgasm' in UIn:
				global pnts
				pnts = pnts - 100;
				if pnts >= 250:
					print('You can have a nice, full orgasm today.')
				elif pnts >= 150:
					print('You have to ruin your orgasm ;)')
				else:
					print('You cannot cum at all today, but edge instead')
			elif 'pee' in UIn:
				print('This feature is under development')
			elif 'shit' in UIn:
				print('This feature is under development')
			elif 'sleep' in UIn:
				print('This feature is under development')
			elif 'update' in UIn or 'change' in UIn:
				if 'items' in UIn:
					def_toys()
					create_play_list()
				elif 'limits' in UIn:
					def_limits()
					create_play_list()
				elif 'clothes' in UIn:
					def_clothes()
					create_play_list()
				elif 'info' in UIn:
					def_domina()
		elif 'what' in UIn:
			if 'safeword' in UIn or 'safe word' in UIn:
				print("Your safeword is " + safeword)
		else:
			print("Please ask your question again, perhaps using the framework shown by typing 'help'")
### Get the persons gender
def def_gender():
	global gender
	print("Are you male or female?")
	complete = False
	while complete == False:
		gender = input('>>> ')
		if gender in ['Male','male','MALE', 'm', 'M', 'Man', 'man']:
			gender = 'male'
			complete = True
		elif gender in ['Female','female','FEMALE','f','F','Woman','woman', 'women', 'Women']:
			gender = 'female'
			complete = True
		else:
			print("Please enter your gender again")
### Defines limits
def def_limits ():
	global limits_master
	while len(limits) > 0 : limits.pop()
	for a in limits_master:
		print('Is ' + a + ' a limit?')
		complete = False
		while complete == False:
			UIn = input('>>> ')
			if UIn in ['Yes','yes','YES','y','Y']:
				limits.append(a)
				complete = True
			elif UIn in ['No','no','NO','n','N']:
				complete = True
			else:
				print('Please answer again using yes or no as an answer.')
	with open('prefs/' + current_version + '_' + name + "_limits", 'w+') as f:
		f.truncate()
		for a in limits:
			f.write( a + "\n" )
	print('I have got your limits now.')
### Defines items
def def_toys():
	global items_master
	while len(items) > 0 : items.pop()
	for a in items_master:
		print("Do you own a "+a+"?")
		complete = False
		while complete == False:
			UIn = input('>>> ')
			if UIn in ['Yes','yes','YES','y','Y']:
				items.append(a)
				complete = True
			elif UIn in ['No','no','NO','n','N']:
				complete = True
			else:
				print("Please answer again using yes or no as an asnwer.")
	with open('prefs/' + current_version + '_' + name + "_toys", 'w+') as f:
		f.truncate()
		for a in items:
			f.write( a + "\n" )
	print('I now know what toys you have, thankyou.')
### Define clothes
def def_clothes():
	global clothes_master
	while len(clothes) > 0 : clothes.pop()
	for a in clothes_master:
		print("Do you have "+a+"?")
		complete = False
		while complete == False:
			UIn = input('>>> ')
			if UIn in ['Yes','yes','YES','y','Y']:
				clothes.append(a)
				complete = True
			elif UIn in ['No','no','NO','n','N']:
				complete = True
			else:
				print("Please answer again using yes or no as an asnwer.")
	with open('prefs/' + current_version + '_' + name + "_clothes", 'w+') as f:
		f.truncate()
		for a in clothes:
			f.write( a + "\n" )
	print('I now know what clothes you have, thankyou.')
### Get dom(me) prefs
def def_domina():
	global dom_gender
	print("Do you want a male or female dominant?")
	complete = False
	while complete == False:
		UIn = input('>>> ')
		if UIn in ['male','Male','MALE','m','M']:
			dom_gender = 'male'
			complete = True
		elif UIn in ['female','Female','FEMALE','f','F']:
			dom_gender = 'female'
			complete = True
		else:
			print("Please enter your response again.")
		save_prefs()
### Check if a users data already exists
def check_if_exists():
	if os.path.isfile('prefs/' + current_version + '_' + name):
		### Already a user
		with open('prefs/' + current_version + '_' + name + "_clothes") as f:
			for line in f:
				clothes.append( line.rstrip( '\n' ) )
		with open('prefs/' + current_version + '_' + name + "_toys") as f:
			for line in f:
				items.append( line.rstrip( '\n' ) )
		with open('prefs/' + current_version + '_' + name + "_limits") as f:
			for line in f:
				limits.append( line.rstrip( '\n' ) )
		load_prefs()
		print("Welcome back " + name)
		main()
	else:
		### Create these files
		print("Welcome " + name)
		def_gender()
		def_domina()
		def_limits()
		def_toys()
		def_clothes()
		main()
### return a random number between a & b
def randRange ( a, b ):
    import random
    import math
    return math.floor( random.random() * ( b - ( a - 1 ) ) + a )
### save general preferences
def save_prefs ():
	with open('prefs/' + current_version + '_' + name, 'w') as f:
		f.truncate()
		f.write( dom_gender + "\n")
		f.write( gender + "\n")
		f.write( str(des_anal) + "\n")
		f.write( str(des_piss) + "\n")
		f.write( str(des_shit) + "\n")
		f.write( str(des_pain) + "\n")
		f.write( str(des_CBT) + "\n")
		f.write( str(des_humiliation) + "\n")
		f.write( str(des_public) + "\n")
		f.write( str(des_play) + "\n")
		f.write( str(pnts) + "\n")
### load general preferences
def load_prefs ():
	with open('prefs/' + current_version + '_' + name) as f:
			global dom_gender
			dom_gender = f.readline().rstrip('\n')
			global gender
			gender = f.readline().rstrip('\n')
			global des_anal
			des_anal = int( f.readline().rstrip( '\n' ) )
			des_piss = int( f.readline().rstrip( '\n' ) )
			des_shit = int( f.readline().rstrip( '\n' ) )
			des_pain = int( f.readline().rstrip( '\n' ) )
			des_CBT = int( f.readline().rstrip( '\n' ) )
			des_humiliation = int( f.readline().rstrip( '\n' ) )
			des_public = int( f.readline().rstrip( '\n' ) )
			des_play = int( f.readline().rstrip( '\n' ) )
			pnts = int( f.readline().rstrip( '\n' ) )
### Make a list of all play phrases
def create_play_list():
	if not 'anal' in limits:
		with open('data/anal.txt') as f:
			global instr_anal
			instr_anal = check_lines( f )
	if not 'pissing yourself' in limits:
		with open('data/pissSelf.txt') as f:
			global instr_piss
			instr_piss = check_lines( f )
	if not 'drinking piss' in limits:
		with open('data/pissDrink.txt') as f:
			global instr_piss
			for a in check_lines( f ):
				instr_piss.append( a )
	if not 'shitting yourself' in limits:
		with open('data/shitSelf.txt') as f:
			global instr_shit
			instr_shit = check_lines( f )
	if not 'holding shit' in limits:
		with open('data/shitHold.txt') as f:
			global instr_shit
			for a in check_lines( f ):
				instr_shit.append( a )
	if not 'eating shit' in limits:
		with open('data/shitEat.txt') as f:
			global instr_shit
			for a in check_lines( f ):
				instr_shit.append( a )
	if not 'pain' in limits:
		with open('data/pain.txt') as f:
			global instr_pain
			instr_pain = check_lines( f ) 
	if not 'CBT' in limits:
		with open('data/CBT.txt') as f:
			global instr_CBT
			instr_CBT = check_lines( f ) 
	if not 'humiliation' in limits:
		with open('data/humiliation.txt') as f:
			global instr_humiliation
			instr_humiliation = check_lines( f ) 
	if not 'hidden public' in limits:
		with open('data/hPublic.txt') as f:
			global instr_Public
			instr_public = check_lines( f ) 
	if not 'obvious public' in limits:
		with open('data/oPublic.txt') as f:
			global instr_public
			for a in check_lines( f ):
				instr_public.append( a )
def check_lines( a ):
	global play_list
	a = a.readlines()
	print(a)
	thing = []
	for line in a:
		print(line)
		mod = line.rstrip( '\n' )
		line_list = mod.split()
		write = True
		if '**limit' in line_list or '**toy' in line_list or '**clothing' in line_list or '**sub_gender' in play_list or '**dom_gender' in play_list:
			print('stuff')
			h = 0
			while h < len(line_list):
				if '**' in line_list[h]:
					if line_list[h] == '**limit':
						print('limits')
						if line_list[h+1] == 'anal':
							if not 'anal' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'pissSelf':
							if not 'pissing yourself' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'pissDrink':
							if not 'drinking piss' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'shitSelf':
							if not 'shitting yourself' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'shitHold':
							if not 'holing shit' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'shitEat':
							print('eating shit')
							if not 'eating shit' in limits: 
								bananaa = 0
								print('added')
							else: 
								write = False
								print('not added')
						elif line_list[h+1] == 'pain':
							if not 'pain' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'CBT':
							if not 'CBT' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'humiliation':
							if not 'humiliation' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'hPublic':
							if not 'hidden public' in limits: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'oPublic':
							if not 'obvious public' in limits: bananaa = 0
							else: write = False
						else:
							print('no valid limit')
							write = False
					elif line_list[h] == '**toy':
						if line_list[h+1] == 'smlDildo':
							if 'small dildo' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'medDildo':
							if 'medium dildo' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'lrgDildo':
							if 'large dildo' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'smlButtPlug':
							if 'small butt plug' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'medButtPlug':
							if 'medium butt plug' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'lrgButtPlug':
							if 'large butt plug' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'infButtPlug':
							if 'inflatable butt plugg' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'vibrator':
							if 'vibrator' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'blindfold':
							if 'blindfold' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'gag':
							if 'gag' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'collar':
							if 'collar' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'chastity':
							if 'chastity belt' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'daiper':
							if 'daiper' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'paddle':
							if 'paddle' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'spoon':
							if 'wooden spoon' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'clothesPeg':
							if 'clothes peg' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'cloverClamp':
							if 'clover clamp' in items: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'tweezerClamp':
							if 'medium dildo' in items: bananaa = 0
							else: write = False
						else:
							write = False;
					elif line_list[h] == '**clothing':
						if line_list[h+1] == 'mBoxers':
							if 'male boxer shorts' in clothes: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'mBriefs':
							if 'mens briefs' in clothes: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'fSkirt':
							if 'a skirt' in clothes: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'fDress':
							if 'a dress' in clothes: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'fBlouse':
							if 'a blouse' in clothes: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'fBra':
							if 'a bra' in clothes: bananaa = 0
							else: write = False
						elif line_list[h+1] == 'fBriefs':
							if 'ladies briefs' in clothes: bananaa = 0
							else: write = False
						else:
							write = False
					elif line_list[h] == '**sub_gender':
						if line_list[h+1] == 'male':
							if gender == 'male': bananaa = 0
							else: write = False
						elif line_list[h+1] == 'female':
							if gender == 'female': bananaa = 0
							else: write = False
						else:
							write = False
					elif line_list[h] == '**dom_gender':
						if line_list[h+1] == 'male':
							if dom_gender == 'male': bananaa = 0
							else: write = False
						elif line_list[h+1] == 'female':
							if dom_gender == 'female': bananaa = 0
							else: write = False
						else:
							write = False
					else:
						write = False
						print('no valid tag')
					line_list.remove( line_list[h] )
					line_list.remove( line_list[h] )
				else:
					h = h + 1
		if write == True:
			x = 0
			mod = ''
			while x < len(line_list):
				mod = mod + line_list[x] + ' '
				x = x + 1
			thing.append( mod )
			play_list.append( mod )
	return thing		
			
### Repeating function
def repeat():
	import threading
	threading.Timer(60.0, repeat).start()
	### Do stuff
	global des_anal
	global des_pissSelf
	global des_pissDrink
	global des_shitSelf
	global des_shitHold
	global des_shitEat
	global des_pain
	global des_CBT
	global des_humiliation
	global des_hPublic
	global des_oPublic
	global des_play
	des_anal = des_anal + randRange( 0, 5 )
	des_pissSelf = des_pissSelf + randRange( 0, 5 )
	des_pissDrink = des_pissDrink + randRange( 0, 5 )
	des_shitSelf = des_shitSelf + randRange( 0, 5 )
	des_shitHold = des_shitHold + randRange( 0, 5 )
	des_shitEat = des_shitEat + randRange( 0, 5 )
	des_pain = des_pain + randRange( 0, 5 )
	des_CBT = des_CBT + randRange( 0, 5 )
	des_humiliation = des_humiliation + randRange( 0, 5 )
	des_hPublic = des_hPublic + randRange( 0, 5 )
	des_oPublic = des_oPublic + randRange( 0, 5 )
	des_play = des_play + randRange( 0, 3 )
	save_prefs()
repeat()

################## PROGRAM START!! #######################

### Greet the user
print("Please enter your name?")
name = input('>>> ')
check_if_exists()
