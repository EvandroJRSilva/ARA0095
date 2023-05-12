from flexx import flx

class Exemplo(flx.Widget):

    def init(self):
        with flx.HBox():
            flx.Button(text='Olá', flex=1)
            flx.Button(text='Mundo', flex=2)

app = flx.App(Exemplo, title='Flexx demonstração')
app.launch('browser')
flx.run()