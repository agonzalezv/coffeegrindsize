# Coffee Grind Size User Manual. 

You can download this instructions [here](./Help/coffee_grind_size_installation.pdf).

## Downloading the app

You can download [the latest release here](https://github.com/jgagneastro/coffeegrindsize/releases/latest).

After downloading, you can place this file anywhere. (e.g., in your `/Applications` directory). 

## Installing the app

The first time you try to open it by double-clicking, you will get the following error message, because I am an _evil_ non-registered Apple developer.

![1](./media/1.png "1")

There is a workaround for this problem. You need to open your computer’s System Preferences by clicking on the Apple logo on the upper left corner of your screen, then choose System Preferences. This will get you here:

![3](./media/3.png "3")

The next step is to go in “Security & Privacy” (highlighted above), and make sure you are in the “General” tab:

![2](./media/2.png "2")

Note how something new appeared in this options window: there’s a message about "coffeegrindsize.app" having been blocked from running because I’m not an Apple Developer. 

You can allow it to open anyway by clicking “Open Anyway” (it is possible that you will need to click on the locker symbol on the lower left window and enter your admin password first).

Once you did this, you can go back to the .app file, and double-click it again. You will get one last warning:

![4](./media/4.png "4")

But this time, you can choose “Open”, in which case you will not need to do any of this next time you open the app !

Then, you can choose to either read this [quick summary](./Help/coffee_grind_size_summarized_manual.pdf) that will get you running with the basics, or this very detailed and wordy [user manual](./Help/coffee_grind_size_manual.pdf) that will guide you through all the detailed options the application offers you.

### [coffeeadastra.com](https://coffeeadastra.com/2019/04/07/an-app-to-measure-your-coffee-grind-size-distribution-2/)

## Building the app

If you know your way around python, you could build the app from source.

- `cd coffeegrindsize/` (this folder)

If you use py2app : 

- `python3 setup.py py2app --packages=PIL` to build for deployment 
- (or) `python3 setup.py py2app -A` to build for testing.

If you use pyinstaller : 

`pyinstaller --onefile --windowed --noconfirm --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' coffeegrindsize.py --clean 
--hidden-import="pkg_resources.py2_warn"`

## Troubleshooting. 

**Note:** (YMMV)

If you have issues building or running the built app, you may need some, of all the packages outlined below: 

```
brew install tcl-tk openssl readline sqlite3 \
             xz zlib pygobject3 gtk+3 pkg-config \
             qt sip pyqt libpng freetype libjpeg \
             jpeg openjpeg zlib
```

Also, you may need the following python libraries: 

```
pip3 install \
  matplotlib pandas tkinter numpy jupyter \
  PyQt5 PyQt4 pycairo cairocffi PyGObject \
  ipython tornado Cython pytest ipykernel \
  configparser six pillow Image macholib \
  scipy pyinstaller setuptools wxPython \
  pysimplegui
```
