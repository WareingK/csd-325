"""
Kristian Wareing
CSD-325 - Module 10 Assignment
Scrolling To-Do List built with Tkinter

Modifications from the tutorial version:
  - Window title changed to Wareing-ToDo
  - Task rows alternate between two complementary colors (violet / gold)
  - Tasks are deleted with a RIGHT click instead of a left click
  - The top label tells the user how to delete a task
  - File -> Exit menu added to close the program cleanly
"""

import tkinter as tk
from tkinter import font


class Todo(tk.Tk):
    # (background, foreground) pairs - violet and gold are complementary
    COLORS = [("#9400D3", "#FFFFFF"), ("#E5C100", "#4B0082")]

    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = tasks if tasks else []

        self.title("Wareing-ToDo")
        self.geometry("400x500")

        self.task_font = font.Font(family="Helvetica", size=11, weight="bold")

        self.build_menu()
        self.build_task_area()
        self.build_entry_box()

    def build_menu(self):
        """File -> Exit menu."""
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_program)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

    def build_task_area(self):
        """Canvas + inner frame + scrollbar so the task list can scroll."""
        self.canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar(
            self.canvas, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="nw", tags="self.tasks_frame"
        )
        self.tasks_frame.bind("<Configure>", self.on_frame_configure)

        # instruction label - tells the user how to delete.
        # It counts as row 0, so the first real task picks up the second color.
        bg, fg = self.COLORS[0]
        self.instructions = tk.Label(
            self.tasks_frame,
            text="Items Added --- ** Right Click Item to Delete **",
            bg=bg,
            fg=fg,
            pady=10,
            font=self.task_font,
        )
        self.instructions.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(self.instructions)

    def build_entry_box(self):
        """Text box at the bottom. Press Enter to add the task."""
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        self.task_create.bind("<Return>", self.add_task)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if task_text:
            bg, fg = self.COLORS[len(self.tasks) % len(self.COLORS)]
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                bg=bg,
                fg=fg,
                pady=10,
                font=self.task_font,
                wraplength=350,
            )

            # right mouse button deletes the task
            new_task.bind("<Button-3>", self.remove_task)  # Windows / Linux
            new_task.bind("<Button-2>", self.remove_task)  # macOS

            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)
        return "break"  # keeps Enter from adding a newline to the text box

    def remove_task(self, event):
        task = event.widget
        if task in self.tasks:
            self.tasks.remove(task)
            task.destroy()
            self.recolor_tasks()

    def recolor_tasks(self):
        """Keep the alternating color pattern after a delete."""
        for index, task in enumerate(self.tasks):
            bg, fg = self.COLORS[index % len(self.COLORS)]
            task.configure(bg=bg, fg=fg)

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def exit_program(self):
        self.destroy()


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
