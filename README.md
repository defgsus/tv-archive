# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**96** channels, **55,594.6** hours playtime between **2023-01-17** and **2023-02-16**


### playtime per genre (top 30)

    3893.7h 7.00% Nachrichten
    2864.9h 5.15% Verkaufsshow
    2363.2h 4.25% Krimiserie
    1908.8h 3.43% Dokusoap
    1873.1h 3.37% Werbesendung
    1638.9h 2.95% Dokureihe
    1605.7h 2.89% Regionalmagazin
    1403.7h 2.52% Dokumentation
    1390.0h 2.50% *unknown*
    1059.3h 1.91% Zeichentrickserie
    1025.3h 1.84% Infomercial
    1016.3h 1.83% Animationsserie
    937.1h  1.69% Comedyserie
    790.0h  1.42% Morgenmagazin
    732.3h  1.32% Talkshow
    731.9h  1.32% Programmende
    726.5h  1.31% Religionsmagazin
    615.4h  1.11% Magazin
    590.0h  1.06% E-Sport
    523.2h  0.94% Sitcom
    490.5h  0.88% Börsenmagazin
    484.0h  0.87% Wetterbericht
    464.6h  0.84% Wirtschaftsmagazin
    437.6h  0.79% Wissensmagazin
    428.5h  0.77% Quiz
    410.2h  0.74% Musikmagazin
    408.4h  0.73% Dramaserie
    399.4h  0.72% Gesundheitsmagazin
    398.8h  0.72% Telenovela
    365.4h  0.66% Gerichtsshow
