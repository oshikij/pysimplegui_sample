import subprocess

def launch_excel():
    subprocess.Popen(['open', '/Applications/Microsoft Excel.app'])

def launch_knime():
    subprocess.Popen(['open', '/Applications/KNIME 4.5.2.app'])

if __name__ == '__main__':
  launch_excel()
  launch_knime()
