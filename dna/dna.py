import csv
from sys import exit
from sys import argv


def main():
    # variables needed:
    dna_data = []
    dna_sample = ""
    sample_sequences_length = {}

    # TODO: Check for command-line usage
    if len(argv) < 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # TODO: Read database file into a variable (dict) name: {dict}
    with open(argv[1], "r") as dna_db_file:
        reader_db = csv.DictReader(dna_db_file)
        row_count = 0
        for row in reader_db:
            dna_data.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2], "r", encoding="utf-8") as samp_file:
        dna_sample = samp_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    for seq in dna_data[0].keys():
        if seq != "name":
            sample_sequences_length[seq] = longest_match(dna_sample, seq)
    # print(f"DATA: {dna_data}\n\n")
    # print(f"SAMPLE: {dna_sample}\n\n")
    # print(f"SEQUENCES LENGTH: {sample_sequences_length}\n\n")

    # TODO: Check database for matching profiles
    guilty_party = "No match"

    for person in dna_data:
        match = True
        for k in person.keys():
            if k != "name":
                # print(k)
                # print(person[k])
                # print(sample_sequences_length[k])
                if int(person[k]) != sample_sequences_length[k]:
                    match = False
        if match == True:
            # print('GUILTY!')
            guilty_party = person["name"]
            break

    return guilty_party


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


print(main())
