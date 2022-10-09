import os


class Menu:

    def __init__(self, name, logo):
        self.width, self.length = os.get_terminal_size()

        self.PROGRAMS_PER_ROW = 2
        self.SPACES_PER_PROGRAM = 4

        self.name = name
        self.files = self.getFiles()
        self.menu = self.indentLogo(logo) + "\n\n"

    def getAverageLength(self, string):
        avg = 0
        count = 0
        for line in string.split("\n"):
            if len(line) != 0:
                avg += len(line)
                count += 1

        return int(avg/count)

    def indentLogo(self, logo):
        width = self.width - self.getAverageLength(logo)
        newLogo = ""
        spaces = " "*int(width/2)
        for i in logo.split("\n"):
            newLogo += f"{spaces}{i}\n"

        return newLogo

    def getFiles(self):
        files = [[]]
        row = 0
        for file in os.listdir(f"results/{self.name}/tools"):
            if len(files[row]) == self.PROGRAMS_PER_ROW:
                row += 1
                files.append([])

            files[row].append(file.replace(".py", ""))

        return files

    def parseFileName(self, name):
        author = name.split("-")[0]
        tool = name.replace(f"{author}-", "")
        tool = tool.replace("-", " ")
        return author, tool

    def build(self):
        tools = []
        programCount = len(self.files)
        lines = programCount/self.PROGRAMS_PER_ROW
        if lines < 1:
            lines = 1

        count = 1
        for i in range(programCount):
            for program in self.files[i]:
                if program != "__pycache__":
                    author, name = self.parseFileName(program)
                    self.menu += f"[{count}] {name}    "
                    tools.append({"choice": count, "file": program})
                    count += 1
            self.menu += "\n"
        return self.menu, tools
