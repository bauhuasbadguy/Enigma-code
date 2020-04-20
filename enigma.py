#enigma in python
#This code contains functions for all versions of the enigma machine. The rotors
#used are those described at:-
#https://en.wikipedia.org/wiki/Enigma_rotor_details
#If you want to use a different set of rotors go nuts.
#Early enigma (Commercial enigma) is a three rotor system with no plug board
#High enigma (Basic military enigma) is a three rotor system with plug board
#Late enigma (Navy enigma) is a four rotor system with a plug board and a double stepping mechanism



#moves the tumbler positions forwards by one
def moverotors(rotorlocations):
    #works to increment the counter no matter how many
    #tumblers are used for single step machines.

    result = rotorlocations

    result[0] += 1

    i = 0
    increment = False

    while increment == False:


        if result[i] >= 26:

            result[i] = 0

            i += 1

            if i < len(result):

                result[i] += 1

            else:
                increment = True

        else:
            increment = True

            
    return result


def double_step_mechanism(ts, four_rotor_poses):

    #first convert the jump letters to jump numbers
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    jump_nos = []
    for i, letters in enumerate(ts):
        #print letters
        jump_nos.append([])
        
        for let in letters:
            jump_nos[i].append(base.index(let))


    #next go through the rotor positions and see if we need
    #to perform any jumps

    for i in range(len(four_rotor_poses[:-1])):
        loc = four_rotor_poses[i]

        if loc in jump_nos[i]:

            four_rotor_poses[i+1] = (four_rotor_poses[i+1] + 1) % 26


    return four_rotor_poses

#pass a letter through a rotor forwards
def passforwards(letter, rotor, rotorlocation):
    #move a letter forwards through a rotor
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    
    for i, b in enumerate(base):

        if letter == b:
            break

    cypherpos = i + rotorlocation
    if cypherpos >= 26:

        cypherpos = (cypherpos % 26)
        

    return rotor[cypherpos]

#pass a letter through a rotor backwards
def passbackwards(letter, rotor, rotorlocation):
    #move a letter back through a rotor
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i, b in enumerate(rotor):

        if letter == b:
            break
    #subtract the position because we're doing the oposite
    cypherpos = i - rotorlocation


    if cypherpos >= 26:

        cypherpos = (cypherpos % 26)
        


    return base[cypherpos]
#pass the letter through the reflector
def throughreflector(t, reflector):

    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i, b in enumerate(base):

        if t == b:
            break
        
    return reflector[i]
    
#pass a letter through the moving rotors and the reflector
#forwards-reflector-backwards
def moveletterthrough(p, rotors, rotorlocations, reflector):

    t = p
    #move the rotors forwards one


    #pass the letter through the rotors
    for i, loc in enumerate(rotorlocations):
        
        
        t = passforwards(t, rotors[i], rotorlocations[i])



    #'into the reflector'
    t = throughreflector(t, reflector)
    #and back again

    for i, loc in enumerate(rotorlocations):

        t = passbackwards(t, rotors[-(i+1)], rotorlocations[-(i+1)])


    return t



#apply the enigma machine to a message
#uses the same system as the early, commercially sold, enigma system
def early_enigmatise(message, rotor_locations, rotors, reflector):

    cyphertext = ''

    

    for letter in message:

        #move the rotors forwards one place
        rotor_locations = moverotors(rotor_locations)
        


        #move the letter through the moving plates and the reflector
        c = moveletterthrough(letter, rotors, rotor_locations, reflector)

        #add the encrypted letter to the end message
        cyphertext = cyphertext + c

    return cyphertext

#This simulates the plug board used in the military enigmas
def plug_board(p, pb):

    #check to see if the plug board settings are valid
    used = []
    for i, double in enumerate(pb):

        if (double[0] in used) or (double[1] in used):
            raise ValueError('Plug board invalid: You used the same letter twice')
        
        elif (len(double) == 1) or (len(double) > 2):
            raise ValueError('One of your plug board settings has the wrong number\nof letters in.')


        used.append(double[0])
        used.append(double[1])
        

    for i, double in enumerate(pb):

        
        #check if the input is the first letter connected
        #to the plug board. If it is switch it to the second
        if p == double[0]:
            p = double[1]

            break

        #check if the input is the second letter connected
        #to the plug board. If it is switch it to the first
        elif p == double[1]:
            p = double[0]

            break

        
    return p

#simulates the 3 rotor enigma system used by the german army and
#airforce. Used by the navy in the early war.
def early_enigmatise(message, rotor_locations, rotors, reflector):

    cyphertext = ''

    

    for letter in message:

        

        #move the rotors forwards one place
        rotor_locations = moverotors(rotor_locations)
        


        #move the letter through the moving plates and the reflector
        c = moveletterthrough(letter, rotors, rotor_locations, reflector)

        #add the encrypted letter to the end message
        cyphertext = cyphertext + c

    return cyphertext

def high_enigmatise(message, rotor_locations, rotors, reflector, pb):

    cyphertext = ''

    

    for letter in message:

        

        t = plug_board(letter, pb)



        #move the rotors forwards one place
        rotor_locations = moverotors(rotor_locations)
        


        #move the letter through the moving plates and the reflector
        c = moveletterthrough(t, rotors, rotor_locations, reflector)


        c = plug_board(c, pb)


        
        #add the encrypted letter to the end message
        cyphertext = cyphertext + c

    return cyphertext


def late_enigmatise(message, rotor_locations, rotors, reflector, pb, ts):

    cyphertext = ''

    

    for letter in message:

        

        t = plug_board(letter, pb)



        #move the rotors forwards one place
        rotor_locations = moverotors(rotor_locations)
        
        #apply the double step mechanism
        rotor_locations = double_step_mechanism(ts, rotor_locations)


        #move the letter through the moving plates and the reflector
        c = moveletterthrough(t, rotors, rotor_locations, reflector)


        c = plug_board(c, pb)


        
        #add the encrypted letter to the end message
        cyphertext = cyphertext + c

    return cyphertext

####################################
######## End of Functions ##########
####################################
#Rotor details taken from the wikipeia article even if they are historically
#inacurate the nature of enigma means that they should all work
#https://en.wikipedia.org/wiki/Enigma_rotor_details


rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
rotor4 = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
rotor5 = 'VZBRGITYUPSDNHLXAWMJQOFECK'
rotor6 = 'JPGVOUMFYQBENHZRDKASXLICTW'
rotor7 = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
rotor8 = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'
ReflectorA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
ReflectorB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
ReflectorC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'


#The thin rotors used in the navy 4 rotor enigma system
beta = 'LEYJVCNIXWPBQMDRTAKZGFUHOS'
gamma = 'FSOKANUERHMBTIYCWLQPZXVGJD'

#the thin reflectors are for the 4 rotor machines
#they were made thin to allow for an extra moving rotor
ReflectorBthin = 'ENKQAUYWJICOPBLMDXZVFTHRGS'
ReflectorCthin = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'

#These turnover positions are used in the double step mechanisms
#I'm using:-
#https://en.wikipedia.org/wiki/Enigma_rotor_details

rotor1turns = 'R'
rotor2turns = 'F'
rotor3turns = 'W'
rotor4turns = 'K'
rotor5turns = 'A'
rotor6turns = 'AN'
rotor7turns = 'AN'
rotor8turns = 'AN'

ts = [rotor8turns, rotor7turns, rotor5turns]

#The plug board had ten wires for connecting
pb = []
pb.append('AB')
pb.append('CD')
pb.append('EF')
pb.append('GH')
pb.append('IJ')
pb.append('KL')
pb.append('MN')
pb.append('OP')
pb.append('QR')
pb.append('ST')

p = 'N'
p = plug_board(p, pb)
print p


#choose your rotors. If your using the navy four rotor
#system then the first rotors need to be beta or gamma
#for historical accuracy
rotors = [rotor1, rotor2, rotor3]
four_rotors = [rotor8, rotor3, rotor5, beta]

#choose your reflector rotor
reflector = ReflectorA



#set the starting locations using a tupple so that
#it does'nt change because of pointer problems
start_rotor_locations = (4, 8, 7)


plaintext = 'HELLOTHERE'

print '======================='
print '===Commercial enigma==='
print '======================='
#This had 3 rotors, a reflector and no plug board.
#You could choose the starting rotor positions as
#your key

#encrypt the plain text
rotor_locations = list(start_rotor_locations)
cyphertext = early_enigmatise(plaintext, rotor_locations, rotors, reflector)

print cyphertext

#decrypt the plain text
rotor_locations = list(start_rotor_locations)
decrypted = early_enigmatise(cyphertext, rotor_locations, rotors, reflector)
    
print decrypted
print '======================='
print '=Basic military enigma='
print '======================='
#This had 3 rotors and a plug board. Your key
#would be the rotor positions and which letters
#were wired to which. There were 10 wires


rotor_locations = list(start_rotor_locations)

cyphertext = high_enigmatise(plaintext, rotor_locations, rotors, reflector, pb)


print cyphertext


rotor_locations = list(start_rotor_locations)

decrypted = high_enigmatise(cyphertext, rotor_locations, rotors, reflector, pb)


print decrypted
print '======================='
print '======Navy enigma======'
print '======================='
#This machine had 4 rotors, a plug board and the
#notorious double step mechanism. When the rotors
#moved to a specific step then they would cause the
#next rotor to step as well
#set the starting locations for the rotors
four_rotor_starting_locs = (13, 25, 5, 12)

#set the rotors and the assosiated double step locations
rotors = [rotor8, rotor7, rotor5, beta]
ts = [rotor8turns, rotor7turns, rotor5turns]



rotor_locations = list(four_rotor_starting_locs)

cyphertext = late_enigmatise(plaintext, rotor_locations, rotors, reflector, pb, ts)


print cyphertext


rotor_locations = list(four_rotor_starting_locs)

decrypted = late_enigmatise(cyphertext, rotor_locations, rotors, reflector, pb, ts)

print decrypted







