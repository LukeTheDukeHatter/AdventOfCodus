from os.path import exists

Cookie = '53616c7465645f5f5bc76fab5147e1e74387071c7afe00854c286d5d7fc448541a85142c0eb9e0887ba5c9b4ce2c91311d138d7f8e0b6d8fa930860b4dc66c00'
CookieDic = {
        'session':Cookie
    }
AGENT_DATA = {"User-Agent": "advent-of-code-automaton"}

def HandleLocalData(filename):
    with open(f"./Inputs/{filename}.txt") as file:
        tl=file.readlines()
        input=[]
        for l in tl:
            input.append(l.strip())
        return input

def FetchData(day, year):
    import requests
    filename = f"d{day}y{year}.txt"
    output = []

    if exists('./inputs/'+filename):
        for l in open('./inputs/'+filename,'r').read().split('\n'):
            output.append(l.strip())
    else:
        response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=CookieDic)
        content = response.content.decode('latin')
        with open('./inputs/'+filename,'w') as f:
            f.write(content)

        for l in content.split('\n'):
            output.append(l.strip())

    if len(output)>1:
        output.pop()
    return output

def Submit(answer, part, day, year):
    import requests

    response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers=AGENT_DATA, cookies=CookieDic, data={"level":part,"answer":answer})
    if "That's not the right answer" in response.text:
        print("Incorrect, your answer was too {}".format(response.text.split("your answer is too ")[1].split(".  If you're stuck")[0]))
        return False
    elif "You gave an answer too recently" in response.text:
        print("You've Been Rate Limited -_-")
        return False
    elif response.status_code != 200:
        print("There was an error sending your request, status code {} was recieved".format(str(response.status_code)))
    else:
        print("Your answer was correct, well done!")
        return True

class AdventOfCode:
    def __init__(self, day, year):
        self.day = day
        self.year = year
        self.filename = f"d{day}y{year}.txt"
        

    def submit(self, part, answer): Submit(answer, part, self.day, self.year)