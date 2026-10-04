from flask import Flask, session
import random
import os

app = Flask(__name__)

# Needed so Flask can remember the previous verse
app.secret_key = os.environ.get("SECRET_KEY", "temporary-secret-key")

verses = [
    {
        "reference": "Philippians 4:13",
        "text": "I can do all things through Christ, who strengthens me."
    },
    {
        "reference": "Proverbs 3:5",
        "text": "Trust in Yahweh with all your heart, and don't lean on your own understanding."
    },
    {
        "reference": "Psalm 46:10",
        "text": "Be still, and know that I am God."
    },
    {
        "reference": "Isaiah 41:10",
        "text": "Don't you be afraid, for I am with you. Don't be dismayed, for I am your God."
    },
    {
        "reference": "Psalm 23:4",
        "text": "Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me."
    },
    {
        "reference": "Matthew 6:34",
        "text": "Therefore don't be anxious for tomorrow, for tomorrow will be anxious for itself."
    },
    {
        "reference": "Romans 8:28",
        "text": "We know that all things work together for good for those who love God."
    },
    {
        "reference": "Joshua 1:9",
        "text": "Haven't I commanded you? Be strong and courageous. Don't be afraid, neither be dismayed, for Yahweh your God is with you wherever you go."
    },
    {
        "reference": "Psalm 118:24",
        "text": "This is the day that Yahweh has made. We will rejoice and be glad in it!"
    },
    {
        "reference": "Psalm 34:8",
        "text": "Oh taste and see that Yahweh is good. Blessed is the man who takes refuge in him."
    },
    {
        "reference": "Psalm 56:3",
        "text": "When I am afraid, I will put my trust in you."
    },
    {
        "reference": "Psalm 119:105",
        "text": "Your word is a lamp to my feet, and a light for my path."
    },
    {
        "reference": "Psalm 37:4",
        "text": "Also delight yourself in Yahweh, and he will give you the desires of your heart."
    },
    {
        "reference": "Psalm 27:1",
        "text": "Yahweh is my light and my salvation. Whom shall I fear?"
    },
    {
        "reference": "Psalm 147:3",
        "text": "He heals the broken in heart, and binds up their wounds."
    },
    {
        "reference": "Proverbs 16:3",
        "text": "Commit your deeds to Yahweh, and your plans shall succeed."
    },
    {
        "reference": "Proverbs 17:17",
        "text": "A friend loves at all times; and a brother is born for adversity."
    },
    {
        "reference": "Proverbs 18:10",
        "text": "Yahweh's name is a strong tower: the righteous run to him, and are safe."
    },
    {
        "reference": "Isaiah 40:31",
        "text": "But those who wait for Yahweh will renew their strength. They will mount up with wings like eagles."
    },
    {
        "reference": "Isaiah 43:2",
        "text": "When you pass through the waters, I will be with you; and through the rivers, they will not overflow you."
    },
    {
        "reference": "Jeremiah 29:11",
        "text": "For I know the thoughts that I think toward you, says Yahweh, thoughts of peace, and not of evil, to give you hope and a future."
    },
    {
        "reference": "Matthew 5:14",
        "text": "You are the light of the world. A city located on a hill can't be hidden."
    },
    {
        "reference": "Matthew 7:7",
        "text": "Ask, and it will be given you. Seek, and you will find. Knock, and it will be opened for you."
    },
    {
        "reference": "Matthew 11:28",
        "text": "Come to me, all you who labor and are heavily burdened, and I will give you rest."
    },
    {
        "reference": "Matthew 19:26",
        "text": "With men this is impossible, but with God all things are possible."
    },
    {
        "reference": "Matthew 22:39",
        "text": "You shall love your neighbor as yourself."
    },
    {
        "reference": "Luke 1:37",
        "text": "For nothing spoken by God is impossible."
    },
    {
        "reference": "John 8:12",
        "text": "I am the light of the world. He who follows me will not walk in the darkness, but will have the light of life."
    },
    {
        "reference": "John 14:6",
        "text": "I am the way, the truth, and the life. No one comes to the Father, except through me."
    },
    {
        "reference": "John 14:27",
        "text": "Peace I leave with you. My peace I give to you; not as the world gives, give I to you."
    },
    {
        "reference": "John 15:5",
        "text": "I am the vine. You are the branches. He who remains in me, and I in him, the same bears much fruit."
    },
    {
        "reference": "Romans 12:12",
        "text": "Rejoicing in hope; enduring in troubles; continuing steadfastly in prayer."
    },
    {
        "reference": "Romans 12:21",
        "text": "Don't be overcome by evil, but overcome evil with good."
    },
    {
        "reference": "1 Corinthians 13:13",
        "text": "But now faith, hope, and love remain, these three. The greatest of these is love."
    },
    {
        "reference": "2 Corinthians 5:7",
        "text": "For we walk by faith, not by sight."
    },
    {
        "reference": "Ephesians 4:32",
        "text": "And be kind to one another, tenderhearted, forgiving each other, just as God also in Christ forgave you."
    },
    {
        "reference": "Ephesians 6:10",
        "text": "Finally, be strong in the Lord, and in the strength of his might."
    },
    {
        "reference": "Philippians 4:4",
        "text": "Rejoice in the Lord always! Again I will say, Rejoice!"
    },
    {
        "reference": "Philippians 4:6",
        "text": "In nothing be anxious, but in everything, by prayer and petition with thanksgiving, let your requests be made known to God."
    },
    {
        "reference": "Colossians 3:23",
        "text": "And whatever you do, work heartily, as for the Lord, and not for men."
    },
    {
        "reference": "1 Thessalonians 5:16",
        "text": "Always rejoice."
    },
    {
        "reference": "1 Thessalonians 5:17",
        "text": "Pray without ceasing."
    },
    {
        "reference": "2 Timothy 1:7",
        "text": "For God didn't give us a spirit of fear, but of power, love, and self-control."
    },
    {
        "reference": "Hebrews 11:1",
        "text": "Now faith is assurance of things hoped for, proof of things not seen."
    },
    {
        "reference": "Hebrews 13:8",
        "text": "Jesus Christ is the same yesterday, today, and forever."
    },
    {
        "reference": "James 1:5",
        "text": "But if any of you lacks wisdom, let him ask of God, who gives to all liberally and without reproach."
    },
    {
        "reference": "James 1:19",
        "text": "Let every man be swift to hear, slow to speak, and slow to anger."
    },
    {
        "reference": "1 Peter 5:7",
        "text": "Casting all your worries on him, because he cares for you."
    },
    {
        "reference": "1 John 4:19",
        "text": "We love him, because he first loved us."
    },
    {
        "reference": "Revelation 21:4",
        "text": "He will wipe away from them every tear from their eyes. Death will be no more."
    }
]


@app.route("/")
def home():

    # Get the verse that was shown last time
    last_verse = session.get("last_verse")

    # Create a list of all verse numbers
    available_verses = list(range(len(verses)))

    # Remove the previous verse so it cannot appear twice
    if last_verse is not None and last_verse in available_verses:
        available_verses.remove(last_verse)

    # Pick a random verse
    verse_number = random.choice(available_verses)

    # Remember this verse
    session["last_verse"] = verse_number

    # Get the actual verse
    verse = verses[verse_number]

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Random Bible Verse</title>

        <style>

            body {{
                margin: 0;
                font-family: Georgia, serif;
                background: linear-gradient(135deg, #f5efe6, #dfd1bd);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}

            .card {{
                background: white;
                width: 430px;
                max-width: 80%;
                padding: 50px;
                border-radius: 24px;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0,0,0,0.12);
            }}

            .title {{
                font-family: Arial, sans-serif;
                font-size: 11px;
                letter-spacing: 4px;
                color: #999;
            }}

            h1 {{
                font-size: 30px;
                margin-top: 12px;
            }}

            .verse {{
                font-size: 23px;
                line-height: 1.6;
                margin-top: 35px;
            }}

            .reference {{
                font-family: Arial, sans-serif;
                font-weight: bold;
                margin-top: 25px;
                font-size: 16px;
            }}

            .button {{
                display: inline-block;
                margin-top: 40px;
                padding: 15px 25px;
                background: #222;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-family: Arial, sans-serif;
                font-weight: bold;
                transition: 0.2s;
            }}

            .button:hover {{
                background: #555;
                transform: translateY(-2px);
            }}

            .footer {{
                font-family: Arial, sans-serif;
                font-size: 11px;
                color: #aaa;
                margin-top: 35px;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <div class="title">
                RANDOM BIBLE VERSE
            </div>

            <h1>A Word for You</h1>

            <div class="verse">
                “{verse["text"]}”
            </div>

            <div class="reference">
                {verse["reference"]}
            </div>

            <a class="button" href="/">
                Generate New Verse
            </a>

            <div class="footer">
                50 verses • World English Bible
            </div>

        </div>

    </body>

    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)