## MyPassword

### Video Demonstration: https://youtu.be/xx3A6DbxePU

### Description:

MyPassword is a password generator that will generate a password for its user given certain specifics input by the user such as length, and inclusion of numbers and punctuations. MyPassword would then generate a random password and give the user the option to save that password in a separate file. If the user decides to save, the password hash is then saved in a separate file for later verification.

---
### Functions

#### Create
+ Randomly generate a password within 8 - 64 characters in length
+ Flexibility to choose length, inclusion of digits, and inclusion of punctuations

#### Save
+ Creates a hash value of that password and saves it in an external file for later verification/retrieval

#### Retrieve
+ Generates an encoded code that is saved in a separate file. If you forget your password, this code can be used to compare the hash values of the decoded code, and retrieve your password.

#### Verify
+ Able to compare your password to its saved hash values and let the user know whether or not this password is in use, and what it belongs to.

---
## About
This project was created in order to test various python skills. Included in the code are the following practices:
+ Use of multiple functions
+ Use of encoding and decoding user inputs and randomly generated characters using the string and random library.
+ Practice with the use of SHA-256 algorithm to create hash values from randomly generated passwords. Use of hashlib library
+ Reading and Writing to multiple csv files

In the process of writing this program, I wanted to really focus on providing examples that proves I can work with reading and writing to csv files, as well as handling encoding text and working with multiple functions at once. I've designed this in a way that can make it easy to add on different functions to this program if I decided to add extra security to this, such as adding a master password to access files.

For the purposes of this project, the hash passwords and code are saved to documents that can be easily accessed by anyone, in order to run proper testing. This specific project is not meant to be used in real life scenarios. It is meant to demonstrate my understanding of basic functions and use of retrieving and verifying password and sensitive materials.