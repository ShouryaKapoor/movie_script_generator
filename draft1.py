import os
import google.generativeai as genai
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

def generate_script():
    genre = genre_entry.get()
    characters = characters_entry.get()
    scene_description = scene_desc_entry.get()

    if not genre or not characters or not scene_description:
        messagebox.showwarning("Input Error", "Please fill in all the fields.")
        return

    try:
        # Configure the model
        genai.configure(api_key="AIzaSyBtYB7Da8VNN8paGnsA2fSNx69UqYfTXao")
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
        )

        prompt = f"Generate a movie script: Genre: {genre}, Characters: {characters}, Scene Description: {scene_description}"
        response = model.generate_content(prompt, stream=True)

        output_text.delete("1.0", tk.END)
        for chunk in response:
            output_text.insert(tk.END, chunk.text)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main GUI window
root = tk.Tk()
root.title("Movie Script Generator")
root.geometry("700x700")
# You can replace the background color with an image by adding:
bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
#root.configure(bg="#2c3e50")

# Configure grid weights to centralize content
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Header Label
header_label = tk.Label(root, text="Movie Script Generator", font=("Helvetica", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Subheading
subheading_label = tk.Label(root, text="A Gen-AI powered platform for movie script generation", font=("Helvetica", 14, "italic"), fg="#bdc3c7", bg="#2c3e50")
subheading_label.grid(row=1, column=0, columnspan=2, pady=5)

# Genre Input
ttk.Label(root, text="Genre:", font=("Helvetica", 12), background="#2c3e50", foreground="#ecf0f1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
genre_entry = ttk.Entry(root, width=50)
genre_entry.grid(row=2, column=1, padx=10, pady=5)

# Characters Input
ttk.Label(root, text="Characters:", font=("Helvetica", 12), background="#2c3e50", foreground="#ecf0f1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
characters_entry = ttk.Entry(root, width=50)
characters_entry.grid(row=3, column=1, padx=10, pady=5)

# Scene Description Input
ttk.Label(root, text="Scene Description:", font=("Helvetica", 12), background="#2c3e50", foreground="#ecf0f1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
scene_desc_entry = ttk.Entry(root, width=50)
scene_desc_entry.grid(row=4, column=1, padx=10, pady=5)

# Generate Button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

generate_button = ttk.Button(root, text="Generate Script", command=generate_script, style="TButton")
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Output Display
output_label = tk.Label(root, text="Generated Script:", font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
output_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, bg="#34495e", fg="#ecf0f1", font=("Courier", 10))
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
