stylesheet = """

QPushButton{
    border :2px solid ;
    border-color : qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #d60cf0, stop:1 #9a08ed);
    color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #d60cf0, stop:1 #9a08ed);  
    font-size: 20px;
    font-weight: bold;
}

QPushButton:pressed{
    background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(240,213,255,180), stop:1 rgba(181,238,255,180));
}

MenuWidget{
    border-radius: 60px;
    border-image: url(resources/menubg.png);
}

MenuWidget QPushButton{
    max-height: 100px;
    max-width: 190px;
    margin-left: 180px;
    margin-right: 15px;
}

OptionsWidget, StatisticsWidget{
    background-color: rgba(255,255,255,255);
    margin-left: 100px;
    border-radius: 60px;
    padding: 100px;
    margin-top: 15px;
}

OptionsWidget QLabel{
    font-size: 20px;
    max-height: 60px;
    margin-left: 15px;
    margin-right: 15px;
}
OptionsWidget QPushButton{
    max-height: 60px;
    max-width: 190px;
}

QLabel[cssClass = 'display']{
    border-image: url(resources/blue_button13.png);
    max-width: 400px;
    padding-left: 10px;
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

GameWidget{
    background-color: rgba(255,255,255,255);
    margin-left: 100px;
    border-radius: 60px;
    padding:60px;
}

GameWindowMenu{
    background-color: rgba(255,255,255,255);
    margin-left: 60px;
    border-radius: 60px;
    padding-top:60px;
    padding-bottom:60px;
}
"""