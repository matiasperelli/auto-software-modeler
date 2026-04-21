
def extract_actors(text: str):
    """
    Extract actors from a software proposal text.
    Returns a set of detected actors.
    """

    # normalize text
    words = text.lower().split()

    # posible actors
    known_actors = {
        "user", "admin", "administrator", "student",
        "teacher", "manager", "customer", "client"
    }

    detected_actors = set()

    for word in words:
        # remove punctuation
        clean_word = word.strip(".,;:")

          # clean data
      if clean_word in known_actors:
            detected_actors.add(clean_word)

      elif clean_word.endswith("s"):
            singular = clean_word[:-1]
            if singular in known_actors:
                detected_actors.add(singular)

    return detected_actors
