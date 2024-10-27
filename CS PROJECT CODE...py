print("WELCOME TO READER'S LOUNGE")


import time
import random
from PIL import Image
import mysql.connector 
con=mysql.connector.connect(host='localhost', user='root', password='1234')
cur=con.cursor()

cur.execute("create database if not exists books ")

cur.execute("use books")

    #1- Autobiographies n biographies
cur.execute(' create table if not exists bio (sno int primary key, book_name varchar (60), author_name varchar (60))')

try:
    cur.execute("""insert into bio values (1, 'The Diary of a Young Girl','Anne Frank'),
                                    (2, 'Becoming', 'Michelle Obama'),
                                    (3,'Wings of Fire', 'A.P.J abdul kalam and Arun Tiwari'),
                                    (4, 'A Long Walk to Freedom', 'Nelson Mandela'),
                                    (5, 'The Story of my Life', 'Hellen Keller'),
                                    (6,'The Autobiography of Benjamin Franklin', 'Benjamin Franklin'),
                                          (7,'Mein Kampf', 'Adolf Hitler'),
                                          (8,'Dreams for my Father','Barack Obama'),
                                          (9, 'I Know Why The Caged Bird Sings', 'Maya Angelou'),
                                          (10,'Steve Jobs', 'Walter Isaacson'),
                                          (11,'Born a Crime', 'Trevor Noah'),
                                          (12, 'Know My Name', ' Chanel Miller'),
                                          (13, 'Up From Slavery','Booker.T,Washington'),
                                          (14,'A Movable Feast', ' Earnst Hemmingsway'),
                                          (15,'Shoe Dog','Phil Knight')""")




    con.commit()

except:
    pass



#2- Children's Book
cur.execute(' create table if not exists child (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into child values (1, 'Charlottes web','E.B. White'),
                                      (2, 'Alice Adventures In Wonderland', 'Lewis Caroll') ,
                                      (3,'Charlie And The Chocolate Factory', 'Roald Dahl'),
                                      (4, 'Matilda', 'Roald Dahl'),
                                      (5, 'The Little Prince', 'Antoine de Saint Emepery'),
                                      (6,'The Wonderful Wizard Of Oz', 'L.Frank Baum'),
                                      (7,'The Jungle Book', 'Rudyard Kipling'),
                                      (8,'The Secret Garden','Frances Hodgson Burnett'),
                                      (9, 'The Hobbit', 'J.R.R Tolkein'),
                                      (10,'The Tale of peter rabbit', 'Beatrix Potter'),
                                      (11,'Black Beauty', 'Anna Sewell'),
                                      (12, 'The wind and the willows', ' Kenneth Grahame'),
                                      (13, 'Winnie The Pooh','A.A.Milne'),
                                      (14,'The Cat in the Hat', ' Dr. Seuss'),
                                      (15,'The Phanton Tollbooth','Norton Justen'),
                                      (16,'Green Eggs And The Ham','Dr. Seuss')''')




    con.commit()
except:
    pass


#3- Classic
cur.execute(' create table if not exists classic (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into classic values (1, 'To Kill a Mocking Bird','Harper Lee'),
                                      (2, '1984', 'George Orwell') ,
                                      (3,'Jane Eyre', 'Charlotte Bronte'),
                                      (4, 'Little Women', 'Charlotte Bronte'),
                                      (5, 'The Catcher in the Rye', 'J.D. Salinger'),
                                      (6,'Animal Farm', 'George Orwell'),
                                      (7,'Dracula', 'Bram Stoker'),
                                      (8,'Great Expectations','Charles Dickens'),
                                      (9, 'A Tale of Two Cities', 'Charles Dickens'),
                                      (10,'A Christmas Carol', 'Charles Dickens'),
                                      (11,'Hamlet', 'Shakespeare'),
                                      (12, 'Julius Caesar', ' Shakespeare'),
                                      (13, 'Pride and Prejudice','Jane Austen'),
                                      (14,'The Great Gatsby', ' F.Scott Fitzgerald'),
                                      (15,'Oliver Twist','Charles Dickens'),
                                      (16,'The Tempest','Shakespeare')''')




    con.commit()
except:
    pass



#4-Fantasy 
cur.execute(' create table if not exists fan (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into fan values (1, 'The Lord of thr Rings','J.R.R Tolkien'),
                                      (2, 'A Game Of Thrones', 'George R.R. Martin') ,
                                      (3,'The Way of Kings', 'Brandon Sanderson'),
                                      (4, 'Harry Potter and the Deathly Hallows', 'J.K Rowling'),
                                      (5, 'The Night Circus', 'Erin Morgenstern'),
                                      (6,'The Name Of the Wind', 'Patrick Rothfuss'),
                                      (7,'The Lies of Locke Lamora', 'Scott Lynch'),
                                      (8,'Harry Potter and the Philosophers Stone','J.K Rowling'),
                                      (9, 'The Eye of the World', 'Robert Jordan'),
                                      (10,'Six Of Crows', 'Leigh Bardugo'),
                                      (11,'The Fifth Season', 'N.K Jemisin'),
                                      (12, 'A Dance with Dragons', ' Geaorge R.R. Martin'),
                                      (13, 'A Storm of Swords','Geaorge R.R. Martin'),
                                      (14,'The Two Towers', 'J.R.R Tolkien'),
                                      (15,'The Wise Mans Fear','Patrick Rothfuss'),
                                      (16,'The Mist of Avalon','Marion Zimmer Bradley'),
                                      (17,'The Princess Bride','William Goldman')''')




    con.commit()
except:
    pass

#5-History 
cur.execute(' create table if not exists his (sno int primary key, book_name varchar (60), author_name varchar (60))')

try:
    cur.execute('''insert into his values (1, 'Grant','Ron Chernow'),
                                      (2, 'Gengis Khan And the Making of the Modern World', 'Jack Weatherford') ,
                                      (3,'The History of Ancient World', 'Susan Wise Bauer'),
                                      (4, 'Democracy', 'Paul Cartledge'),
                                      (5, 'Churchill', 'Andrew Roberts'),
                                      (6,'The Womans Hour', 'Elaine Weiss'),
                                      (7,'Fredrick Douglas', 'David W. Blight'),
                                      (8,'An Army at Dawn','Rick Atkinson'),
                                      (9, 'Appeasement', 'Tim Bouverie'),
                                      (10,'Iran:A Modern History', 'Abbas Amanat'),
                                      (11,'The Gulf', 'Jack E. Davis'),
                                      (12, 'SPQR', ' Mary Beard'),
                                      (13, 'Embracing Defeat','John W. Dower'),
                                      (14,'1776', 'David McCullough')''')

                                      




    con.commit()
except:
    pass
    

#6-Mystery
cur.execute(' create table if not exists mys (sno int primary key, book_name varchar (60), author_name varchar (60))')

try:
    cur.execute('''insert into mys values (1, 'And Then There Were None','Agatha Christie'),
                                      (2, 'Angles and Demons', 'Dan Brown') ,
                                      (3,'Rebecca', 'Daphne du Maurier'),
                                      (4, 'In Cold Blood', 'Truman Capote'),
                                      (5, 'The Godfather', 'Mario Puzo'),
                                      (6,'Gone Girl','Gillian Flynn'),
                                      (7,'The Firm', 'John Grishan'),
                                      (8,'Mystic River','Dennis Lehane'),
                                      (9, 'The Girl With Dragon Tattoo', 'Stieg Larsson'),
                                      (10,'The Silent Patient', 'Alex Michaelides'),
                                      (11,'Big Little Lies', 'Liane Moriarty'),
                                      (12, 'Shutter Island', 'Denis Lehane'),
                                      (13, 'Murder at the Vicarage','Agatha Christie'),
                                      (14,'The Study In Scarlet', 'Conan Doyle'),
                                      (15,'The Murder of Roger Ackroyde','Agatha Christie'),
                                      (16,'The Da Vinci Code','Dan Brown')''')


    con.commit()
except:
    pass


#7-Poetry 
cur.execute(' create table if not exists poem (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute("""insert into poem values (1, 'The Collected Poems','Sylvia Plath'),
                                      (2, 'Pillow Thoughts', 'Courtney Peppernell') ,
                                      (3,'The Complete poems of Emily Dickinson', 'Emily Dickinson'),
                                      (4, 'The Rumi Collections', 'Rumi'),
                                      (5, 'The Complete Sonnets and Poems', 'Shakespeare'),
                                      (6,'Leaves and Grass', 'Walt Whitman'),
                                      (7,'John Donnes Poetry', 'John Donnes and Wilbur Sanders'),
                                      (8,'Complete poetry of Edgar Allan Poe','Edgar Allen Poe'),
                                      (9, 'Robert Frost Poems', 'Robert Frost'),
                                      (10,'The Essential Neruda', 'Pablo Neruda')""")


    con.commit()
except:
    pass
    

#8-Romance 
cur.execute(' create table if not exists rom (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into rom values (1, 'The Wuthering Heights','Emily Bronte'),
                                      (2, 'Pride and Prejudice', 'Jane Austen') ,
                                      (3,'Outlander', 'Diana Gabaldon'),
                                      (4, 'Divergent', 'Veronica Roth'),
                                      (5, 'Emma', 'Jane Austen'),
                                      (6,'The Notebook', 'Nicholas Sparks'),
                                      (7,'Sense and Sensibilities', 'Jane Austen'),
                                      (8,'Romeo and Juliet','William Shakespeare'),
                                      (9, 'Persuasion', 'Jane Austen'),
                                      (10,'It Ends With US ', 'Colleen Hoover'),
                                      (11,'The Hating Game', 'Sally Throne'),
                                      (12, 'Beautiful Disaster', 'Jamie McGuire'),
                                      (13, 'Gone With The Wind','Margaret Mitchell'),
                                      (14,'Call Me By Your Name', 'Andre Aciman'),
                                      (15,'The Time Travellers Wife','Audrey Niffenegger'),
                                      (16,'The Kiss Quotient','Helen Hoang')''')




    con.commit()
except:
    pass
    

#9-Self Help 
cur.execute(' create table if not exists help (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into help values (1, 'How to win friends and influence people','Dale Carnegie'),
                                      (2, 'The 7 habbits of highly effective people', 'Stephan Covey') ,
                                      (3,'Think and grow rich', 'Napolean Hill'),
                                      (4, 'The power of positive thinking', 'Norman Vincent Peale'),
                                      (5, 'Atomic habbits', 'James Clear'),
                                      (6,'Wisdom from rich dad, poor dad', 'Robert Kiyosaki'),
                                      (7,'The power of your subconscious mind', 'Joseph Murphy'),
                                      (8,'The Alchemist','Paulo Coelho'),
                                      (9, 'The road less travelled', 'M. Scott Peck'),
                                      (10,'Think like a monk', 'Jay Shetty'),
                                      (11,'Thinking fast and slow', 'Daniel Kahman'),
                                      (12, 'Ikigai', 'Albert Liebermann and Hector Garcia'),
                                      (13, 'The gifts of Imperfections','Brene Brown')''')
                                      



    con.commit()
except:
    pass

#10-Young Adult
cur.execute(' create table if not exists ya (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into ya values (1, 'The Fault In our Stars','John Green'),
                                      (2, 'The Book Thief', 'Markus Zusak') ,
                                      (3,'The Perks of Being a Wallflower', 'Stephan Chbosky'),
                                      (4, 'One Of Us Is Lying', 'M. McManus'),
                                      (5, 'Eleanor and Park', 'Rainbow Rowell'),
                                      (6,'We Were Liars', 'E. Lockhart'),
                                      (7,'Aristotle and Dante Discover the Secrets of the Universe', 'Benjamin Alire Saenz'),
                                      (8,'All the Bright Places','Jennifer Niven'),
                                      (9, 'To All the Boys I Have Loved Before', 'Jenny Han'),
                                      (10,'Fangirl', 'Rainbow Rowell'),
                                      (11,'Thirteen Reasons Why', 'Jay Asher'),
                                      (12, 'They Both Die in the End', 'Adam Silvers'),
                                      (13, 'Cinder','Marissa Meyer'),
                                      (14,'Carry On', 'Rainbow Rowell'),
                                      (15,'Paper Town','John Green')''')




    con.commit()
except:
    pass


#11-MostRead2020 
cur.execute(' create table if not exists mostread (sno int primary key, book_name varchar (60), author_name varchar (60))')
try:
    cur.execute('''insert into mostread values (1, 'The Silent Patient','Alex Michaelides'),
                                      (2, 'Sapiens', 'Yoval Noah Harari') ,
                                      (3,'Harry Potter and the Sorcerers Stone', 'J.K. Rowling'),
                                      (4, 'The Alchemist', 'Paulo Coelho'),
                                      (5, 'Mans search for meaning', 'Victor Frankl'),
                                      (6,'Raavan', 'Amish Tripathy'),
                                      (7,'The Immortals of Meluha', 'Amish Tripathy'),
                                      (8,'The Kite Runner','Khaled Hosseini'),
                                      (9, 'A Man Called Ove', 'Fredrik Backman'),
                                      (10,'The Thousand Splendid Suns', 'Khaled Hosseini')''')


    con.commit()

except:
    pass

cur.execute('create table if not exists user(sno int primary key, u_name varchar(40), phno bigint, emailid varchar(30),datetime timestamp default current_timestamp, tbr varchar(2000))')


#time.sleep(3)
cur.execute("use books")






s1="Be yourself; everyone else is already taken. -Oscar Wilde"
s2="You've gotta dance like there's nobody watching,Love like you'll never be hurt,Sing like there's nobody listening,And live like it's heaven on earth.― William W. Purkey"
s3="No one can make you feel inferior without your consent.  -Eleanor Roosevelt"
s4="Without music, life would be a mistake. -Friedrich Nietzsche"
s5="We accept the love we think we deserve. -Stephen Chbosky"
s6="Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring. -Marilyn Monroe"
s7="There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle. -Albert Einstein"
s8="We are all in the gutter, but some of us are looking at the stars.-Oscar Wilde"
s9="Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.-Bil Keane"
s10="Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.-Neil Gaiman"
s11="I have not failed. I've just found 10,000 ways that won't work.― Thomas A. Edison"
s12="The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.― Elie Wiesel"
s13="I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.― Albert Einstein"
s14="You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own. And you know what you know. And YOU are the one who'll decide where to go... ― Dr. Seuss"
s15="This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends -they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything -they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them -actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.-Marilyn Monroe"
s16="It is never too late to be what you might have been.-George Eliot"
s17="There is no greater agony than bearing an untold story inside you.-Maya Angelou"
s18="Everything you can imagine is real.-Pablo Picasso"
s19="You can never get a cup of tea large enough or a book long enough to suit me.-C.S. Lewis"
s20="To the well-organized mind, death is but the next great adventure.-J.K. Rowling"
s21="Life isn't about finding yourself. Life is about creating yourself.-George Bernard Shaw"
s22="Do what you can, with what you have, where you are.-Theodore Roosevelt"
s23="Listen to the mustn'ts, child. Listen to the don'ts. Listen to the shouldn'ts, the impossibles, the won'ts. Listen to the never haves, then listen close to me... Anything can happen, child. Anything can be.-Shel Silvers tein"
s24="When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.-Helen Keller"
s25="Success is not final, failure is not fatal: it is the courage to continue that counts.-Winston S. Churchill"
s26="So, this is my life. And I want you to know that I am both happy and sad and I'm still trying to figure out how that could be.-Stephen Chbosky"
s27="You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.-John Lennon"
s28="And, when you want something, all the universe conspires in helping you to achieve it.-Paulo Coelho"
s29="Our deepest fear is not that we are inadequate. Our deepest fear is that we are powerful beyond measure. It is our light, not our darkness that most frightens us. We ask ourselves, 'Who am I to be brilliant, gorgeous, talented, fabulous?' Actually, who are you not to be? You are a child of God. Your playing small does not serve the world. There is nothing enlightened about shrinking so that other people won't feel insecure around you. We are all meant to shine, as children do. We were born to make manifest the glory of God that is within us. It's not just in some of us; it's in everyone. And as we let our own light shine, we unconsciously give other people permission to do the same. As we are liberated from our own fear, our presence automatically liberates others.-Marianne Williamson"
s30="It’s no use going back to yesterday, because I was a different person then.-Lewis Carroll"
s31="War is peace.Freedom is slavery.Ignorance is strength.-George Orwell"
s32="None but ourselves can free our minds.-Bob Marley"
s33="Don't judge each day by the harvest you reap but by the seeds that you plant."
s34="Only in the darkness can you see the stars.-Martin Luther King Jr."
s35="Sometimes our light goes out, but is blown again into instant flame by an encounter with another human being.-Albert Schweitzer"
s36="I do not fear death. I had been dead for billions and billions of years before I was born, and had not suffered the slightest inconvenience from it.-Mark Twain"
s37="A woman's heart should be so hidden in God that a man has to seek Him just to find her.-Max Lucado"
s38="It's kind of fun to do the impossible.-Walt Disney Company"
s39="A painter should begin every canvas with a wash of black, because all things in nature are dark except where exposed by the light.-Leonardo da Vinci"
s40="What you're supposed to do when you don't like a thing is change it. If you can't change it, change the way you think about it. Don't complain.-Maya Angelou"
s41="A person's a person, no matter how small.-Dr. Seuss"
s42="He’s not perfect. You aren’t either, and the two of you will never be perfect. But if he can make you laugh at least once, causes you to think twice, and if he admits to being human and making mistakes, hold onto him and give him the most you can. He isn’t going to quote poetry, he’s not thinking about you every moment, but he will give you a part of him that he knows you could break. Don’t hurt him, don’t change him, and don’t expect for more than he can give. Don’t analyze. Smile when he makes you happy, yell when he makes you mad, and miss him when he’s not there. Love hard when there is love to be had. Because perfect guys don’t exist, but there’s always one guy that is perfect for you.-Bob Marley"
s43="It's the possibility of having a dream come true that makes life interesting.-Paulo Coelho"
s44="When we honestly ask ourselves which person in our lives mean the most to us, we often find that it is those who, instead of giving advice, solutions, or cures, have chosen rather to share our pain and touch our wounds with a warm and tender hand. The friend who can be silent with us in a moment of despair or confusion, who can stay with us in an hour of grief and bereavement, who can tolerate not knowing, not curing, not healing and face with us the reality of our powerlessness, that is a friend who cares. -Henri J.M. Nouwen"
s45="You can't live your life for other people. You've got to do what's right for you, even if it hurts some people you love.-Nicholas Sparks"
s46="Well-behaved women seldom make history.-Laurel Thatcher Ulrich"
s47="I can't give you a sure-fire formula for success, but I can give you a formula for failure: try to please everybody all the time.- Herbert Bayard Swope"
s48="Do what you feel in your heart to be right for you’ll be criticized anyway.-Eleanor Roosevelt"
s49="the only people for me are the mad ones, the ones who are mad to live, mad to talk, mad to be saved, desirous of everything at the same time, the ones who never yawn or say a commonplace thing, but burn, burn, burn like fabulous yellow roman candles exploding like spiders across the stars and in the middle you see the blue centerlight pop and everybody goes 'Awww'-Jack Kerouac"
s50="Happiness is not something ready made. It comes from your own actions.-Dalai Lama XIV"
s51="So we beat on, boats against the current, borne back ceaselessly into the past.-F. Scott Fitzgerald"
s52="Imagining the future is a kind of nostalgia. (...) You spend your whole life stuck in the labyrinth, thinking about how you'll escape it one day, and how awesome it will be, and imagining that future keeps you going, but you never do it. You just use the future to escape the present.-John Green"
s53="Do not read, as children do, to amuse yourself, or like the ambitious, for the purpose of instruction. No, read in order to live.-Gustave Flaubert"
s54="Never doubt that a small group of thoughtful, committed, citizens can change the world. Indeed, it is the only thing that ever has.-Margaret Mead"
s55="What lies behind us and what lies before us are tiny matters compared to what lies within us.-Ralph Waldo Emerson"
s56="Whatever you are, be a good one.-Abraham Lincoln"
s57="First they ignore you. Then they ridicule you. And then they attack you and want to burn you. And then they build monuments to you.-Nicholas Klein"
s58="Two wrongs don't make a right, but they make a good excuse.-Thomas Szasz"
s59="Friendship is unnecessary, like philosophy, like art.... It has no survival value; rather it is one of those things which give value to survival.-C.S. Lewis"
s60="I hope she'll be a fool --that's the best thing a girl can be in this world, a beautiful little fool.-F. Scott Fitzgerald"
s61="I believe that imagination is stronger than knowledge. That myth is more potent than history. That dreams are more powerful than facts. That hope always triumphs over experience. That laughter is the only cure for grief. And I believe that love is stronger than death.-Robert Fulghum"
s62="May you live every day of your life.-Jonathan Swift"

s63="You can't stay in your corner of the Forest waiting for others to come to you. You have to go to them sometimes.-A.A. Milne"
s64="Isn't it nice to think that tomorrow is a new day with no mistakes in it yet?-L.M. Montgomery"
s65="If my life is going to mean anything, I have to live it myself.-Rick Riordan"
s66="You can talk with someone for years, everyday, and still, it won't mean as much as what you can have when you sit in front of someone, not saying a word, yet you feel that person with your heart, you feel like you have known the person for forever.... connections are made with the heart, not the tongue.-C. JoyBell C."
s67="When I was 5 years old, my mother always told me that happiness was the key to life. When I went to school, they asked me what I wanted to be when I grew up. I wrote down ‘happy’. They told me I didn’t understand the assignment, and I told them they didn’t understand life.-John Lennon"

s68="Hope is the thing with feathers That perches in the soul And sings the tune without the words And never stops at all.-Emily Dickinson"
s69="Always do what you are afraid to do.-Ralph Waldo Emerson"
s70="Who controls the past controls the future. Who controls the present controls the past.-George Orwell"
s71="Our lives begin to end the day we become silent about things that matter.-Martin Luther King Jr"
s72="There is neither happiness nor misery in the world; there is only the comparison of one state with another, nothing more. He who has felt the deepest grief is best able to experience supreme happiness. We must have felt what it is to die, Morrel, that we may appreciate the enjoyments of life."
s126="Live, then, and be happy, beloved children of my heart, and never forget, that until the day God will deign to reveal the future to man, all human wisdom is contained in these two words, 'Wait and Hope'.-Alexandre Dumas"
s73="In the end, we will remember not the words of our enemies, but the silence of our friends.-Martin Luther King Jr."
s74="It is so hard to leave—until you leave. And then it is the easiest goddamned thing in the world.-John Green"
s75="Talent hits a target no one else can hit. Genius hits a target no one else can see.-Arthur Schopenhauer"
s76="Pain is inevitable. Suffering is optional.-Haruki Murakami"
s77="The mind is its own place, and in itself can make a heaven of hell, a hell of heaven.-John Milton"

s78="Waiting is painful. Forgetting is painful. But not knowing which to do is the worst kind of suffering.-Paulo Coelho"
s79="Fantasy is hardly an escape from reality. It's a way of understanding it.- Lloyd Alexander"
s80="Do not go where the path may lead, go instead where there is no path and leave a trail.-Ralph Waldo Emerson"
s81="And once the storm is over, you won’t remember how you made it through, how you managed to survive. You won’t even be sure, whether the storm is really over. But one thing is certain. When you come out of the storm, you won’t be the same person who walked in. That’s what this storm’s all about.-Haruki Murakami"
s82="If you can't fly then run, if you can't run then walk, if you can't walk then crawl, but whatever you do you have to keep moving forward.-Martin Luther King Jr."
s83="When you have eliminated all which is impossible, then whatever remains, however improbable, must be the truth.-Arthur Conan Doyle"
s84="Turn your wounds into wisdom.-Oprah Winfrey"
s85="Never let your sense of morals prevent you from doing what is right. -Isaac Asimov"
s86="Hell is empty and all the devils are here.-William Shakespeare"
s87="And, in the end The love you take is equal to the love you make.-Paul McCartney"
s88="The future belongs to those who believe in the beauty of their dreams.-Eleanor Roosevelt"

s89="It isn't what you have or who you are or where you are or what you are doing that makes you happy or unhappy. It is what you think about it.-Dale Carnegie"
s90="I like living. I have sometimes been wildly, despairingly, acutely miserable, racked with sorrow; but through it all I still know quite certainly that just to be alive is a grand thing.-Agatha Christie"
s91="Clouds come floating into my life, no longer to carry rain or usher storm, but to add color to my sunset sky.-Rabindranath Tagore"
s92="Pain is temporary. Quitting lasts forever. -Lance Armstrong"
s93="The truth is, unless you let go, unless you forgive yourself, unless you forgive the situation, unless you realize that the situation is over, you cannot move forward.-Steve Maraboli"
s94="Stories never really end...even if the books like to pretend they do. Stories always go on. They don't end on the last page, any more than they begin on the first page.-Cornelia Funke"
s95="People say nothing is impossible, but I do nothing every day.-A.A. Milne"
s96="The most important kind of freedom is to be what you really are. You trade in your reality for a role. You trade in your sense for an act. You give up your ability to feel, and in exchange, put on a mask. There can't be any large-scale revolution until there's a personal revolution, on an individual level. It's got to happen inside first.-Jim Morrison"
s97="The Chinese use two brush strokes to write the word 'crisis.' One brush stroke stands for danger; the other for opportunity. In a crisis, be aware of the danger--but recognize the opportunity.-John F. Kennedy"
s98="All the darkness in the world cannot extinguish the light of a single candle.-Francis of Assisi"
s99="If you want to forget something or someone, never hate it, or never hate him/her. Everything and everyone that you hate is engraved upon your heart; if you want to let go of something, if you want to forget, you cannot hate.-C. JoyBell C."
s100="We are just an advanced breed of monkeys on a minor planet of a very average star. But we can understand the Universe. That makes us something very special.-Stephen Hawking"
s101="You have to grow from the inside out. None can teach you, none can make you spiritual. There is no other teacher but your own soul.-Swami Vivekananda"

s102="In a conflict between the heart and the brain, follow your heart. -Swami Vivekananda"
s103="In a day, when you don't come across any problems - you can be sure that you are travelling in a wrong path-Swami Vivekananda"
s104="The great secret of true success, of true happiness, is this: the man or woman who asks for no return, the perfectly unselfish person, is the most successful.-Swami Vivekananda"
s105="All power is within you; you can do anything and everything. Believe in that, do not believe that you are weak; do not believe that you are half-crazy lunatics, as most of us do nowadays. You can do any thing and everything, without even the guidance of any one. Stand up and express the divinity within you.-Swami Vivekananda"
s106="The greatest religion is to be true to your own nature. Have faith in yourselves.-Swami Vivekananda"
s107="The greatest sin is to think yourself weak-Swami Vivekananda"
s108=" Dare to be free, dare to go as far as your thought leads, and dare to carry that out in your life.   -Swami Vivekananda"
s109=" Anything that makes weak - physically, intellectually and spiritually, reject it as poison.  -Swami Vivekananda"
s110=" Be not Afraid of anything. You will do Marvelous work. it is Fearlessness that brings Heaven even in a moment.-Swami Vivekananda"
s111=" Freedom is not worth having if it does not include the freedom to make mistakes.  -Mahatma Gandhi"
s112=" Prayer is not asking. It is a longing of the soul. It is daily admission of one's weakness. It is better in prayer to have a heart without words  than words without a heart.-Mahatma Gandhi"
s113=" They alone live, who live for others. -Swami Vivekananda"
s114="We are what our thoughts have made us; so take care about what you think. Words are secondary. Thoughts live; they travel far. -Swami Vivekananda"
s115=" Arise, awake, stop not till the goal is reached.  -Swami Vivekananda"
s116="All love is expansion, all selfishness is contraction. Love is therefore the only law of life. He who loves lives, he who is selfish is dying.Therefore love for love's sake, because it is the only law of life, just as you breathe to live. -Swami Vivekananda"
s117="Dream is not that which you see while sleeping it is something that does not let you sleep. -A.P.J. Abdul Kalam"
s118="Dream, Dream Dream Dreams transform into thoughts And thoughts result in action.-A.P.J. Abdul Kalam"
s119="It Is Very Easy To Defeat Someone, But It Is Very Hard To Win Someone  -A.P.J. Abdul Kalam"
s120=" All Birds find shelter during a rain.But Eagle avoids rain by flying above the Clouds."
s121=" Problems are common, but attitude makes the difference... -A.P.J. Abdul Kalam"
s122="Don't take rest after your first victory because if you fail in second, more lips are waiting to say that your first victory was just luck.  -A.P.J. Abdul Kalam"
s123="For great men, religion is a way of making friends; small people make religion a fighting tool.  -A.P.J. Abdul Kalam"
s124=" Be the change that you wish to see in the world.  -Mahatma Gandhi"
s125=" Live as if you were to die tomorrow. Learn as if you were to live forever.  -Mahatma Gandhi"




quotes=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89,s90,s91,s92,s93,s94,s95,s96,s97,s98,s99,s100,s101,s102,s103,s104,s105,s106,s107,s108,s109,s110,s111,s112,s113,s114,s115,s116,s117,s118,s119,s120,s121,s122,s123,s124,s125,s126]








def genre(table,sort_by):
    query="select sno, book_name, author_name from %s order by %s" % (table, sort_by)
    cur.execute(query)
    z=cur.fetchall()
    if z!=[]:
        for rec in z:
            for i in range(len(rec)):
                if i==0:
                    print(rec[i],'-')
                elif i==1:
                    print("Book's name-" ,rec[i])
                elif i==2:
                    print("Author's name-" ,rec[i])
                
            print('-'*55,'\n','\n')

    else:
        print("please enter valid details")
        mainmenu()


global name
name=input("enter your name-")
pno=int(input("enter your phone no-"))

email=input("enter you email address-")
if name.lower()=="annanya" or name.lower()=="sparsh" and email=="annanya1110jain@gmail.com":
    print("WELCOME ADMIN",'\n')
else:
    print("HELLO DEAR",name,"\n")
    

cur.execute("select u_name from user where phno=%s" %(pno))
userexists= cur.fetchall()
if userexists==[]:
    cur.execute('select*from user')
    l=cur.fetchall()
    s=len(l)+1
    query="insert into user(sno) values(%s)"%(s) 
    cur.execute(query)
    con.commit()

    query="update user set u_name='%s', phno=%s, emailid='%s' where sno= %s"%(name, pno, email,s) 
    cur.execute(query)
    con.commit()




def mainmenu():
    while True:
        try:
            userChoice = int(input("""
            1- Browse books
            2- View to be read list
            3- View a random quote
            4- Search a quote by keyword
            5- Search quote using author's name
            6- Add a book in database(admin only)
            7- Add quote in database(admin only)
            8- Exit
            Enter the no. adjacent to your choice-"""))
        except:
            print("only numerical values are accepted")
            print('_'*60)
            mainmenu()

        if userChoice ==1:
                
        
            print('''
            1- Autobiographies and Biographies
            2- Children's
            3- Classics
            4- Fantasy
            5- Historical
            6- Mystery
            7- Poetry
            8- Romance
            9- Self Help
            10- Young Adult
            11- Most Read of 2020''')
            time.sleep(3)
            try:
                x= int(input("Please enter the number beside your choice-"))
            except:
                mainmenu()
            check = True
            if x==1:
                g='bio'
            elif x==2:
                g='child'
            elif x==3:
                g='classic'
            elif x==4:
                g="fan"
            elif x==5:
                g='his'
            elif x==6:
                g='mys'
            elif x==7:
                g='poem'
            elif x==8:
                g='rom'
            elif x==9:
                g='help'
            elif x==10:
                g='ya'
            elif x==11:
                g='mostread'
            else:
                check = False
                print("invalid value", end='\n\n')
                
                mainmenu()
                
            if check:    
                y= (input("""Sort the book list by
                p - author's name
                q - book's name
                r - none

                please enter the alphabet adjacent to your choice-"""))
                print('\n','\n')
                if y.lower()== 'p':
                    genre(g,'author_name')
                elif y.lower()=='q':
                    genre(g, 'book_name')
                else:
                    genre(g, 'sno')
                



            
            def invalidbookno():
                summ=input("would you like to know more about any book? (Y/N)-")
                if summ.upper()=="YES" or summ.upper()=="Y":
                    global bookno
                    bookno=int(input('Enter the sno of your desired book:'))
                    print('\n','_'*60,'\n')

                    aboutbook=".\\Bookcover\\"+g+str(bookno)+".jpg"
                    
                    image= Image.open(aboutbook)
                    image.show()
                       
                    add=input("Would you like to add it to your to be read list? (Y/N)-")
                    if add.upper()=="YES" or summ.upper()=="Y":
                        l=""    
                        
                        cur.execute("select tbr from user where phno='%s'"%(pno))
                        z=cur.fetchall()
                        
                            
                        for r in z:
                            for v in r:
                                if type(v)!=str:
                                    pass
                                else:
                                    l=l+v+','
                                
                        cur.execute("select book_name from %s where sno=%s"%(g,bookno))
                        f=cur.fetchall()
                        for e in f:
                            for d in e:
                                l=l+d
                                
                                
                        cur.execute("update user set tbr='%s' where u_name='%s'"%(l,name))
                        con.commit()
                        mainmenu()      
                    else:
                        mainmenu()
                            
                else:
                    mainmenu()

            invalidbookno()


            
                    
        elif userChoice==2:
            query="select tbr from user where phno=%s"%(pno)
            cur.execute(query)
            z=cur.fetchall()
            if z==[]:
                print("empty to be read list")
                mainmenu()
                   
            else: 
                for rec in z:
                    for v in rec:
                        print(v)
                        print('_'*60)
                        mainmenu()
        elif userChoice==3:
            quote=random.choice(quotes)
            print("\n")
            print(quote)
            time.sleep(2)


        elif userChoice==4:
            keyword=input("enter the search key:")
    
            for q in quotes:
                c=q.split()
                for i in c:
                    if i.lower()==keyword.lower():
                        print(q, '\n','\n')
            time.sleep(2)        
                    
            
        
        elif userChoice==5:
            author=input("enter author's name:")
            print("\n")
            for q in quotes:
                if author.lower() in q.lower():
                    print(q)
                    print("\n")
                    time.sleep(2)


        elif userChoice==6:
            if name.lower()=="annanya" or name.lower()=="sparsh" and email=="annanya1110jain@gmail.com":
                print('''
                    1- Autobiographies and Biographies
                    2- Children's
                    3- Classics
                    4- Fantasy
                    5- Historical
                    6- Mystery
                    7- Poetry
                    8- Romance
                    9- Self Help
                    10- Young Adult
                    11- Most Read of 2020''')
                time.sleep(3)
                try:
                    x= int(input("Please enter the number beside your choice-"))
                except:
                    mainmenu()
                check = True
                if x==1:
                    g='bio'
                elif x==2:
                    g='child'
                elif x==3:
                    g='classic'
                elif x==4:
                    g="fan"
                elif x==5:
                    g='his'
                elif x==6:
                    g='mys'
                elif x==7:
                    g='poem'
                elif x==8:
                    g='rom'
                elif x==9:
                    g='help'
                elif x==10:
                    g='ya'
                elif x==11:
                    g='mostread'

                
                cur.execute("select sno from %s" %(g))
                
                l=cur.fetchall()
                
                
                s=len(l)+1
                query="insert into %s (sno) values(%s)"%(g,s) 
                cur.execute(query)
                con.commit()
                bn=input("Enter book's name:")
                an=input("Enter it's author's name:")         

                query="update %s set book_name='%s', author_name='%s'"%(g, bn, an) 
                cur.execute(query)
                con.commit()
                print("Book added successfully")
            else:
                print("ADMIN PRIVILEGE ONLY")


        elif userChoice==7:
            if name.lower()=="annanya" or name.lower()=="sparsh" and email=="annanya1110jain@gmail.com":
                quote=input("Please enter the quote:")
                qname=input("Enter name of the Quotee:")
                addquote=quote+'-'+qname
                quotes.append(addquote)
                print(addquote)
                print("Quote added successfully")

            else:
                print("ADMIN PRIVILEGE ONLY")
                
                
        


        elif userChoice==8:
            print("HOPE YOU HAD A GREAT TIME")
            print("bye bye")
            break
            

        else:
            print("enter a valid value")
            print()
            mainmenu()




            
   
mainmenu()
