# encryption-decryption-algorithms
Learning and playing around with encryption/decryption algorithms


Caeser Cipher:
Simple algorithm that simply shifts the letters used in the alphabet by 4. 
Ex: ABCD -> EFGH
Edge Cases: In the case of letters like x, y, and z - the algorithm simply goes back to the beginning of the alphabet when ecrypting.
Ex: Z -> D

AES (Advanced Encryption Standard):
Uses a 16 byte(128-bit) randomized key to scramble and randomize your message. This is useful as anyone who doesn't have the key cannot decrypt the message. Depending on the key size (in our case, 128-bits), the proccess of swapping, substituting, and mixing the bits happens a matter of times. As long as the key remains strong and complicated, the AES encryption algorithm remains very difficult to crack.
