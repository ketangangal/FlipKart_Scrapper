# Flipkart Review Scrapper
This is a flask based app to scrap user reviews and comments from a retail website and generates word-cloud with CSV data. 
The data that was gathered is available to download as well.


## Prerequisites
1. Environment setup.
```commandline
conda create --prefix ./env python=3.8 -y
conda activate ./env
```
2. Install Requirements
```commandline
pip install -r requirements.txt
```
3. Run setup to make internal packages usable
```commandline
pip install -e .
```
4. Run App 
windows
```commandline
python app.py 
```
Mac/linux
```commandline
python3 app.py 
```

## Running the tests
Navigate to flipkart_scrapper_testing/tests.py
```commandline
python tests.py
```
Be sure that your app is running.
Results after running tests.py

![img.png](img.png)

## Interface 
![img_1.png](img_1.png)
## Built With

1. FastApi 
2. Python
3. Html 
4. Css
5. shell script

## Authors
iNeuron Private limited
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
