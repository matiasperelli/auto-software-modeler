from app,core.analyzer import analyze_project

def main():
    description = input("Enter your software proposal:\n")

    result = analyze_project(description)

    print("\nDetected actors:")
    for actor in result["actors"]:
        print("-", actor)


if __name__ == "__main__":
  main()

