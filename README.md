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

**96** channels, **11,887.6** hours playtime between **2023-01-17** and **2023-01-23**


### playtime per genre (top 30)

    800.9h 6.74% Nachrichten
    653.8h 5.50% Verkaufsshow
    485.2h 4.08% Krimiserie
    399.2h 3.36% Dokusoap
    388.3h 3.27% Werbesendung
    358.1h 3.01% Dokureihe
    338.5h 2.85% *unknown*
    333.6h 2.81% Regionalmagazin
    308.6h 2.60% Dokumentation
    245.2h 2.06% Infomercial
    222.1h 1.87% Zeichentrickserie
    201.5h 1.70% Animationsserie
    198.7h 1.67% Comedyserie
    167.6h 1.41% Talkshow
    164.5h 1.38% Religionsmagazin
    147.8h 1.24% Magazin
    136.7h 1.15% E-Sport
    129.3h 1.09% Morgenmagazin
    119.8h 1.01% Programmende
    102.8h 0.87% Wirtschaftsmagazin
    98.6h  0.83% Sitcom
    98.5h  0.83% Wissensmagazin
    98.5h  0.83% Wirtschaftstalk
    98.0h  0.82% Musikmagazin
    97.5h  0.82% Tennis
    95.5h  0.80% Dramaserie
    93.2h  0.78% Wetterbericht
    91.0h  0.77% Drama
    81.6h  0.69% Gesundheitsmagazin
    80.7h  0.68% Krankenhausserie
