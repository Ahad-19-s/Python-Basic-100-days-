import win32com.client

# speaker object তৈরি করা হলো
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# নামের list
l = ["sabina", "ma", "vaia"]

# প্রত্যেক নামের জন্য "Shoutout to ..." বলবে
for name in l:
    text = f"i love you {name}"
    print(text)       # স্ক্রিনে প্রিন্টও করবে
    speaker.Speak(text)
