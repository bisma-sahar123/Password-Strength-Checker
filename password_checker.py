print("======================================")
print("     PASSWORD STRENGTH CHECKER")
print("======================================")

password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

score = 0

for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

    else:
        has_special = True

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("\n------ Password Analysis ------")

print("Length Check      :", "Passed" if len(password) >= 8 else "Failed")
print("Uppercase Letter  :", "Present" if has_upper else "Missing")
print("Lowercase Letter  :", "Present" if has_lower else "Missing")
print("Number            :", "Present" if has_digit else "Missing")
print("Special Character :", "Present" if has_special else "Missing")

print("\nPassword Strength :", end=" ")

if score <= 1:
    print("WEAK")

elif score <= 3:
    print("MEDIUM")

else:
    print("STRONG")

print("\nSuggestions:")

if len(password) < 8:
    print("- Use at least 8 characters.")

if not has_upper:
    print("- Add an uppercase letter.")

if not has_digit:
    print("- Add at least one number.")

if not has_special:
    print("- Add a special character.")

if score == 4:
    print("Excellent Password!")