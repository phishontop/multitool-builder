import core


logo = """
████████╗███████╗███████╗████████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
   ██║   █████╗  ███████╗   ██║   
   ██║   ██╔══╝  ╚════██║   ██║   
   ██║   ███████╗███████║   ██║   
   ╚═╝   ╚══════╝╚══════╝   ╚═╝                                 
"""


github = core.Github(
    name="test",
    repos=[
        "https://github.com/blob0005/Webhook-Spammer", #this won't be added the user is a skid
        "https://github.com/KMKINGMAN/Discord-WebHook-Spammer",
        "https://github.com/blob0005/Roblox-Username-Sniper", #this won't be added the user is a skid
        "https://github.com/FederalCodes/Discord-Account-Creator"
    ]
)

github.saveCode()

menu = core.Menu(
    logo=logo,
    name="test"  
)

display = menu.build()

builder = core.Build(
    name="test",
    menu=display
)

builder.create()


