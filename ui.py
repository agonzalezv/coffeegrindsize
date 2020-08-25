import PySimpleGUI as sg
from PIL import ImageTk, Image

sg.theme("GreenTan")

top_frame = sg.Frame(
    title="Anaylsis",
    layout=[
        [
            sg.Input(key="_FILEBROWSE_", enable_events=True, visible=False),
            sg.FileBrowse(
                key="image_filename",
                target="_FILEBROWSE_",
                button_text="Open Image",
                file_types=(
                    ("png files", "*.png"),
                    ("jpeg files", "*.jpg"),
                    ("jpeg files", "*.jpeg"),
                ),
                enable_events=True,
            ),
            sg.Button("Select Reference Object"),
            sg.Button("Select Anaylsis Region"),
            sg.Button("Threshold Image"),
            sg.Button("Launch Particle Detection"),
            sg.Button("Erase Clusters"),
            sg.Button("Create Histogram"),
            sg.Button("Read Blog"),
        ],
        [
            sg.Button("Reduce Image Quality"),
            sg.Button("Load Data"),
            sg.Button("Load Comparison Data"),
            sg.Button("Flush Comparison Data"),
            sg.Button("Save Data"),
            sg.Button("Save View"),
            sg.Button("Help"),
            sg.Button("Reboot"),
            sg.Button("Quit"),
        ],
    ],
)

other_top_frame = sg.Frame(
    title="Properties of the Particle Distribution",
    layout=[
        [
            sg.Text("Average Diameter :"),
            sg.Text("None (mm)"),
            sg.Text("Average Surface :"),
            sg.Text("None (Sq mm)"),
            sg.Text("Efficiency :"),
            sg.Text("None (%)"),
        ],
        [
            sg.Text("Scatter in Diameter :"),
            sg.Text("None (mm)"),
            sg.Text("Scatter in Surface :"),
            sg.Text("None (Sq mm)"),
            sg.Text("Quality :"),
            sg.Text("None"),
        ],
    ],
)

F1 = [
    sg.Frame(
        title="Pysical Scale of the Image",
        layout=[
            [sg.Text("Reference Pixel Length (px) :"), sg.InputText()],
            [sg.Text("Reference Physical Size (mm) :"), sg.InputText()],
            [sg.Text("Reference Object"), sg.InputText("I am a combobox")],
            [sg.Text("Pixel Scale (px/mm)"), sg.InputText()],
        ],
    )
]

F2 = [
    sg.Frame(
        title="Threshold Step", layout=[[sg.Text("Threshold (%) :"), sg.InputText()]],
    )
]

F3 = [
    sg.Frame(
        title="Particle Detection Step",
        layout=[
            [sg.Text("Max. Cluster Diameter (px) :"), sg.InputText()],
            [sg.Text("Min. Cluster Surface (Sq px) :"), sg.InputText()],
            [sg.Text("Min. Roundness"), sg.InputText()],
            [sg.CBox("Quick & Approximate")],
        ],
    )
]

F4 = [
    sg.Frame(
        title="Create Histogram Step",
        layout=[
            [sg.Text("Histogram Options :"), sg.InputText("I am a combobox")],
            [sg.Text("Label Position :"), sg.InputText("I am a combobox")],
            [sg.Text("Data Label"), sg.InputText("Current Data")],
            [sg.Text("Comparison Label"), sg.InputText("Comparison Data")],
            [sg.CBox("Auto X axis"), sg.Text("Min. X Axis"), sg.InputText("0.01"),],
            [sg.CBox("Log X axis"), sg.Text("Max. X Axis"), sg.InputText("10")],
            [sg.CBox("Auto Bins"), sg.Text("Bins"), sg.InputText("10")],
        ],
    )
]

F5 = [
    sg.Frame(
        title="Output Options",
        layout=[
            [
                sg.Text("Select Output Directory", justification="right"),
                sg.InputText("Default Folder"),
                sg.FolderBrowse(),
            ],
            [sg.Text("Base of File Names"), sg.InputText()],
        ],
    )
]

F6 = [
    sg.Frame(
        title="Display Options",
        layout=[[sg.Text("Display Type"), sg.InputText("I am a combobox")]],
    )
]

F7 = [
    sg.Frame(
        title=None,
        layout=[[sg.Button("Reset View"), sg.Button("Reset all Parameters")]],
    )
]

left_frame = sg.Frame(title=None, layout=[F1, F2, F3, F4, F5, F6, F7])

canvas_frame = sg.Frame(
    title="Canvas",
    layout=[[sg.Canvas(background_color="red", key="canvas", size=(1000,None))]],
)

layout = [[top_frame], [other_top_frame], [left_frame, canvas_frame]]

window = sg.Window("Coffee Particle Size Distribution by Jonathan Gagne", layout, resizable=True)
window.Finalize()

while True:
    event, values = window.read()
    # print(event, values)
    if event in (None, "Exit"):
        break
    if event == "_FILEBROWSE_":
        # update canvas
        image_filename = values.get("_FILEBROWSE_", None)

        # # Open image and remember it as the source image
        img = Image.open(image_filename)

        # # Set it to the current plotting object
        # self.display_type.set(original_image_display_name)

        # # Determine smallest zoom such that the full image fits in the canvas
        width_factor = img.size[0]
        height_factor = img.size[1]
        # scale_factor = min(width_factor, height_factor)
        # nx = round(scale_factor * self.img.size[0])
        # ny = round(scale_factor * self.img.size[1])

        # # Interpret the image with tkinter
        canvas_elem = window["canvas"]
        canvas = canvas_elem.TKCanvas
        image_obj = ImageTk.PhotoImage(img)
        canvas.create_image(640 / 2, 480 / 2, image=image_obj)

        # # Set the resulting scale in an internal variable
        # self.scale = scale_factor
        # self.original_scale = scale_factor

        # # Delete any object that was currently displayed
        # self.noimage_label.pack_forget()

        # # Refresh the image
        # self.redraw(x=self.canvas_width / 2, y=self.canvas_height / 2)

        # # Reset zoom to center the image properly
        # self.reset_zoom()

        # # Refresh the user interface status
        # self.status_var.set("Image opened: " + image_filename)

        # # Refresh the state of the user interface window
        # self.master.update()

window.close()
