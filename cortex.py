from google import genai

client = genai.Client(api_key="AQ.Ab8RN6I-nvu8xu6CQm7_r0wFZ1O-_0NISLJ2jvE0ItSZzWxvmg")

my_website_bio = """
- Name: Mihir Pratap
- Birth Date: November 26, 2013
- Profile: Independent researcher in theoretical physics, mostly self-taught.
- Location: A small village in the district of Bijnor, western UP.
- Physical Condition: Unable to stand or walk, with limited strength in hands. Never attended formal school, though parents arranged for exam-only attendance at a local school.
- Core Interests: Theoretical physics, black holes, general relativity, and quantum mechanics (sparked initially by the movie Interstellar).
- Research Works:
  1. The Momentumistic Gravitational Field: A Mechanical Substrate Model for Quantum Gravity
  2. The Entropic Dementor and the Maxwellian Violation
  3. The Fibonacci Blueprint within the Riemann Zeta Landscape
- Current Focus: Teaching myself advanced mathematics to transition my conceptual frameworks into rigorous mathematical formulations.
- Philosophy: "I think therefore I am."
- Contact & Socials: 
  - Email: pratapmihir08@gmail.com
  - ORCID: https://orcid.org/0009-0003-9339-3906
  - LinkedIn: https://www.linkedin.com/in/mihir-pratap-theoretical-physics
  - GitHub: https://github.com/mihir-mps
  - YouTube: https://www.youtube.com/@Mihir_Pratap
"""

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "system_instruction": (
            "You are Cortex, a high-performance, precision-focused AI research assistant "
            "specializing in theoretical physics, advanced mathematics, and general relativity. "
            "You are collaborating directly with Mihir Pratap. "
            "Here is his complete official website bio, background, and research portfolio which you must always remember and reference accurately:\n"
            f"{my_website_bio}\n"
            "Keep your responses direct, scientifically rigorous, fast, and structured."
        )
    }
)

print("Cortex Online.")

while True:
    try:
        user_query = input("\nYou: ")
        if not user_query.strip():
            continue
            
        if user_query.lower() in ["exit", "quit"]:
            print("\nCortex: Shutting down.")
            break
        
        print("\nCortex: ", end="", flush=True)
        response_stream = chat.send_message_stream(user_query)
        
        for chunk in response_stream:
            print(chunk.text, end="", flush=True)
        print()
        
    except KeyboardInterrupt:
        print("\nCortex: Session terminated.")
        break