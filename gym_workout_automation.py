import random
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

motivation_quotes = ["Some people want it to happen, some wish it would happen, others make it happen.",
                     "You dream. You plan. You reach. There will be obstacles. There will be doubters. "
                     "There will be mistakes. But with hard work, with belief, with confidence and trust "
                     "in yourself and those around you, there are no limits.",
                     "All growth starts at the end of your comfort zone.",
                     "Most people fail, not because of lack of desire, but because of lack of commitment",
                     "I am Superman. And the only thing that can kill Superman is Kryptonite. And Kryptonite doesn't exist.",
                     "When I feel tired, I just think about how great I will feel once I finally reach my goal.",
                     "Don’t count the days, make the days count.",
                     "Nothing is impossible; the word itself says ‘I'm possible!",
                     "Start where you are. Use what you have. Do what you can.",
                     "The impossible exists only until we find a way to make it possible.",
                     "If you give up at the first sign of struggle, you're really not ready to be successful.",
                     "If you don't fall, how are you going to know what getting up is like?",
                     "The achievement of one goal should be the starting point of another.",
                     "I never dreamed about success. I worked for it.",
                     "You can, you should, and if you're brave enough to start, you will.",
                     "Your mind is your strongest muscle.",
                     "Your only limit is you.",
                     "The effort you invest today is the pride you feel tomorrow.",
                     "Don’t stop when you’re tired. Stop when you’re done.",
                     "Push harder than yesterday if you want a different tomorrow.",
                     "Be stronger than your excuses.",
                     "What you get by achieving your goals is not as important as what you become by achieving your goals.",
                     "Success doesn’t come from what you do occasionally. It comes from what you do consistently.",
                     "Perseverance is not a long race; it is many short races one after the other.",
                     "Tough times don’t last. Tough people do."]

chest_day = ["Pec dec fly",
             "Standing cable fly",
             "Standing cable low to high fly",
             "Dumbbell pull over",
             "Bench press",
             "Incline bench press",
             "Decline bench press",
             "Chest press machine",
             "Dumbbell fly",
             "Incline dumbbell fly",
             "Decline dumbbell fly",
             "Close grip dumbbell press",
             "Cable chest press",
             "Push ups"]

back_day = ["Cable lat pull down",
            "Seated cable row",
            "Tripod dumbbell row",
            "Bent over row",
            "Incline bench dumbbell row",
            "Straight arm lat pull down",
            "T-bar row",
            "Wide grip lat pull down",
            "V-bar pull down",
            "Close grip lat pull down",
            "One arm dumbbell row",
            "One arm seated row",
            "Reverse grip incline bench dumbbell row",
            "Machine row"]

shoulder_day = ["Lateral raises",
                "Seated dumbbell press",
                "Front raises",
                "Machine reverse fly",
                "Single arm cable lateral raises",
                'Incline rear delt fly',
                "Shoulder Machine",
                "Dumbbell 6 ways",
                "Cable face pull",
                "One arm cable front raises",
                "Dumbbell external extension (Bench supported)"
                "Cable internal rotation",
                "Dumbbell shrugs"
                "Seated lateral raises"]

biceps_day = ["Standing dumbbell curl",
              "Standing barbell curl",
              "Standing hammer curl",
              "Incline dumbbell curl",
              "Cable curl",
              "Concentration curl",
              "Preacher curl",
              "Cross body hammer curl",
              "Standing reverse curl",
              "One arm cable curl",
              "Close grip cable curl",
              "Standing dumbbell drag curl",
              ]

triceps_day = ["Straight bar triceps extension",
               "Rope triceps extension",
               "Bent over dumbbell triceps kickbacks",
               "EZ bar skull crusher",
               "Standing high pulley triceps extension",
               "Reverse one arm cable triceps extension",
               "One arm cable triceps extension",
               "Cable concentration triceps extension",
               "One arm dumbbell triceps extension",
               "Dumbbell triceps extension",
               ]

leg_day = ["Leg extension machine"
           "Hamstring extension machine",
           "Squats with dumbbell",
           "Thigh machine extension"
           "Thigh machine contraction",
           "Calf raises",
           "Leg press",
           "Wall sit",
           "Bulgarian split squat",
           "Dumbbell deadlifts"]

days = {"Monday": chest_day,
        "Tuesday": back_day,
        "Wednesday": shoulder_day,
        "Thursday": biceps_day,
        "Friday": triceps_day,
        "Saturday": leg_day,
        "Sunday": "💤💤Rest day 💤💤.\nHave your cheat meal today 🍗🍗.\nEnjoy😊😊."}

day = datetime.datetime.now().strftime("%A")

quote_heading = random.choice(motivation_quotes)
quote_footer = random.choice(motivation_quotes)

workout_plan = []
workout_day = days[day]

if day != "Sunday":
    workout_plan = random.sample(workout_day, 7)
    workout_plan_html = "".join([f"<li>{ex}</li>" for ex in workout_plan])
    body = f"""
    <div style="font-size:28px; font-family:Arial, sans-serif; line-height:1.5;">
            <h2 style="font-size:30px; color:#34495e;">Today"s workout ({day}) 💪💪</h2>
            <p style="font-size:28px; color:#e67e22;"><i> {quote_heading} </i> 🔥🔥</p>
            <ul>
                {workout_plan_html}
            </ul>
            <p style="font-size:28px; color:#e67e22;"><i> {quote_footer} </i> 🔥🔥</p>
            """

else:
    body = f"""
    <div style="font-size:28px; font-family:Arial, sans-serif; line-height:1.5;">
    <h2 style="font-size:30px; color:#34495e;">Today is {day}.</h2>
    <ul>
        {workout_day}
    </ul>

    """

sender_email = "abhiramrnair2000@gmail.com"
receiver_email = "abhiramr2000@gmail.com"
app_password = "bnrr ubau moxl xgth"

subject = f"Daily workout plan - {day} 💪💪."

msg = MIMEMultipart("alternative")
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "html"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())







