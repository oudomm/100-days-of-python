
# Band Name Generator 🎸

This is a simple Python program that generates a fun band name based on your personal inputs.

## How it Works
- The program asks you for:
  - The city you grew up in
  - Your pet’s name
- It then combines them to suggest a unique band name!

## Example
```bash
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
> New York
What's your pet's name?
> Shadow
Your band name could be: New York Shadow
```

## How to Run
1. Make sure you have Python installed.

2. Save the code into a file, for example band_name_generator.py.

3. Run it with:
```bash
python band_name_generator.py
```

## Code
```python
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be: " + city + " " + pet)
```