import random
import tkinter

from PIL import Image, ImageTk


class RockPaperScissor:
    def __init__(self) -> None:
        self.all_choices = ['rock', 'paper', 'scissors']
        self.font_button_text = ('Helvetica', 13)
        self.font_text_label = ('MS Serif', 11)
        self.user_interface()

    def user_interface(self):
        self.root = tkinter.Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry('450x300+450+100')
        self.root.title('Rock-Paper-Scissors-Game')

        self.rock_image = tkinter.PhotoImage(file='images/rock.png')
        self.paper_image = tkinter.PhotoImage(file='images/paper.png')
        self.scissors_image = tkinter.PhotoImage(file='images/scissors.png')

        new_size = (450, 200)
        rock_image_pill = Image.open('images/rock.png').resize(new_size)
        paper_image_pill = Image.open('images/paper.png').resize(new_size)
        scissors_image_pill = Image.open('images/scissors.png').resize(new_size)

        self.rock_new_image = ImageTk.PhotoImage(rock_image_pill)
        self.paper_new_image = ImageTk.PhotoImage(paper_image_pill)
        self.scissors_new_image = ImageTk.PhotoImage(scissors_image_pill)

        self.frame_widget()

        self.first_label = tkinter.Label(
            text='Make your move by clicking rock, paper or scissors 👇',
            background='#5AB2FF',
            font=self.font_text_label,
        )
        self.second_label = tkinter.Label(
            text='Computer Chose 👇',
            background='#A0DEFF',
            font=self.font_text_label,
        )
        self.label_image_computer = tkinter.Label(background='white')
        self.label_text_result = tkinter.Label(font=self.font_text_label)

        self.button_widget()
        self.show_widget()

        self.root.mainloop()

    def frame_widget(self):
        self.frame_buttons = tkinter.Frame(bg='cyan')

    def button_widget(self):
        self.rock_button = tkinter.Button(
            master=self.frame_buttons,
            image=self.rock_image,
            height=220,
            command=lambda: self.check_result('rock'),
        )
        self.paper_button = tkinter.Button(
            master=self.frame_buttons,
            image=self.paper_image,
            height=220,
            command=lambda: self.check_result('paper'),
        )
        self.scissors_button = tkinter.Button(
            master=self.frame_buttons,
            image=self.scissors_image,
            height=220,
            command=lambda: self.check_result('scissors'),
        )
        self.restart_button = tkinter.Button(
            text='Restart Game',
            background='#5AB2FF',
            command=self.restart_game,
            font=self.font_button_text,
        )

    def check_result(self, human_choice):
        """
        Rules:
            - Rock beats scissors (by crushing or breaking them).
            - Scissors beat paper (cutting it).
            - Paper beats rock (wrapping it).
        """

        self.human_choice_index = self.all_choices.index(human_choice)
        self.computer_choice = self.all_choices[random.randint(0, len(self.all_choices) - 1)]
        self.computer_choice_index = self.all_choices.index(self.computer_choice)

        if self.human_choice_index == 2 and self.computer_choice_index == 0:
            self.label_text_result['text'], self.label_text_result['background'], = (
                '💔 You lose 💔',
                'red',
            )
        elif self.human_choice_index == 0 and self.computer_choice_index == 2:
            self.label_text_result['text'], self.label_text_result['background'], = (
                '👾🥳 You win 🥳👾',
                'green',
            )
        elif self.human_choice_index > self.computer_choice_index:
            self.label_text_result['text'], self.label_text_result['background'], = (
                '🥳🎉 You win 🥳🎉',
                'green',
            )
        elif self.human_choice_index == self.computer_choice_index:
            self.label_text_result['text'], self.label_text_result['background'], = (
                '🥶 All the same 😝',
                'gray',
            )
        else:
            self.label_text_result['text'], self.label_text_result['background'], = (
                '💔 You lose 💔',
                'red',
            )

        print(self.label_text_result['text'], self.label_text_result['background'])

        self.disable_buttons(human_choice)
        self.show_result()

    def show_result(self):
        all_new_imagem_object = {
            'rock': self.rock_new_image,
            'paper': self.paper_new_image,
            'scissors': self.scissors_new_image,
        }

        self.root.geometry('450x550+450+100')

        self.label_image_computer['image'] = all_new_imagem_object.get(self.computer_choice)
        self.label_image_computer.pack(fill=tkinter.BOTH)
        self.label_text_result.pack(fill=tkinter.BOTH, expand=True)
        self.restart_button.pack(fill=tkinter.BOTH)

    def disable_buttons(self, human_choice: str):
        all_buttons_object = {
            'rock': self.rock_button,
            'paper': self.paper_button,
            'scissors': self.scissors_button,
        }

        for name_button, button in all_buttons_object.items():
            if human_choice != name_button:
                button['state'] = 'disabled'
            else:
                button['command'] = ''

    def restart_game(self):
        self.root.destroy()
        self.user_interface()

    def show_widget(self):
        self.first_label.pack(fill=tkinter.BOTH, expand=True)
        self.frame_buttons.pack(fill=tkinter.X, expand=False)
        self.rock_button.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        self.paper_button.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        self.scissors_button.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
        self.second_label.pack(fill=tkinter.BOTH, expand=True)


start_game = RockPaperScissor()
