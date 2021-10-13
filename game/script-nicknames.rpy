init 0 python in nicknames:
    
    # Nickname types
    NICKNAME_TYPE_INVALID = 0
    NICKNAME_TYPE_LOVED = 1
    NICKNAME_TYPE_NEUTRAL = 2
    NICKNAME_TYPE_DISLIKED = 3
    NICKNAME_TYPE_HATED = 4
    NICKNAME_TYPE_PROFANITY = 5
    NICKNAME_TYPE_FUNNY = 6
    
    # Natsuki loves these nicknames; awarding them awards affinity/trust
    NICKNAME_LOVED_LIST = [
        "babe",
        "amazing",
        "angel",
        "babygirl",
        "baby",
        "babycakes",
        "beautiful",
        "betterhalf",
        "boo",
        "bun bun",
        "bunbun",
        "bun-bun",
        "bunny",
        "buttercup",
        "butterscotch",
        "candy",
        "cookie",
        "cupcake",
        "cuteypie",
        "cutey",
        "cutiepie",
        "cutie",
        "darlin",
        "darling",
        "doll",
        "dollface",
        "dove",
        "gem",
        "gorgeous",
        "heartstring",
        "heart-string",
        "heartthrob",
        "heart-throb",
        "heaven",
        "honey",
        "honeybun",
        "hun",
        "ki",
        "kitten",
        "kitty",
        "love",
        "mine",
        "myflower",
        "mylove",
        "mylovely",
        "myprincess",
        "myqueen",
        "myrose",
        "natnat",
        "nat",
        "nat-nat",
        "natsu",
        "natsukitten",
        "natsukitty",
        "natty",
        "nattykins",
        "numberone",
        "precious",
        "princess",
        "qtpie",
        "qt",
        "queen",
        "snooki",
        "snookums",
        "special",
        "squeeze",
        "starlight",
        "starshine",
        "su",
        "sugar",
        "sugarlump",
        "sugarplum",
        "'suki",
        "suki",
        "summer",
        "sunny",
        "sunshine",
        "sweetcakes",
        "sweetpea",
        "sweetheart",
        "sweetie",
        "sweetness",
        "sweety"
        "the best"
    ]

    # Natsuki dislikes these nicknames; no penalty given but name will not be permitted
    NICKNAME_DISLIKED_LIST = [
        "baka",
        "dad",
        "daddy",
        "father",
        "lily",
        "moni",
        "monika",
        "monmon",
        "mon-mon",
        "papa",
        "sayo",
        "sayori",
        "yuri",
        "weeb"
    ]

    # Natsuki hates these (non-profanity) nicknames; awarding them detracts affinity/trust
    NICKNAME_HATED_LIST = [
        "arrogant",
        "brat",
        "bratty",
        "bonebag",
        "bonehead",
        "breadboard",
        "child",
        "clown",
        "cuttingboard",
        "dog",
        "dunce",
        "dumbo",
        "dimwit",
        "disgusting",
        "dumb",
        "dumbo",
        "dwarf",
        "dweeb",
        "fat",
        "fatso",
        "fatty",
        "flat",
        "gremlin",
        "halfling",
        "halfwit",
        "half-pint",
        "halfpint",
        "horrible",
        "horrid",
        "hungry",
        "gross",
        "idiot",
        "ignoramus",
        "ignorant",
        "imbecile",
        "imp",
        "ironingboard",
        "kid",
        "moron",
        "nasty",
        "nerd",
        "nimrod",
        "punchbag",
        "punch-bag",
        "punching-bag",
        "punchingbag",
        "putrid",
        "sick",
        "simpleton",
        "skinny",
        "slave",
        "smelly",
        "starved",
        "starving",
        "stinky",
        "stuck-up",
        "stupid",
        "tiny",
        "twerp",
        "twit",
        "useless",
        "vendingmachine",
        "vomit",
        "washboard",
        "wretch"
    ]

    # Natsuki hates these; awarding them detracts affinity/trust. Please forgive me.
    # Source courtest of: https://github.com/RobertJGabriel/Google-profanity-words
    NICKNAME_PROFANITY_LIST = [
        "4r5e",
        "5h1t",
        "5hit",
        "a_s_s",
        "a55",
        "aids",
        "anal",
        "anus",
        "ar5e",
        "arrse",
        "arse",
        "ass",
        "asses",
        "assfucker",
        "ass-fucker",
        "assfukka",
        "asshole",
        "assholes",
        "asswhole",
        "b!tch",
        "b00bs",
        "b17ch",
        "b1tch",
        "ballbag",
        "balls",
        "ballsack",
        "bastard",
        "beastial",
        "beastiality",
        "bellend",
        "bestial",
        "bestiality",
        "bi+ch",
        "biatch",
        "bitch",
        "bitcher",
        "bitchers",
        "bitches",
        "bitchin",
        "bitching",
        "bloody",
        "blow job",
        "blowjob",
        "blowjobs",
        "boiolas",
        "bollock",
        "bollok",
        "boner",
        "boob",
        "boobs",
        "booobs",
        "boooobs",
        "booooobs",
        "booooooobs",
        "breasts",
        "buceta",
        "bugger",
        "bum",
        "bunnyfucker",
        "butt",
        "butthole",
        "buttmunch",
        "buttplug",
        "c0ck",
        "c0cksucker",
        "carpetmuncher",
        "cawk",
        "chink",
        "cipa",
        "cl1t",
        "clit",
        "clitoris",
        "clits",
        "cnut",
        "cock",
        "cockface",
        "cockhead",
        "cockmunch",
        "cockmuncher",
        "cocks",
        "cocksuck",
        "cocksucked",
        "cocksucker",
        "cock-sucker",
        "cocksucking",
        "cocksucks",
        "cocksuka",
        "cocksukka",
        "cok",
        "cokmuncher",
        "coksucka",
        "coon",
        "cox",
        "crap",
        "cum",
        "cummer",
        "cumming",
        "cums",
        "cumshot",
        "cunilingus",
        "cunillingus",
        "cunnilingus",
        "cunt",
        "cuntlick",
        "cuntlicker",
        "cuntlicking",
        "cunts",
        "cyalis",
        "cyberfuc",
        "cyberfuck",
        "cyberfucked",
        "cyberfucker",
        "cyberfuckers",
        "cyberfucking",
        "d1ck",
        "damn",
        "dick",
        "dickhead",
        "dildo",
        "dildos",
        "dink",
        "dinks",
        "dirsa",
        "dlck",
        "dog-fucker",
        "doggin",
        "dogging",
        "donkeyribber",
        "doosh",
        "duche",
        "dyke",
        "ejaculate",
        "ejaculated",
        "ejaculates",
        "ejaculating",
        "ejaculatings",
        "ejaculation",
        "ejakulate",
        "f_u_c_k",
        "f4nny",
        "fag",
        "fagging",
        "faggitt",
        "faggot",
        "faggs",
        "fagot",
        "fagots",
        "fags",
        "fanny",
        "fannyflaps",
        "fannyfucker",
        "fanyy",
        "fatass",
        "fcuk",
        "fcuker",
        "fcuking",
        "feck",
        "fecker",
        "felching",
        "fellate",
        "fellatio",
        "fingerfuck",
        "fingerfucked",
        "fingerfucker",
        "fingerfuckers",
        "fingerfucking",
        "fingerfucks",
        "fistfuck",
        "fistfucked",
        "fistfucker",
        "fistfuckers",
        "fistfucking",
        "fistfuckings",
        "fistfucks",
        "flange",
        "fook",
        "fooker",
        "fuck",
        "fucka",
        "fucked",
        "fucker",
        "fuckers",
        "fuckhead",
        "fuckheads",
        "fuckin",
        "fucking",
        "fuckings",
        "fuckingshitmotherfucker",
        "fuckme",
        "fucks",
        "fuckwhit",
        "fuckwit",
        "fudge packer",
        "fudgepacker",
        "fuk",
        "fuker",
        "fukker",
        "fukkin",
        "fuks",
        "fukwhit",
        "fukwit",
        "fux",
        "fux0r",
        "gangbang",
        "gangbanged",
        "gangbangs",
        "gaylord",
        "gaysex",
        "goatse",
        "God",
        "god-dam",
        "goddamn",
        "goddamned",
        "god-damned",
        "hardcoresex",
        "hell",
        "heshe",
        "hoar",
        "hoare",
        "hoer",
        "homo",
        "hore",
        "horniest",
        "horny",
        "hotsex",
        "jackoff",
        "jack-off",
        "jap",
        "jerk-off",
        "jism",
        "jiz",
        "jizm",
        "jizz",
        "kawk",
        "knob",
        "knobead",
        "knobed",
        "knobend",
        "knobhead",
        "knobjocky",
        "knobjokey",
        "kock",
        "kondum",
        "kondums",
        "kum",
        "kummer",
        "kumming",
        "kums",
        "kunilingus",
        "l3i+ch",
        "l3itch",
        "labia",
        "lmfao",
        "lust",
        "lusting",
        "m0f0",
        "m0fo",
        "m45terbate",
        "ma5terb8",
        "ma5terbate",
        "masochist",
        "masterb8",
        "masterbat*",
        "masterbat3",
        "masterbate",
        "master-bate",
        "masterbation",
        "masterbations",
        "masturbate",
        "mof0",
        "mofo",
        "mo-fo",
        "mothafuck",
        "mothafucka",
        "mothafuckas",
        "mothafuckaz",
        "mothafucked",
        "mothafucker",
        "mothafuckers",
        "mothafuckin",
        "mothafucking",
        "mothafuckings",
        "mothafucks",
        "motherfuck",
        "motherfucked",
        "motherfucker",
        "motherfuckers",
        "motherfuckin",
        "motherfucking",
        "motherfuckings",
        "motherfuckka",
        "motherfucks",
        "muff",
        "mutha",
        "muthafecker",
        "muthafuckker",
        "muther",
        "mutherfucker",
        "n1gga",
        "n1gger",
        "nazi",
        "nigg3r",
        "nigg4h",
        "nigga",
        "niggah",
        "niggas",
        "niggaz",
        "nigger",
        "niggers",
        "nob",
        "nobhead",
        "nobjocky",
        "nobjokey",
        "numbnuts",
        "nutsack",
        "orgasim",
        "orgasims",
        "orgasm",
        "orgasms",
        "p0rn",
        "pawn",
        "pecker",
        "penis",
        "penisfucker",
        "phonesex",
        "phuck",
        "phuk",
        "phuked",
        "phuking",
        "phukked",
        "phukking",
        "phuks",
        "phuq",
        "pigfucker",
        "pimpis",
        "piss",
        "pissed",
        "pisser",
        "pissers",
        "pisses",
        "pissflaps",
        "pissin",
        "pissing",
        "pissoff",
        "poop",
        "porn",
        "porno",
        "pornography",
        "pornos",
        "prick",
        "pricks",
        "pron",
        "pube",
        "pusse",
        "pussi",
        "pussies",
        "pussy",
        "pussys",
        "rectum",
        "retard",
        "rimjaw",
        "rimming",
        "s hit",
        "s.o.b.",
        "s_h_i_t",
        "sadist",
        "schlong",
        "screwing",
        "scroat",
        "scrote",
        "scrotum",
        "semen",
        "sex",
        "sh!+",
        "sh!t",
        "sh1t",
        "shag",
        "shagger",
        "shaggin",
        "shagging",
        "shemale",
        "shi+",
        "shit",
        "shitdick",
        "shite",
        "shited",
        "shitey",
        "shitfuck",
        "shitfull",
        "shithead",
        "shiting",
        "shitings",
        "shits",
        "shitted",
        "shitter",
        "shitters",
        "shitting",
        "shittings",
        "shitty",
        "skank",
        "slut",
        "sluts",
        "smegma",
        "smut",
        "snatch",
        "son-of-a-bitch",
        "spac",
        "spunk",
        "t1tt1e5",
        "t1tties",
        "teets",
        "teez",
        "testical",
        "testicle",
        "tit",
        "titfuck",
        "tits",
        "titt",
        "tittie5",
        "tittiefucker",
        "titties",
        "tittyfuck",
        "tittywank",
        "titwank",
        "tosser",
        "turd",
        "tw4t",
        "twat",
        "twathead",
        "twatty",
        "twunt",
        "twunter",
        "v14gra",
        "v1gra",
        "vagina",
        "viagra",
        "vulva",
        "w00se",
        "wang",
        "wank",
        "wanker",
        "wanky",
        "whoar",
        "whore",
        "willies",
        "willy",
        "xrated",
        "xxx"
    ]

    # Natsuki finds these nicknames funny
    NICKNAME_FUNNY_LIST = [
        "gorgeous",
        "hot",
        "hotstuff",
        "hottie",
        "mama",
        "mom",
        "mommy",
        "mother",
        "mum",
        "mummy",
        "sexy",
        "smol",
        "snack"
    ]

    """
    Returns the nickname type for a given string nickname, defaulting to NICKNAME_TYPE_NEUTRAL

    IN:
        nickname - The nickname to test
    OUT:
        Nickname type, integer as defined in constant list
    """
    def get_nickname_type(nickname):

        if not isinstance(nickname, basestring):
            return NICKNAME_TYPE_INVALID
        
        else:
            nickname = nickname.lower().replace(" ", "")

            if nickname in NICKNAME_LOVED_LIST:
                return NICKNAME_TYPE_LOVED

            elif nickname in NICKNAME_DISLIKED_LIST:
                return NICKNAME_TYPE_DISLIKED

            elif nickname in NICKNAME_HATED_LIST:
                return NICKNAME_TYPE_HATED

            elif nickname in NICKNAME_PROFANITY_LIST:
                return NICKNAME_TYPE_PROFANITY

            elif nickname in NICKNAME_FUNNY_LIST:
                return NICKNAME_TYPE_FUNNY

            else:
                return NICKNAME_TYPE_NEUTRAL