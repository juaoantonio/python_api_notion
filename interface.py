import tkinter as tk


def token_getter():
    app = tk.Tk()
    app.title('Token de Acesso')
    app.geometry('300x100')
    app.eval('tk::PlaceWindow . center')

    label_land = tk.Label(app,
                          text="Token")
    label_land.grid(column=0, row=0, sticky=tk.W)

    token = tk.StringVar()
    entry_land = tk.Entry(app, width=20, textvariable=token)

    entry_land.grid(column=1, row=0, padx=10)

    confirm_button = tk.Button(app, text='Confirmar',
                               command=app.destroy)

    confirm_button.grid(column=0, row=2, pady=10, sticky=tk.W)

    app.mainloop()

    return token.get()
