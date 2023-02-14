import PySimpleGUI as sg
import launcher

def main():
    # テーマを決める
    sg.theme("DarkBlue")

    # 表示する画面の設定
    layout = [[sg.Text("Click buttons")],
        [sg.Button(key="excel", size=(1,1), image_filename="./images/excel_icon.png"), 
         sg.Button(key="knime", size=(1,1), image_filename="./images/knime_icon.png")]]

    window = sg.Window("GUI App Launcher", layout, size=(600, 600))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "excel":
            launcher.launch_excel()
        elif event == "knime":
            launcher.launch_knime()

    window.close()

if __name__ == '__main__':
    main()
