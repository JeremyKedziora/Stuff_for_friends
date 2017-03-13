#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Napolons triumph combat resolution
#Jeremy Kedziora
#8/29/15
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import console

intro = 'The combat resolution sequence is as follows:\n 1) Attacker names the attack approach but does not indicate what units are attacking.\n 2) Defender choose to either retreat or defend. \n 3) Attacker announces whether the attack is a feint.\n 4) Defender announces which of his pieces will be leading the defense.\n 5) Attacker names the command/pieces making the attack, the attack width, and the pieces leading the attack. \n 6) Initial results are computed. \n 7) Defender may name pieces to participate in a counterattack. \n 8) Final results are computed.'

retreat_text = 'All pieces in the locale must retreat.\n 1) Pieces forced to retreat must go into the reserve in one or more adjacent locales. This cannot be the locale that the attack came from, cannot be an enemy occupied locale, and cannot be a locale across an impassible approach. \n 2) All artillery are eliminated. \n 3) The pieces in each approach occupied by cavalry or infantry must share one loss if the approach is narrow and two losses if it is wide. \n 4) Any pieces in the reserve not named as defending pieces above must share one loss if it is narrow or two losses if it is wide.'

defend_text = 'If the defender chooses not to retreat then he must name which pieces will defend. \n 1) If there are pieces blocking the approach through which the attack is coming then they and only they must be named as defenders. If the defending player has such pieces then he may not retreat. \n 2) If there are no pieces blocking the approach through which the attack is coming then the defending player may name pieces in the reserve as defenders. These can come include any number of pieces from any number of corps. They can include at most one detached unit. \n 3) Pieces blocking another approach cannot be named as defenders. \n 4) Pieces that defended another approach from an attack this turn or that retreated earlier this turn cannot benamed as defenders.'

attack_declaration_feint = 'The attacking player names the command and pieces he is using to make the attack, the attack width, and the pieces leading the attack. Turn the leading pieces face up. \n 1) Attacking pieces do not enter the defense locale. If they were blocking the attack approach they continue to do so. If they were is reservethen they may all move up to block the attack approach or they may all stay in reserve. \n 2) If the defending pieces are in reserve then the defending player may advance any or all of his named defending units to block the defense approach. He must advance at least one (it becomes detached from its corps).'

attack_declaration_nofeint = '5) The attacking player names the command and pieces he is using to make the attack, the attack width, and the pieces leading the attack. Turn the leading pieces face up. \n 1) The pieces leading the attack must have been moved by the attack command. \n 2) 0, 1, or 2 pieces can be leading the attack if the attack approach is wide. \n 3) 0 or 1 pieces can be leading the attack if the attack approach is narrow. \n 4) Pieces leading the attack must all be of the same kind. \n 5) Cavalry cannot lead the attack if the attack approach is obstructed and artillery cannot lead attacks across the same attack approach on consecutive turns unless the attack locale is a hill and the defense locale is not.'

defense_declaration = '4) The defending player names which of his defending pieces will be leading the defense and turns them face up. \n 1) The pieces leading the defense must have been named as defending pieces in step 2. \n 2) 0, 1, or 2 pieces can be leading the defense if the defense approach is wide. \n 3) 0 or 1 pieces can be leading the defense if the defense approach is narrow. \n 4) Reserve pieces leading the defense must all be of the same kind from the same corps. \n 5) The defending player cannot lead the defense with cavalry if the defense approach is obstructed, with artillery from reserve, or with a strength one piece.'

counter_attack = '7) The defending player may name pieces for a counter-attack and turn them face up. Each counter-attacking piece must take an immediate one step loss. \n 1) The pieces must have been named as defending pieces and must not have been named as pieces leading the defense. \n 2) 1 or 2 pieces can be named to counter-attack. \n 3) 2 pieces can only be named if they are of the same type and from the same corps. \n 4) If the attacking player won the initial result then infantry or cavalry may be named to counter-attack. \n 5) If the defending player won the initial result then only cavalry may be named to counterattack.'

attacker_casualty = 'Apply losses to attacking pieces leading the attack first. If all attacking pieces leading the attack are eliminated apply the remaining hits to any remaining attacking pieces.'

defender_casualty = 'Apply losses to defending pieces leading the defense first. If all defending pieces leading the defense are eliminated apply the remaining hits to any remaining counterattacking pieces. If all defending pieces leading the defense and all counterattacking pieces are eliminated apply the remaining hits to any remaining defending pieces.'

go = 'yes'
while go == 'yes':
	try:	
		print(intro)
		cont = raw_input('press return to continue...')
		console.clear()

		retreat = 'no'
		feint = 'no'
		cont = 'yes'
		attacking_units = 0
		defending_units = 0
		leading_attack_units = 0
		leading_defend_units = 0
		obstructed = 'no'
		penalty_cavalry = 'no'
		penalty_infantry = 'no'
		penalty_artillery = 'no'
		approach_blocked = 'no'
		attacker_French = 'yes'
		winner = 'attacker'
		modifier = 0
		combat_result = 0
		attackers = {'cavalry': 0, 'infantry': 0, 'artillery': 0}
		defenders = {'cavalry': 0, 'infantry': 0, 'artillery': 0}
		defenders_counterattack = {'cavalry': 0, 'infantry': 0}

		print('1) Attacker names the attack approach but does not indicate what units are attacking.')
		obstructed = raw_input('Is the approach obstructed (yes or no)? ')
		penalty_cavalry = raw_input('Is there a penalty to cavalry attacks into this locale (yes or no)? ')
		penalty_infantry = raw_input('Is there a penalty to infantry attacks into this locale (yes or no)? ')
		penalty_artillery = raw_input('Is there a penalty to artillery attacks into this locale (yes or no)? ')
		cont = raw_input('press return to continue...')
		console.clear()

		retreat = raw_input(' 2) Defender chooses to either retreat or defend.  Note that if the defender has pieces blocking the attack approach he cannot retreat.  Do you want to retreat (yes or no)? ')
		console.clear()

		if retreat == 'yes':
			print(retreat_text)
			cont = raw_input('press return to continue...')
			console.clear()
		else:
			print(defend_text)
			defending_units = int(raw_input('How many units have been named as defending units? '))
			approach_blocked = raw_input('Do the defending units block the approach (yes or no)? ')
			#cont = raw_input('press return to continue...')
			console.clear()
	
			feint = raw_input('3) The attacker decides whether or not the attack is a feint. Do you want the attack to be a feint (yes or no)? ')
			console.clear()
	
			if feint == 'yes':
				print(attack_declaration_feint)
				cont = raw_input('press return to continue...')
				console.clear()
			else:
				print(defense_declaration)
				leading_defend_units = int(raw_input('Defender, how any units lead the defense?'))
				defenders['cavalry'] = int(raw_input('Defender, how much cavalry strength is in the units leading the defense? '))
				defenders['infantry'] = int(raw_input('Defender, how much infantry strength is in the units leading the defense? '))
				defenders['artillery'] = int(raw_input('Defender, how much artillery strength is in the units leading the defense? '))
				console.clear()
		
				print(attack_declaration_nofeint)
				attacking_units = int(raw_input('How many units have been named as attacking units?'))
				leading_attack_units = int(raw_input('Attacker, how many units lead the attack?'))
				attackers['cavalry'] = int(raw_input('Attacker, how much cavalry strength is in the units leading the attack? '))
				attackers['infantry'] = int(raw_input('Attacker, how much infantry strength is in the units leading the attack? '))
				attackers['artillery'] = int(raw_input('Attacker, how much artillery strength is in the units leading the attack? '))
				console.clear()
		
				attacker_French = raw_input('Is the attacker French (yes or no)?')
				console.clear()
		
				if attackers['infantry'] > 0 and approach_blocked == 'yes':
					modifier = modifier - 1
				if (attackers['infantry'] > 0 and penalty_infantry == 'yes') or (attackers['cavalry'] > 0 and penalty_cavalry == 'yes') or (attackers['artillery'] > 0 and penalty_artillery == 'yes'):
					modifier = modifier - 1
				if attackers['cavalry'] > 0 or attackers['infantry'] > 0:
					result = (attackers['cavalry'] + attackers['infantry'] + attackers['artillery']) - (defenders['cavalry'] + defenders['infantry'] + defenders['artillery']) + modifier
				else:
					result = attackers['artillery'] + modifier
			
				if result > 0 and attackers['artillery'] == 0:
					winner = 'attacker'
					print('6) The attacker has the advantage and will win unless circumstances change.')
				if result < 0 and attackers['artillery'] == 0:
					winner = 'defender'
					print('6) The defender has the advantage and will win. It only remains to determine by how much.')
				if result == 0 and attackers['artillery'] == 0:
					if approach_blocked == 'yes':
						winner = 'defender'
						print('6) The defender has the advantage and will win. It only remains to determine by how much.')
					else:
						if attacking_units > defending_units:
							winner = 'attacker'
							print('6) The attacker has the advantage and will win unless circumstances change.')
						if attacking_units < defending_units:
							winner = 'defender'
							print('6) The defender has the advantage and will win. It only remains to determine by how much.')
						if attacking_units == defending_units:
							if attacker_French == 'yes':
								winner = 'attacker'
								print('6) The attacker has the advantage.')
							if attacker_French != 'yes':
								winner = 'defender'
								print('6) The defender has the advantage and will win. It only remains to determine by how much.')
				cont = raw_input('press return to continue...')
				console.clear()
				if attackers['artillery'] == 0:
					print(counter_attack)
					defenders_counterattack['cavalry'] = int(raw_input('Defender, how much cavalry strength is in the counterattacking units? '))
					defenders_counterattack['infantry'] = int(raw_input('Defender, how much infantry strength is in the counterattacking units? '))
			
					result = result - defenders_counterattack['cavalry'] - defenders_counterattack['infantry']
					if result > 0:
						winner = 'attacker'
						print('8) The attacker has won.')
					if result < 0:
						winner = 'defender'
						print('8) The defender has won.')
					if result == 0 and attackers['artillery'] == 0:
						if approach_blocked == 'yes':
							winner = '8) defender'
							print('The defender has won.')
						else:
							if attacking_units > defending_units:
								winner = '8) attacker'
								print('The attacker has won.')
							if attacking_units < defending_units:
								winner = 'defender'
								print('8) The defender has won.')
							if attacking_units == defending_units:
								if attacker_French == 'yes':
									winner = 'attacker'
									print('8) The attacker has won.')
								if attacker_French != 'yes':
									winner = 'defender'
									print('8) The defender has won.')
			
				if attackers['artillery'] > 0:
					winner = 'attacker'
					attacker_losses = 0
					print('8) This is artillery bombardment; the attacker has won.')
				cont = raw_input('press return to continue...')
				console.clear()
				if attackers['artillery'] == 0:
					attacker_losses = leading_defend_units - min(0,result)
				defender_losses = leading_attack_units + max(result,0) - max(min(attackers['cavalry'] + attackers['infantry'],1),0)*defenders['artillery']
		
				print(['The attacker loses: ',attacker_losses])
				print(attacker_casualty)
				print(['The defender loses: ',defender_losses])
				print(defender_casualty)
				cont = raw_input('press return to continue...')
				console.clear()
		
				if attackers['artillery'] > 0:
					print('Because this was an artillery bombardment all pieces remain in place.')
				if attackers['artillery'] == 0 and winner == 'attacker':
					print('All of the defending players pieces in the locale must retreat. Attacking pieces move into the reserve of the locale they attacked.')
					print(retreat_text)
				if attackers['artillery'] == 0 and winner == 'defender':
					print('Attacking pieces must withdraw into the reserve of the locale that they attacked from. All attacking pieces are detached from their corps. If the defending pieces are in reserve the defending player may advance any or all of his named defending units to block the defense approach. He must advance at least one (it becomes detached from its corps).')
				cont = raw_input('press return to continue...')
				console.clear()
	except:
		print('Uh oh - something went wrong; lets start over.')
		cont = raw_input('press return to continue...')
		console.clear()
