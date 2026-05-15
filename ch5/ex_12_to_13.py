# 5-12. Styling if statements: Review the programs you wrote in this chapter, and
# make sure you styled your conditional tests appropriately.
# 5-13. Your Ideas: At this point, you’re a more capable programmer than you
# were when you started this book. Now that you have a better sense of how
# real-world situations are modeled in programs, you might be thinking of some
# problems you could solve with your own programs. Record any new ideas you
# have about problems you might want to solve as your programming skills con-
# tinue to improve. Consider games you might want to write, data sets you might
# want to explore, and web applications you’d like to create.
# Simple password security checker:
# Length Criteria:
SHORT = 10 
MEDIUM = 15
LARGE = 22

# Character Parameters:
# ord function changes char into ascii code
# chr function changes ascii code into char
LC_LETTERS = [chr(char) for char in range(ord('a'), ord('z')+1)]
UC_LETTERS = [chr(char) for char in range(ord('A'), ord('Z')+1)]
NUMBERS = [chr(char) for char in range(ord('0'), ord('9')+1)]

# Security Score:
score = 0   # 1 - 20 weak, 21 - 40 medium, 41 - 60 strong

# String to be tested
password = "HelloWord1-"

# Length check
length = len(password)

if length <= SHORT:
    score += 10
elif length <= MEDIUM:
    score += 30
elif length <= LARGE:
    score += 60
else:
    score += 100

# Composition check
lc_component = False
uc_component = False
num_component = False
esp_component = False

for char in password:
    # the or part check if the value already had true in order to not overwrite
    lc_component = (char in LC_LETTERS) or lc_component
    uc_component = (char in UC_LETTERS) or uc_component
    num_component = (char in NUMBERS) or num_component
    esp_component = (char not in LC_LETTERS and 
                     char not in UC_LETTERS and 
                     char not in NUMBERS) or esp_component

if lc_component:
    score += 5
if uc_component:
    score += 10
if num_component:
    score += 15
if esp_component:
    score += 20

# Security-Score message
security = ""
if score <= 50:
    security = "weak"
elif score <= 90:
    security = "medium"
elif score <= 140:
    security = "strong"
else:
    security = "unhackeable"

print(f"Your password is {security}.")
print(f"Your score is: {score}")