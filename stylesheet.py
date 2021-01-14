stylesheet = """
MenuWidget QPushButton{
    border :2px solid ;
    border-color : qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #d60cf0, stop:1 #9a08ed);
    max-height: 100px;
    max-width: 190px;
    margin-left: 15px;
    margin-right: 15px;
    color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #d60cf0, stop:1 #9a08ed);  
    font-size: 20px;
    font-weight: bold;
}

MenuWidget QPushButton:pressed{
    background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(240,213,255,180), stop:1 rgba(181,238,255,180));
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