import random



from ..models import Card

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class LayoutGenerator:
    birthday_message = [
        "Another adventure filled year awaits you. Welcome it by celebrating your birthday with pomp and splendor. Wishing you a very happy and fun-filled birthday!",
        "Happy birthday! Your life is just about to pick up speed and blast off into the stratosphere. Wear a seat belt and be sure to enjoy the journey. Happy birthday!",
        "This birthday, I wish you abundant happiness and love. May all your dreams turn into reality and may lady luck visit your home today. Happy birthday to one of the sweetest people I’ve ever known"
    ]
    getwellsoon_message = [
        "Get Whale Soon – It makes a BIG difference when you’re missing!",
        "Thinking of you and wishing and wishing and wishing you well",
        "I want you to be happy and healthy again. Take care of yourself and get well"
    ]
    missing_you_message = [
        "There is an ocean of distance between us… and I am drowning in it",
        "That’s the worst way to miss somebody. When they’re right beside you and you miss them anyway",
        "It’s difficult for me to imagine the rest of my life without you. But I suppose I don’t have to imagine it... I just have to live it"
    ]

    def __init__(self):
        pass

    # def generate_layout(self, cardType, layout_type=1):
    #     # This will generate layout with the html tags -> for Future Update
    #     # if layout_type == 1:
    #     #     return [name, self.__generate_message(cardType), self.__fetch_svg(image_name)]
    #     return self.__generate_message(cardType)
        

    def generate_message(self, cardType):
        message = ""
        random_number = random.randint(0, 2)
        print(random_number, '\n\n\n')
        if cardType == "birthday":
            message = self.birthday_message[random_number]

        elif cardType == "get_well_soon":
            message = self.getwellsoon_message[random_number]
        
        elif cardType == "missing_you":
            message = self.missing_you_message[random_number]


        return message

    def fetch_svg(self, image_name):
        full_path = f"{BASE_DIR}/staticfiles/cards/assest/{image_name}.svg"
        with open(full_path, "r") as f:
            svg_image = f.read()

        return svg_image