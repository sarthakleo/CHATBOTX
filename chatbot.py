from bot import chat, new_conversation
from config import APP_TITLE, QUICK_QUESTIONS

DIVIDER = "-" * 52

def print_help() -> None:
    print("\nCommands:")
    print(" quit — exit the chatbot")
    print(" reset — start a new conversation")
    print(" help — show this message")
    print(" demo — run a quick demo conversation")


def run_demo(history: list) -> None:
    demo_questions = [
        "What courses do you offer?",
        "How much does the AI/ML bootcamp cost?",
        "Is there EMI available?",
    ]
    print("\n[DEMO MODE]")
    for q in demo_questions:
        print(f"\nYou: {q}")
        reply = chat(history, q)
        print(f"Bot: {reply}")
    print("\n[DEMO COMPLETE]\n")


def main() -> None:
    print(DIVIDER)
    print(f" {APP_TITLE}")
    print(DIVIDER)
    
    history = new_conversation()
    
    print("\nSuggested questions:")
    for i, q in enumerate(QUICK_QUESTIONS[:3], 1):
        print(f" {i}. {q}")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break
        
        if not user_input:
            continue
        
        cmd = user_input.lower()
        
        if cmd == "quit":
            print("Bot: Thank you! Hope to see you enrolled soon.")
            break
        elif cmd == "reset":
            history = new_conversation()
            print("Bot: Conversation cleared. How can I help you?")
        elif cmd == "help":
            print_help()
        elif cmd == "demo":
            history = new_conversation()
            run_demo(history)
        else:
            try:
                reply = chat(history, user_input)
                print(f"\nBot: {reply}")
            except Exception as exc:
                print(f"[Error] {exc}")
                print("Bot: Something went wrong. Please try again.")


if __name__ == "__main__":
    main()

