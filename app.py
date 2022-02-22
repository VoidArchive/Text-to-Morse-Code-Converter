import data


print("""___________              __      __              _____                                                .___      
\__    ___/___ ___  ____/  |_  _/  |_  ____     /     \   ___________  ______ ____     ____  ____   __| _/____  
  |    |_/ __ \\  \/  /\   __\ \   __\/  _ \   /  \ /  \ /  _ \_  __ \/  ___// __ \  _/ ___\/  _ \ / __ |/ __ \ 
  |    |\  ___/ >    <  |  |    |  | (  <_> ) /    Y    (  <_> )  | \/\___ \\  ___/  \  \__(  <_> ) /_/ \  ___/ 
  |____| \___  >__/\_ \ |__|    |__|  \____/  \____|__  /\____/|__|  /____  >\___  >  \___  >____/\____ |\___  >
             \/      \/                               \/                  \/     \/       \/           \/    \/ """)

user_input = input("Write down the text you want to convert: ").lower().split()

def convert_to_morse(text):
    morse_code = ""
    for word in text:
        for character in word:
            morse_code += data.morse_code[character] + " "
    
    return morse_code


user_output = convert_to_morse(user_input)
print(f"The morse code for {user_input} is {user_output}")

#TODO make the morse code in sound 