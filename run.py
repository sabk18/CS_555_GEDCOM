from src.gedcom import *
from src.sprint1.story4 import s4test
from src.sprint1.story1_peer import s1test
from src.sprint1.story22 import s22_test
from src.sprint1.story3 import s3test


def main():
    file = open('Khalid_GEDCOM.txt', 'r', encoding="utf-8")
    new_file = open("Gedcome-output.txt", "w", encoding='utf-8')

    # This duplicate_data will pair up Individuals and Families, having same IDs. This will help in finding
    # whether Individuals and Families are having unique IDs or not (For story 22).
    data, new_file = createoutput(file, new_file)
    new_file = s4test(data, new_file)
    new_file = s1test(data, new_file)
    new_file = s22_test(duplicate_info, all_individuals_ids, all_families_ids, new_file)
    new_file.close()
    file.close()


if __name__ == "__main__":
    main()
