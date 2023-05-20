# Encryption
Program that encrypts and deciphers the given text.
This program can encrypt and decrypt the code it makes. In order to encrypt the text, you need to enter it in a large field and click the Encrypt button. Subsequently, a digital code will appear on the text field, which is the encrypted text, and in the field below, next to the inscription "Password:", a set of letters and characters will appear that will need to be saved, because without them it will not be possible to decrypt the text.
To decrypt, you need to enter the digital code in the large field and the password in the "Password:" field and click on the "Decipher:" button

How the programm works:
It first creates a string full of password elements and then creates a list containing the sum of the parallel element codes from the password and text strings. Then the program divides this list into several blocks and changes their position, so that at the end we get the encoded text, where all the elements are replaced by different character codes and, in addition, the letters change their position
