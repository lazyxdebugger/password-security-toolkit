# password-security-toolkit
Python-based password security toolkit that checks password strength and generates secure passwords.


---

**`Features`**
- Password strength analysis
- Detection of common weak passwords
- Personalized security recommendations
- Secure random password generation
- Hidden password input for better privacy

---
**`what it does?`**
- Helps users evaluate the strength of their passwords and generate secure ones.
---

**`how to run?`**
```bash
python pass_check.py
```
---

**`example output`**

### Password Strength Checker

```bash
$ python pass_check.py

1. Check Password Strength
2. Generate Password

Enter your choice: 1
Enter your password:

Password Strength: WEAK!

Suggestions:
- Use at least 8 characters.
- Add uppercase letters.
- Add numbers.
- Add a special character.
```

```bash
$ python pass_check.py

1. Check Password Strength
2. Generate Password

Enter your choice: 1
Enter your password:

Password Strength: MEDIUM!

Suggestions:
- Add uppercase letters.
- Add a special character.
```

```bash
$ python pass_check.py

1. Check Password Strength
2. Generate Password

Enter your choice: 1
Enter your password:

Password Strength: STRONG!
```

### Password Generator

```bash
$ python pass_check.py

1. Check Password Strength
2. Generate Password

Enter your choice: 2
Enter password length: 8

Generated Password: ~jQ>^?K
```

---



**`Disclaimer`**

This project is intended for educational and learning purposes. The password strength evaluation is based on basic security rules and should not be considered a complete assessment of password security. Generated passwords are suitable for practice and demonstration purposes, but this tool should not be relied upon as a replacement for professional password management or security solutions.

