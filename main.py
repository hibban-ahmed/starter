# from fastapi import FastAPI
# import random

# app = FastAPI()

# quotes = [
#     'Be yourself; everyone else is already taken. — Oscar Wilde',
#     'In the middle of difficulty lies opportunity. — Albert Einstein',
#     'Life is what happens when you’re busy making other plans. — John Lennon',
#     'The only way to do great work is to love what you do. — Steve Jobs',
#     'Do what you can, with what you have, where you are. — Theodore Roosevelt',
#     'Happiness is not something ready made. It comes from your own actions. — Dalai Lama',
#     'Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau',
#     'Don’t watch the clock; do what it does. Keep going. — Sam Levenson',
#     'You miss 100percentage of the shots you don’t take. — Wayne Gretzky',
#     'Whether you think you can or you think you can’t, you’re right. — Henry Ford',
#     'The best way out is always through. — Robert Frost',
#     'Dream big and dare to fail. — Norman Vaughan',
#     'Turn your wounds into wisdom. — Oprah Winfrey',
#     'To live is the rarest thing in the world. Most people exist, that is all. — Oscar Wilde',
#     'What we think, we become. — Buddha',
#     'Everything you can imagine is real. — Pablo Picasso',
#     'The journey of a thousand miles begins with one step. — Lao Tzu',
#     'It does not matter how slowly you go as long as you do not stop. — Confucius',
#     'You only live once, but if you do it right, once is enough. — Mae West',
#     'Believe you can and you’re halfway there. — Theodore Roosevelt',
#     'The mind is everything. What you think you become. — Buddha',
#     'Change your thoughts and you change your world. — Norman Vincent Peale',
#     'Keep your face always toward the sunshine—and shadows will fall behind you. — Walt Whitman',
#     'The only limit to our realization of tomorrow is our doubts of today. — Franklin D. Roosevelt',
#     'Do not go where the path may lead, go instead where there is no path and leave a trail. — Ralph Waldo Emerson',
#     'Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill',
#     'Act as if what you do makes a difference. It does. — William James',
#     'Happiness depends upon ourselves. — Aristotle',
#     'The purpose of our lives is to be happy. — Dalai Lama',
#     'Your time is limited, so don’t waste it living someone else’s life. — Steve Jobs',
#     'You become what you believe. — Oprah Winfrey',
#     'Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. — Roy T. Bennett',
#     'Everything has beauty, but not everyone sees it. — Confucius',
#     'The best revenge is massive success. — Frank Sinatra',
#     'The harder the conflict, the more glorious the triumph. — Thomas Paine',
#     'We become what we think about. — Earl Nightingale',
#     'Do one thing every day that scares you. — Eleanor Roosevelt',
#     'The secret of getting ahead is getting started. — Mark Twain',
#     'Fall seven times, stand up eight. — Japanese Proverb',
#     'The only person you are destined to become is the person you decide to be. — Ralph Waldo Emerson',
#     'You can’t go back and change the beginning, but you can start where you are and change the ending. — C.S. Lewis',
#     'Don’t let yesterday take up too much of today. — Will Rogers',
#     'Success is not how high you have climbed, but how you make a positive difference to the world. — Roy T. Bennett',
#     'To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. — Ralph Waldo Emerson',
#     'Doubt kills more dreams than failure ever will. — Suzy Kassem',
#     'It always seems impossible until it’s done. — Nelson Mandela',
#     'You don’t have to be great to start, but you have to start to be great. — Zig Ziglar',
#     'I am not a product of my circumstances. I am a product of my decisions. — Stephen Covey',
#     'Don’t count the days, make the days count. — Muhammad Ali',
#     'Opportunities don’t happen. You create them. — Chris Grosser',
#     'The best dreams happen when you’re awake. — Cherie Gilderbloom',
#     'To handle yourself, use your head; to handle others, use your heart. — Eleanor Roosevelt',
#     'If you want to lift yourself up, lift up someone else. — Booker T. Washington',
#     'A smooth sea never made a skilled sailor. — Franklin D. Roosevelt',
#     'What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson',
#     'Don’t be afraid to give up the good to go for the great. — John D. Rockefeller',
#     'Start where you are. Use what you have. Do what you can. — Arthur Ashe',
#     'The best preparation for tomorrow is doing your best today. — H. Jackson Brown Jr.',
#     'Great things never come from comfort zones. — Anonymous',
#     'Be so good they can’t ignore you. — Steve Martin',
#     'Sometimes the smallest step in the right direction ends up being the biggest step of your life. — Naeem Callaway',
#     'You have within you right now, everything you need to deal with whatever the world can throw at you. — Brian Tracy',
#     'Do not wait to strike till the iron is hot; but make it hot by striking. — William Butler Yeats',
#     'The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt',
#     'When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. — Henry Ford',
#     'Don’t judge each day by the harvest you reap but by the seeds that you plant. — Robert Louis Stevenson',
#     'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. — Christian D. Larson',
#     'The best way to predict your future is to create it. — Abraham Lincoln',
#     'Success is liking yourself, liking what you do, and liking how you do it. — Maya Angelou',
#     'It is never too late to be what you might have been. — George Eliot',
#     'The only thing standing between you and your goal is the story you keep telling yourself. — Jordan Belfort',
#     'Your life does not get better by chance, it gets better by change. — Jim Rohn',
#     'If opportunity doesn’t knock, build a door. — Milton Berle',
#     'Magic is believing in yourself, if you can do that, you can make anything happen. — Johann Wolfgang von Goethe',
#     'Don’t let the fear of losing be greater than the excitement of winning. — Robert Kiyosaki',
#     'Do not fear failure but rather fear not trying. — Roy T. Bennett',
#     'You are never too old to set another goal or to dream a new dream. — C.S. Lewis',
#     'Nothing will work unless you do. — Maya Angelou',
#     'Success is walking from failure to failure with no loss of enthusiasm. — Winston Churchill',
#     'When you arise in the morning, think of what a precious privilege it is to be alive. — Marcus Aurelius',
#     'A goal without a plan is just a wish. — Antoine de Saint-Exupéry',
#     'The difference between ordinary and extraordinary is that little extra. — Jimmy Johnson',
#     'Don’t be discouraged. It’s often the last key in the bunch that opens the lock. — Unknown',
#     'Life isn’t about finding yourself. Life is about creating yourself. — George Bernard Shaw',
#     'Your only limit is your mind. — Unknown',
#     'Great minds discuss ideas; average minds discuss events; small minds discuss people. — Eleanor Roosevelt',
#     'Courage doesn’t always roar. Sometimes courage is the quiet voice at the end of the day saying, “I will try again tomorrow.” — Mary Anne Radmacher',
#     'Do not go where the path may lead, go instead where there is no path and leave a trail. — Ralph Waldo Emerson',
#     'It’s not whether you get knocked down, it’s whether you get up. — Vince Lombardi',
#     'The best way to find yourself is to lose yourself in the service of others. — Mahatma Gandhi',
#     'Don’t stop when you’re tired. Stop when you’re done. — Marilyn Monroe',
#     'If you want to fly, give up everything that weighs you down. — Buddha',
#     'Don’t wait. The time will never be just right. — Napoleon Hill',
#     'Energy and persistence conquer all things. — Benjamin Franklin',
#     'Believe that life is worth living and your belief will help create the fact. — William James',
#     'Try not to become a man of success but rather try to become a man of value. — Albert Einstein',
#     'The harder you work for something, the greater you’ll feel when you achieve it. — Unknown',
#     'Success is the sum of small efforts, repeated day in and day out. — Robert Collier',
#     'If you don’t like something, change it. If you can’t change it, change your attitude. — Maya Angelou',
#     'Keep going. Be all in. — Bryan Hutchinson',
# ]

# @app.get("/random-quote")
# def random_quote():
#     return {"quote": random.choice(quotes)}

# @app.get("/")
# def root():
#     return {"message": "Welcome! Use /random-quote to get a quote."}


# from fastapi import FastAPI
# import httpx
# import random
# import os

# app = FastAPI()

# SUPABASE_URL = os.getenv("https://earpvsgouyfhuqmjtuca.supabase.co")
# SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVhcnB2c2dvdXlmaHVxbWp0dWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI2Nzc3MjAsImV4cCI6MjA2ODI1MzcyMH0.HUi-r_wrtlBfXnJKRUfcI3W4UDqwhM6ygtK2EsAKr4A")

# headers = {
#     "apikey": SUPABASE_KEY,
#     "Authorization": f"Bearer {SUPABASE_KEY}",
# }

# @app.get("/random-quote")
# async def random_quote():
#     async with httpx.AsyncClient() as client:
#         # Fetch all quotes (or you can optimize for random selection server-side)
#         response = await client.get(f"{SUPABASE_URL}/rest/v1/quotes?select=text", headers=headers)
#         response.raise_for_status()
#         quotes = response.json()
#         if not quotes:
#             return {"error": "No quotes found"}
#         selected = random.choice(quotes)
#         return {"quote": selected['text']}

from fastapi import FastAPI, HTTPException
import asyncpg
import os

app = FastAPI()

SUPABASE_URL = os.getenv("https://earpvsgouyfhuqmjtuca.supabase.co")  # like 'xyzcompany.supabase.co'
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVhcnB2c2dvdXlmaHVxbWp0dWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI2Nzc3MjAsImV4cCI6MjA2ODI1MzcyMH0.HUi-r_wrtlBfXnJKRUfcI3W4UDqwhM6ygtK2EsAKr4A")  # your anon key
DATABASE_URL = f"postgresql://anon:{SUPABASE_KEY}@{SUPABASE_URL[8:]}/postgres"

@app.get("/random-quote")
async def random_quote():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        row = await conn.fetchrow("SELECT text FROM quotes ORDER BY RANDOM() LIMIT 1;")
        await conn.close()
        if row:
            return {"quote": row['text']}
        else:
            return {"error": "No quotes found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {"status": "ok", "message": "API is running"}
