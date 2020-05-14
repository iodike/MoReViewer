'''
Imports
'''
import sys
import pkg_resources
import subprocess
from src.main.MRE_MainWindow import *
from src.main.MRE_SplashScreen import *


def checkPackages():
    '''
    Check if all necessary packages are installed
    and install missing packages.
    '''

    print("Checking for missing packages...")

    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = REQUIRED - installed

    if missing:
        confirm = input("The following packages are missing: %s.\n"
                        "Do you want to install them now? [Y/N] " % list(missing))

        if confirm.lower() == "yes" or confirm.lower() == "y":
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
            print("Done.")

        else:
            exit(0)

    else:
        print("Packages up-to-date.")

    return


'''
Start App
'''
if __name__ == "__main__":

    checkPackages()

    # app settings
    app = QApplication(sys.argv)
    app.setApplicationName(APP_SHORT_NAME)
    app.setWindowIcon(QIcon('media/app-icons/nlp.ico'))
    app.setOrganizationName(ORG_NAME)
    app.setOrganizationDomain(ORG_ID)
    app.setApplicationDisplayName(APP_SHORT_NAME)
    app.setApplicationVersion(APP_VERSION)

    # main window
    mainWin = MRE_MainWindow()
    mainWin.setWindowTitle(app.applicationDisplayName())
    mainWin.show()

    sys.exit(app.exec_())
