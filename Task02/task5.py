if __name__ == "__main__":
    # Dictionary storing Dortmund events (key) and their dates (value)
    dortmund_events = {
        "Marquess Live Concert at Friedensplatz (Museumsnacht)": "2026-09-19",
        "3D Facade Mapping 'What is Wisdom' at Dortmunder U": "2026-09-19",
        "Musical Fireworks on the Town Hall Roof": "2026-09-19",
        "Reading with Sasa Stanisic & Frank Goosen": "2026-09-19",
        "Screen Printing Workshop at Kunsthalle Dortmund": "2026-09-19",
        "Exhibition & Fun/Noise Workshop at Dortmunder Kunstverein": "2026-09-19",
        "Nicolas Namoradze Piano Concert at Konzerthaus": "2026-09-19",
        "Culinary Experience Tour at Dortmund U-Tower": "2026-11-13",
        "La Klave Salsa & Bachata Festival": "2026-11-13",
        "Torsten Strater Live at Westfalenhallen": "2026-11-13",
    }

    target_date = "2026-09-19"

    print(f"Events running during the Night of Museums in Dortmund ({target_date}):\n")
    for event_name, event_date in dortmund_events.items():
        if event_date == target_date:
            print(f"- {event_name}")
