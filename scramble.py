import tkinter as tk
import os
import random
from PIL import Image, ImageTk

words = ['cat', 'dog', 'bird', 'fish', 'frog', 'duck', 'bear', 'lion', 'wolf', 'cow']

image_directory = "E:\College\Internship and Service Learning\Lower KG School TLM\images"  # Directory where the images are stored


def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

class WordGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Rearrangement Game")
        self.geometry("600x500")
        self.configure(background="#F0F0F0")  # Soft color background
        
        self.score = 0
        self.question_counter = 0
        
        self.custom_font = ("Helvetica", 12)  # Custom font and size
        
        self.word_label = tk.Label(self, text="", bg="#F0F0F0", font=self.custom_font, anchor="center")
        self.word_label.pack()
        
        self.answer_entry = tk.Entry(self, font=self.custom_font)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())  # Bind Enter key to submit answer
        
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer, padx=10)
        self.submit_button.pack(pady=5)
        
        self.result_label = tk.Label(self, text="", bg="#F0F0F0", font=self.custom_font, anchor="center")
        self.result_label.pack()
        
        self.image_label = tk.Label(self, bg="#F0F0F0")  # Label for displaying image
        self.image_label.pack()
        
        self.next_question()
        
        self.bind("<Escape>", lambda event: self.exit_app())  # Bind Escape key to exit application
        
    def next_question(self):
        self.question_counter += 1
        if self.question_counter <= 15:
            self.answer_entry.delete(0, tk.END)
            self.remove_image()  # Remove the image from the previous question
            word = random.choice(words)
            scrambled_word = scramble_word(word)
            self.unscrambled_word = word
            self.word_label.config(text="Unscramble the word: " + scrambled_word)
            self.reset_word_background()  # Reset the background color
        else:
            self.show_score()
        
    def check_answer(self):
        guess = self.answer_entry.get()
        if guess == self.unscrambled_word:
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
            self.word_label.config(bg="lightgreen")  # Change background color on correct answer
            self.load_image(self.unscrambled_word)
            self.after(2000, self.remove_image_after_delay)  # Remove image after 2 seconds
            self.after(500, self.reset_word_background)
        else:
            self.result_label.config(text=f"Incorrect. The correct word was: {self.unscrambled_word}", fg="red")
        self.after(1000, self.clear_result)
        self.after(1000, self.next_question)
        
    def clear_result(self):
        self.result_label.config(text="")
        
    def show_score(self):
        self.word_label.config(text=f"Game Over! Your score is: {self.score}")
        
    def reset_word_background(self):
        self.word_label.config(bg="#F0F0F0")  # Reset background color
        
    def exit_app(self):
        self.destroy()
        
    def load_image(self, word):
        image_path = os.path.join(image_directory, f"{word}.png")
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                resized_image = image.resize((100, 100), Image.LANCZOS)  # Resize image to 100x100 using LANCZOS
                photo_image = ImageTk.PhotoImage(resized_image)
                self.image_label.config(image=photo_image)
                self.image_label.image = photo_image
            except Exception as e:
                print(f"Failed to load and resize image: {e}")
        else:
            print(f"Image not found: {image_path}")
            
    def remove_image(self):
        self.image_label.config(image=None)

    def remove_image_after_delay(self):
        self.remove_image()

if __name__ == "__main__":
    app = WordGameApp()
    app.mainloop()
