import math
import tkinter as tk
import statistics as st
import itertools as it
import numpy as np
import math as m

# Main class:
class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("CMPSC 136 Calculator")  # window title
        self.configure(bg='gray')   # window color
        self.resizable(width=False, height=False)   # cannot resize window
        self.geometry("500x600")    # window size

        # menu
        menubar = tk.Menu(self)
        menubar.add_command(label='Home', command=lambda: self.show_frame(HomePage))
        menubar.add_command(label='About', command=lambda: self.show_frame(AboutPage))
        self.config(menu=menubar)

        # main frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame_class in (HomePage, DS, FD, P, SP, DRV, SD, CLT, CI, HT, AboutPage):
            frame = frame_class(container, self)

            self.frames[frame_class] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # Function that changes frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Home Page class:
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='grey')  #Frame

        # Title
        lbl_Title = tk.Label(self, text='CMPSC 136 CALCULATOR\n', bg='gray', fg='black',
                          font=('Cambria', 28, 'bold'), bd=0)
        lbl_Title.grid(row=0, column=0, columnspan=2, padx=30)

        # Buttons
        btnDS = tk.Button(self, text="Descriptive Statistics", width=25,
                          height=4, bg='powder blue', font=('Helvetica', 10, 'bold'), bd=4,
                          command=lambda: controller.show_frame(DS))
        btnDS.grid(row=1, column=0, padx=10, pady=10)

        btnFD = tk.Button(self, text="Frequency Distribution", width=25,
                          height=4, bg='powder blue',
                          font=('Helvetica', 10, 'bold'), bd=4,
                          command=lambda: controller.show_frame(FD))
        btnFD.grid(row=1, column=1)

        btnP = tk.Button(self, text="Probability", width=25,
                         height=4, bg='powder blue',
                         font=('Helvetica', 10, 'bold'), bd=4,
                         command=lambda: controller.show_frame(P))
        btnP.grid(row=2, column=0, padx=10, pady=10)


        btnSP = tk.Button(self, text="Sample Points", width=25,
                          height=4, bg='powder blue',
                          font=('Helvetica', 10, 'bold'), bd=4,
                          command=lambda: controller.show_frame(SP))
        btnSP.grid(row=2, column=1)

        btnDRV = tk.Button(self, text="Discrete Random Variables", width=25,
                           height=4, bg='powder blue',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=lambda: controller.show_frame(DRV))
        btnDRV.grid(row=3, column=0, padx=10, pady=10)

        btnSD = tk.Button(self, text="Sampling Distribution", width=25,
                          height=4, bg='powder blue',
                          font=('Helvetica', 10, 'bold'), bd=4,
                          command=lambda: controller.show_frame(SD))
        btnSD.grid(row=3, column=1)

        btnCLT = tk.Button(self, text="Central Limit\nTheorem", width=25,
                          height=4, bg='powder blue',
                          font=('Helvetica', 10, 'bold'), bd=4,
                          command=lambda: controller.show_frame(CLT))
        btnCLT.grid(row=4, column=0, padx=10, pady=10)

        btnCI = tk.Button(self, text="Confidence\nInterval", width=25,
                           height=4, bg='powder blue',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=lambda: controller.show_frame(CI))
        btnCI.grid(row=4, column=1)

        btnHT = tk.Button(self, text="Hypothesis\nTesting", width=25,
                          height=4, bg='powder blue',
                          font=('Helvetica', 10, 'bold'), bd=4,
                          command=lambda: controller.show_frame(HT))
        btnHT.grid(row=5, columnspan=2, pady=10)

# Descriptive statistics class:
class DS(tk.Frame):
    def __init__(self, parent, controller):
        # Frame
        tk.Frame.__init__(self, parent, bg='powder blue')

        # Input
        input_Text = tk.StringVar() # Holds string value
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 14, 'bold'),
                             bg='black', fg='white', bd=25, highlightcolor='red', justify=tk.RIGHT,
                             width=41, insertbackground='white')  # Takes string input from user
        input_Box.grid(row=0, column=0, columnspan=3)
        input_Box.insert(0, 'Separate with comma or space.')   # default text

        # Output
        output_Box = tk.Text(self, bg='white', font=('Cambria', 20, 'bold'),
                             width=30, height=3)    # Textbox where output will be displayed
        output_Box.grid(row=6, column=0, columnspan=3, pady=10)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)     # Restricts user from putting input in textbox

        # Function that deletes 'INPUT' text from entry when clicked
        def click(event):
            if input_Box.get() == 'Separate with comma or space.':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')
        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        # Button Functions
        def mean():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            # input_Box.delete(0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = st.mean(arr)
            str_result = 'Mean = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def median():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            # input_Box.delete(0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = st.median(arr)
            str_result = 'Median = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def mode():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            # input_Box.delete(0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = st.multimode(arr)
            str_result = 'Mode = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def range():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = max(arr) - min(arr)
            str_result = 'Range = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def var():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = st.variance(arr)
            str_result = 'Variance = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def std():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = st.stdev(arr)
            str_result = 'Standard Deviation = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def cov():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = (st.stdev(arr) / st.mean(arr)) * 100
            str_result = 'Coefficient of Variation = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def quarts():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = st.quantiles(arr)
            str_result = 'Quartiles = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def iqr():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            quartiles = st.quantiles(arr)
            q1 = quartiles[0]
            q3 = quartiles[2]
            result = q3 - q1
            str_result = 'IQR = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def outliers():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            quartiles = st.quantiles(arr)
            q1 = quartiles[0]
            q3 = quartiles[2]
            iqrMultiplied = (q3 - q1) * 1.5
            low = q1 - iqrMultiplied
            high = q3 + iqrMultiplied
            result = [y for y in arr if y < low or y > high]
            if len(result) == 0:
                str_result = 'Outliers = None'
            else:
                str_result = 'Outliers = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        # Buttons
        mean_Btn = tk.Button(self, text='Mean', width=16, height=4, bg='gray',
                          font=('Helvetica', 10, 'bold'), bd=4, command=mean)
        mean_Btn.grid(row=1, column=0, pady=10)

        median_Btn = tk.Button(self, text='Median', width=16, height=4, bg='gray',
                            font=('Helvetica', 10, 'bold'), bd=4, command=median)
        median_Btn.grid(row=1, column=1, pady=10)

        mode_Btn = tk.Button(self, text='Mode', width=16, height=4, bg='gray',
                          font=('Helvetica', 10, 'bold'), bd=4, command=mode)
        mode_Btn.grid(row=1, column=2, pady=10)

        range_Btn = tk.Button(self, text='Range', width=16, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4, command=range)
        range_Btn.grid(row=2, column=0, pady=10)

        var_Btn = tk.Button(self, text='Variance', width=16, height=4, bg='gray',
                         font=('Helvetica', 10, 'bold'), bd=4, command=var)
        var_Btn.grid(row=2, column=1, pady=10)

        std_Btn = tk.Button(self, text='Standard\nDeviation', width=16, height=4, bg='gray',
                         font=('Helvetica', 10, 'bold'), bd=4, command=std)
        std_Btn.grid(row=2, column=2, pady=10)

        cov_Btn = tk.Button(self, text='Coefficient\nof Variation', width=16, height=4, bg='gray',
                         font=('Helvetica', 10, 'bold'), bd=4, command=cov)
        cov_Btn.grid(row=3, column=0, pady=10)

        quarts_Btn = tk.Button(self, text='Quartiles', width=16, height=4, bg='gray',
                            font=('Helvetica', 10, 'bold'), bd=4, command=quarts)
        quarts_Btn.grid(row=3, column=1, pady=10)

        iqr_Btn = tk.Button(self, text='Interquartile\nRange', width=16, height=4, bg='gray',
                         font=('Helvetica', 10, 'bold'), bd=4, command=iqr)
        iqr_Btn.grid(row=3, column=2, pady=10)

        outliers_Btn = tk.Button(self, text='Outliers', width=16, height=4, bg='gray',
                              font=('Helvetica', 10, 'bold'), bd=4, command=outliers)
        outliers_Btn.grid(row=4, column=0, pady=10)

        clear_Btn = tk.Button(self, text='Clear', width=37, height=4, bg='gray',
                              font=('Helvetica', 10, 'bold'), bd=4,
                              command=lambda: input_Box.delete(0, tk.END))
        clear_Btn.grid(row=4, column=1, pady=10, columnspan=2)

# Frequency Distribution Table
class FD(tk.Frame):
    def __init__(self, parent, controller):
        # Same lang as last
        tk.Frame.__init__(self, parent, bg='powder blue')
        input_Text = tk.StringVar()
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 14, 'bold'),
                             bg='black', fg='white', bd=25, highlightcolor='red', justify=tk.RIGHT,
                             width=41, insertbackground='white')
        input_Box.grid(row=0, column=0, columnspan=2)
        input_Box.insert(0, 'Separate with comma or space.')

        output_Box1 = tk.Text(self, bg='white', bd=1, font=('Cambria', 15, 'bold'),
                              width=38, height=3)
        output_Box1.grid(row=2, column=0, columnspan=2, pady=5)
        output_Box1.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                              state=tk.DISABLED)
        output_Box2 = tk.Text(self, bg='white', bd=1, font=('Cambria', 15, 'bold'),
                              width=38, height=3)
        output_Box2.grid(row=3, column=0, columnspan=2, pady=5)
        output_Box2.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                              state=tk.DISABLED)
        output_Box3 = tk.Text(self, bg='white', bd=1, font=('Cambria', 15, 'bold'),
                              width=38, height=3)
        output_Box3.grid(row=4, column=0, columnspan=2, pady=5)
        output_Box3.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                              state=tk.DISABLED)
        output_Box4 = tk.Text(self, bg='white', bd=1, font=('Cambria', 15, 'bold'),
                              width=38, height=3)
        output_Box4.grid(row=5, column=0, columnspan=2, pady=5)
        output_Box4.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                              state=tk.DISABLED)
        output_Box5 = tk.Text(self, bg='white', bd=1, font=('Cambria', 15, 'bold'),
                              width=38, height=3)
        output_Box5.grid(row=6, column=0, columnspan=2, pady=5)
        output_Box5.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                              state=tk.DISABLED)

        def click(event):
            if input_Box.get() == 'Separate with comma or space.':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')
        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        def table():
            given = input_Text.get().replace(' ', ',')
            output_Box1.configure(state=tk.NORMAL)
            output_Box1.delete(1.0, tk.END)
            output_Box2.configure(state=tk.NORMAL)
            output_Box2.delete(1.0, tk.END)
            output_Box3.configure(state=tk.NORMAL)
            output_Box3.delete(1.0, tk.END)
            output_Box4.configure(state=tk.NORMAL)
            output_Box4.delete(1.0, tk.END)
            output_Box5.configure(state=tk.NORMAL)
            output_Box5.delete(1.0, tk.END)
            arr = sorted([float(x) for x in given.split(',')])
            n = len(arr)
            ordered = sorted([int(x) for x in set(arr)])
            frequency = [len(list(group)) for key, group in it.groupby(arr)]
            rfd = [round(x/n, 2) for x in frequency]
            cfd = list(np.cumsum(frequency))
            crf = [round(x/n, 2) for x in cfd]
            str_result1 = ' Inputs:\n ' + str(ordered)
            str_result2 = ' Frequency:\n ' + str(frequency)
            str_result3 = ' RFD:\n ' + str(rfd)
            str_result4 = ' CFD:\n ' + str(cfd)
            str_result5 = ' CRF:\n ' + str(crf)
            output_Box1.insert(tk.END, str_result1)
            output_Box1.configure(state=tk.DISABLED)
            output_Box2.insert(tk.END, str_result2)
            output_Box2.configure(state=tk.DISABLED)
            output_Box3.insert(tk.END, str_result3)
            output_Box3.configure(state=tk.DISABLED)
            output_Box4.insert(tk.END, str_result4)
            output_Box4.configure(state=tk.DISABLED)
            output_Box5.insert(tk.END, str_result5)
            output_Box5.configure(state=tk.DISABLED)

        enterBtn = tk.Button(self, text='Frequency\nDistribution', width=25, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4, command=table)
        enterBtn.grid(row=1, column=0, padx=5, pady=10)

        # Clear Button
        clearBtn = tk.Button(self, text='Clear', width=25, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=lambda: input_Box.delete(0, tk.END))
        clearBtn.grid(row=1, column=1, padx=5, pady=10)

# Probability class:
class P(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        input_Text = tk.StringVar()
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 14, 'bold'),
                             bg='black', fg='white', bd=25, highlightcolor='red', justify=tk.RIGHT,
                             width=41, insertbackground='white')
        input_Box.grid(row=0, column=0, columnspan=2)
        input_Box.insert(0, 'Input :  n , r ')
        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=9)
        output_Box.grid(row=3, column=0, columnspan=2, pady=15)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        def click(event):
            if input_Box.get() == 'Separate with comma or space.':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')
        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        def nPr():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [int(x) for x in given.split(',')]
            n = arr[0]
            r = arr[1]
            result = int(m.factorial(n) / m.factorial((n-r)))
            str_result = ' nPr = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def nCr():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [int(x) for x in given.split(',')]
            n = arr[0]
            r = arr[1]
            result = int(m.factorial(n) / (m.factorial(r) * m.factorial((n-r))))
            str_result = ' nCr = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        nprBtn = tk.Button(self, text='nPr', width=25, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4, command=nPr)
        nprBtn.grid(row=1, column=0, padx=5, pady=10)

        cprBtn = tk.Button(self, text='nCr', width=25, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=nCr)
        cprBtn.grid(row=1, column=1, padx=5, pady=10)

        # Clear Button
        clearBtn = tk.Button(self, text='Clear', width=57, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=lambda: input_Box.delete(0, tk.END))
        clearBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=10)


# Sample points class:
class SP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        input_Text = tk.StringVar()
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 14, 'bold'),
                             bg='black', fg='white', bd=25, highlightcolor='red', justify=tk.RIGHT,
                             width=41, insertbackground='white')
        input_Box.grid(row=0, column=0, columnspan=2)
        input_Box.insert(0, 'Input :  n1 , n2 , n3 , ... ')
        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=9)
        output_Box.grid(row=3, column=0, columnspan=2, pady=15)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        def click(event):
            if input_Box.get() == 'Separate with comma or space.':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')
        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        def multiRule():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [int(x) for x in given.split(',')]
            result = m.prod(arr)
            str_result = ' Multiplication Rule = ' + str(result) + ' ways'
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def distinct():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [int(x) for x in given.split(',')]
            n = int(m.fsum(arr))
            nk = [m.factorial(x) for x in arr]
            result = int(m.factorial(n) / m.prod(nk))
            str_result = ' Distinct Permutation = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        mrBtn = tk.Button(self, text='Multiplication Rule', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4, command=multiRule)
        mrBtn.grid(row=1, column=0, padx=5, pady=10)

        dpBtn = tk.Button(self, text='Distinct Permutation', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=distinct)
        dpBtn.grid(row=1, column=1, padx=5, pady=10)

        # Clear Button
        clearBtn = tk.Button(self, text='Clear', width=57, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=lambda: input_Box.delete(0, tk.END))
        clearBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Discrete Random Variables class:
class DRV(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        bpd_Text = tk.StringVar()
        bpd_lbl = tk.Label(self, text='Binomial Probability Distribution', bg='powder blue', fg='black',
                          font=('Cambria', 14, 'bold'))
        bpd_lbl.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky='nw')
        bpd_input_Box = tk.Entry(self, textvariable=bpd_Text, font=('Helvetica', 12, 'bold'),
                             bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                             width=49, bd=9, insertbackground='white')
        bpd_input_Box.grid(row=1, column=0, columnspan=2, padx=17)
        bpd_input_Box.insert(0, ' Input :  p , n , x')

        ppd_Text = tk.StringVar()
        ppd_lbl = tk.Label(self, text='Poisson Probability Distribution', bg='powder blue', fg='black',
                           font=('Cambria', 14, 'bold'))
        ppd_lbl.grid(row=2, column=0, columnspan=2, padx=15, pady=10, sticky='nw')
        ppd_input_Box = tk.Entry(self, textvariable=ppd_Text, font=('Helvetica', 12, 'bold'),
                                 bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                                 width=49, bd=9, insertbackground='white')
        ppd_input_Box.grid(row=3, column=0, columnspan=2, padx=17)
        ppd_input_Box.insert(0, ' Input :  λ , x')

        hpd_Text = tk.StringVar()
        hpd_lbl = tk.Label(self, text='Hypergeometric Probability Distribution', bg='powder blue', fg='black',
                           font=('Cambria', 14, 'bold'))
        hpd_lbl.grid(row=4, column=0, columnspan=2, padx=15, pady=10, sticky='nw')
        hpd_input_Box = tk.Entry(self, textvariable=hpd_Text, font=('Helvetica', 12, 'bold'),
                                 bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                                 width=49, bd=9, insertbackground='white')
        hpd_input_Box.grid(row=5, column=0, columnspan=2, padx=17)
        hpd_input_Box.insert(0, ' Input : N , K , n , x')


        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=3)
        output_Box.grid(row=8, column=0, columnspan=2, padx=15, pady=15)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        def click1(event):
            if bpd_input_Box.get() == ' Input :  p , n , x':
                event.widget.delete(0, tk.END)
            else:
                bpd_input_Box.config(foreground='white')
        bpd_input_Box.bind('<Button-1>', click1)
        bpd_input_Box.bind('<FocusIn>', click1)

        def click2(event):
            if ppd_input_Box.get() == ' Input :  λ , x':
                event.widget.delete(0, tk.END)
            else:
                ppd_input_Box.config(foreground='white')
        ppd_input_Box.bind('<Button-1>', click2)
        ppd_input_Box.bind('<FocusIn>', click2)

        def click3(event):
            if hpd_input_Box.get() == ' Input : N , K , n , x':
                event.widget.delete(0, tk.END)
            else:
                hpd_input_Box.config(foreground='white')
        hpd_input_Box.bind('<Button-1>', click3)
        hpd_input_Box.bind('<FocusIn>', click3)

        def BPD():
            given = bpd_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            p = arr[0]
            n = int(arr[1])
            x = int(arr[2])
            nCx = int(m.factorial(n) / (m.factorial(x) * m.factorial((n-x))))
            result = nCx * (m.pow(p, x) * (m.pow(1-p, n-x)))
            str_result = ' P(x): ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def PPD():
            given = ppd_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            mean = int(arr[0])
            x = int(arr[1])
            e = float(2.71828)
            result = round((m.pow(mean, x) * m.pow(e, -mean)) / m.factorial(x), 9)
            str_result = ' P(X = x): ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def HPD():
            given = hpd_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [int(x) for x in given.split(',')]
            N = int(arr[0])
            K = int(arr[1])
            n = int(arr[2])
            x = int(arr[3])
            kCx = m.factorial(K) / (m.factorial(x) * m.factorial((K-x)))
            NkCnx = m.factorial(N-K) / (m.factorial(n-x) * m.factorial(((N-K)-(n-x))))
            NCn = m.factorial(N) / (m.factorial(n) * m.factorial((N-n)))
            result = round((kCx * NkCnx) / NCn, 4)
            str_result = ' h(x; N, n, k): ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def clear():
            bpd_input_Box.delete(0, tk.END)
            ppd_input_Box.delete(0, tk.END)
            hpd_input_Box.delete(0, tk.END)

        bpdBtn = tk.Button(self, text='Binomial\nProbability Distribution', width=26, height=4, bg='gray',
                          font=('Helvetica', 10, 'bold'), bd=4, command=BPD)
        bpdBtn.grid(row=6, column=0, pady=15)

        ppdBtn = tk.Button(self, text='Poisson\nProbability Distribution', width=26, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4, command=PPD)
        ppdBtn.grid(row=6, column=1, pady=15)
        hpdBtn = tk.Button(self, text='Hypergeometric\nProbability Distribution', width=26, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4, command=HPD)
        hpdBtn.grid(row=7, column=0, pady=5)
        clearBtn = tk.Button(self, text='Clear', width=26, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=clear)
        clearBtn.grid(row=7, column=1, pady=5)

# Sampling Distribution class:
class SD(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        input_Text = tk.StringVar()
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 14, 'bold'),
                             bg='black', fg='white', bd=25, highlightcolor='red', justify=tk.RIGHT,
                             width=41, insertbackground='white')
        input_Box.grid(row=0, column=0, columnspan=2)
        input_Box.insert(0, 'Input :  n1 , n2 , n3 , ... ')
        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=9)
        output_Box.grid(row=3, column=0, columnspan=2, pady=15)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        def click(event):
            if input_Box.get() == 'Separate with comma or space.':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')
        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        def PSD():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = round(st.pstdev(arr), 4)
            str_result = ' Population Standard Deviation = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def SSD():
            given = input_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            result = round(st.stdev(arr), 4)
            str_result = ' Sample Standard Deviation = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        psdBtn = tk.Button(self, text='Population\nStandard Deviation', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4, command=PSD)
        psdBtn.grid(row=1, column=0, padx=5, pady=10)

        ssdBtn = tk.Button(self, text='Sample\nStandard Deviation', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=SSD)
        ssdBtn.grid(row=1, column=1, padx=5, pady=10)

        # Clear Button
        clearBtn = tk.Button(self, text='Clear', width=57, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=lambda: input_Box.delete(0, tk.END))
        clearBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

class CLT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        ssd_Text = tk.StringVar()
        ssd_lbl = tk.Label(self, text='Sample Standard Deviation', bg='powder blue', fg='black',
                           font=('Cambria', 14, 'bold'))
        ssd_lbl.grid(row=0, column=0, columnspan=2, padx=15, pady=5, sticky='nw')
        ssd_input_Box = tk.Entry(self, textvariable=ssd_Text, font=('Helvetica', 12, 'bold'),
                                 bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                                 width=49, bd=9, insertbackground='white')
        ssd_input_Box.grid(row=1, column=0, columnspan=2, padx=15)
        ssd_input_Box.insert(0, ' Input : σ , n')

        zs_Text = tk.StringVar()
        zs_lbl = tk.Label(self, text='Z-Score', bg='powder blue', fg='black',
                           font=('Cambria', 14, 'bold'))
        zs_lbl.grid(row=2, column=0, columnspan=2, padx=15, pady=5, sticky='nw')
        zs_input_Box = tk.Entry(self, textvariable=zs_Text, font=('Helvetica', 12, 'bold'),
                                 bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                                 width=49, bd=9, insertbackground='white')
        zs_input_Box.grid(row=3, column=0, columnspan=2, padx=15)
        zs_input_Box.insert(0, ' Input : x , μx , σx')

        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=6)
        output_Box.grid(row=8, column=0, columnspan=2, padx=15, pady=20)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        def click1(event):
            if ssd_input_Box.get() == ' Input : σ , n':
                event.widget.delete(0, tk.END)
            else:
                ssd_input_Box.config(foreground='white')
        ssd_input_Box.bind('<Button-1>', click1)
        ssd_input_Box.bind('<FocusIn>', click1)

        def click2(event):
            if zs_input_Box.get() == ' Input : x , μx , σx':
                event.widget.delete(0, tk.END)
            else:
                zs_input_Box.config(foreground='white')
        zs_input_Box.bind('<Button-1>', click2)
        zs_input_Box.bind('<FocusIn>', click2)

        def SSD():
            given = ssd_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            std = float(arr[0])
            n = int(arr[1])
            result = round(std / m.sqrt(n), 4)
            str_result = ' σx̄ = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def ZS():
            given = zs_Text.get().replace(' ', ',')
            output_Box.configure(state=tk.NORMAL)
            output_Box.delete(1.0, tk.END)
            arr = [float(x) for x in given.split(',')]
            x = arr[0]
            mean = arr[1]
            std = arr[2]
            result = round((x - mean) / std, 4)
            str_result = ' z = ' + str(result)
            output_Box.insert(tk.END, str_result)
            output_Box.configure(state=tk.DISABLED)

        def clear():
            ssd_input_Box.delete(0, tk.END)
            zs_input_Box.delete(0, tk.END)

        ssdBtn = tk.Button(self, text='Sample\nStandard Deviation', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=SSD)
        ssdBtn.grid(row=4, column=0, pady=15)
        zsBtn = tk.Button(self, text='Z-Score', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=ZS)
        zsBtn.grid(row=4, column=1, pady=15)
        clearBtn = tk.Button(self, text='Clear', width=57, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=clear)
        clearBtn.grid(row=7, column=0, columnspan=2, pady=5)

class CI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        input_Text = tk.StringVar()
        input_lbl = tk.Label(self, text='Confidence Interval:', bg='powder blue', fg='black',
                             font=('Cambria', 14, 'bold'))
        input_lbl.grid(row=0, column=0, columnspan=2, padx=15, pady=5, sticky='nw')
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 12, 'bold'),
                             bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                             width=49, bd=9, insertbackground='white')
        input_Box.grid(row=1, column=0, columnspan=2, padx=15)
        input_Box.insert(0, 'Input :  n , x̄ , σ')

        input_Text2 = tk.StringVar()
        input_lbl2 = tk.Label(self, text='Determining Sample Size (σ Known):', bg='powder blue', fg='black',
                             font=('Cambria', 14, 'bold'))
        input_lbl2.grid(row=3, column=0, columnspan=2, padx=15, sticky='nw')
        input_Box2 = tk.Entry(self, textvariable=input_Text2, font=('Helvetica', 12, 'bold'),
                             bg='black', fg='white', highlightcolor='red', justify=tk.LEFT,
                             width=49, bd=9, insertbackground='white')
        input_Box2.grid(row=4, column=0, columnspan=2, padx=15)
        input_Box2.insert(0, 'Input :  σ , E')

        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=2)
        output_Box.grid(row=2, column=0, columnspan=2, pady=15)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        output_Box2 = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                              width=29, height=2)
        output_Box2.grid(row=5, column=0, columnspan=2, pady=15)
        output_Box2.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                              state=tk.DISABLED)

        def click(event):
            if input_Box.get() == 'Input :  n , x̄ , σ':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')

        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        def click2(event):
            if input_Box2.get() == 'Input :  σ , E':
                event.widget.delete(0, tk.END)
            else:
                input_Box2.config(foreground='white')

        input_Box2.bind('<Button-1>', click2)
        input_Box2.bind('<FocusIn>', click2)

        def p90():
            if len([x for x in input_Text.get().replace(' ', ',').split(',')]) == 3:
                given = input_Text.get().replace(' ', ',')
                output_Box.configure(state=tk.NORMAL)
                output_Box.delete(1.0, tk.END)
                arr = [float(x) for x in given.split(',')]
                n = arr[0]
                sMean = arr[1]
                std = arr[2]
                z = 1.645
                result = [round(sMean - z * (std / m.sqrt(n)), 2), round(sMean + z * (std / m.sqrt(n)), 2)]
                str_result = str(result)
                output_Box.insert(tk.END, str_result)
                output_Box.configure(state=tk.DISABLED)

            if len([x for x in input_Text2.get().replace(' ', ',').split(',')]) == 2:
                given2 = input_Text2.get().replace(' ', ',')
                output_Box2.configure(state=tk.NORMAL)
                output_Box2.delete(1.0, tk.END)
                arr2 = [float(x) for x in given2.split(',')]
                std2 = arr2[0]
                e = arr2[1]
                z2 = 1.645
                result2 = round(((z2 * std2) / e) **2, 2)
                str_result2 = str(result2)
                output_Box2.insert(tk.END, str_result2)
                output_Box2.configure(state=tk.DISABLED)

        def p95():
            if len([x for x in input_Text.get().replace(' ', ',').split(',')]) == 3:
                given = input_Text.get().replace(' ', ',')
                output_Box.configure(state=tk.NORMAL)
                output_Box.delete(1.0, tk.END)
                arr = [float(x) for x in given.split(',')]
                n = arr[0]
                sMean = arr[1]
                std = arr[2]
                z = 1.96
                result = [round(sMean - z * (std / math.sqrt(n)), 2), round(sMean + z * (std / math.sqrt(n)), 2)]
                str_result = str(result)
                output_Box.insert(tk.END, str_result)
                output_Box.configure(state=tk.DISABLED)

            if len([x for x in input_Text2.get().replace(' ', ',').split(',')]) == 2:
                given2 = input_Text2.get().replace(' ', ',')
                output_Box2.configure(state=tk.NORMAL)
                output_Box2.delete(1.0, tk.END)
                arr2 = [float(x) for x in given2.split(',')]
                std2 = arr2[0]
                e = arr2[1]
                z2 = 1.960
                result2 = round(((z2 * std2) / e) ** 2, 2)
                str_result2 = str(result2)
                output_Box2.insert(tk.END, str_result2)
                output_Box2.configure(state=tk.DISABLED)

        def p99():
            if len([x for x in input_Text.get().replace(' ', ',').split(',')]) == 3:
                given = input_Text.get().replace(' ', ',')
                output_Box.configure(state=tk.NORMAL)
                output_Box.delete(1.0, tk.END)
                arr = [float(x) for x in given.split(',')]
                n = arr[0]
                sMean = arr[1]
                std = arr[2]
                z = 2.575
                result = [round(sMean - z * (std / math.sqrt(n)), 2), round(sMean + z * (std / math.sqrt(n)), 2)]
                str_result = str(result)
                output_Box.insert(tk.END, str_result)
                output_Box.configure(state=tk.DISABLED)

            if len([x for x in input_Text2.get().replace(' ', ',').split(',')]) == 2:
                given2 = input_Text2.get().replace(' ', ',')
                output_Box2.configure(state=tk.NORMAL)
                output_Box2.delete(1.0, tk.END)
                arr2 = [float(x) for x in given2.split(',')]
                std2 = arr2[0]
                e = arr2[1]
                z2 = 2.576
                result2 = round(((z2 * std2) / e) ** 2, 2)
                str_result2 = str(result2)
                output_Box2.insert(tk.END, str_result2)
                output_Box2.configure(state=tk.DISABLED)

        def clear():
            input_Box.delete(0, tk.END)
            input_Box2.delete(0, tk.END)

        p90Btn = tk.Button(self, text='90%', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=p90)
        p90Btn.grid(row=6, column=0, pady=15)
        p95Btn = tk.Button(self, text='95%', width=25, height=4, bg='gray',
                          font=('Helvetica', 10, 'bold'), bd=4,
                          command=p95)
        p95Btn.grid(row=6, column=1, pady=15)
        p99Btn = tk.Button(self, text='99%', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=p99)
        p99Btn.grid(row=7, column=0, pady=15)

        clearBtn = tk.Button(self, text='Clear', width=25, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=clear)
        clearBtn.grid(row=7, column=1, pady=15)

class HT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        input_Text = tk.StringVar()
        input_Box = tk.Entry(self, textvariable=input_Text, font=('Helvetica', 14, 'bold'),
                             bg='black', fg='white', bd=25, highlightcolor='red', justify=tk.RIGHT,
                             width=41, insertbackground='white')
        input_Box.grid(row=0, column=0, columnspan=2)
        input_Box.insert(0, 'Input :  μ₀ , σ , n , x̄')

        output_Box = tk.Text(self, bg='white', bd=1, font=('Cambria', 20, 'bold'),
                             width=29, height=12)
        output_Box.grid(row=2, column=0, columnspan=2, pady=10)
        output_Box.configure(highlightbackground='powder blue', highlightcolor='powder blue',
                             state=tk.DISABLED)

        def click(event):
            if input_Box.get() == 'Input :  μ₀ , σ , n , x̄':
                event.widget.delete(0, tk.END)
            else:
                input_Box.config(foreground='white')

        input_Box.bind('<Button-1>', click)
        input_Box.bind('<FocusIn>', click)

        def test():
            if len([x for x in input_Text.get().replace(' ', ',').split(',')]) == 4:
                given = input_Text.get().replace(' ', ',')
                output_Box.configure(state=tk.NORMAL)
                output_Box.delete(1.0, tk.END)
                arr = [float(x) for x in given.split(',')]
                ev = arr[0]
                std = arr[1]
                n = arr[2]
                pmean = arr[3]
                result = round((pmean - ev) / (std / m.sqrt(n)), 2)
                str_result = str(result)
                output_Box.insert(tk.END, str_result)
                output_Box.configure(state=tk.DISABLED)

        def clear():
            input_Box.delete(0, tk.END)

        testBtn = tk.Button(self, text='Test Statistic', width=25, height=4, bg='gray',
                           font=('Helvetica', 10, 'bold'), bd=4,
                           command=test)
        testBtn.grid(row=1, column=0, pady=15)

        clearBtn = tk.Button(self, text='Clear', width=25, height=4, bg='gray',
                             font=('Helvetica', 10, 'bold'), bd=4,
                             command=clear)
        clearBtn.grid(row=1, column=1, pady=15)

class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='powder blue')
        sb = tk.Label(self, text='SUBMITTED BY:', bg='powder blue', fg='black',
                          font=('Cambria', 28, 'bold'), bd=0, width=20)
        sb.grid(row=0, column=0, padx=30, pady=20)
        bareng = tk.Label(self, text='Bareng, Shelzy', bg='powder blue', fg='black',
                      font=('Cambria', 24, 'bold'), bd=0)
        bareng.grid(row=1, column=0, pady=15)
        buduan = tk.Label(self, text='Buduan, Christian', bg='powder blue', fg='black',
                          font=('Cambria', 24, 'bold'), bd=0)
        buduan.grid(row=2, column=0, pady=15)
        bumanglag = tk.Label(self, text='Bumanglag, Eleina', bg='powder blue', fg='black',
                      font=('Cambria', 24, 'bold'), bd=0)
        bumanglag.grid(row=3, column=0, pady=15)
        clemente = tk.Label(self, text='Clemente, Kyron', bg='powder blue', fg='black',
                            font=('Cambria', 24, 'bold'), bd=0)
        clemente.grid(row=4, column=0, pady=15)
        lucero = tk.Label(self, text='Lucero, Jennica', bg='powder blue', fg='black',
                             font=('Cambria', 24, 'bold'), bd=0)
        lucero.grid(row=5, column=0, pady=15)
        magulod = tk.Label(self, text='Magulod, Floren', bg='powder blue', fg='black',
                             font=('Cambria', 24, 'bold'), bd=0)
        magulod.grid(row=6, column=0, pady=15)
        obsania = tk.Label(self, text='Obsania, Romeo', bg='powder blue', fg='black',
                          font=('Cambria', 24, 'bold'), bd=0)
        obsania.grid(row=7, column=0, pady=15)

app = Calculator()
app.mainloop()