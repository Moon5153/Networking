#Assignment-4
#Najmun Nahar
from tkinter import *
from tkinter.ttk import *
from Najmun_data_generator import Generator
import threading
import time


class DynamicChart(Tk):
    frame: Frame
    cnvs: Canvas
    # Values used for drawing
    canvas_width = 500
    canvas_height = 300
    incrementX = 13
    incrementY = 20
    startY = canvas_height


    def __init__(self, title):
        Tk.__init__(self, title)
        self.title(title)
        self.generate_values()
        self.create_form_ui()
        self.create_canvas()
        self.set_form_style()


    def generate_values(self):
        self.generator = Generator()
        self.listOfValues = [
            self.generator.value for _ in range(250)]

    # Method for part 1 of the lab
    def update_values(self):
        while True:
            self.listOfValues.pop(0)
            new_value = self.generator.value
            self.listOfValues.append(new_value)
            self.redraw_lines()
            time.sleep(0.5)

    def create_form_ui(self, parent=None):
        self.minsize(500, 300)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Setup frame
        self.frame = Frame(self, width=500, height=300)
        self.frame['padding'] = (5, 10)
        self.frame['borderwidth'] = 10
        self.frame['relief'] = 'ridge'
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid(sticky=(W, E))


        # Create labels
        Label(self.frame,text='Temperature',font=('arial',21)).grid(row=0, columnspan=3, pady=10)
        Label(self.frame, text='==========').grid(column=0, row=1, sticky=W, padx=5)
        self.btn = Button(self.frame, text='Go',style='TButton',command=self.initUI,state=NORMAL)
        self.btn.grid(column=1, row=1, sticky=(W, E), padx=5)
        Label(self.frame, text='==========').grid(column=2, row=1, sticky=W, padx=5)

    def create_canvas(self):
        self.cnvs = Canvas(self.frame,width=self.canvas_width,height=self.canvas_height,bg='#f1dbdb',bd=0, highlightthickness=0,relief='ridge')
        self.cnvs.grid(row=3, columnspan=3)

        # Create lines and labels for graph
        startValue = 0
        self.incrementY = 40
        for x in range(21):
            self.startY -= self.incrementY

        self.redraw_lines()

    def set_form_style(self):
        style = Style()
        style.theme_use('alt')
        style.configure('.',background='#f7f7f7',foreground='#463f3a')
        style.configure('TButton', font="Arial 12",foreground="black", background="white")

    def redraw_lines(self):
        # Delete previously drawn lines
        self.cnvs.delete('line')
        
        first_notch_position = self.incrementY
        last_notch_position = 21 * self.incrementY
        height = last_notch_position - first_notch_position
        startX = 10

        # Draw lines
        for i in range(len(self.listOfValues) - 1):
            lineY1 = self.canvas_height - \
                (self.listOfValues[i] / 100 * height) - first_notch_position
            lineY2 = self.canvas_height - \
                (self.listOfValues[i + 1] / 100 *
                 height) - first_notch_position
            self.cnvs.create_line(
                (startX, lineY1), (startX + self.incrementX, lineY2), width=3, fill='red', tag='line')
            startX = startX + self.incrementX

    # Method for part 2 of the lab
    def initUI(self):
        self.btn.configure(state=DISABLED)
        threading.Thread(target=self.update_values, daemon=True).start()


app = DynamicChart('Dynamic Display-Najmun Nahar')
app.mainloop()
