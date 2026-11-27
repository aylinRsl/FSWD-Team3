
-- Stammdaten, die in der DB schon enthalten sind

-- Codes für die jeweiligen Wohnheime sind gehasht in der dorm-Tabelle enthalten
INSERT INTO dormitory (name, verification_code) VALUES
    --random code generator + scrypt hash
    ('Wohnheim Eichkamp', 'scrypt:32768:8:1$VPkZtBKpHZcwzOgc$20e6fb80e1e92474804a3bdb65ff9dedb48caccd5046e4bd6b713a62362b6f2fcf75e68d267566c106abd9c67683c5e37116cce50f7adca3395f171e766db542'), 
    ('Wohnheim Fraunhoferstraße', 'scrypt:32768:8:1$R6bnloCEzHLjA7p8$ee553ed73b27d785fa9111738640be20c3ea916f967a63728485f57b98afbcdd1c7fd6d8ced05ce2c73a0f5dd1c722e23a2b041bcaaf792af9de85a1841960e5'),
    ('Wohnheim Goerzallee', 'scrypt:32768:8:1$DArQldrS6rXSaa1s$8e196f6f26fbd6968036ebe03d6bbda3a8c4e8abd9288d899a24890a05da1560975690c5c137b45af4ca5334561a7b080e57174c0aaeace5320e90a911120a1a'),
    ('Wohnheim Halbauer Weg', 'scrypt:32768:8:1$hFh4bDSI7oiQSLal$1083de2b17d6bf6a57215839f79e6c3e6c7cb3cf408e12a94cdc9eb4891b0d2aaab7b78d6e1f7e65c17e82a516e5433897f6c1f9c8f7750edf0b595493f37ea1'),
    ('Wohnheim Haus Unger', 'scrypt:32768:8:1$C2k4N8FkrXTidjFi$8e87ea5b5a9a0f49880d8d6078b04d2099e1e3c71997f3ac8bbf4da63274758836d733cd0c8d486be15c4a5ddede0094e9942816089412e3520bf6929f4fe6d6'),
    ('Wohnheim Hoppestraße', 'scrypt:32768:8:1$fCkGk2DJCVmNtTPe$f7a92a1d67e790cc314202ccf296d91c788eb66250a188d8023e3c76b85cdc76494618c949e66e8179536758e549dc22f72b5a13b74d4610ba18c4338c4c443d'),
    ('Wohnheim Neue Hochstraße', 'scrypt:32768:8:1$Be5fwf51KipHNvb7$41a3b31979c08db0bc7ef9d00b89e96c6ba8db53401ef58dd0d14e373b7f8c74667d9402062298738c9287cc7abbe62cf66a0c37b2024ad0bbe0a0371a0706f9'),
    ('Wohnheim Oberfeldstraße (Vicror Jara)', 'scrypt:32768:8:1$7jotiLhhXArK2AqI$7a30fd1171848080075da33c7da277d8cb2693fa5fd0809c1c86850e7877c020477f57c356a2ec2b6162db72f9ba2ac11515b76b1a83243e300ddc0a0b577430'),
    ('Wohnheim Pfalzburger Straße', 'scrypt:32768:8:1$4KrMuxJCzTQZUvGW$14aefb4a739b7845c97cb1b5f02deba535ae35d1171db7cab8b9f21216d91233e6d7ace2b52e5b653fdc5a327ec55976272041ab6fc1e8dd184431a310267e4a'),
    ('Wohnheim Wassertorplatz', 'scrypt:32768:8:1$g1jtJGJ1FwqXfMz8$9aa7873e99f81a14c770780b06b543bcd4627fadbc1ea15cb480a2ca6b06c39b72d2ec9d80578632415af4146ec3aee53bf37e46a008012a8f45c3bd75a9690d');

INSERT INTO category (name) VALUES
    ('Lernen & Nachhilfe'),
    ('Wohnen & WG'),
    ('Alltag & Unterstützung'),
    ('Fundsachen'),
    ('Tools & Skills'),
    ('Sonstiges');
