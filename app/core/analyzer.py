from app.core.parser import extract_actors 

def analyze_project(text: str):
    actors = extract_actors(text)

return {
      "actors": list(actors) 
}
