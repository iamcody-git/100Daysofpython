import PySimpleGUI as sg
from zip_creater import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")


label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FileBrowse("Choose")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File compressor", layout=[[label1, input1,choose_button1],
                                              [label2,input2,choose_button2],
                                              [compress_button, output_label]])

while True:
    event, value = window.read()
    print(event, value)
    filepaths = value["files"].split(";")
    folder = value["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value = "compressed is done")


window.read()
window.close()