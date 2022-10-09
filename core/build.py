

class Build:
    
    def __init__(self, name, menu):
        self.name = name
        self.menu, self.tools = menu
        self.code = ""
        
    def menuCode(self):
        self.code += f"""
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    

finished = False
tools = {self.tools}
finshed = False
menu = '''{self.menu}'''
while finished == False:
    print(menu)
    choice = input('      > ')
    for i in tools:
        if i['choice'] == int(choice):
            clear()
            print('credit goes to the original creator')
            importName = 'tools.'+i['file']
            __import__(importName)
    
    
"""
        
    def create(self):
        self.menuCode()
        with open(rf"./results/{self.name}/main.py", "w+") as file:
            file.write(self.code)
        
        