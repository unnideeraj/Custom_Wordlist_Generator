#!/usr/bin/env python3

import itertools
import os


def get_user_input():
    # Prompts for inputs
    data = {
        "first_name": input("Enter first name: "),
        "last_name": input("Enter last name: "),
        "age": input("Enter age: "),
        "year": input("Enter a significant year: "),
        "dob": input("Enter date of birth (e.g., 1990): "),
        "pet_name": input("Enter pet name: "),
        "parents_name": input("Enter parents' names (comma-separated if more than one): "),
        "siblings_name": input("Enter siblings' names (comma-separated if more than one): "),
        "favorite_movies_series": input("Enter favorite movies/series (comma-separated): "),
        "mobile_numbers": input("Enter mobile numbers (comma-separated): "),
        "phone_model": input("Enter phone model: "),
        "favorite_numbers": input("Enter favorite numbers (comma-separated): "),
        "favorite_characters": input("Enter favorite characters (comma-separated): "),
        "favorite_places": input("Enter favorite places (comma-separated): "),
        "college_name": input("Enter college name: "),
        "school_name": input("Enter school name: "),
        "known_passwords": input("Enter known or leaked passwords (comma-separated): ")
    }
    # Convert multi-value inputs to lists
    for key, value in data.items():
        data[key] = [item.strip() for item in value.split(",") if item.strip()]
    return data


def generate_variations(data, min_length, max_length):
    base_words = []
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '/', ',', '\\', ']', '[', '{', '}', ':', '"', ';', '?', ' ']

    # Add all input data to base_words
    for key, values in data.items():
        base_words.extend(values)

    # Start generating variations
    variations = set(base_words)

    # Basic transformations and extended leetspeak
    for word in base_words:
        for variation in [
            word.lower(),
            word.upper(),
            word.capitalize(),
            word[::-1],  # Reversed
            word.replace('a', '@').replace('s', '$').replace('i', '1').replace('o', '0'),  # Simple leetspeak
            word.replace('e', '3').replace('g', '9').replace('t', '7'),  # Extended leetspeak
            word + word  # Repeat word
        ]:
            if min_length <= len(variation) <= max_length:
                variations.add(variation)

    # Advanced combinations of words, including trios
    combinations = list(itertools.permutations(base_words, 3))  # Triple combinations
    for combo in combinations:
        combined = ''.join(combo)
        reversed_combined = ''.join(combo[::-1])
        if min_length <= len(combined) <= max_length:
            variations.add(combined)  # Concatenate trio
        if min_length <= len(reversed_combined) <= max_length:
            variations.add(reversed_combined)  # Concatenate in reverse

    # Patterns with special characters and numbers
    for name in base_words:
        for char in special_chars:
            for num in range(0, 100):  # Add number suffix/prefix
                variation1 = f"{name}{char}{num}"
                variation2 = f"{num}{char}{name}"
                if min_length <= len(variation1) <= max_length:
                    variations.add(variation1)
                if min_length <= len(variation2) <= max_length:
                    variations.add(variation2)

    # Complex patterns from keywords and extra fields
    keywords = ["first_name", "last_name", "pet_name", "college_name", "school_name"]
    extras = ["dob", "parents_name", "favorite_movies_series", "mobile_numbers", "favorite_numbers"]

    for key in keywords:
        for extra_key in extras:
            for name in data.get(key, []):
                for extra in data.get(extra_key, []):
                    for char in special_chars:
                        variation1 = f"{name}{char}{extra}"
                        variation2 = f"{extra}{char}{name}"
                        if min_length <= len(variation1) <= max_length:
                            variations.add(variation1)
                        if min_length <= len(variation2) <= max_length:
                            variations.add(variation2)

    return variations


def add_common_passwords(variations, known_passwords, min_length, max_length):
    # Add common passwords, number suffixes, and known passwords
    common_passwords = ["password", "123456", "qwerty", "letmein", "iloveyou", "12345", "abc123", "welcome", "1234567890", "0987654321", "user", "password", "admin5"]
    number_suffixes = [str(num) for num in range(1, 10)]
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '/', ',', '\\', ']', '[', '{', '}', ':', '"', ';', '?', ' ']


    # Known passwords
    if known_passwords:
        common_passwords.extend(known_passwords)

    for pwd in common_passwords:
        if min_length <= len(pwd) <= max_length:
            variations.add(pwd)
        for num in number_suffixes:
            variation1 = f"{pwd}{num}"
            variation2 = f"{num}{pwd}"
            if min_length <= len(variation1) <= max_length:
                variations.add(variation1)
            if min_length <= len(variation2) <= max_length:
                variations.add(variation2)
        for char in special_chars:
            variation1 = f"{pwd}{char}"
            variation2 = f"{char}{pwd}"
            if min_length <= len(variation1) <= max_length:
                variations.add(variation1)
            if min_length <= len(variation2) <= max_length:
                variations.add(variation2)
    return variations


def save_to_file(variations):
    # Prompt for full file path including directory and filename
    filename = input("Enter the full path and filename for the wordlist (e.g., '/path/to/dir/custom_wordlist.txt'): ")

    # If file exists, read existing words to avoid duplication
    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_words = set(file.read().splitlines())
        variations = variations.difference(existing_words)  # Only add new variations

    # Save the variations to the specified file
    with open(filename, "a") as file:  # Open in append mode
        for word in sorted(variations):
            file.write(word + "\n")
    print(f"Wordlist saved to {filename} (appended new entries if file existed)")


def main():
    # Get min and max length from user
    min_length = int(input("Enter minimum word length: "))
    max_length = int(input("Enter maximum word length: "))

    user_data = get_user_input()
    variations = generate_variations(user_data, min_length, max_length)
    # Add common passwords and previously known passwords
    known_passwords = user_data.get("known_passwords", [])
    variations = add_common_passwords(variations, known_passwords, min_length, max_length)
    save_to_file(variations)


if __name__ == "__main__":
    main()
