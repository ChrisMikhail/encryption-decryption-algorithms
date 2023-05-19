# encryption-decryption-algorithms
Learning and playing around with encryption/decryption algorithms


### Caeser Cipher:
Simple algorithm that simply shifts the letters used in the alphabet by 4. 
Ex: ABCD -> EFGH
Edge Cases: In the case of letters like x, y, and z - the algorithm simply goes back to the beginning of the alphabet when ecrypting.
Ex: Z -> D

### AES (Advanced Encryption Standard):
Uses a 16 byte (128-bit) randomized key to scramble and randomize your message organized into fixed sized blocks of data. This is useful as anyone who doesn't have the key cannot decrypt the message. Depending on the key size (in our case, 128-bits), the proccess of swapping, substituting, permutating and mixing the bits happens a matter of times, knows as rounds. As long as the key remains strong and complicated, the AES encryption algorithm remains very difficult to crack - only those with the key can decrypt your message.

### RSA (Rivest-Shamir-Adleman):
Uses a public key and a private key to allow access to your message. The public key serves as the lock that protects your message that only the private key can unlock (decrypt). When someone wants to send a secure message to another person using RSA, they obtain the recipient's public key. They use this public key to encrypt the message before sending it. Once the message is encrypted, it becomes jumbled and unreadable (as seen in encrypted.message). The encrypted message can then be sent over something like the internet, without worrying about someone intercepting and reading it. Only the person with the corresponding private key can decrypt and read the message. 

### Reference Links:
What is AES encryption and how does it work?: https://cybernews.com/resources/what-is-aes-encryption/ <br>
What is RSA? How does an RSA work?: https://www.encryptionconsulting.com/education-center/what-is-rsa/
