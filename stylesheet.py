stylesheet = """

QPushButton{
    border :2px solid ;
    border-radius: 10;
    border-color : qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #d60cf0, stop:1 #9a08ed);
    color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #d60cf0, stop:1 #9a08ed);  
    font-size: 20px;
    font-weight: bold;
}

QPushButton:pressed{
    background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(240,213,255,180), stop:1 rgba(181,238,255,180));
}
QLineEdit{
    background: transparent;
    border:none;
    font-size: 20px;
}
MenuWindow{
    border-image: url(resources/key.png) 0 0 0 0 stretch stretch;
}
MenuWidget{
    border-radius: 10px;
    background-color: rgba(255,255,255,180);
}

MenuWidget QPushButton{
    max-height: 100px;
    max-width: 190px;
    margin-left: 15px;
    margin-right: 15px;
}

OptionsWidget, StatisticsWidget{
    background-color: rgba(255,255,255,180);
    margin-left: 100px;
    border-radius: 10px;
    padding: 50px;
    margin-top: 15px;
    border-right: 3px solid rgba(200,200,200,180);
    border-bottom: 3px solid rgba(200,200,200,180);
    border-left: 2px solid rgba(200,200,200,180);
    border-top: 2px solid rgba(200,200,200,180);
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
GameWindow{
    background-color: rgb(211,211,211);
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
    background-color: rgba(112,112,165,180);
    margin-left: 20px;
    border-radius: 5px;
    padding:20px;
}

GameWindowMenu{
    background-color: rgba(112,112,165,180);
    margin-left: 20px;
    border-radius: 5px;
    padding-top:20px;
    padding-bottom:20px;
}

KeyboardWidget{
    background-color: rgba(255,255,255,180);
    margin-top: 40px;
    border-radius: 5px;
    border: 3px solid rgb(112,112,170);
    border-right: 6px solid rgb(112,112,170);
    border-bottom: 6px solid rgb(112,112,170);
}

KeyboardWidget QPushButton{
    background-color: rgba(255,255,255,255);
    border-radius: 5;
}

GameWidget QFrame#text_input_frame{
    background-color: rgba(255,255,255,180);
    border-radius: 5px;
    border: 3px solid rgb(112,112,170);
    padding:10px;
}
"""