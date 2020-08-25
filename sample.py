import PySimpleGUI as sg

layout = [
    [sg.Text("Slider Demonstration"), sg.Text("", key="_OUTPUT_")],
    [
        sg.T("0", key="_LEFT_"),
        sg.Slider(
            (1, 100),
            key="_SLIDER_",
            orientation="h",
            enable_events=True,
            disable_number_display=True,
        ),
        sg.T("0", key="_RIGHT_"),
    ],
    [sg.Button("Show"), sg.Button("Exit")],
]

window = sg.Window("Window Title", layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event is None or event == "Exit":
        break
    window["_LEFT_"].update(values["_SLIDER_"])
    window["_RIGHT_"].update(values["_SLIDER_"])

window.close()
