def vitabot_wellness_chatbot():
    """
    VitaBot - Your Wellness Chatbot Assistant
    A health and wellness tracking chatbot template
    Students: Fill in the sections marked with # TODO: YOUR CODE HERE

    VitaBot helps users track sleep, exercise, and wellness habits through
    conversational check-ins, personalized feedback, and gentle motivation.
    """

    import random

    # --- Login/Sign-In Section ---
    print("🌟 Welcome to VitaBot! 🌟")
    print("Before we start, please sign in or create a new account.")

    users_db = {}  # simple in-memory "user database" as dict username:password

    def login():
        print("VitaBot: Please enter your username:")
        username = input("You: ").strip()
        if username in users_db:
            print("VitaBot: Please enter your password:")
            password = input("You: ").strip()
            if users_db[username] == password:
                print(f"VitaBot: Welcome back, {username}! Let’s get started on your wellness journey.")
                return username
            else:
                print("VitaBot: Incorrect password. Try again or type 'exit' to quit.")
                return None
        else:
            print("VitaBot: Username not found. Would you like to create a new account? (yes/no)")
            answer = input("You: ").lower().strip()
            if answer == "yes":
                print("VitaBot: Please enter a password for your new account:")
                password = input("You: ").strip()
                users_db[username] = password
                print(f"VitaBot: Account created! Welcome, {username}!")
                return username
            else:
                print("VitaBot: Okay, let's try logging in again.")
                return None

    current_user = None
    while current_user is None:
        current_user = login()
        if current_user is None:
            retry = input("You: ").lower().strip()
            if retry == "exit":
                print("VitaBot: Goodbye! Come back anytime for your wellness check-in. 💚")
                return

    # --- Main Chatbot Section ---

    print("\nVitaBot: Your personal wellness assistant here to check in on your habits")
    print("and help you feel your best every day!")
    print("Type 'bye' to exit anytime.\n")

    bot_name = "VitaBot"
    wellness_style = "gentle and encouraging"

    sleep_responses = {
        "excellent": [
            "Awesome! You're giving your body the rest it needs!",
            "Great job prioritizing sleep — your future self thanks you!",
            "That's the kind of sleep that supercharges your day! 💪"
        ],
        "good": [
            "Solid rest! You’re on the right track.",
            "That’s pretty good! Keep aiming for consistency.",
            "Nice — just a little more and you’ll feel even better!"
        ],
        "poor": [
            "Hmm, sounds like a light night. Let’s aim for more tonight.",
            "Sleep is fuel — let’s try for a bit more rest soon!",
            "Getting enough rest can help everything feel easier."
        ],
        "very_poor": [
            "That’s really not much sleep — your body must be tired.",
            "Sounds like a tough night. Want to plan a better bedtime today?",
            "Lack of sleep adds up. Let’s focus on rest tonight. You deserve it."
        ]
    }

    exercise_responses = {
        "excellent": [
            "Amazing! Your consistency is inspiring! 🏆",
            "Whoa — fitness goals achieved! Keep crushing it!",
            "You're moving like a champ — that’s fantastic!"
        ],
        "good": [
            "Nice job staying active! That’s great progress.",
            "Well done — you're building a solid habit!",
            "You're moving in the right direction — literally!"
        ],
        "fair": [
            "Every bit of movement counts — great start!",
            "You're doing something, and that matters!",
            "That’s a step in the right direction. Let’s build on it!"
        ],
        "poor": [
            "That’s okay — there’s always tomorrow to start fresh!",
            "No worries, movement can be fun and simple. Let’s try soon?",
            "One walk, one stretch — it all starts with one step!"
        ]
    }

    wellness_tips = {
        "sleep_improvement": [
            "Stick to a consistent bedtime and wake-up time — even on weekends.",
            "Avoid screens 30 minutes before bed to help your brain unwind.",
            "Try deep breathing or stretching before bed for better rest."
        ],
        "exercise_motivation": [
            "Find something active you enjoy — dance, walk, stretch — fun counts!",
            "Schedule your movement like an appointment — it’s self-care!",
            "Start small: 5 minutes today is better than none."
        ],
        "stress_relief": [
            "Try 4-7-8 breathing: In for 4, hold for 7, out for 8.",
            "Take a moment outside — sunlight and nature help!",
            "Write down 3 things you're grateful for — it can shift your mindset."
        ],
        "energy_boost": [
            "Drink a glass of water — dehydration often feels like fatigue.",
            "Take a 5-minute movement break — even stretching helps!",
            "Try standing in sunlight for a few minutes — it really works!"
        ],
        "meditation": [
            "Try a 5-minute guided meditation to relax your mind and body.",
            "Focus on your breath and gently bring your attention back when distracted.",
            "Mindfulness helps reduce stress and improve focus — give it a try!"
        ],
        "screen_time": [
            "Take regular breaks from screens using the 20-20-20 rule: every 20 minutes, look 20 feet away for 20 seconds.",
            "Try to limit screen time before bed to help your sleep quality.",
            "Balance your day with screen-free activities like reading or walking."
        ],
        "social": [
            "Reach out to a friend or family member today — connection boosts happiness!",
            "Try scheduling a regular chat or activity with someone you care about.",
            "Social wellness is key — even a quick 'hello' can brighten your day."
        ],
        "nature": [
            "Spend at least 10 minutes outside in fresh air — nature is a natural stress reliever.",
            "Try a walk in the park or just sit outside and notice the sounds around you.",
            "Being in nature improves mood and creativity — get outside when you can!"
        ],
        "routine": [
            "Try creating a simple morning or evening routine to build healthy habits.",
            "Consistency helps your body and mind — small habits add up over time.",
            "Set reminders for self-care activities to keep your routine on track."
        ]
    }

    wellness_quotes = [
        "You don’t have to be perfect — just consistent.",
        "Progress, not perfection. Keep going!",
        "Small steps lead to big changes. 🌱",
        "Rest is productive too — honor your body’s needs.",
        "Every day is a fresh start to care for yourself."
    ]

    user_wellness_data = {
        "sleep_hours": [],
        "exercise_days": [],
        "mood_ratings": [],
        "wellness_goals": []
    }

    def get_sleep_category(hours):
        if hours >= 8:
            return "excellent"
        elif hours >= 6:
            return "good"
        elif hours >= 4:
            return "poor"
        else:
            return "very_poor"

    def get_exercise_category(days):
        if days >= 5:
            return "excellent"
        elif days >= 3:
            return "good"
        elif days >= 1:
            return "fair"
        else:
            return "poor"

    while True:
        user_input = input("You: ").lower().strip()

        if any(word in user_input for word in ["bye", "goodbye", "exit"]):
            print(f"{bot_name}: It’s been great checking in with you. Keep being kind to yourself!")
            print(f"{bot_name}: Remember, small steps lead to big changes! Take care of yourself! 💚✨")
            break

        elif any(word in user_input for word in ["hello", "hi", "hey"]):
            print(f"{bot_name}: Hello! I'm {bot_name}, your {wellness_style} wellness companion!")
            print(f"{bot_name}: It’s wonderful to see you! Let’s check in on your wellness journey.")
            print(f"{bot_name}: Ready for a quick wellness check-in? Let's see how you're doing!")

        elif any(word in user_input for word in ["sleep", "slept", "tired", "rest"]):
            print(f"{bot_name}: Let's talk about your sleep! 😴")
            print(f"{bot_name}: How many hours of sleep did you get last night?")

            try:
                sleep_input = input("You: ").strip()
                hours = float(sleep_input)

                if 0 <= hours <= 24:
                    user_wellness_data["sleep_hours"].append(hours)
                    category = get_sleep_category(hours)
                    response = random.choice(sleep_responses[category])
                    print(f"{bot_name}: {response}")

                    if category == "excellent":
                        print(f"{bot_name}: That’s the kind of rest that helps your body and brain thrive!")
                    elif category == "good":
                        print(f"{bot_name}: Pretty solid! A bit more consistency and you’ll feel amazing.")
                    elif category == "poor":
                        print(f"{bot_name}: You deserve more rest. Let's try for at least 7 hours tonight.")
                        tip = random.choice(wellness_tips["sleep_improvement"])
                        print(f"{bot_name}: {tip}")
                    else:
                        print(f"{bot_name}: Please take care — your body needs sleep to recover and recharge.")
                        tip = random.choice(wellness_tips["sleep_improvement"])
                        print(f"{bot_name}: {tip}")
                else:
                    print(f"{bot_name}: That doesn't seem like a realistic number of hours. Try again!")

            except ValueError:
                print(f"{bot_name}: Please enter a number for your sleep hours.")

        elif any(word in user_input for word in ["exercise", "workout", "activity", "physical", "gym"]):
            print(f"{bot_name}: Time to check on your physical activity! 💪")
            print(f"{bot_name}: How many days did you exercise this week? (0-7)")

            try:
                exercise_input = input("You: ").strip()
                days = int(exercise_input)

                if 0 <= days <= 7:
                    user_wellness_data["exercise_days"].append(days)
                    category = get_exercise_category(days)
                    response = random.choice(exercise_responses[category])
                    print(f"{bot_name}: {response}")

                    if category == "excellent":
                        print(f"{bot_name}: You're setting the bar high — keep it up!")
                    elif category == "good":
                        print(f"{bot_name}: You’re doing well! Let’s aim for one more active day next week?")
                    elif category == "fair":
                        print(f"{bot_name}: You’ve started — and that’s awesome! What’s one more activity to add?")
                        tip = random.choice(wellness_tips["exercise_motivation"])
                        print(f"{bot_name}: {tip}")
                    else:
                        print(f"{bot_name}: No worries — we all start somewhere. Want to try a 5-minute walk tomorrow?")
                        tip = random.choice(wellness_tips["exercise_motivation"])
                        print(f"{bot_name}: {tip}")

                else:
                    print(f"{bot_name}: Please enter a number between 0 and 7.")

            except ValueError:
                print(f"{bot_name}: Please enter a whole number for exercise days.")

        elif any(word in user_input for word in ["mood", "feeling", "energy", "wellness"]):
            print(f"{bot_name}: Let's check in on how you're feeling! 😊")
            print(f"{bot_name}: On a scale of 1-10, how's your energy level today?")

            try:
                mood_input = input("You: ").strip()
                energy = int(mood_input)

                if 1 <= energy <= 10:
                    user_wellness_data["mood_ratings"].append(energy)

                    if energy >= 8:
                        print(f"{bot_name}: Love that energy! Keep riding the wave. 🌊")
                    elif energy >= 6:
                        print(f"{bot_name}: Pretty good! Let’s keep those good vibes going.")
                    elif energy >= 4:
                        print(f"{bot_name}: You’re doing your best — let’s find ways to recharge.")
                        tip = random.choice(wellness_tips["energy_boost"])
                        print(f"{bot_name}: {tip}")
                    else:
                        print(f"{bot_name}: That sounds rough. Sending you kindness — it’s okay to have off days.")
                        tip = random.choice(wellness_tips["stress_relief"])
                        print(f"{bot_name}: {tip}")

                else:
                    print(f"{bot_name}: Please rate your energy from 1 to 10.")

            except ValueError:
                print(f"{bot_name}: Please enter a number from 1 to 10.")

        elif any(word in user_input for word in ["progress", "summary", "report", "how am i doing"]):
            if not any(user_wellness_data.values()):
                print(f"{bot_name}: You’re making progress — and that matters more than perfection.")
            else:
                print(f"{bot_name}: Here's your wellness summary! 📊")

                if user_wellness_data["sleep_hours"]:
                    avg_sleep = sum(user_wellness_data["sleep_hours"]) / len(user_wellness_data["sleep_hours"])
                    print(f"{bot_name}: Average sleep: {avg_sleep:.1f} hours per night")

                if user_wellness_data["exercise_days"]:
                    recent_exercise = user_wellness_data["exercise_days"][-1] if user_wellness_data["exercise_days"] else 0
                    print(f"{bot_name}: Recent exercise: {recent_exercise} days this week")

                if user_wellness_data["mood_ratings"]:
                    avg_energy = sum(user_wellness_data["mood_ratings"]) / len(user_wellness_data["mood_ratings"])
                    print(f"{bot_name}: Average energy level: {avg_energy:.1f}/10")

                print(f"{bot_name}: Looks like you're building great self-awareness. Keep tracking — your habits are your superpower! 💪")

        elif any(word in user_input for word in ["tips", "advice", "help", "improve"]):
            print(f"{bot_name}: I'd love to share some wellness tips! 💡")
            print(f"{bot_name}: What area would you like help with?")
            print(f"{bot_name}: I can help with: sleep, exercise, stress, energy, meditation, screen time, social, nature, routine")

            tip_input = input("You: ").lower().strip()

            if "sleep" in tip_input:
                tip = random.choice(wellness_tips["sleep_improvement"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Good sleep makes everything easier — even small improvements help!")
            elif any(word in tip_input for word in ["exercise", "workout", "activity"]):
                tip = random.choice(wellness_tips["exercise_motivation"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Start where you are. Even 5–10 minutes counts — let's make it doable!")
            elif "stress" in tip_input:
                tip = random.choice(wellness_tips["stress_relief"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: You're not alone — take things one moment at a time. You've got this.")
            elif "energy" in tip_input:
                tip = random.choice(wellness_tips["energy_boost"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Little actions like stretching, sunlight, or deep breathing can lift your energy.")
            elif "meditation" in tip_input:
                tip = random.choice(wellness_tips["meditation"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Taking mindful moments can refresh your whole day.")
            elif "screen" in tip_input or "screen time" in tip_input:
                tip = random.choice(wellness_tips["screen_time"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Digital balance helps your mind and body relax.")
            elif "social" in tip_input:
                tip = random.choice(wellness_tips["social"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Meaningful connections nourish your soul.")
            elif "nature" in tip_input:
                tip = random.choice(wellness_tips["nature"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Fresh air and nature reset your mind and body.")
            elif "routine" in tip_input:
                tip = random.choice(wellness_tips["routine"])
                print(f"{bot_name}: {tip}")
                print(f"{bot_name}: Healthy routines build a strong foundation for your day.")
            else:
                all_tips = []
                for tip_list in wellness_tips.values():
                    all_tips.extend(tip_list)
                tip = random.choice(all_tips)
                print(f"{bot_name}: {tip}")

        elif any(word in user_input for word in ["goal", "want to", "trying to", "improve"]):
            print(f"{bot_name}: What’s one wellness goal you'd like to work on right now?")
            goal = input("You: ")
            user_wellness_data["wellness_goals"].append(goal)
            print(f"{bot_name}: That’s a great goal! I'm here to help you stick with it.")
            print(f"{bot_name}: Let’s take small steps together. You've already started by naming it!")

        elif any(word in user_input for word in ["motivated", "motivation", "encourage", "struggling"]):
            quote = random.choice(wellness_quotes)
            print(f"{bot_name}: {quote}")
            print(f"{bot_name}: You’re doing better than you think — just by checking in, you’re growing.")
            print(f"{bot_name}: Little steps each day build lifelong habits. Keep going!")

        elif any(word in user_input for word in ["stressed", "overwhelmed", "difficult", "hard day"]):
            print(f"{bot_name}: It’s okay to feel overwhelmed — you’re human. This moment will pass.")
            tip = random.choice(wellness_tips["stress_relief"])
            print(f"{bot_name}: {tip}")
            print(f"{bot_name}: Be gentle with yourself today. Rest is part of resilience. 💚")

        elif any(word in user_input for word in ["great", "amazing", "wonderful", "fantastic"]):
            print(f"{bot_name}: That’s fantastic! It’s important to celebrate the wins, big or small.")
            print(f"{bot_name}: Keep doing what makes you feel good — you’re on the right path! 🌟")

        elif any(word in user_input for word in ["water", "hydration", "drink", "thirsty"]):
            print(f"{bot_name}: How much water have you had today? Staying hydrated helps everything — from focus to energy.")
            print(f"{bot_name}: Try keeping a water bottle nearby. A sip here and there adds up!")

        elif any(word in user_input for word in ["food", "eat", "nutrition", "hungry"]):
            print(f"{bot_name}: How have your meals been lately? Any fruits or veggies today?")
            print(f"{bot_name}: Aim for variety — your body loves colorful plates and steady meals.")

        elif "help" in user_input and "tips" not in user_input:
            print(f"{bot_name}: I’m here to support your wellness journey in a kind and simple way.")
            print(f"{bot_name}: I can help you with:")
            print(f"{bot_name}: 😴 Sleep tracking and improvement tips")
            print(f"{bot_name}: 💪 Exercise motivation and activity tracking")
            print(f"{bot_name}: 😊 Mood check-ins and energy boosting")
            print(f"{bot_name}: 📊 Wellness progress summaries")
            print(f"{bot_name}: 🎯 Setting and achieving wellness goals")
            print(f"{bot_name}: 🧘‍♂️ Meditation and mindfulness")
            print(f"{bot_name}: 📱 Managing screen time")
            print(f"{bot_name}: 🤝 Social wellness and connections")
            print(f"{bot_name}: 🌳 Nature and outdoor activities")
            print(f"{bot_name}: 🔄 Building healthy routines")

        else:
            wellness_responses = [
                "Tell me how you’re feeling today — I’m here for you!",
                "Let’s chat about your sleep, exercise, or stress levels.",
                "Wellness is a journey — want to take a step today?",
                "I’ve got tips, support, and encouragement ready whenever you are!"
            ]
            print(f"{bot_name}: {random.choice(wellness_responses)}")

vitabot_wellness_chatbot()
