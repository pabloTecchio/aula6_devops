from tkinter import*


class funcoes_app:

    def vResultado():
        if str(inpQEx.get().isnumeric()):
            limite = int(inpQEx.get())
            if limite > 2001:
                limite = 2000
            else:
                r = funcoes_app.geraNum(limite)

                lblResultado['text'] = r
        else:
            pass

    def vPrimo(numero):
        for k in range(2, numero + 1):
            if k != numero:
                k = numero % k
                if k == 0:
                    return False
            else:
                return True

    def geraNum(limite):
        numeros = []
        contador_primos = 0
        numero_vez = 2

        while contador_primos < limite + 1:
            if funcoes_app.vPrimo(numero_vez) is True:
                numeros.append(numero_vez)
                contador_primos += 1

            numero_vez = numero_vez + 1

        return numeros

app = Tk()

altura = app.winfo_screenheight()
largura = app.winfo_screenwidth()

app.geometry(str(largura)+'x'+ str(altura))
app.minsize(width=int(largura/2), height=int(altura/2))
app.configure(background='#ffffff')
app.title('AC2 - DevOps')

lblTitle = Label(app)
lblTitle['text'] = 'AC2 - DevOps'
lblTitle['fg'] = '#780000'
lblTitle['bg'] = '#ffffff'
lblTitle['font'] = ('arial', '18', 'bold')
lblTitle.pack(side=TOP, fill=BOTH)

lblEx = Label(app)
lblEx['text'] = 'Digite a quantidade de números primos que você deseja ver'
lblEx['fg'] = '#780000'
lblEx['bg'] = '#ffffff'
lblEx['font'] = ('arial', '16', 'italic')
lblEx.pack(side=TOP, fill=BOTH)

inpQEx = Entry(app)
inpQEx['fg'] = '#000000'
inpQEx['bg'] = "#aaaaaa"
inpQEx['font'] = ('arial', '14')
inpQEx['width'] = 20
inpQEx.pack(side=TOP)

btnBusca = Button(app, command=funcoes_app.vResultado)
btnBusca['fg'] = '#000000'
btnBusca['text'] ='Buscar números PRIMOS'
btnBusca['bg'] = '#780000'
btnBusca['font'] = ('arial', '12', 'bold')
btnBusca['width'] = 30
btnBusca.pack(side=TOP)

lblResultado = Message(app)
lblResultado['bg'] = '#ffffff'
lblResultado['fg'] = '#780000'
lblResultado['font'] = ('arial', '10', 'bold')
lblResultado['width'] = largura - 100
lblResultado['pady'] = altura
lblResultado['justify'] = CENTER
lblResultado.pack(side=TOP, padx=50)

app.mainloop()
