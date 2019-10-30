To get stated with this project python version used 3.8.0

install pyenv or any other python version manager
then make a virtual env named 3-8-0

pip install pytest
pip install selenium


We have used chromediver 
chrome driver with pip is not working 

once chrome driver has been install do 

which chromedriver (linux command)

copy paste path in chromeWebDriver.py

EXAMPLE
self.wd = webdriver.Chrome(executable_path='PATH') windows
seld.wd = webdriver.Chrome('/usr/local/bin/chromedriver') MacOS (homebrew install)
self.wd = webdriver.Chrome('/usr/bin/chromedriver') linux (please check not confirm )


Then once setup complete run

python main.py (terminal)