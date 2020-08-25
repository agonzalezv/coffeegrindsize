# Import the required packages

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import numpy as np


def CreateDropdown(
    self, label, choices, method, default_choice_index=0, advanced=False
):

    # Create a variable that will be bound to the dropdown menu
    data_var = StringVar()

    # First option is the initial choice by default
    data_var.set(choices[default_choice_index])

    # Create a label for the dropdown menu
    dropdown_label = Label(self.frame_options, text=label)
    dropdown_label.grid(row=self.options_row, sticky=E)

    # Also create simple version if needed
    if advanced is False:
        simple_dropdown_label = Label(self.simple_frame_options, text=label)
        simple_dropdown_label.grid(row=self.simple_options_row, sticky=E)

    # Create the dropdown menu itself
    dropdown_menu = OptionMenu(self.frame_options, data_var, *choices)
    dropdown_menu.grid(row=self.options_row, column=1, columnspan=2, sticky=EW)

    # Also create simple version if needed
    if advanced is False:
        simple_dropdown_menu = OptionMenu(self.simple_frame_options, data_var, *choices)
        simple_dropdown_menu.grid(
            row=self.simple_options_row, column=1, columnspan=2, sticky=EW
        )

    # Link the tropdown menu to a method
    data_var.trace("w", method)

    # Update the display row
    self.options_row += 1

    # Also update simple version if needed
    if advanced is False:
        self.simple_options_row += 1

    # Return internal variable to caller
    return data_var


# Method to display a label in the options frame
def CreateEntryWithLabels(
    self,
    default_var,
    text,
    units_text,
    columnspan=None,
    width=None,
    entry_id=False,
    clear_on_click=False,
    event_on_entry=None,
    addcol=0,
    event_on_enter=None,
    advanced=False,
):

    # Default width is located in the internal class variables
    if width is None:
        width = self.width_entries

    # Introduce a variable to be linked with the entry dialogs
    data_var = StringVar()

    # Set variable to default value
    data_var.set(str(default_var))

    # Display the label for the name of the option
    if text != "":
        data_label = Label(self.frame_options, text=text)
        data_label.grid(row=self.options_row, sticky=E, column=addcol)
        # Also display simplified version if required
        if advanced is False:
            simple_data_label = Label(self.simple_frame_options, text=text)
            simple_data_label.grid(row=self.simple_options_row, sticky=E, column=addcol)

    # Link data entry to an event if this is required
    if event_on_entry is not None:
        # Determine the function to be triggered
        function_trigger = getattr(self, event_on_entry)
        data_var.trace(
            "w", lambda name, index, mode, data_var=data_var: function_trigger()
        )

    # Display the data entry box
    data_entry = Entry(self.frame_options, textvariable=data_var, width=width)
    data_entry.grid(row=self.options_row, column=1 + addcol, columnspan=columnspan)

    # Bind Entry with clearing of data
    if clear_on_click is True:
        data_entry.bind("<Button-1>", lambda event: self.clear_entry(data_entry))

    # Also display simplified version if required
    if advanced is False:
        simple_data_entry = Entry(
            self.simple_frame_options, textvariable=data_var, width=width
        )
        simple_data_entry.grid(
            row=self.simple_options_row, column=1 + addcol, columnspan=columnspan
        )
        # Bind Entry with clearing of data
        if clear_on_click is True:
            simple_data_entry.bind(
                "<Button-1>", lambda event: self.clear_entry(simple_data_entry)
            )

    # Bind the return key with a method
    if event_on_enter is not None:
        function_trigger = getattr(self, event_on_enter)
        data_entry.bind("<Return>", function_trigger)
        if advanced is False:
            simple_data_entry.bind("<Return>", function_trigger)

    # Display the physical units of this option
    if units_text != "":
        data_label_units = Label(self.frame_options, text=units_text)
        data_label_units.grid(row=self.options_row, column=2 + addcol, sticky=W)
        # Also display simplified version if required
        if advanced is False:
            simple_data_label_units = Label(self.simple_frame_options, text=units_text)
            simple_data_label_units.grid(
                row=self.simple_options_row, column=2 + addcol, sticky=W
            )

    # Update the row where next labels and entries will be displayed
    self.options_row += 1

    # Also updated row of simplified window if required
    if advanced is False:
        self.simple_options_row += 1

    # Return data entry ID to caller if required
    if entry_id is True:
        if advanced is False:
            return data_var, data_entry, simple_data_entry
        else:
            return data_var, data_entry
    else:
        # Otherwise return just value of the bound variable to the caller
        return data_var


# Method to display a title for option groups
def CreateTitleLabel(self, text, advanced=False):

    # Add label to the simplified frame if this is not an advanced option
    if advanced is False:
        title_label = Label(
            self.simple_frame_options, text=text, font="Helvetica 16 bold"
        )
        title_label.grid(
            row=self.simple_options_row, sticky=W, padx=self.title_padx, columnspan=2,
        )
        self.simple_options_row += 1

    # Add label to the advanced frame
    title_label = Label(self.frame_options, text=text, font="Helvetica 16 bold")
    title_label.grid(row=self.options_row, sticky=W, padx=self.title_padx, columnspan=2)
    self.options_row += 1


# Method to display a vertical blank separator in the options frame
def CreateLabelSeparator(self, advanced=False, simpleonly=False):
    if simpleonly is False:
        separator_label = Label(self.frame_options, text="")
        separator_label.grid(row=self.options_row)
        self.options_row += 1
    if advanced is False:
        simple_separator_label = Label(self.simple_frame_options, text="")
        simple_separator_label.grid(row=self.simple_options_row)
        self.simple_options_row += 1
