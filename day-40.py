# # Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# # Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# ## Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
import  random
import string

def encode_word(word):
     """Encodes a single word into secret code"""
     if len(word)<=3:
          # 1️⃣ remove first letter & append at end
          new_word= word[1:]+word[0]

          # 2️⃣ add 3 random characters at start and end
          prefix=''.join(random.choices(string.ascii_lowercase,k=3))
          suffix = ''.join(random.choices(string.ascii_lowercase, k=3))
          code_word=prefix+new_word+suffix
          return code_word
     else:
                      # If word < 3 → just reverse it
        return word[::-1]


def decode_word(word):
    """Decodes a single word"""
    if len(word) < 3:
        # reverse short word
        return word[::-1]
    else:
        # remove 3 random letters from start & end
        core = word[3:-3]
        # last letter to beginning
        decoded = core[:-1] + core[:-1]
        return decoded







# main program 

choice =input("Enter 'E' to encode or'D' to decode : ").strip().upper()
message =input("enter your input: ")

words= message.split()
translateword= []
if choice== 'E':
    for w in words:
        translateword.append(encode_word(w))
    print("\n🔐 Encoded Message:")
    print(' '.join(translateword))

elif choice == 'D':
    for w in words:
        translateword.append(decode_word(w))
    print("\n🔓 Decoded Message:")
    print(' '.join(translateword))

else:
    print("❌ Invalid choice! Please enter E or D.")

print(type(translateword))