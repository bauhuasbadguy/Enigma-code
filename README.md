## Enigma code ##

This repo contains my attempt from several years ago to build examples of the various enigma machines used throughout WWII.
I did this because I was curious as to how the enigma machine actually worked and I found building the machine in code helped me gain an intuative understanding of the core principals. 

### IMPORTANT NOTE ###

This code is a very simple enactment of the enigma machines that I wrote as a learning exercise. It should not be used as authoritative a source for how these machines worked since I am just some guy in a room with no special training or expertise in encryption. For proper sources look to the bottom of the page where I have included linkts. If you are looking for a general idea of how one would simulate the enigma machine in code or are struggling to develop an intuition as to the process of enigma encryption/decryption I hope you will find this helpful however.

### Explanation ###

TAKE WITH AN OCEAN OF SALT!!!

The core concept of the enigma machine is that there is a series of rotors. These rotors transfer an input letter to an output letter. As the rotors move the mapping between these letters will change. In the typical example of the enigma machine there are three rotors. When you press a key to input a letter the encrypted letter will light up and the first rotor will rotate one place. Once this first rotor has completed a full rotation of all 26 letters in the alphabet then the next rotor will rotate. This is also true of the second and third rotors meaning the core of the machine works a lot like a watch with second, minute and hour hands. 

At the end of the three rotors is a reflector board with remaps its input similar to the way the rotors remap inputs except that the mirrorboard is fixed. This means that the input letter can never be the same as the output letter but also makes frequency analysis on messages encrypted using this system very difficult since the encryption scheme changes with each character.

In this system the rotors and reflector boards chosen as well as the starting positions of these components constitutes the key for the encryption. 

Since the system is symetrical decryption simply involves reseting the system to its starting conditions and then running the cypher text through to recover the plaintext.

There are three versions of the enigma machine worked through in the file `enigma.py`.

The first is the version of the machine was commercially available before the war and used three rotors and reflector-board in order to produce the cypher text. This machine is refered to in the code as `early_enigmatise`. Here the key is the initial position of the rotors. 

The second machine simulated here is refered to as `high_enigmatise`. This machine contains the first three rotors but adds in a plugboard to add another, static, remapping step to the encryption on the way in and out. Here the key is the initial position of the rotors as well as the connections used on the plugboard. This was the version used by the german military. Here the key also involves the plugboard setup.

 Finally there is the function `late_enigmatise`. This simulates the machine with 4 rotors, a plugboard and the double step mechanism. This version of the machine was used by U-boats from 1942 onwards.

The double step mechanism would cause the machine to take a second step and skip over certain configurations when they were reached in the process of encoding a message. This was done in order to ensure the third rotor only moved forwards once the second rotor completed a full rotation, otherwise the third rotor would move every time the second rotor moved. I don't fully understand the mechanical complexities of this solution but it was fairly simple to include it in code so I added it in.

### Sources ###

* https://en.wikipedia.org/wiki/Enigma_machine
* https://en.wikipedia.org/wiki/Enigma_rotor_details