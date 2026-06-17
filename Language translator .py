
from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

languages = {
    "English":"en",
    "Hindi":"hi",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Japanese":"ja",
    "Chinese":"zh-CN",
    "Arabic":"ar",
    "Russian":"ru"
}

def translate_text():

    try:

        text = input_text.get(
            "1.0",
            END
        ).strip()

        source_lang = languages[
            source_combo.get()
        ]

        target_lang = languages[
            target_combo.get()
        ]

        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        output_text.delete(
            "1.0",
            END
        )

        output_text.insert(
            END,
            translated
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

def copy_translation():

    pyperclip.copy(
        output_text.get(
            "1.0",
            END
        )
    )

    messagebox.showinfo(
        "Success",
        "Copied Successfully"
    )

window = Tk()

window.title(
    "AI Language Translation Tool"
)

window.geometry(
    "900x650"
)

Label(
    window,
    text="🌍 AI Language Translation Tool",
    font=("Arial",20,"bold")
).pack(pady=20)

Label(
    window,
    text="Source Language"
).pack()

source_combo = ttk.Combobox(
    window,
    values=list(languages.keys()),
    width=30
)

source_combo.pack()
source_combo.set("English")

Label(
    window,
    text="Target Language"
).pack()

target_combo = ttk.Combobox(
    window,
    values=list(languages.keys()),
    width=30
)

target_combo.pack()
target_combo.set("Hindi")

Label(
    window,
    text="Enter Text"
).pack(pady=5)

input_text = Text(
    window,
    height=8,
    width=80
)

input_text.pack()

Button(
    window,
    text="Translate",
    bg="lightgreen",
    command=translate_text
).pack(pady=10)

Label(
    window,
    text="Translated Text"
).pack()

output_text = Text(
    window,
    height=8,
    width=80
)

output_text.pack()

Button(
    window,
    text="Copy Translation",
    bg="lightblue",
    command=copy_translation
).pack(pady=10)

window.mainloop()

