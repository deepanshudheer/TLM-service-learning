import tkinter as tk
import os
import random
from PIL import Image, ImageTk

def create_module_d():
    root = tk.Tk()
    root.title("Word Rearrangement Game")
    root.geometry("800x600")
    root.configure(background="#F0F0F0")  # Soft color background
    
    score = 0
    question_counter = 0
    custom_font = ("Helvetica", 18)  # Custom font and size
    unscrambled_word = ""  # Define unscrambled_word variable
    
    def next_question():
        nonlocal question_counter, unscrambled_word  # Reference unscrambled_word variable
        question_counter += 1
        if question_counter <= 15:
            answer_entry.delete(0, tk.END)
            remove_image()  # Remove the image from the previous question
            word = random.choice(words)
            scrambled_word = scramble_word(word)
            unscrambled_word = word  # Assign value to unscrambled_word
            word_label.config(text="Unscramble the word: " + scrambled_word)
            reset_word_background()  # Reset the background color
        else:
            show_score()

    def check_answer():
        nonlocal score
        guess = answer_entry.get()
        if guess == unscrambled_word:
            score += 1
            result_label.config(text="Correct!", fg="green")
            word_label.config(bg="lightgreen")  # Change background color on correct answer
            load_image(unscrambled_word)
            root.after(2000, remove_image_after_delay)  # Remove image after 2 seconds
            root.after(500, reset_word_background)
        else:
            result_label.config(text=f"Incorrect. The correct word was: {unscrambled_word}", fg="red")
        root.after(1000, clear_result)
        root.after(1000, next_question)

    def clear_result():
        result_label.config(text="")

    def show_score():
        word_label.config(text=f"Game Over! Your score is: {score}")

    def reset_word_background():
        word_label.config(bg="#F0F0F0")  # Reset background color

    def exit_app():
        root.destroy()

    def load_image(word):
        image_path = os.path.join(image_directory, f"{word}.png")
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                resized_image = image.resize((100, 100), Image.LANCZOS)  # Resize image to 100x100 using LANCZOS
                photo_image = ImageTk.PhotoImage(resized_image)
                image_label.config(image=photo_image)
                image_label.image = photo_image
            except Exception as e:
                print(f"Failed to load and resize image: {e}")
        else:
            print(f"Image not found: {image_path}")

    def remove_image():
        image_label.config(image=None)

    def remove_image_after_delay():
        remove_image()

    # Global variables
    words = ['cat', 'dog', 'bird', 'fish', 'frog', 'duck', 'bear', 'lion', 'wolf', 'cow']
    image_directory = "D:/Coding/ServiceLearning/TLM_menu/images"  # Directory where the images are stored

    def scramble_word(word):
        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)

    # Widgets
    word_label = tk.Label(root, text="", bg="#F0F0F0", font=custom_font, anchor="center")
    word_label.pack()

    answer_entry = tk.Entry(root, font=custom_font)
    answer_entry.pack(pady=10)
    answer_entry.bind("<Return>", lambda event: check_answer())  # Bind Enter key to submit answer

    submit_button = tk.Button(root, text="Submit", command=check_answer, padx=20)
    submit_button.pack(pady=5)

    result_label = tk.Label(root, text="", bg="#F0F0F0", font=custom_font, anchor="center")
    result_label.pack()

    image_label = tk.Label(root, bg="#F0F0F0")  # Label for displaying image
    image_label.pack()

    next_question()

    root.bind("<Escape>", lambda event: exit_app())  # Bind Escape key to exit application

    root.mainloop()

if __name__ == "__main__":
    create_module_d()
