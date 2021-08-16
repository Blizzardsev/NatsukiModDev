default persistent._farewell_database = dict()

init python in farewells:
    import random
    import store

    # Natsuki will not ask a player to stay again if they agreed previously
    store.jn_globals.player_already_stayed = False

    FAREWELL_MAP = dict()

    def select_farewell():
        """
        Picks a random farewell, accounting for affinity
        If the player has already been asked to stay by Natsuki, a farewell without the option
        to stay will be selected
        """
        # Get the farewells the current affinity allows for us
        #TODO: Generalized filter function
        farewells_in_affinity_range = filter(lambda x: x.evaluate_affinity_range(), FAREWELL_MAP.values())

        # Filter any time-sensitive topics
        if divmod((store.utils.get_current_session_length()).total_seconds(), 60)[0] > 30:
            farewells_in_affinity_range = filter(
                lambda farewell: store.Topic.get_topic_has_additional_property_with_value(farewell, "is_time_sensitive", False),
                farewells_in_affinity_range
            ).label

        # If Natsuki has already asked her player to stay, filter any topics that would let her ask again, and return a random one
        if store.jn_globals.player_already_stayed:
            return random.choice(filter(
                lambda farewell: store.Topic.get_topic_has_additional_property_with_value(farewell, "has_stay_option", False),
                farewells_in_affinity_range
            )).label

        # Otherwise, just return a random farewell
        else:
            return random.choice(farewells_in_affinity_range).label

    def try_trust_dialogue():
        """
        Coinflip decision on whether to additionally call trust-based dialogue on farewell
        """
        if random.choice([True, False]):
            renpy.call_in_new_context("farewell_extra_trust")

    def get_time_in_session_descriptor():
        """
        Get a descriptor based on the number of minutes the player has spent in the session, up to 30 minutes

        OUT:
            Brief descriptor relating to the number of minutes spent in the session
        """
        minutes_in_session = divmod((farewells.store.utils.get_current_session_length()).total_seconds(), 60)[0]
        if minutes_in_session <= 1:
            time_in_session_descriptor = "like a minute"

        elif minutes_in_session <= 3:
            time_in_session_descriptor = "a couple of minutes"

        elif minutes_in_session > 3 and minutes_in_session <= 5:
            time_in_session_descriptor = "like five minutes"

        elif minutes_in_session > 5 and minutes_in_session <= 10:
            time_in_session_descriptor = "around ten minutes"

        elif minutes_in_session > 10 and minutes_in_session <= 15:
            time_in_session_descriptor = "around fifteen minutes"

        elif minutes_in_session > 15 and minutes_in_session <= 20:
            time_in_session_descriptor = "around twenty minutes"

        elif minutes_in_session <= 30:
            time_in_session_descriptor = "about half an hour"

        else:
            time_in_session_descriptor = "a while"

init 1 python:
    # DEBUG: TODO: Resets - remove these later, once we're done tweaking affinity/trust!
    try:
        store.persistent._farewell_database.pop("farewell_love_aff_1")
        store.persistent._farewell_database.pop("farewell_love_aff_2")
        store.persistent._farewell_database.pop("farewell_love_aff_3")
        store.persistent._farewell_database.pop("farewell_love_aff_4")
        store.persistent._farewell_database.pop("farewell_love_aff_5")

        store.persistent._farewell_database.pop("farewell_affectionate_enamored_aff_1")
        store.persistent._farewell_database.pop("farewell_affectionate_enamored_aff_2")
        store.persistent._farewell_database.pop("farewell_affectionate_enamored_aff_3")
        store.persistent._farewell_database.pop("farewell_affectionate_enamored_aff_4")
        store.persistent._farewell_database.pop("farewell_affectionate_enamored_aff_5")

        store.persistent._farewell_database.pop("farewell_happy_affectionate_aff_1")
        store.persistent._farewell_database.pop("farewell_happy_affectionate_aff_2")
        store.persistent._farewell_database.pop("farewell_happy_affectionate_aff_3")
        store.persistent._farewell_database.pop("farewell_happy_affectionate_aff_4")
        store.persistent._farewell_database.pop("farewell_happy_affectionate_aff_5")

        store.persistent._farewell_database.pop("farewell_normal_happy_aff_1")
        store.persistent._farewell_database.pop("farewell_normal_happy_aff_2")
        store.persistent._farewell_database.pop("farewell_normal_happy_aff_3")
        store.persistent._farewell_database.pop("farewell_normal_happy_aff_4")
        store.persistent._farewell_database.pop("farewell_normal_happy_aff_5")

        store.persistent._farewell_database.pop("farewell_upset_distressed_aff_1")
        store.persistent._farewell_database.pop("farewell_upset_distressed_aff_2")
        store.persistent._farewell_database.pop("farewell_upset_distressed_aff_3")
        store.persistent._farewell_database.pop("farewell_upset_distressed_aff_4")
        store.persistent._farewell_database.pop("farewell_upset_distressed_aff_5")

        store.persistent._farewell_database.pop("farewell_broken_ruined_aff_1")
        store.persistent._farewell_database.pop("farewell_broken_ruined_aff_2")
        store.persistent._farewell_database.pop("farewell_broken_ruined_aff_3")
        store.persistent._farewell_database.pop("farewell_broken_ruined_aff_4")
        store.persistent._farewell_database.pop("farewell_broken_ruined_aff_5")

        store.persistent._farewell_database.pop("farewell_gentle_ask")
        store.persistent._farewell_database.pop("farewell_pleading_ask")
        store.persistent._farewell_database.pop("farewell_fake_confidence_ask")
        store.persistent._farewell_database.pop("farewell_short_session_ask")
        store.persistent._farewell_database.pop("farewell_short_session_ask_alt")

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

# LOVE+ farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_aff_1:
    n "Aww...{w=0.3} you're leaving now,{w=0.1} [player]?{w=0.2} Well,{w=0.1} okay..."
    n "Y-you know I'll miss you,{w=0.1} right?"
    n "Take care, [player]! You mean the world to me!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_aff_2:
    n "You know I don't like saying goodbye,{w=0.1} [player]..."
    n "..."
    n "I'll be okay!{w=0.2} Just come back soon,{w=0.1} alright?"
    n "Stay safe,{w=0.1} dummy!{w=0.2} I love you!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_aff_3:
    n "Uuuu...{w=0.3} I never like saying goodbye to you..."
    n "But I guess it can't be helped,{w=0.1} [player]."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Take care of yourself out there,{w=0.1} [chosen_endearment]!{w=0.2} I'm counting on you!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_aff_4:
    n "Oh?{w=0.2} You're heading out now?"
    n "That's fine,{w=0.1} I guess..."
    n "I'll really miss you,{w=0.1} [player]."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Do your best,{w=0.1} [chosen_endearment]!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_aff_5:
    n "Huh?{w=0.2} You're leaving now?"
    n "I always hate it when you have to go somewhere..."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "...But I know you'll always be back for me,{w=0.1} [chosen_endearment]."
    n "Well...{w=0.1} I'm rooting for you!"
    n "Make me proud,{w=0.1} [player]! I love you!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

# AFFECTIONATE/ENAMORED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_aff_1:
    n "Hmm?{w=0.2} You're leaving now?"
    n "Aww,{w=0.1} man..."
    n "And I was having fun,{w=0.1} too..."
    n "Well,{w=0.1} if you gotta go,{w=0.1} you gotta go!"
    n "Take care,{w=0.1} [player]!{w=0.2} Make me proud!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_aff_2:
    n "You're going,{w=0.1} [player]?"
    n "Uuuuu...{w=0.3} okay..."
    n "Hurry back if you can,{w=0.1} alright?"
    n "I'll be waiting for you!"
    n "Goodbye,{w=0.1} [player]!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_aff_3:
    n "Huh?{w=0.2} You're leaving?"
    n "..."
    n "That's fine...{w=0.3} I'll be okay..."
    n "You better come back soon,{w=0.1} alright [player]?"
    n "Goodbye!{w=0.2} I'll miss you!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_aff_4:
    n "Oh?{w=0.2} Heading off now,{w=0.1} [player]?"
    n "I wish you didn't have to..."
    n "But I know you have things to do."
    n "Come see me later,{w=0.1} promise?"
    n "Don't make me come find you!{w=0.2} Ehehe."
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_aff_5:
    n "Mmm?{w=0.2} You're going now,{w=0.1} [player]?"
    n "I was hoping you'd be around longer..."
    n "Well,{w=0.2} I'll be okay!"
    n "Take care of yourself,{w=0.1} [player]!{w=0.2} For both of us!"
    n "See you later!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

# HAPPY/AFFECTIONATE farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_aff_1:
    n "Going now,{w=0.1} [player]?{w=0.2} I'll see you later!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_aff_2:
    n "Heading off now,{w=0.1} [player]?"
    n "Okay!{w=0.2} Take care!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_aff_3:
    n "Okaaay!{w=0.2} I'll be waiting for you!"
    n "Stay safe,{w=0.1} [player]!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_aff_4:
    n "See you later,{w=0.1} [player]!"
    n "Take care out there!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_aff_5:
    n "Goodbye,{w=0.1} [player]!"
    n "Come see me soon,{w=0.1} alright?"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

# NORMAL/HAPPY farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_aff_1:
    n "See you later, [player]!"
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_aff_2:
    n "Later, [player]!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_aff_3:
    n "Goodbye, [player]!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_aff_4:
    n "'kay! Bye for now!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_aff_5:
    n "See ya, [player]!"
    $ farewells.try_trust_dialogue()
    $ renpy.quit()

# UPSET/DISTRESSED farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_aff_1:
    n "Bye, [player]."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_aff_2:
    n "Later, [player]."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_aff_3:
    n "'kay, [player]. Later."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_aff_4:
    n "Goodbye, [player]."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
            "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_aff_5:
    n "See you around."
    $ renpy.quit()

# DISTRESSED/BROKEN/RUINED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_aff_1:
    n "Yeah."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_aff_2:
    n "Yep."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_aff_3:
    n "Uh huh."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_aff_4:
    n "..."
    $ renpy.quit()

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_aff_5:
    n "'kay."
    $ renpy.quit()

# Farewells that allow the player to choose to stay

# Natsuki calls the player out on how long they've been here, and asks for more time together
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": True
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask:
    n "What?{w=0.2} You're leaving?{w=0.2} But you've barely been here at all today,{w=0.1} [player]!"
    $ time_in_session_descriptor = farewells.get_time_in_session_descriptor()
    n "In fact, you've only been here for [time_in_session_descriptor]!"
    n "You're sure you can't stay just a little longer?"
    menu:
        "I can stay a little longer.":
            n "Yay{nw}!"
            n "I-I mean...!"
            n "Yeah!{w=0.2} That's what I thought!"
            n "Yeah..."
            n "..."
            n "Stop looking at me like that,{w=0.1} jeez!"
            n "Now,{w=0.1} where were we?"
            $ farewells.store.jn_globals.player_already_stayed = True

        "Sorry, Natsuki. I really have to leave.":
            n "Nnnnnn-!"
            n "..."
            n "Well...{w=0.3} alright."
            n "Don't take too long,{w=0.1} alright?"
            n "See you later!"
            $ farewells.try_trust_dialogue()
            $ renpy.quit()

    return

# Natsuki calls the player out on how long they've been here, and asks for more time together (alt)
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask_alt",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": True
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask_alt:
    n "N-now just wait one second,{w=0.1} [player]!{w=0.2} This isn't fair at all!"
    $ time_in_session_descriptor = farewells.get_time_in_session_descriptor()
    n "You've barely been here [time_in_session_descriptor],{w=0.1} and you're already going?"
    n "Come on!{w=0.2} You'll stay a little longer,{w=0.1} won't you?"
    menu:
        "Sure, I can stay a while.":
            n "H-Ha!{w=0.2} I knew it."
            n "Ehehe.{w=0.1} Looks like I win again,{w=0.1} [player]!"
            n "O-or maybe you just can't bring yourself to leave my side?"
            menu:
                "You got me, Natsuki. I couldn't leave you even if I tried.":
                    n "W-wha...?"
                    n "Nnnnnnn-!"
                    n "Don't just come out with stuff like that,{w=0.1} [player]!"
                    n "Jeez...{w=0.3} you're such a dummy sometimes..."

                "Yeah, yeah.":
                    n "Ehehe.{w=0.2} What's wrong,{w=0.1} [player]?"
                    n "A little too close to the truth?"
                    n "Ahaha!"

            n "Well,{w=0.1} either way,{w=0.1} I'm glad you can stay a little longer!"
            n "So...{w=0.3} what else did you wanna do today?"
            $ farewells.store.jn_globals.player_already_stayed = True
            $ relationship("affinity+")

        "Fine, I guess.":
            n "You {i}guess{/i}?{w=0.2} What do you mean,{w=0.1} you guess?!"
            n "Jeez...{w=0.3} what's with the attitude today, [player]?"
            n "Well, anyway...{w=0.3} Thanks for staying with me a little longer."
            n "Now,{w=0.1} where were we?"
            $ farewells.store.jn_globals.player_already_stayed = True

        "Sorry Natsuki, I can't right now.":
            n "Uuuu-"
            n "Well,{w=0.1} I guess that's fine.{w=0.2} It can't be helped,{w=0.1} after all."
            n "But you gotta make it up to me,{w=0.1} alright?"
            n "Stay safe,{w=0.1} [player]!{w=0.2} I'll see you later!"
            $ farewells.try_trust_dialogue()
            $ renpy.quit()
    return

# Natsuki tries to confidently ask her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fake_confidence_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fake_confidence_ask:
    n "Huh? You don't really have to leave already, do you?"
    n "It feels like you've barely been here!"
    n "I bet you can hang out with me a little longer! Right, [player]?"
    n "...right?"
    menu:
        "Right!":
            n "A-Aha!{w=0.2} I knew it!"
            n "I totally don't need you here,{w=0.1} or anything dumb like that!"
            n "You'd have to be pretty lonely to be {i}that{/i} dependent on someone else...{w=0.3} ahaha..."
            n "..."
            n "Jeez!{w=0.2} Let's just get back to it already..."
            n "Now,{w=0.1} where were we?"
            $ farewells.store.jn_globals.player_already_stayed = True
            $ relationship("affinity+")

        "Sorry, I really need to go.":
            n "Oh...{w=0.3} aha..."
            n "That's fine,{w=0.1} I guess..."
            n "I'll see you later then,{w=0.1} [player]!"
            n "Don't keep me waiting,{w=0.1} alright?"
            $ farewells.try_trust_dialogue()
            $ renpy.quit()
    return

# Natuski really doesn't want to be alone today; she pleads for her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_pleading_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.ENAMORED, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_pleading_ask:
    n "N-no!{w=0.2} You can't leave yet!"
    n "..."
    n "[player]...{w=0.3} I...{w=0.3} really...{w=0.3} want you here right now."
    n "Just stay with me a little longer...{w=0.3} please?"
    menu:
        "Of course!":
            n "Yes!{nw}"
            n "I-I mean...!"
            n "..."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n "T-thanks, [player].{w=0.1} You're [chosen_descriptor],{w=0.1} you know that?"
            n "Really.{w=0.1} Thank you."
            n "N-now,{w=0.1} where were we? Heh..."
            $ farewells.store.jn_globals.player_already_stayed = True
            $ relationship("affinity+")

        "I can't right now.":
            n "Oh..."
            n "Well,{w=0.1} if you gotta go,{w=0.1} it can't be helped,{w=0.1} I guess..."
            n "Come back soon,{w=0.1} alright?"
            n "Or you'll have to make it up to me...{w=0.3} ahaha..."
            n "Stay safe,{w=0.1} [player]!"
            $ farewells.try_trust_dialogue()
            $ renpy.quit()
    return

# Natsuki gently asks her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_gentle_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_gentle_ask:
    n "[player]...{w=0.3} do you really have to leave now?"
    n "I know you have stuff to do,{w=0.1} but I...{w=0.3} really...{w=0.3} wanna spend more time with you."
    n "Are you sure you have to go?"
    menu:
        "I can stay a little longer.":
            n "[player]..."
            n "Thank you.{w=0.1} That really means a lot to me right now."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n "Y-You're [chosen_descriptor], [player]."
            n "Truly.{w=0.1} Thanks..."
            n "..."
            n "Aha...{w=0.3} so what else did you wanna do today?"
            $ farewells.store.jn_globals.player_already_stayed = True
            $ relationship("affinity+")

        "Sorry, I really have to go.":
            n "Oh..."
            n "I'd be lying if I said I wasn't disappointed, but I understand."
            n "Just be careful out there, okay?"
            n "..."
            n "I-I love you,{w=0.1} [player]..."
            n "I'll see you later."
            $ farewells.try_trust_dialogue()
            $ renpy.quit()
    return

# Trust dialogue; chance to call upon farewell completing and prior to the game closing

label farewell_extra_trust:
    # ABSOLUTE+
    if store.trust.trust_is_between_bounds(
        lower_bound=store.jn_globals.TRUST_ABSOLUTE,
        trust=store.persistent.trust,
        upper_bound=None):
        n "My [player]...{w=0.3} I'll be waiting..."

    # FULL-COMPLETE
    elif store.trust.trust_is_between_bounds(
        lower_bound=store.jn_globals.TRUST_FULL,
        trust=store.persistent.trust,
        upper_bound=store.jn_globals.TRUST_ABSOLUTE):
        n "I'll be waiting..."

    # NEUTRAL-PARTIAL
    elif store.trust.trust_is_between_bounds(
        lower_bound=store.jn_globals.TRUST_NEUTRAL,
        trust=store.persistent.trust,
        upper_bound=store.jn_globals.TRUST_PARTIAL):
        n "You'll be back...{w=0.3} right?"

    # SCEPTICAL-NEUTRAL
    elif store.trust.trust_is_between_bounds(
        lower_bound=store.jn_globals.TRUST_SCEPTICAL,
        trust=store.persistent.trust,
        upper_bound=store.jn_globals.TRUST_NEUTRAL):
        n "I'll be okay...{w=0.3} I'll be okay..."

    # DIMINISHED-SCEPTICAL
    elif store.trust.trust_is_between_bounds(
        lower_bound=store.jn_globals.TRUST_DIMINISHED,
        trust=store.persistent.trust,
        upper_bound=store.jn_globals.TRUST_SCEPTICAL):
        n "...?"

    # DIMINISHED-
    elif store.trust.trust_is_between_bounds(
        lower_bound=None,
        trust=store.persistent.trust,
        upper_bound=store.jn_globals.TRUST_DIMINISHED):
        n "..."

    # Debug
    else:
        n "Um...{w=0.3} I think you messed up somewhere,{w=0.1} [player]...{w=0.3} Aha..."
        n "Bye now! Good luck fixing it!"
