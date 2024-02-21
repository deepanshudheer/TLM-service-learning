import tkinter as tk
from tkinter import messagebox
import random
import os

# Define the folder path where all images are located
folder_path = "E:/College/Internship and Service Learning/Lower KG School TLM/images/"

# Define a dictionary of images and their corresponding names
images = {
    "cat": "cat.png", 
    "dog": "dog.png", 
    "bear": "bear.png", 
    "bird": "bird.png", 
    "cow": "cow.png", 
    "duck": "duck.png", 
    "fish": "fish.png", 
    "frog": "frog.png",
    "lion": "lion.png", 
    "wolf": "wolf.png"
}

# Concatenate folder path with image filenames
for name, filename in images.items():
    images[name] = os.path.join(folder_path, filename)

# Define a function to check the answer
def check_answer(selected_option):
    global correct_answer
    if selected_option == correct_answer:
        messagebox.showinfo("Correct", "Correct Option!")
        next_image()  # Automatically move to the next question if correct
    else:
        messagebox.showerror("Incorrect", f"Wrong Answer! Correct answer is: {correct_answer}")

# Define a function to display the next image and options
def next_image():
    global correct_answer
    global image_object
    global option_buttons
    
    # Randomly choose an image
    image_name, image_path = random.choice(list(images.items()))
    correct_answer = image_name
    
    # Display the image
    image_object = tk.PhotoImage(file=image_path)
    image_label.config(image=image_object)
    
    # Get all image names except the correct one
    option_names = list(images.keys())
    option_names.remove(correct_answer)
    
    # Randomly select 3 incorrect options
    incorrect_options = random.sample(option_names, 3)
    
    # Add correct answer to options
    options = incorrect_options + [correct_answer]
    random.shuffle(options)
    
    # Update option buttons
    for i in range(4):
        option_buttons[i].config(text=options[i])

# Create the main window
root = tk.Tk()
root.title("Image Guessing Game")

# Create the image label with fixed size
image_label = tk.Label(root)
image_label.pack()

# Create the option buttons
options_frame = tk.Frame(root, width=600, height=100)
options_frame.pack(pady=(0, 10))

# Create option buttons with larger font size
option_buttons = []
for i in range(4):
    option_button = tk.Button(options_frame, text="", font=("Arial", 16), width=15, height=2,
                              command=lambda idx=i: check_answer(option_buttons[idx]["text"]))
    option_button.pack(side=tk.LEFT, padx=10)
    option_buttons.append(option_button)

# Create the next button with larger font size
next_button = tk.Button(root, text="Next Image", font=("Arial", 16), width=15, height=2, command=next_image)
next_button.pack(pady=(0, 10))

# Bind the escape key to close the window
root.bind("<Escape>", lambda event: root.destroy())

# Display the first image and options
next_image()

# Run the Tkinter event loop
root.mainloop()
