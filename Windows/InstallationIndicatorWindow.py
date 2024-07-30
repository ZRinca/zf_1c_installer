from itertools import cycle
import customtkinter as ctk
import tkinter as tk


class LoadingIndicator(ctk.CTkCanvas):
    def __init__(self, parent, size=100, speed=10, label_text="", *args, **kwargs):
        super().__init__(parent, width=size, height=size, bg="#F8F8F8", highlightthickness=0, *args, **kwargs)

        self.size = size
        self.speed = speed
        self.label_text = label_text

        self.inner_arc = self.create_arc((10, 10, size - 10, size - 10), start=0, extent=270, style=tk.ARC,
                                         outline="#EDF8F3", width=5)

        self.outer_arc = self.create_arc((10, 10, size - 10, size - 10), start=0, extent=270, style=tk.ARC,
                                         outline="#88DE71", width=5)

        self.angles = cycle(range(0, 360, 5))

        self.label = None

    def set_label_text(self, new_text):
        if self.label:
            self.label_text = new_text
            self.label.configure(text=new_text)

    def animate(self):
        angle = next(self.angles)
        self.itemconfig(self.inner_arc, start=angle)
        self.itemconfig(self.outer_arc, start=angle)
        self.after(self.speed, self.animate)

    def set_parent(self, parent):
        self.pack(expand=True, pady=(50, 20))

        # Создаем метку внутри родительского виджета и размещаем ее внизу слева
        self.label = ctk.CTkLabel(parent, text=self.label_text, font=("Rubik Light", 12), text_color="#6EC756")
        self.label.pack(side="bottom", anchor="w", padx=24, pady=(0, 24))

        self.animate()

