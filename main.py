import customtkinter


# customtkinter apperance and color theme
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # individual color options
        numeric_buttons_color = '#3797FF'

        # window configuration
        self.title("CCA - Calculator & Convert App")
        self.geometry(f"{650}x{580}")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # navigation label
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame,
                                                             text="Calculate & Convert\nApplication",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # navigation buttons
        self.calculator_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                         border_spacing=10,
                                                         text="Calculator",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         anchor="w", command=self.calculator_button_event)
        self.calculator_button.grid(row=1, column=0, sticky="ew")

        self.contacts_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                       border_spacing=10, text="Contacts",
                                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w",
                                                       command=self.contacts_button_event)
        self.contacts_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"), anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        """CALCULATOR FRAME"""
        # functions first
        # method for recognizing a clicked number and putting it into input
        def btn_click(item):
            nonlocal expression
            expression = expression + str(item)
            input_text.set(expression)

        # this method calculates the expression
        # present in input field
        def btn_equal():
            nonlocal expression
            result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
            input_text.set(result)
            expression = result

        # this metod clear entry input
        def btn_clear():
            nonlocal expression
            expression = ""
            input_text.set("")

        # this metod delete single character from entry input
        def btn_delete():
            nonlocal expression
            expression = expression[:-1]
            input_text.set(expression)

        # globally declare the expression variable
        expression = ""

        # StringVar() is the variable class
        # we create an instance of this class
        input_text = customtkinter.StringVar()

        # create calculator frame
        self.calculator_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.calculator_frame.grid_rowconfigure((1, 2, 3, 4, 5), weight=0, uniform="row")
        self.calculator_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="column")

        # calculator display
        self.calculator_display = customtkinter.CTkEntry(self.calculator_frame, textvariable=input_text)
        self.calculator_display.grid(row=0, column=0, columnspan=4, padx=5, pady=(30, 10), sticky="nsew")
        self.calculator_display.configure(state="disabled", height=40)

        # keyboard binding for calculator input
        # numbers
        self.bind('1', lambda event: btn_click(1))
        self.bind('2', lambda event: btn_click(2))
        self.bind('3', lambda event: btn_click(3))
        self.bind('4', lambda event: btn_click(4))
        self.bind('5', lambda event: btn_click(5))
        self.bind('6', lambda event: btn_click(6))
        self.bind('7', lambda event: btn_click(7))
        self.bind('8', lambda event: btn_click(8))
        self.bind('9', lambda event: btn_click(9))
        self.bind('0', lambda event: btn_click(0))
        # other functions
        self.bind("/", lambda event: btn_click("/"))
        self.bind('*', lambda event: btn_click("*"))
        self.bind('+', lambda event: btn_click("+"))
        self.bind('-', lambda event: btn_click("-"))
        self.bind('<BackSpace>', lambda event: btn_delete())
        self.bind('<Return>', lambda event: btn_equal())
        self.bind('<Delete>', lambda event: btn_clear())

        # row functions on the top of buttons
        self.calculator_frame_button_allclear = customtkinter.CTkButton(self.calculator_frame, text="CE",
                                                                        command=lambda: btn_delete())
        self.calculator_frame_button_allclear.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_clear = customtkinter.CTkButton(self.calculator_frame, text="C",
                                                                     command=lambda: btn_clear())
        self.calculator_frame_button_clear.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_divide = customtkinter.CTkButton(self.calculator_frame, text="/",
                                                                      command=lambda: btn_click("/"))
        self.calculator_frame_button_divide.grid(row=1, column=2, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_multiply = customtkinter.CTkButton(self.calculator_frame, text="*",
                                                                        command=lambda: btn_click("*"))
        self.calculator_frame_button_multiply.grid(row=1, column=3, padx=2, pady=2, sticky="nsew")

        # row 789
        self.calculator_frame_button_7 = customtkinter.CTkButton(self.calculator_frame, text="7",
                                                                 command=lambda: btn_click(7),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_7.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_8 = customtkinter.CTkButton(self.calculator_frame, text="8",
                                                                 command=lambda: btn_click(8),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_8.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_9 = customtkinter.CTkButton(self.calculator_frame, text="9",
                                                                 command=lambda: btn_click(9),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_9.grid(row=2, column=2, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_minus = customtkinter.CTkButton(self.calculator_frame, text="-",
                                                                     command=lambda: btn_click("-"))
        self.calculator_frame_button_minus.grid(row=2, column=3, padx=2, pady=2, sticky="nsew")

        # row 456
        self.calculator_frame_button_4 = customtkinter.CTkButton(self.calculator_frame, text="4",
                                                                 command=lambda: btn_click(4),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_4.grid(row=3, column=0, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_5 = customtkinter.CTkButton(self.calculator_frame, text="5",
                                                                 command=lambda: btn_click(5),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_5.grid(row=3, column=1, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_6 = customtkinter.CTkButton(self.calculator_frame, text="6",
                                                                 command=lambda: btn_click(6),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_6.grid(row=3, column=2, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_plus = customtkinter.CTkButton(self.calculator_frame, text="+",
                                                                    command=lambda: btn_click("+"))
        self.calculator_frame_button_plus.grid(row=3, column=3, padx=2, pady=2, sticky="nsew")

        # row 123
        self.calculator_frame_button_1 = customtkinter.CTkButton(self.calculator_frame, text="1",
                                                                 command=lambda: btn_click(1),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_1.grid(row=4, column=0, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_2 = customtkinter.CTkButton(self.calculator_frame, text="2",
                                                                 command=lambda: btn_click(2),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_2.grid(row=4, column=1, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_3 = customtkinter.CTkButton(self.calculator_frame, text="3",
                                                                 command=lambda: btn_click(3),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_3.grid(row=4, column=2, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_equals = customtkinter.CTkButton(self.calculator_frame, text="=",
                                                                      command=lambda: btn_equal())
        self.calculator_frame_button_equals.grid(row=4, column=3, rowspan=2, padx=2, pady=2, sticky="nsew")

        # row with functions on the bottom of buttons
        self.calculator_frame_button_0 = customtkinter.CTkButton(self.calculator_frame, text="0",
                                                                 command=lambda: btn_click(0),
                                                                 fg_color=numeric_buttons_color)
        self.calculator_frame_button_0.grid(row=5, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")

        self.calculator_frame_button_decimal = customtkinter.CTkButton(self.calculator_frame, text=".",
                                                                       command=lambda: btn_click("."),
                                                                       )
        self.calculator_frame_button_decimal.grid(row=5, column=2, padx=2, pady=2, sticky="nsew")

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("calculator")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.calculator_button.configure(fg_color=("gray75", "gray25") if name == "calculator" else "transparent")
        self.contacts_button.configure(fg_color=("gray75", "gray25") if name == "contacts" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "calculator":
            self.calculator_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.calculator_frame.grid_forget()
        if name == "contacts":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def calculator_button_event(self):
        self.select_frame_by_name("calculator")

    def contacts_button_event(self):
        self.select_frame_by_name("contacts")

    def frame_3_button_event(self):
        self.select_frame_by_name("more soon")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


# run application
if __name__ == "__main__":
    app = App()
    app.mainloop()
