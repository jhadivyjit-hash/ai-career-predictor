# AI Career Guidance + Mini Quiz (Python Version)

def analyze_career():

    print("\n🤖 AI CAREER GUIDANCE SYSTEM\n")

    print("Career Motivation:")
    print("1. High salary and growth")
    print("2. Creativity and innovation")
    print("3. Stability and security")
    print("4. Helping people and society")
    print("5. Leadership and influence")
    motivation = input("Enter choice (1-5): ")

    print("\nTechnology Comfort Level:")
    print("1. Very comfortable — I enjoy exploring new tech")
    print("2. Comfortable with guidance")
    print("3. Neutral")
    print("4. Prefer familiar tools only")
    tech = input("Enter choice (1-4): ")

    print("\nPreferred Type of Tasks:")
    print("1. Writing code or automating systems")
    print("2. Designing visuals or user experiences")
    print("3. Analyzing business or financial data")
    print("4. Communicating, teaching, or counseling")
    print("5. Managing projects and teams")
    task = input("Enter choice (1-5): ")

    career = ""
    confidence = 0

    # AI Logic
    if task == "1" and tech == "1":
        career = "Software Engineer / AI Developer"
        confidence = 92
    elif task == "2":
        career = "UI/UX Designer"
        confidence = 85
    elif task == "3":
        career = "Business Analyst / Commerce Field"
        confidence = 88
    elif task == "4":
        career = "Teacher / Psychologist"
        confidence = 90
    elif task == "5":
        career = "Entrepreneur / Manager"
        confidence = 84
    else:
        career = "Medical Field / Explore Multiple Fields"
        confidence = 70

    print("\n✨ Recommended Career:", career)
    print("📊 Confidence Level:", confidence, "%")
    print("🤖 AI Explanation: Based on your interests and comfort level, this career best matches your profile.")


def mini_quiz():

    print("\n🎮 MINI CAREER QUIZ\n")

    score = 0

    print("1. AI stands for?")
    print("a) Automatic Intelligence")
    print("b) Artificial Intelligence")
    ans = input("Enter answer (a/b): ")
    if ans.lower() == "b":
        score += 1

    print("\n2. Which field uses coding the most?")
    print("a) Software Engineering")
    print("b) History")
    ans = input("Enter answer (a/b): ")
    if ans.lower() == "a":
        score += 1

    print("\n3. Who manages business operations?")
    print("a) Manager")
    print("b) Painter")
    ans = input("Enter answer (a/b): ")
    if ans.lower() == "a":
        score += 1

    print("\n4. Doctors belong to which field?")
    print("a) Medical")
    print("b) Mechanical Repair")
    ans = input("Enter answer (a/b): ")
    if ans.lower() == "a":
        score += 1

    print("\n5. UI/UX Designers focus on?")
    print("a) User Experience")
    print("b) Farming")
    ans = input("Enter answer (a/b): ")
    if ans.lower() == "a":
        score += 1

    percentage = (score / 5) * 100

    print("\n🎉 Your Quiz Score:", score, "/5")
    print("📊 Percentage:", percentage, "%")


# Main Program
analyze_career()
mini_quiz()