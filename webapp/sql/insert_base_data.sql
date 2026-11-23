--@aylinRsl
-- Stammdaten, die in der DB schon enthalten sind

-- Codes für die jeweiligen Wohnheime sind gehasht in der dorm-Tabelle enthalten
INSERT INTO dormitory (name, verification_code) VALUES
    ('Wohnheim Eichkamp', 'CODE einfügen'),
    ('Wohnheim Fraunhoferstraße', 'CODE'),
    ('Wohnheim Goerzallee', 'CODE einfügen'),
    ('Wohnheim Halbauer Weg', 'CODE einfügen'),
    ('Wohnheim Haus Unger', 'CODE einfügen'),
    ('Wohnheim Hoppestraße', 'CODE einfügen'),
    ('Wohnheim Neue Hochstraße', 'CODE einfügen'),
    ('Wohnheim Oberfeldstraße (Vicror Jara)', 'CODE einfügen'),
    ('Wohnheim Pfalzburger Straße', 'CODE einfügen'),
    ('Wohnheim Wassertorplatz', 'CODE einfügen');

INSERT INTO category (name) VALUES
    ('Lernen & Nachhilfe'),
    ('Wohnen & WG'),
    ('Alltag & Unterstützung'),
    ('Fundsachen'),
    ('Tools & Skills'),
    ('Sonstiges');