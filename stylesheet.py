stylesheet = """
QPushButton{
    border-image: url(resources/blue_button00.png);
    height: 49px;
    width: 190px;
    max-height: 49px;
    max-width: 190px;
    margin-left: 15px;
    margin-right: 15px;
    margin-top: 15px;
    color: white;  
    font-size: 18px;
}

QPushButton:pressed{
    border-image: url(resources/blue_button01.png);
    height: 45px;
    width: 190px;
}

OptionsWidget QLabel{
    font-size: 20px;
    max-height: 60px;
    margin-left: 15px;
    margin-right: 15px;
}

QLabel[cssClass = 'display']{
    border-image: url(resources/blue_button13.png);
    max-width: 400px;

    padding-left: 10px;
}

MenuWindow{
    border-image: url(resources/key.png) 0 0 0 0 stretch stretch ;
}

MenuWidget{
    background-color: rgba(255,255,255,180);
    padding-top: 30px;
}

OptionsWidget, StatisticsWidget{
    background-color: rgba(255,255,255,180);
    margin-top: 35px;
    margin-left: 100px;
}

GameWindow{
    background-color: rgba(112,112,112,200);
}

GameWindow QProgressBar{
    border: 2px solid gray;
    border-radius: 5px;
    text-align: center;
}

GameWindow QProgressBar::chunk{
    background-color: #05B8CC;
    width: 20px;
    margin: 0.5px;
}

GameWindow QLabel{
    font-size: 20px;
}
"""