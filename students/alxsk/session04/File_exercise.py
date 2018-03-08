'''
Read file exercise
A script that reads students.txt and generates a list of the languages students know. 

'''

languages=set()

with open('students.txt', 'r') as file_name:
    
    for line in file_name:
        line_split = line.split(":") #creates list
        keep_lang=line_split.pop() # removes and returns last item in the list
        langs=keep_lang.split(",") # splitting string

        for lang in langs: # loop through each string and clean up whitespace
            strip_lang= lang.strip()

            if strip_lang and not strip_lang[0].isupper(): # Check if first letter isn't uppercase and empty string
                languages.add(strip_lang)

print(languages)

            




        
        
      
            

