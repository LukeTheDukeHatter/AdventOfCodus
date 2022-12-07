from os.path import exists

Cookie = '53616c7465645f5f8a4aa11dc86c69ad218034cde4908cf8fb9a57240654f13d56f66c5502c5fe6d4b3ae807f08a442d51150add75968ee3d79d74d71b25f2ac'
CookieDic = {
        'session':Cookie
    }
AGENT_DATA = {"User-Agent": "advent-of-code-automaton luke.harrison.lh04@gmail.com +44 7392068340"}

def HandleLocalData(filename):
    with open(f"./Inputs/{filename}.txt") as file:
        tl=file.readlines()
        input=[]
        for l in tl:
            input.append(l.strip())
        if len(input) == 1:
            return input[0]
        else:
            return input

def FetchData(day, year):
    import requests
    filename = f"d{day}y{year}.txt"
    output = []

    if exists('./inputs/'+filename):
        with open(f"./inputs/{filename}",'r') as file:
            tl=file.readlines()
            for l in tl:
                output.append(l.strip())
            if len(output) == 1:
                return output[0]
            else:
                return output
    else:
        response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=CookieDic)
        content = response.content.decode('latin')
        with open('./inputs/'+filename,'w') as f:
            f.write(content)

        for l in content.split('\n'):
            output.append(l.strip())

    if len(output)>1:
        output.pop()

    if len(output) == 1:
        return output[0]
    else:
        return output

def Submit(answer, part, day, year):
    import requests

    response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers=AGENT_DATA, cookies=CookieDic, data={"level":part,"answer":answer})
    if "That's not the right answer" in response.text:
        print("Incorrect, your answer was too {}".format(response.text.split("your answer is too ")[1].split(".  If you're stuck")[0]))
        return False
    elif "You gave an answer too recently" in response.text:
        print(f"You've Been Rate Limited -_- ({response.text.split('trying again. You have ')[1].split(' left to wait.')[0]} left)")
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
        self.data = FetchData(day, year)

    def submit(self, part, answer): Submit(answer, part, self.day, self.year)