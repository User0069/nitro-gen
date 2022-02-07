import random, string
import webbrowser

print(">>> DISCORD NITRO CODE GENERATOR <<< ")
print(">>> NiNj4HAX <<< ")
print(">>> THANK YOU FOR BOOSTING NiNj4HAX <<< \n\n\n")

webbrowser.open('https://www.youtube.com/channel/UC-IjRNqIuG8CxNpjHTJ4BZA?view_as=subscriber')

num=input('Input How Many Codes to Generate: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Generating...")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()
input("\n\nFinished, Press enter to exit. Codes saved in Nitro Codes")
