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

# class Install(InstallerWindow):
#     draw_back_button = True
#     draw_next_button = True
#     header_text = None
#     body_text = None
#
#     def draw(self):
#         super().draw()
#
#         self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50, label_text="Loading Apache...")
#         self.loading_indicator.set_parent(self.main_frame)

# if self.header_text is not None:
#     label1 = ctk.CTkLabel(self.main_frame, text=self.header_text, font=("Rubik Light", 12), anchor='w',
#                           text_color="#6EC756",
#                           justify='left', wraplength=self.main_frame.winfo_width() - 48)
#     label1.pack(padx=24, pady=(24, 0), fill='x')
#
#     line = ctk.CTkFrame(self.main_frame, height=2, fg_color="#6EC756")
#     line.pack(padx=24, pady=(24, 0), fill='x')
#
# if self.body_text is not None:
#     label2 = ctk.CTkLabel(self.main_frame,
#                           text=self.body_text,
#                           font=("Rubik Light", 10), anchor='w', justify='left',
#                           wraplength=self.main_frame.winfo_width() - 48)
#     label2.pack(padx=24, pady=(24, 0), fill='x')
