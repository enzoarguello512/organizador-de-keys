from tkinter import Button
from tkinter import Checkbutton
from tkinter import END
from tkinter import Frame
from tkinter import IntVar
from tkinter import Menu
from tkinter import Scrollbar
from tkinter import Text
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog


def resource_path (relative_path):
    """El único propósito de esta función es poner bien el icono, porque auto-py-to-exe tiene un error al
    tratar de meter referencias externas y con esto lo 'arreglamos' """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath (".")

    return os.path.join (base_path, relative_path)


root = Tk()
root.title("Organizador de keys")
root.iconbitmap (resource_path ('default_icon.ico'))

MenuBar = Menu(root)
root.config(menu = MenuBar)
Frame_TextBox1 = Frame(root, width = 140, height = 140, bg = "black")
Frame_TextBox1.pack(fill = "both", expand = 1)
Frame_Buttons = Frame(root, width = 20, height = 20, bg = "black")
Frame_Buttons.pack(fill = "both", expand = 0)
Frame_TextBox2 = Frame(root, width = 140, height = 140, bg = "black")
Frame_TextBox2.pack(fill = "both", expand = 1)

# ----------------Functions/Variables-------------------------------------
VarRepetition = IntVar()

blacklist = ["GABEN", "G4B3N", "SCUM"]


def ExitApp():
    value = messagebox.askokcancel("Salir", "¿Desea salir del programa?")
    if value:
        root.destroy()


def HelpApp():
    messagebox.showinfo('Organizador de keys', 'Está a medio desarrollo el "programa" así que es muy probable que te '
                                               'encuentres algún que otro fallo . Entre los más destacables:'
                                               '\n*Intentar achicar el tamano de la ventana demasiado'
                                               '\n*Intentar ingresar caracteres inválidos en los casilleros de texto'
                                               '\n\nOriginalmente creado para hacer mucho más fácil '
                                               'registrar keys en steam , el formato en el que deja las keys está '
                                               'hecho para funcionar con ASF (archisteamfarm) por lo tanto es un '
                                               'requisito tenerlo')


def ReadFile(*event):
    global path
    try:
        var = filedialog.askopenfile(title = "Abrir...", mode = "r+", initialdir = "C:", filetypes = (
            ("Texto sin formato", "*.txt"), ("Todos los archivos", "*.*")))
        path = var.name
        Op_File = open(path, "r+", encoding = 'cp437', errors = 'ignore')
        Re_File = Op_File.read()
        TextBox1.delete("1.0", END)
        TextBox1.insert(END, Re_File)
        Op_File.close()
    except AttributeError:
        pass



def SaveFile(*event):
    try:
        with open(str(path), "w+") as f:
            SaveText = TextBox1.get("1.0", "end-1c")
            print(SaveText)
            f.seek(0)
            f.write(SaveText)
    except NameError:
        SaveAsFile(event)



def SaveAsFile(*event):
    global path

    try:
        Op_File = filedialog.asksaveasfile(title = "Guardar como...", initialdir = "C:", filetypes = (
            ("Texto sin formato", "*.txt"), ("Todos los archivos", "*.*")), defaultextension = ".*")
        SaveAsText = TextBox1.get("1.0", "end-1c")
        Op_File.write(SaveAsText)
        Op_File.close()
        path = Op_File.name
    except AttributeError:
        pass


def transformText():
    try:
        EntryText = TextBox1.get("1.0", "end-1c")

        def CheckRepetition(text):
            amount = {}
            ListAfterChange = []
            lastLetter = ""
            count = 1
            for letter in text:
                if lastLetter == letter:
                    count += 1
                    if count >= 4:
                        count = 404
                    amount[letter] += 1
                elif letter in amount:
                    lastLetter = letter
                    amount[letter] += 1
                else:
                    lastLetter = letter
                    amount[letter] = 1
            for key in amount:
                if amount[key] > 5:
                    ListAfterChange.append(key)
            if (len(ListAfterChange) > 0) or (count == 404):
                return True
            else:
                return False

        def split(text):
            return text.upper().split()

        def Reformat(var):
            num = 0
            for x in var:
                if x == "-":
                    num += 1
            if num == 2 or num == 4:
                return True
            return False

        def BList(key, blacklist):
            if any(item in key for item in blacklist):
                return True
            else:
                return False

        def Search_Keys(text, blacklist):
            KeyNotRept = []
            AllKeys = []
            Detected = []
            ObtainedKeys = []
            text = split(text)
            text = [x for x in text if "-" in x]
            for x in text:
                if Reformat(x):
                    Detected.append(x)
                else:
                    continue

            keys = [x.replace("-", "") for x in Detected]
            keys = [x for x in keys if len(x) == 15 or len(x) == 25]
            for x in keys:
                AllKeys.append("-".join([x[i:i + 5] for i in range(0, len(x), 5)]))

            def RemoveRKeys():
                for key in AllKeys:
                    fullkey = key.replace("-", "")
                    if not CheckRepetition(fullkey):
                        KeyNotRept.append(key)

            if VarRepetition.get() == 0:
                KeyNotRept = AllKeys
            elif VarRepetition.get() == 1:
                RemoveRKeys()

            for x in KeyNotRept:
                SplitKey = x.split("-")
                for part in SplitKey:
                    if len(SplitKey) == 5 or len(SplitKey) == 3:
                        if not "*" in x and not "@" in x:
                            if not BList(x, blacklist):
                                ObtainedKeys.append(x)

            ObtainedKeys = list(dict.fromkeys(ObtainedKeys))
            TextBox2.delete(1.0, END)
            if len(ObtainedKeys) == 0:
                TextBox2.insert(END, "No se detectaron keys")
            else:
                TextBox2.insert(END, "!redeem " + ",".join(ObtainedKeys))

        Search_Keys(EntryText, blacklist)

    except:
        messagebox.showinfo("Organizador de keys", "Se produjo un error inesperado")


# -----------------MiniMenus------------------------------------

ArchiveMenu = Menu(MenuBar, tearoff = 0)
ArchiveMenu.add_command(label = "Abrir...", command = ReadFile, accelerator = "Ctrl+O")
ArchiveMenu.add_command(label = "Guardar", command = SaveFile, accelerator = "Ctrl+S")
ArchiveMenu.add_command(label = "Guardar como...           ", command = SaveAsFile, accelerator = "Ctrl+Shift+S")  # Done intentionally
ArchiveMenu.add_separator()
ArchiveMenu.add_command(label = "Salir", command = ExitApp, accelerator = "Ctrl+Q")
MenuBar.add_cascade(label = "Archivo", menu = ArchiveMenu)

HelpMenu = Menu(MenuBar, tearoff = 0)
HelpMenu.add_command(label = "Acerca de...", command = HelpApp)
MenuBar.add_cascade(label = "Ayuda", menu = HelpMenu)

# ----------------Lockers-------------------------------------
TextBox1 = Text(Frame_TextBox1, width = 40, height = 10, bd = 5, relief = "ridge", bg = "white")

VertScroll1 = Scrollbar(Frame_TextBox1, command = TextBox1.yview)
VertScroll1.pack(fill = "y", expand = 0, pady = 10, padx = 10, side = "right")

TextBox1.config(yscrollcommand = VertScroll1.set)
TextBox1.pack(fill = "both", expand = 1, anchor = "center", side = "right", pady = 10, padx = 10)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
TextBox2 = Text(Frame_TextBox2, width = 40, height = 10, bd = 5, relief = "ridge", bg = "white")

VertScroll2 = Scrollbar(Frame_TextBox2, command = TextBox2.yview)
VertScroll2.pack(fill = "y", expand = 0, pady = 10, padx = 10, side = "right")

TextBox2.config(yscrollcommand = VertScroll2.set)
TextBox2.pack(fill = "both", expand = 1, anchor = "center", side = "right", pady = 10, padx = 10)

# ----------------Buttons-------------------------------------
ConvertButton = Button(Frame_Buttons, text = "Enviar", command = transformText, bd = 5, relief = "sunken",
                       bg = "yellow", cursor = "hand2")
ConvertButton.pack(fill = "x", expand = 1, anchor = "center", side = "left", pady = 2, padx = 5)

CheckRepButton = Checkbutton(Frame_Buttons, text = "Comprobar repeticiones de letras en keys",
                             variable = VarRepetition,
                             onvalue = 1, offvalue = 0, bd = 5, relief = "sunken", bg = "yellow", cursor = "hand2")
CheckRepButton.pack(expand = 1, anchor = "center", side = "right", pady = 10, padx = 10)

# ------------------Binds----------------------------------------
root.bind("<Control-o>", ReadFile)
root.bind("<Control-s>", SaveFile)
root.bind("<Control-S>", SaveAsFile)
root.bind("<Control-q>", lambda x: root.quit())
# ---------------------------------------------------------------
root.mainloop()